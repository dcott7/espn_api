from typing import List, Tuple, Callable
import logging
import asyncio

from src.rest_adapter import RESTAdapter
from src.response import ESPNResponse
from src.exceptions import APIError
from typing import Optional
from src.sport import Sport


class ESPNClient(RESTAdapter):
    def __init__(
        self,
        api_key: str = None,
        default_base_url: str = "https://sports.core.api.espn.com",
        logger: Optional[logging.Logger] = None,
    ):
        super().__init__(base_url=default_base_url, api_key=api_key, logger=logger),

    async def fetch_data(
        self,
        endpoint: str,
        version: Optional[str] = None,
        params: Optional[dict] = None,
    ) -> ESPNResponse:
        url = f"{version}/{endpoint}" if version else f"/{endpoint}"
        data, headers = await self.get(url, params)
        return ESPNResponse(data), headers

    async def _is_valid_league(self, sport: Sport, league: str) -> bool:
        """Check if the provided league is valid."""
        acceptable_leagues = await self.get_leagues(sport)
        if league not in acceptable_leagues:
            raise ValueError(f"Invalid league: '{league}' not in {acceptable_leagues}")
        return True

    async def _is_valid_team(self, sport: Sport, league: str, team_id: int) -> bool:
        """Check if the provided teams is valid."""
        acceptable_team_ids = await self.get_team_ids(sport, league)
        if team_id not in acceptable_team_ids:
            raise ValueError(f"Invalid team: '{team_id}' not in {acceptable_team_ids}")
        return True

    async def _is_valid_athlete(self, sport: Sport, league: str, athlete_id: int) -> bool:
        """Check if the provided teams is valid."""
        acceptable_athlete_ids = await self.get_athlete_ids(sport, league)
        if athlete_id not in acceptable_athlete_ids:
            raise ValueError(f"Invalid team: '{athlete_id}' not in {acceptable_athlete_ids}")
        return True

    async def get_league(self, sport: Sport, league: str) -> ESPNResponse:
        """Gets the league information."""
        league = league.lower()
        await self._is_valid_league(sport, league)
        response, _ = await self.fetch_data(
            endpoint=f"sports/{sport.value}/leagues/{league}",
            version="v2",
            params={"lang": "en", "region": "us"},
        )
        return response.data

    async def get_team(self, sport: Sport, league: str, team_id: int) -> ESPNResponse:
        """"Gets the team information."""
        league = league.lower()
        await self._is_valid_league(sport, league)
        await self._is_valid_team(sport, league, team_id)
        response, _ = await self.fetch_data(
            endpoint=f"sports/{sport.value}/leagues/{league}/teams/{team_id}",
            version="v2",
            params={"lang": "en", "region": "us"},
        )
        return response.data

    async def get_leagues(self, sport: Sport) -> List[str]:
        """Gets the available leagues for a particular sport, handling pagination asynchronously."""
        leagues = []

        initial_response, headers = await self.fetch_data(
            endpoint=f"sports/{sport.value}/leagues",
            version="v2",
            params={"lang": "en", "region": "us", "page": "1", "limit": "500", "active": "false"},
        )

        page_count = int(headers.get("X-Page-Count", 1))

        tasks = [
            self.fetch_data(
                endpoint=f"sports/{sport.value}/leagues",
                version="v2",
                params={"lang": "en", "region": "us", "page": str(page), "limit": "500", "active": "false"},
            )
            for page in range(1, page_count + 1)
        ]

        responses = await asyncio.gather(*tasks)

        for response, _ in responses:
            for item in response.data.get("items", []):
                ref_url = item.get("$ref")
                if ref_url:
                    league_name = ref_url.split("/")[-1].replace("?lang=en&region=us", "")
                    leagues.append(league_name)

        return leagues

    async def get_team_ids(self, sport: Sport, league: str) -> List[int]:
        """Gets the available team ids for a particular sports league, handling pagination asynchronously."""
        league = league.lower()
        await self._is_valid_league(sport, league)

        team_ids = []

        initial_response, headers = await self.fetch_data(
            endpoint=f"sports/{sport.value}/leagues/{league}/teams",
            version="v2",
            params={"lang": "en", "region": "us", "page": "1", "limit": "500", "active": "false"},
        )

        page_count = int(headers.get("X-Page-Count", 1))

        tasks = [
            self.fetch_data(
                endpoint=f"sports/{sport.value}/leagues/{league}/teams",
                version="v2",
                params={"lang": "en", "region": "us", "page": str(page), "limit": "500", "active": "false"},
            )
            for page in range(1, page_count + 1)
        ]

        responses = await asyncio.gather(*tasks)

        for response, _ in responses:
            for item in response.data.get("items", []):
                ref_url = item.get("$ref")
                if ref_url:
                    team_id = int(ref_url.split("/")[-1].replace("?lang=en&region=us", ""))
                    team_ids.append(team_id)

        return team_ids

    async def get_athlete_ids(self, sport: Sport, league: str) -> List[int]:
        """Gets the available athlete ids for a particular sports league, handling pagination asynchronously."""
        league = league.lower()
        await self._is_valid_league(sport, league)

        athlete_ids = []

        initial_response, headers = await self.fetch_data(
            endpoint=f"sports/{sport.value}/leagues/{league}/athletes",
            version="v2",
            params={"lang": "en", "region": "us", "page": "1", "limit": "500", "active": "false"},
        )

        page_count = int(headers.get("X-Page-Count", 1))

        tasks = [
            self.fetch_data(
                endpoint=f"sports/{sport.value}/leagues/{league}/athletes",
                version="v2",
                params={"lang": "en", "region": "us", "page": str(page), "limit": "500", "active": "false"},
            )
            for page in range(1, page_count + 1)
        ]

        responses = await asyncio.gather(*tasks)

        for response, _ in responses:
            for item in response.data.get("items", []):
                ref_url = item.get("$ref")
                if ref_url:
                    athlete_id = int(ref_url.split("/")[-1].replace("?lang=en&region=us", ""))
                    athlete_ids.append(athlete_id)

        return athlete_ids