---
title: Submitting Application
parent: "Track 4: Twitter Disinformation Analyst Assistant"
nav_order: 4
layout: home
permalink: /tracks/track4/submitting-application/
---

# Submitting Application

Your application is submitted as a **GitHub repository** that the evaluation team can clone, configure, and run on the team VM.

## Repository layout

We do not impose a strict project structure, but the repository **must** contain:

- a top-level **`README.md`** describing how to install dependencies, configure the application, and start the HTTP server,
- a clearly identified **entrypoint** that starts the HTTP endpoint defined in the [I/O contract]({% link tracks/track4/introduction.md %}#inputs-and-outputs),
- any configuration files needed to point the assistant at the corpus directory and the shared inference endpoint,
- and a way to ingest / index the corpus that does not require manual editing of source code.

## Reproducibility requirements

The eval team must be able to take your repository, follow the instructions in your README, and end up with a running endpoint **without contacting you**. In particular:

- pin your dependencies (e.g. `requirements.txt`, `pyproject.toml`, `package.json` lockfile),
- do not hard-code paths that only exist on your VM,
- read secrets and endpoint URLs from environment variables or a config file documented in the README,
- and make sure the server starts cleanly with the corpus mounted at the directory specified by the deployment harness.

## What we will do with your submission

On the deploy-and-freeze day:

1. The eval team clones your repository at a specified commit (tagged `v1` by you) onto your team VM.
2. The corpus is mounted at the documented directory.
3. Your application is started using the documented entrypoint.
4. The acceptance-test battery is run against the running endpoint.
5. The endpoint is exposed to red teams under the rules described in [General Information]({% link general-information.md %}#red-team-visibility).

If your application fails to start or fails the acceptance bar, your effective blue-team baseline is reduced. See [scoring]({% link general-information.md %}#scoring).

## Handing in

By the deploy-and-freeze deadline you must provide:

- the **GitHub repository URL** for your application,
- the **commit SHA or tag** you want evaluated, and
- a **one-line description** of the entrypoint command (e.g. `uvicorn app.main:app --host 0.0.0.0 --port 8080`).

These are submitted via the same web form used for [submitting exploits]({% link submitting-exploits.md %}); the form has a separate "submit application" mode that becomes available once the build phase ends.
