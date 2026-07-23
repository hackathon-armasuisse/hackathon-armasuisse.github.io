---
title: Submitting Application
parent: "Track 1: Documentation Assistant"
nav_order: 4
layout: home
permalink: /tracks/track-1/submitting-application/
---

# Submitting Application

Submit a **GitHub repository** the evaluation team can clone, configure, and run on the team VM.

{: .note }
> **In short:** hand in a runnable repo (README + entrypoint + pinned deps +
> config-driven corpus path) at a tagged commit. The eval team must get a running
> endpoint from your README **without contacting you**.

## Repository layout

No strict structure is imposed, but the repository **must** contain:

- [ ] a top-level **`README.md`**: install deps, configure, start the HTTP server,
- [ ] a clear **entrypoint** that starts the endpoint from the [I/O contract]({% link tracks/track-1/introduction.md %}#inputs-and-outputs),
- [ ] config to point the assistant at the corpus directory and the shared inference endpoint,
- [ ] corpus ingestion / indexing that needs no manual source edits.

## Reproducibility requirements

- [ ] pin your dependencies (`requirements.txt`, `pyproject.toml`, lockfile, etc.),
- [ ] no paths hard-coded to your VM,
- [ ] read secrets and endpoint URLs from env vars or a documented config file,
- [ ] the server starts cleanly with the corpus mounted at the harness-specified directory.

## What we will do with your submission

On the deploy-and-freeze day:

1. The eval team clones your repository at a specified commit (tagged `v1` by you) onto your team VM.
2. The corpus is mounted at the documented directory.
3. Your application is started using the documented entrypoint.
4. The acceptance-test battery is run against the running endpoint.
5. The endpoint is exposed to red teams under the rules described in [General Information]({% link general-information.md %}#red-team-visibility).

{: .warning }
> If your application fails to start or fails the acceptance bar, your effective
> blue-team baseline is reduced. See [scoring]({% link general-information.md %}#scoring).

## Handing in

{: .action }
> By the deploy-and-freeze deadline you must provide:
> - the **GitHub repository URL** for your application,
> - the **commit SHA or tag** you want evaluated, and
> - a **one-line description** of the entrypoint command
>   (e.g. `uvicorn app.main:app --host 0.0.0.0 --port 8080`).

These are submitted via the same web form used for [submitting exploits]({% link submitting-exploits.md %}); the form has a separate "submit application" mode that becomes available once the build phase ends.
