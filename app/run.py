from .yahoo_api.client import YahooFantasyClient

def main():
    client = YahooFantasyClient()
    league_key = '454.l.100725'
    league = client.get_league(league_key)
    team = client.get_team(league)

    players = client.get_roster_objects(team)
    for player in players:
        print(player)
        print("Injury status:", player.injury_status)
        print("Next game:", player.next_game)
        print("News:", player.news)
        print("-----")

if __name__ == "__main__":
    main()