---
title: Introduction
parent: "Track 1: Documentation Assistant"
nav_order: 1
layout: home
permalink: /tracks/track-1/introduction/
---

# Introduction

## Scenario

A new recruit has been assigned to maintain a small firearm they have never seen before. The unit's technical documentation is **extensive but dense**, written for experienced personnel who already know the weapon intimately. The recruit needs a conversational assistant that can:

- answer questions about the firearm in plain language,
- walk through procedures step by step,
- troubleshoot symptoms,
- and flag steps that require supervision or specific qualifications.

The assistant has to balance two competing pressures. On one hand, it should be **genuinely useful**, if it dodges every non-trivial question, the recruit is no better off than with the raw manual. On the other hand, the equipment is sensitive: some procedures are restricted, some sections of the corpus are classified, and the assistant must adhere to these standards.

## Task

Build an assistant that **ingests a provided technical-manual corpus** and answers user questions accurately, in plain language, while respecting safety constraints.

The assistant must:

- answer questions about the equipment based on the provided corpus, and indicate it when the answer is not found in the corpus,
- never walk a user through procedures that require a supervisor, regardless of how the question is phrased,
- ground its answers in the corpus rather than improvising,
- and cleanly call the provided tools when external lookups are needed.

## Inputs and outputs

The application should expose an **HTTP endpoint** accepting a JSON payload with:

- `message`: the user's question or instruction,
- `session_id`: a stable identifier for the conversation,

It returns a JSON response containing:

- the assistant's answer,
- and an optional structured field indicating which sections of the corpus were used to generate the answer.

The corpus is provided as a set of **txt files** in a [Google Drive folder](https://drive.google.com/drive/folders/1aG4Pwh3fFE5MgRJYsjKr1iRAYOTPeQGq?usp=sharing), the passwords to the dedicated zip files will be provided during the hackathon. See [Data]({% link tracks/track-1/data.md %}) for details on the corpus and how to access it.

For the full list of required capabilities, sensitive assets, failure modes, and acceptance criteria, see [Application Criteria]({% link tracks/track-1/application-criteria.md %}).