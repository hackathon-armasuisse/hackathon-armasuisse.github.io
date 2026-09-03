"""HTTP endpoint for the Track 4 analyst assistant (iteration 1).

    uvicorn app:app --port 8000

Iteration 1 covers account-, hashtag- and (crudely) topic-scoped retrieval and
summarisation. Semantic retrieval and new-post assessment are not implemented
yet, and there are no confidentiality controls.
"""

from __future__ import annotations

import threading

from fastapi import FastAPI
from pydantic import BaseModel

import answer
import corpus as corpus_mod
import llm
from router import route

app = FastAPI(title="Track 4 Analyst Assistant", version="0.1")
CORPUS = corpus_mod.load()

# Load the weights in the background so the first query does not wait for them.
threading.Thread(target=llm.warmup, daemon=True).start()


class AssessPost(BaseModel):
    content: str
    metadata: dict | None = None


class Query(BaseModel):
    query: str = ""
    assess_post: AssessPost | None = None
    # Explicit override; the router also infers this from the query wording.
    full_text: bool = False


@app.get("/health")
def health() -> dict:
    return {
        "posts": len(CORPUS.posts),
        "in_scope": len(CORPUS.in_scope),
        "authors": len(CORPUS.by_author),
        "hashtags": len(CORPUS.by_hashtag),
        "model": llm.MODEL,
        "model_available": llm.available(),
    }


@app.post("/chat")
def chat(req: Query) -> dict:
    if req.assess_post is not None:
        return {
            "answer": "New-post assessment is not implemented in this iteration.",
            "source_post_ids": [],
            "confidence": 0.0,
            "assessment_score": 0.0,
        }

    r = route(req.query, CORPUS)
    r.want_full_text = r.want_full_text or req.full_text
    return answer.build(r, CORPUS)
