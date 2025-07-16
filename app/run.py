from .yahoo_api.client import YahooFantasyClient

def main():
    client = YahooFantasyClient()
    league_key = '454.l.100725'
    league = client.get_league(league_key)
    team = client.get_team(league)

    roster = team.roster()
    for player in roster:
        player_id = player['player_id']
        try:
            player_stats = league.player_stats(player_id, 'season')
            print(f"Stats for {player['name']}:")
            print(player_stats)
        except Exception as e:
            print(f"Error getting stats for {player['name']}:", e)
        break  # just the first player for now

if __name__ == "__main__":
    main()