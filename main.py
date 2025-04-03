from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerindex
from matplotlib import pyplot as plt

# Get player ID
player_index = playerindex.PlayerIndex().get_normalized_dict()['PlayerIndex']
player_id = None
for player in player_index:
    if player['PLAYER_LAST_NAME'] == 'Curry' and player["PLAYER_FIRST_NAME"] == 'Stephen':
        player_id = player['PERSON_ID']
        break

# Get team ID
player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()['CommonPlayerInfo'][0]
team_id = player_info['TEAM_ID']

# Get shot chart data
shot_details = shotchartdetail.ShotChartDetail(
    team_id=team_id,
    player_id=player_id,
    season_type_all_star='Regular Season'
).get_normalized_dict()['Shot_Chart_Detail']

# Filter only made shots
made_shots_x = [shot['LOC_X'] for shot in shot_details if shot['SHOT_MADE_FLAG'] == 1]
made_shots_y = [shot['LOC_Y'] for shot in shot_details if shot['SHOT_MADE_FLAG'] == 1]

# Plot made shots using matplotlib
plt.figure(figsize=(10, 7))
plt.scatter(made_shots_x, made_shots_y, c='green', alpha=0.6, label='Made Shots')

plt.title("Stephen Curry - Made Shots")
plt.xlabel("Court X")
plt.ylabel("Court Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
