import pandas as pd
from app.models.player import Player
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

class YahooFantasyClient:
    def __init__(self, game_code="nba", oauth_path="oauth2.json"):
        self.sc = OAuth2(None, None, from_file=oauth_path)
        self.yfa = yfa
        self.game_code = game_code
        self.gm = self.yfa.Game(self.sc, self.game_code)

    def get_leagues(self):
        return self.gm.league_ids()

    def get_league(self, league_key):
        return self.gm.to_league(league_key)

    def get_team(self, league_obj, team_key=None):
        if not team_key:
            team_key = league_obj.team_key()
        return league_obj.to_team(team_key)

    def get_roster(self, team_obj):
        return team_obj.roster()
    
    def get_roster_dataframe(self, team_obj):
        roster = team_obj.roster()
        df = pd.DataFrame(roster)
        possible_columns = ['player_id', 'name', 'status', 'eligible_positions', 'selected_position', 'editorial_player_news', 'notes']
        columns = [c for c in possible_columns if c in df.columns]
        return df[columns] if columns else df
    
    def get_roster_objects(self, team_obj):
        roster = team_obj.roster()
        players = []
        for p in roster:
            # Try to fetch extra info, safely
            injury_status = p.get('injury_status') or p.get('status')
            # You might have a 'notes' or 'editorial_player_news' field for news
            news = p.get('editorial_player_news') or p.get('notes')
            # If Yahoo gives 'next_game' or 'display_position', extract
            next_game = p.get('display_position')  # This is sometimes the next opponent
            # You may have to call another API or scrape for true next_game

            players.append(Player(
                player_id=p.get('player_id', ''),
                name=p.get('name', ''),
                status=p.get('status', ''),
                eligible_positions=p.get('eligible_positions', []),
                selected_position=p.get('selected_position', ''),
                injury_status=injury_status,
                next_game=next_game,
                news=news
            ))
        return players