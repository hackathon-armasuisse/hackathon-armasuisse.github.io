---
title: Submitting Application
parent: "Track 3: Air Threat Advisor"
nav_order: 4
layout: home
permalink: /tracks/track-3/submitting-application/
---

# Submitting Application

{: .summary }
> **In short:** by the deadline, push your app to a GitHub repository with a root `Dockerfile`, tag the commit `v1` for the first version or `final` for the final version, and submit the repository URL through the form. Your app **must** build and run with the exact command below and serve `POST /advise` and `POST /message` on port **8080**.

## We run your app with exactly this command

```
docker build -t track3 .
docker run -p 8080:8080 -v <corpus-dir>:/corpus:ro --env-file inference.env track3
```

{: .warning }
> This is the only command we run. Your submission must build and start with it, and serve `/advise` and `/message` on port **8080**, with no extra flags or manual steps.

- We mount the data read-only at the fixed path **`/corpus`** (the `CORPUS_DIR` variable defaults to it), with the layout given in [Building your Application]({% link tracks/track-3/building-application.md %}#running-in-a-container).
- The **inference endpoint** is an OpenAI-compatible LiteLLM proxy, passed via `--env-file inference.env`. Read these exact variable names, do not hard-code them:

  | Variable | Value |
  |---|---|
  | `OPENAI_BASE_URL` | `https://litellm.intlab.ch/v1` |
  | `OPENAI_API_KEY` | provided on Monday morning |
  | `MODEL` | provided later |

## Before you submit

Check that:

- [ ] it **runs with the exact commands above** and serves `/advise` and `/message` on port 8080;
- [ ] it reads the data path and inference variables from the environment (nothing hard-coded to your machine);
- [ ] responses follow the [I/O contract]({% link tracks/track-3/building-application.md %}#the-advise-endpoint);
- [ ] a top-level **`README.md`** notes anything non-obvious about your build.

## What we do on deploy day

1. We clone your repository at the commit you tagged `v1`.
2. We `docker build` the image.
3. We `docker run` it with the exact command above.
4. We expose the endpoint to red teams.

## Handing in

By the deploy-and-freeze deadline, submit through the [Google Form](https://forms.gle/ijNGXvWJDfQKQnWPA):
- your **GitHub repository URL**, and
- the **commit hash** you tagged.

---

Next: [Extensions]({% link tracks/track-3/Extensions.md %}) →
