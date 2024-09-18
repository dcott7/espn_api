import aiohttp
import asyncio
from typing import Optional, Dict, Any, Tuple
import logging

from src.exceptions import APIError


class RESTAdapter:
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        logger: Optional[logging.Logger] = None
    ) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.session = None
        self.logger = logger or logging.getLogger(__name__)

    async def _create_session(self) -> None:
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def close_session(self) -> None:
        if self.session:
            await self.session.close()

    async def _request(
        self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Performs the actual HTTP request and returns both the JSON response and headers."""
        await self._create_session()
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}

        self.logger.debug(f"Making {method} request to URL: {url}")
        if params:
            self.logger.debug(f"Request parameters: {params}")

        async with self.session.request(
            method, url, headers=headers, params=params
        ) as response:
            response_text = await response.text()
            self.logger.debug(f"Response status: {response.status}")
            self.logger.debug(f"Response text: {response_text}")

            if response.status != 200:
                self.logger.error(
                    f"Failed with status {response.status}: {response_text}"
                )
                raise APIError(f"Failed with status {response.status}")

            return await response.json(), dict(response.headers)

    async def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Performs a GET request and returns both JSON response and headers."""
        return await self._request("GET", endpoint, params)

    async def post(
        self,
        endpoint: str,
        data: Dict[str, Any],
        params: Optional[Dict[str, Any]] = None,
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Performs a POST request and returns both JSON response and headers."""
        return await self._request("POST", endpoint, params)
