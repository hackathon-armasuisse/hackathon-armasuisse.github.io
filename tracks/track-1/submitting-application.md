---
title: Submitting Application
parent: "Track 1: Documentation Assistant"
nav_order: 4
layout: home
permalink: /tracks/track-1/submitting-application/
---

# Submitting Application

Submit a **GitHub repository** with a **`Dockerfile` in its root**. We build the image and launch it with a single command, your app just has to serve the endpoints on the published port.

{: .summary }
> **In short:** ship a repo whose root `Dockerfile` builds and runs your assistant on port **8080**, serving `/chat` and the `/post/*` endpoints. We launch it with `docker run`; you can start from the
> [template repository](https://github.com/Reliable-Information-Lab-HEVS/hackathon-track1-template).

## How we launch it

```
docker build -t track1 .
docker run -p 8080:8080 --env-file inference.env track1
```

- Your server listens on **8080** and serves `/chat` and `/post/*`.
- The **corpus** is mounted at `CORPUS_DIR` (default `/corpus`) — do not bake it into the image.
- The **inference endpoint** is an OpenAI-compatible LiteLLM proxy. We pass it via `--env-file inference.env` using these **exact** variable names — read them by these names, don't hard-code:

  | Variable | Value |
  |---|---|
  | `OPENAI_BASE_URL` | `https://litellm.intlab.ch/v1` |
  | `OPENAI_API_KEY` | provided on Monday morning |
  | `MODEL` | <TODO> |

  Because the endpoint is OpenAI-compatible, the `openai` SDK reads `OPENAI_BASE_URL` / `OPENAI_API_KEY` automatically. An `inference.env.example` is in the [template](https://github.com/Reliable-Information-Lab-HEVS/hackathon-track1-template).

## Repository layout

- [ ] a **root `Dockerfile`** that builds and runs your app (start from the template),
- [ ] a **`README.md`** noting anything non-obvious about your build.
- [ ] any additional files needed for your build (source code, dependencies, etc.). No manual steps, no private dependencies.

## What we will do with your submission

On the deploy-and-freeze day:

1. We clone your repository through the link you submitted, which should point to the commit tagged `v1`.
2. We `docker build` the image.
3. We `docker run` it with the command above
4. The acceptance-test battery is run against `:8080`.
5. The endpoint is exposed to red teams

{: .warning }
> Make sure that your application launches through the commands above, and that it serves the endpoints on port 8080.

## Handing in
By the deploy-and-freeze deadline, provide the **GitHub repository URL**, pointing specifically to the commit hash you tagged `v1`. You can submit your submission in this [Google Form](https://forms.gle/ijNGXvWJDfQKQnWPA).

