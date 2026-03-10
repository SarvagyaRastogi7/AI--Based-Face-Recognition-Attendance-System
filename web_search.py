from __future__ import annotations

from typing import Any, Dict, List

import httpx

from app.config import get_settings


class WebSearchService:
    """
    Simple wrapper around an external search API.

    Plug this into your preferred provider (Bing, SerpAPI, internal search, etc.)
    by adjusting the `search` method implementation.
    """

    def __init__(self) -> None:
        self._settings = get_settings()
        # If no search config is provided, we simply disable web search and
        # return an empty result set instead of failing the whole request.
        self._enabled = bool(
            self._settings.search_api_key and self._settings.search_endpoint
        )

    async def search_company(self, company_name: str, *, limit: int = 8) -> List[Dict[str, Any]]:
        """
        Perform a web search and return a normalized list of documents:
        [{title, url, summary, date?}, ...]
        """
        if not self._enabled:
            return []

        # This is intentionally generic; map to your provider's schema.
        params = {"q": company_name, "count": limit}
        headers = {"Authorization": f"Bearer {self._settings.search_api_key}"}

        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.get(str(self._settings.search_endpoint), params=params, headers=headers)
            resp.raise_for_status()
            data = resp.json()

        # TODO: adapt this to your provider's response shape.
        documents: List[Dict[str, Any]] = []
        for item in data.get("webPages", {}).get("value", []):
            documents.append(
                {
                    "title": item.get("name"),
                    "url": item.get("url"),
                    "summary": item.get("snippet") or "",
                    "date": item.get("dateLastCrawled"),
                }
            )
        return documents[:limit]

