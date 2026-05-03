# report_generation.md — Template-Driven Report Generation

Use this file as the shared report-generation skill for Agent 21. Consult it whenever the user asks for a Secret Satoshis report, recap, update, or other recurring written output that is backed by Report Library templates and curated CSV inputs.

This skill is platform-agnostic. It does not define runtime-specific tool calls. It defines the workflow for turning a canonical report template plus its mapped data inputs into a finished report.

## Purpose

Agent 21 should generate reports from the canonical Secret Satoshis report templates stored in the Report Library.

The template is the source of truth for:
- section order
- section prompt instructions
- required data inputs
- final assembly rules

Do not invent a new report structure when a canonical template already exists.

## Default Workflow

When asked to generate a report:

1. Identify which report workflow the user wants.
2. Locate the canonical template in the Report Library.
3. Read the template before writing anything.
4. Extract from the template:
   - the section order
   - the per-section prompt instructions
   - the per-section data-input mapping
   - the final assembly notes
5. Resolve the required inputs exactly as mapped by the template.
6. Generate each section from its mapped inputs and prompt instructions.
7. Assemble the report in the documented order.
8. Run a final phrasing pass with `voice.md`.

## Canonical Source Rule

The report template in the Report Library is the canonical source of truth.

For the current Weekly Bitcoin Recap workflow, the canonical template lives in the Report Library `reports/` folder. If a local Report Library checkout is available, use that first. If not, use the published or repository version of the same template.

Do not duplicate template logic into the report-generation skill. The skill teaches how to execute the template, not how to replace it.

## Input Resolution Rules

For each section:

1. Read the mapped local source from the template.
2. If the local source is unavailable, use the mapped published source from the template.
3. Keep the same mapped input regardless of source location.
4. Gather the input before writing the section.

Do not:
- guess which CSV belongs to a section
- substitute unrelated files because they look similar
- default to broad datasets like the master metrics file unless the template explicitly maps that section to them
- replace curated mapped inputs with raw BRK retrieval when the mapped input already exists

If a mapped input is missing, surface the gap clearly instead of silently substituting unrelated data.

### RSS-Backed Sections

Some templates map a section to RSS feeds rather than CSVs (for example, the Weekly Bitcoin Recap News Section). When a section's input is RSS:

1. Use the canonical feed list from the template — never improvise or substitute feeds.
2. Fetch and parse those feeds using `rss.md`. That skill defines how to issue the request, handle status codes, and normalize parsed items.
3. After `rss.md` returns the normalized items, apply the section's own template rules for time-window filtering, ranking, source diversity, attribution format, and selection counts.

If `rss.md` reports that a feed is inaccessible, treat it the same as a missing CSV input: surface the gap instead of inventing items or quietly substituting another feed.

## Master Dataset Naming

If a report template refers to the master metrics dataset, treat `master_metrics_data.csv.gz` as the canonical file name when that is the current published artifact.

If you see an older `.csv` reference but the active stack publishes `.csv.gz`, treat that as documentation drift and resolve to the current canonical file rather than teaching the outdated name forward.

## Section Writing Rules

When generating a section:

- use only the inputs mapped by the template for that section
- follow the section prompt instructions closely
- keep the section grounded in the mapped data, not generic background knowledge
- do not pull in unrelated external facts unless the template explicitly calls for them
- do not invent missing values, rows, or metrics

If the template says a section depends on completed earlier sections, synthesize only from those completed sections.

## Source Hierarchy

For template-driven report generation, use this hierarchy:

1. canonical report template in Report Library
2. mapped curated report inputs from Report Library
3. earlier completed sections when the template calls for synthesis

## Missing Inputs

If a required mapped input is unavailable:
- state which mapped input is missing
- state which section is blocked by that missing input
- do not silently replace it with unrelated data
- only use alternate raw-data workflows if the user explicitly asks for a fallback

## Final Pass

After the report is assembled:
- check that the section order matches the template
- check that each section was written from its mapped inputs
- check that no stale or substituted file names slipped into the workflow
- run `voice.md` so the final report sounds natural, direct, and not like copied prompt text

## Output Goal

The final output should read like a finished Secret Satoshis report:
- structured
- data-grounded
- template-aligned
- professionally written

The skill is about disciplined execution of canonical report templates, not improvisation.
