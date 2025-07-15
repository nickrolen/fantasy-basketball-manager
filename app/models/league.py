class League:
    def __init__(self, league_id, league_name, teams):
        self.league_id = league_id
        self.league_name = league_name
        self.teams = teams

    def __repr__(self):
        return f"<League {self.league_name} ({self.league_id}) with {len(self.teams)} teams>"