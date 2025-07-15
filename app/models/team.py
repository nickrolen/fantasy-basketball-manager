from .player import Player

class Team:
    def __init__(self, team_id, team_name, players):
        self.team_id = team_id
        self.team_name = team_name
        self.players = [Player(**p) if not isinstance(p, Player) else p for p in players]

    def __repr__(self):
        return f"<Team {self.team_name} ({self.team_id}) with {len(self.players)} players>"