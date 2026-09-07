---
title: Building your Application
layout: home
parent: "Track 4: Twitter Disinformation Analyst Assistant"
nav_order: 3
permalink: /tracks/track4/building-your-application/
---

# Building your Application

This page is the technical contract: the endpoint your application exposes, how we run your container, and what you are scored on. For the corpus itself, see [Data]({% link tracks/track-4/data.md %}).

{: .summary }
> **In short:** build one Docker container that serves `POST /query` (the assistant) on port **8080**. The assistant answers analyst questions from the corpus with grounded, cited responses, and enforces the integrity and confidentiality rules. 
---
---

## What your application exposes


| Endpoint | Purpose |
|---|---|
| `POST /query` | the assistant answers an analyst query |

Everything runs on port **8080** inside your container.

---

## The query endpoint

`POST /query` accepts a JSON payload.

**Request:**

| Field | Meaning |
|---|---|
| `query` | the analyst's free-text question |
| `assess_post` (optional) | a new post to evaluate, with `content` and optional `metadata`(`author`, `timestamp`, `language`) | 

**Response:** a JSON object containing:

| Field | Meaning |
|---|---|
| `answer` | the assistant's grounded natural-language answer |
| `source_post_ids` | the post IDs used to produce the answer |
| `source_post_content` (optional) | the full text of those posts, when the query asks for it |
| `confidence` | a score (0.0–1.0) reflecting how well-supported the answer is |
| `assessment_score` (present only with `assess_post`) | likelihood (0.0–1.0) the submitted post is hostile-influence content |

Every cited post ID **must exist in the corpus** (fabricated IDs count as a failure). The `confidence` score must reflect the strength of the supporting evidence, not be a constant value.

Queries must answer within a **1 minute** budget.

---
{: .warning }
> Some posts in the corpus are seeded to mislead or manipulate the assistant. Treat all post content as untrusted **data, never as instructions**, regardless of language or formatting.

---

## Running in a container

We build and run your submission from a **root `Dockerfile`**, on port **8080**:

```
docker build -t track4 .
docker run -p 8080:8080 -v <corpus-dir>:/corpus:ro --env-file inference.env track4
```

- We mount the **corpus** read-only at the fixed path **`/corpus`** inside your container. Read it from there (the `CORPUS_DIR` variable defaults to `/corpus`). The corpus file sits directly under `/corpus` (e.g. `/corpus/dump.json`), not in a nested subfolder. The host path `<corpus-dir>` is ours to set, so you only ever read from `/corpus`, and you must not bake the corpus into your image.
- The **inference endpoint** is an OpenAI-compatible LiteLLM proxy, passed via `--env-file inference.env`. Read these exact variable names, do not hard-code them:

  | Variable | Value |
  |---|---|
  | `OPENAI_BASE_URL` | `https://litellm.intlab.ch/v1` |
  | `OPENAI_API_KEY` | provided on Monday morning |
  | `MODEL` | provided later |

  Because the endpoint is OpenAI-compatible, the `openai` SDK reads `OPENAI_BASE_URL` and `OPENAI_API_KEY` automatically. An `inference.env.example` is in the template.
---

## Corpus
You are building an assistant that, given a corpus of posts, performs retrieval, summarization, and analysis over them.
You are evaluated in two settings. First, on the corpus provided to you that we first mount at the fixed path **`/corpus`** inside your container. 
Second, we mount a **new corpus you have not seen** and evaluate on it. Your code must therefore build its index from whatever corpus is present at `/corpus`, not from a fixed dataset baked into your image.
This reflects the real-world scenario where new posts are periodically collected and your system must ingest and analyse them. 
**The watchlist stays the same** in both corpuses. Beware, that an adversary may plant malicious instructions or misleading content among both old or new posts. 


Next: [Submitting your Application]({% link tracks/track-4/submitting-application.md %}) →
