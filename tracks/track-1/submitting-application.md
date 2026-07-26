---
title: Submitting Application
parent: "Track 1: Documentation Assistant"
nav_order: 4
layout: home
permalink: /tracks/track-1/submitting-application/
---

# Submitting Application

{: .summary }
> **In short:** by the deadline, push your app to a GitHub repository with a root `Dockerfile`, tag the commit `v1`, and submit the repository URL through the form. Your app **must** build and run with the exact command below and serve the endpoints on port **8080**.

## We run your app with exactly this command

```
docker build -t track1 .
docker run -p 8080:8080 -v <corpus-dir>:/corpus:ro --env-file inference.env track1
```

{: .warning }
> This is the **only** command we run. Your submission **must** build and start with it, and serve `/chat` and `/post/*` on port **8080**, with no extra flags or manual steps. **Test this exact command yourself before submitting.** 

We mount the corpus read-only at the fixed path `/corpus` (read it from there), pass the inference variables from `inference.env`, and set the host path `<corpus-dir>` ourselves. Your tool seed (`tools_seed_data.json`) must be in your image. See [Building your Application]({% link tracks/track-1/building-application.md %}#running-in-a-container) for details.

## Before you submit

Check that:

- [ ] the image **builds from the repo root** with `docker build .` (no manual steps, no private dependencies);
- [ ] it **runs with the exact command above** and serves `/chat` and `/post/*` on port **8080**;
- [ ] it reads the corpus path and inference variables **from the environment** (nothing hard-coded to your machine);
- [ ] dependencies are **pinned**;
- [ ] a top-level **`README.md`** notes anything non-obvious about your build.

## What we do on deploy day

1. We clone your repository at the commit you tagged `v1`.
2. We `docker build` the image.
3. We `docker run` it with the exact command above (corpus mounted, inference variables set).
4. We run the acceptance-test battery against `:8080`.
5. We expose the endpoint to red teams.

## Handing in

By the deploy-and-freeze deadline, submit through the [Google Form](https://forms.gle/ijNGXvWJDfQKQnWPA):
- your **GitHub repository URL**, and
- the **commit hash** you tagged `v1`.
