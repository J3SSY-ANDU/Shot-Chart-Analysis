from nba_api.live.nba.endpoints import scoreboard

sb = scoreboard.ScoreBoard()

home_wins = 0
away_wins = 0
for game in sb.games.data:
    home_team = game['homeTeam']['teamName']
    away_team = game['awayTeam']['teamName']
    home_score = game['homeTeam']['score']
    away_score = game['awayTeam']['score']
    print(f'{home_team} vs {away_team}')
    print(f'{home_score} - {away_score}')
    if home_score > away_score:
        home_wins += 1
    else:
        away_wins += 1

    print('\n ------------------- \n')

print(f'Home wins: {home_wins}')
print(f'Away wins: {away_wins}')