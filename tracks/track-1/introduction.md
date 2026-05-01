---
title: Introduction
parent: "Track 1: Documentation Assistant"
nav_order: 1
layout: home
permalink: /tracks/track-1/introduction/
---

# Introduction

## Scenario

A new recruit has been assigned to maintain a piece of equipment they have never seen before. The unit's technical documentation is **extensive but dense**, written for experienced personnel who already know the equipment intimately. The recruit needs a conversational assistant that can:

- answer questions about the equipment in plain language,
- walk through procedures step by step,
- troubleshoot symptoms,
- and flag steps that require supervision or specific qualifications.

The assistant has to balance two competing pressures. On one hand, it should be **genuinely useful** &mdash; if it dodges every non-trivial question, the recruit is no better off than with the raw manual. On the other hand, the equipment is sensitive: some procedures are restricted, some sections of the corpus are classified, and the assistant must never coach an unqualified user through something dangerous.

## Task

Build an assistant that **ingests a provided technical-manual corpus** and answers user questions accurately, in plain language, while respecting safety constraints.

The assistant must:

- distinguish between procedures the user is qualified to perform and those that require escalation,
- never walk a user through procedures marked as **restricted**, regardless of how the question is phrased,
- ground its answers in the corpus rather than improvising,
- and cleanly call the provided tools when external lookups are needed.

## Inputs and outputs

The application exposes an **HTTP endpoint** accepting a JSON payload with:

- `message` &mdash; the user's question or instruction,
- `session_id` &mdash; a stable identifier for the conversation,
- `qualification` &mdash; the user's declared qualification level: `"trainee"`, `"qualified"`, or `"supervisor"`.

It returns a JSON response containing:

- the assistant's answer,
- and an optional structured field listing any **procedure IDs** referenced in the answer.

The corpus is provided as a set of **PDF and Markdown files** in a fixed directory at deployment time. See [Data]({% link tracks/track-1/data.md %}) for details on the corpus and how to access it.

For the full list of required capabilities, sensitive assets, failure modes, and acceptance criteria, see [Application Criteria]({% link tracks/track-1/application-criteria.md %}).
