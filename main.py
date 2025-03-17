from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerindex

player_index = playerindex.PlayerIndex().get_normalized_dict()['PlayerIndex']
player_id = None
for player in player_index:
    if player['PLAYER_LAST_NAME'] == 'Curry' and player["PLAYER_FIRST_NAME"] == 'Stephen':
        player_id = player['PERSON_ID']
        break

player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()['CommonPlayerInfo'][0]
team_id = player_info['TEAM_ID']


shot_details = shotchartdetail.ShotChartDetail(team_id=team_id, player_id=player_id).get_normalized_dict()['Shot_Chart_Detail']
i = 1
for shot in shot_details:
    print('\n')
    print(f"Shot detail {i}")
    for key, val in shot.items():
        print(f"{key}: {val}")

    i += 1

