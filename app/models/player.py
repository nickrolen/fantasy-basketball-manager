class Player:
    def __init__(self, player_id, name, status, eligible_positions, selected_position, injury_status=None, next_game=None, news=None):
        self.player_id = player_id
        self.name = name
        self.status = status
        self.eligible_positions = eligible_positions
        self.selected_position = selected_position
        self.injury_status = injury_status
        self.next_game = next_game
        self.news = news

    def __repr__(self):
        return (f"<Player {self.name} ({self.player_id}) - {self.status}, "
                f"Injury: {self.injury_status}, Next: {self.next_game}>")