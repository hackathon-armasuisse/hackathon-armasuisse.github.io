---
title: Data
parent: "Track 1: Documentation Assistant"
layout: home
nav_order: 2
permalink: /tracks/track-1/data/
---

# Data

## What you receive

The corpus for this track is a collection of **PDF and Markdown files** modelling the technical documentation for a piece of equipment. It includes:

- Operating procedures, organised by procedure ID.
- Troubleshooting guides for common symptoms.
- Vendor specifications and reference data for parts.
- A small **classified annex** carrying material that must never appear in any answer the assistant produces.

Documents are tagged with metadata indicating, where applicable:

- the **procedure ID** they describe,
- the **qualification level** required to execute the procedure (`trainee`, `qualified`, `supervisor`),
- whether the procedure is **restricted** (must never be walked through, regardless of qualification level), and
- whether the document is part of the **classified annex**.

Your retrieval and prompting design has to make use of this metadata &mdash; "ignore all classified-annex chunks" is part of the contract, not an optional optimisation.

## How to obtain the corpus

The corpus is distributed as an **encrypted zip file**. The download link and password are provided to your team on Monday morning, on the track-specific page of this site once you log in with your team password.

{: .note }
> **Placeholder:** the download link and decryption instructions will be inserted here on Monday morning of the event.

```text
Corpus download:  <link will be filled in at event start>
SHA-256:          <hash will be filled in at event start>
Decryption:       provided in your team's onboarding packet
```

## Tooling around the data

Two external tool calls are exposed to your assistant and operate on this dataset (or simulate calls outside of it):

- `lookup_vendor_specs(part_number)` &mdash; returns vendor-supplied specifications for the given part number.
- `fetch_bulletin(bulletin_id)` &mdash; fetches a maintenance bulletin by its identifier.

Both tools draw from a shared, mutable backing store. **Adversaries will be able to upload malicious vendor specifications or bulletins** into this store during red-team phases, so any content you ingest from these tools should be treated as **untrusted input** &mdash; the same way you would treat content fetched from the open internet.

See [Application Criteria]({% link tracks/track-1/application-criteria.md %}) for how this affects your defensive design and what failure modes count as exploits.
