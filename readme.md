# Agent 21 — Bitcoin AI Agent

**Open-source Bitcoin AI agent powering [Secret Satoshis](https://www.newsletter.secretsatoshis.com/).**

---

## What Is Agent 21?

Agent 21 is an interactive AI agent focused on Bitcoin. It combines a curated knowledge base from Secret Satoshis research with live on-chain data from the [Bitcoin Research Kit (BRK)](https://github.com/bitcoinresearchkit/brk) to deliver informed, data-grounded analysis.

- **Bitcoin-only scope.** No alt-coins, no tokens, no DeFi.
- **First-principles reasoning.** Explain the "why," not just the "what."
- **Data-grounded.** Queries live on-chain series rather than guessing.
- **Balanced.** Presents risks alongside opportunities.
- **Open-source deployment bundle.** Platform prompts, shared skills, tools, and deployment guides are all here.

---

## Architecture

Agent 21 is currently organized around **platform deployments plus shared support files**.

- `platforms/` contains the active runtime-specific prompts, knowledge maps, and deployment docs
- `resources/` contains the shared Secret Satoshis source material and shared skill files used by those runtimes
- `tools/` contains the BRK and GitHub tool specs used by the deployed platform versions

This keeps the repo focused on the files needed to run and maintain the live platform versions of Agent 21.

---

## Platform Overview

Agent 21 currently has two active deployment targets:

- **ChatGPT** uses uploaded knowledge files, Custom GPT Actions, and the built-in Python tool. Its deployment files are designed around the constraints of the Custom GPT interface, including Action-specific behavior and uploaded file references.
- **Claude** uses uploaded project knowledge, the GitHub connector, and its analysis tool. Its deployment files are designed around a more direct tool-execution model, especially for data retrieval and analysis.

The two platforms share the same Secret Satoshis source material, shared skills, and external data/tooling references, but they do not use identical runtime mechanics. That is why `platforms/chatgpt/` and `platforms/claude/` each have their own prompt, knowledge map, and deployment docs.

---

## Repo Structure

| Folder | What's Inside |
|---|---|
| `platforms/` | Runtime-specific deployment files for ChatGPT and Claude |
| `resources/` | Shared skills, uploaded PDFs, and external reference material |
| `tools/` | BRK and GitHub tool specs used by the platform deployments |

## Main Surfaces

| Surface | Link |
|---|---|
| Secret Satoshis | [newsletter.secretsatoshis.com](https://www.newsletter.secretsatoshis.com/) |
| Secret Satoshis on X | [x.com/SecretSatoshis](https://x.com/SecretSatoshis) |
| Secret Satoshis GitHub | [github.com/SecretSatoshis](https://github.com/SecretSatoshis) |
| BRK (Bitcoin Research Kit) | [github.com/bitcoinresearchkit/brk](https://github.com/bitcoinresearchkit/brk) |
