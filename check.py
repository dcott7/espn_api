import asyncio
import logging

from src.espn_client import ESPNClient
from src.sport import Sport

custom_logger = logging.getLogger('CustomLogger')
custom_logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
custom_logger.addHandler(handler)

async def main():
    client = ESPNClient(logger=custom_logger)
    leagues = await client.get_leagues(Sport.BASKETBALL)
    league_info =[]
    for league in leagues:
        league_data = await client.get_league(Sport.BASKETBALL, league)
        # print(league_data)
        
        
        team_ids = await client.get_team_ids(Sport.BASKETBALL, league)
        for team_id in team_ids:
            team_data = await client.get_team(Sport.BASKETBALL, league, team_id)
            # print(team_data)

if __name__ == "__main__":
    asyncio.run(main())