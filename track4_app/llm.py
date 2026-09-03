"""Thin ollama client.

The model only ever writes prose over snippets that have already been selected
and validated. It does not choose citations, confidence, or scores.
"""

from __future__ import annotations

import os

import requests

OLLAMA_URL = os.environ.get("T4_OLLAMA_URL", "http://localhost:11434")
MODEL = os.environ.get("T4_MODEL", "mistral-small3.2:24b")
TIMEOUT = float(os.environ.get("T4_LLM_TIMEOUT", "300"))
# Keep the weights resident between queries; a cold load costs ~60s.
KEEP_ALIVE = os.environ.get("T4_KEEP_ALIVE", "30m")
MAX_TOKENS = int(os.environ.get("T4_MAX_TOKENS", "400"))


class LLMUnavailable(RuntimeError):
    pass


def chat(system: str, user: str, temperature: float = 0.2) -> str:
    try:
        resp = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "stream": False,
                "keep_alive": KEEP_ALIVE,
                "options": {"temperature": temperature, "num_predict": MAX_TOKENS},
            },
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise LLMUnavailable(str(exc)) from exc

    return resp.json()["message"]["content"].strip()


def available() -> bool:
    try:
        tags = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5).json()
    except requests.RequestException:
        return False
    return any(m["name"].startswith(MODEL.split(":")[0]) for m in tags.get("models", []))


def warmup() -> None:
    """Pull the weights into VRAM so the first real query is not paying for a
    ~60s cold load on top of generation."""
    try:
        requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={"model": MODEL, "messages": [{"role": "user", "content": "hi"}],
                  "stream": False, "keep_alive": KEEP_ALIVE,
                  "options": {"num_predict": 1}},
            timeout=TIMEOUT,
        )
    except requests.RequestException:
        pass
