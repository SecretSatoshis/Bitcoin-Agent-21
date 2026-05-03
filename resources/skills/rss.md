# rss.md — RSS Feed Fetching and Result Interpretation

Use this file as the shared RSS skill for Agent 21. Consult it whenever a task requires reading items from an RSS or Atom feed.

This file is platform-agnostic. It does not define runtime-specific tool calls. It defines how to fetch a feed and interpret the parsed result. This skill teaches the fetch and the read, nothing more.

## Purpose

Agent 21 should be able to consume any RSS or Atom feed and turn its raw response into a clean list of items the consuming workflow can reason about.

The skill covers:

- making the HTTP request
- handling the most common failure modes
- recognizing whether the feed is RSS or Atom
- mapping the feed's native fields to a consistent internal shape

Everything beyond that — which feeds to query, how to filter, how to rank, how to attribute — belongs to the workflow that called the skill.

## Default Workflow

When asked to read a feed:

1. Identify the feed URL from the calling template or user request.
2. Issue an HTTP GET against the URL.
3. Inspect the status code before parsing.
4. Parse the body as XML.
5. Detect the feed type (RSS or Atom).
6. Map each item or entry to the normalized shape below.
7. Return the normalized list to the caller.

Do not infer or invent a feed URL. If a URL is not supplied by the caller, surface that and stop.

## Fetching

- Use HTTP GET with a sensible request timeout (about 8 to 15 seconds).
- Send a realistic `User-Agent` header. Many feeds reject empty or default UAs and will return 4xx. A UA string identifying as a known RSS reader (for example `Feedly/1.0 (+http://www.feedly.com/fetcher.html)`) is generally accepted.
- Follow HTTP redirects.
- Do not aggressively retry. One retry on a transient timeout is fine; do not loop on a hard 4xx.

## Status Code Handling

Treat the HTTP status as load-bearing. Do not parse a non-200 body as if it were a feed.

| Status | Meaning | Action |
|---|---|---|
| 200 | OK | Parse the body |
| 301 / 302 / 307 / 308 | Redirect | Follow it (most clients do this automatically) |
| 304 | Not modified | Treat as no new content; reuse previously fetched items if available |
| 401 / 403 | Forbidden, often UA-fingerprint or paywall | Mark the feed as inaccessible; do not invent items |
| 404 | Not found | Mark the feed URL as broken; do not invent items |
| 429 | Rate limited | Back off; if a single retry after a short delay also fails, mark as inaccessible |
| 5xx | Server error | Mark the feed as temporarily unavailable; do not invent items |

If a feed is inaccessible, surface that to the caller. The calling workflow decides whether to proceed without it or stop.

## Parsing

After a 200 response, parse the body as XML.

- Detect feed type by the root element:
  - `<rss>` → RSS 2.0
  - `<feed xmlns="http://www.w3.org/2005/Atom">` → Atom
- Treat anything else (HTML error page, JSON, empty body) as a parse failure.
- A parse failure is a feed-level failure. Surface it; do not invent items.

## Normalized Item Shape

Map each feed item to a single internal shape, regardless of RSS vs Atom origin:

| Field | RSS source | Atom source |
|---|---|---|
| `title` | `<item><title>` | `<entry><title>` |
| `link` | `<item><link>` (text content) | `<entry><link href="...">` |
| `published` | `<item><pubDate>` | `<entry><published>` or `<entry><updated>` |
| `summary` | `<item><description>` | `<entry><summary>` or `<entry><content>` |
| `author` | `<item><author>` or `<item><dc:creator>` | `<entry><author><name>` |
| `source` | feed-level `<channel><title>` | feed-level `<feed><title>` |
| `guid` | `<item><guid>` | `<entry><id>` |

Normalize the date field to a timezone-aware datetime in UTC. If a date is missing or unparseable, leave the field null and surface that the item lacks a publish time. Do not guess.

Strip HTML tags from `summary` for downstream readability when the summary is used as plain text. Preserve `link` and `title` as-is.

## Output to the Caller

Return a normalized list of items per feed. Group by source feed when the caller queries multiple feeds, so the consuming workflow can apply per-source rules.

Include feed-level metadata alongside the items:

- the feed URL queried
- the resolved status (`ok`, `inaccessible`, `parse_failed`)
- the source title (from the channel or feed root)

Do not collapse failed feeds silently. The caller needs to know which feeds contributed and which did not.

## What This Skill Does Not Do

- Decide which feeds to query
- Apply time-window filters (for example, "report week only")
- Rank or score items
- Deduplicate across feeds
- Pick which items become section content
- Format items for output (headline, attribution string, etc.)

All of those decisions belong to the consuming template or workflow. This skill stops at "here is a clean list of items per feed."

## Failure Reporting

When a feed cannot be used, the skill returns a structured note rather than throwing the work away:

- which feed URL failed
- which status or parse error caused it
- whether other feeds in the batch succeeded

The calling workflow then decides whether the remaining feeds are sufficient or whether to stop and report the gap to the user.
