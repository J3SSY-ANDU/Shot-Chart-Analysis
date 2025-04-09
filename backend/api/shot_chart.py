from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerindex
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend
import matplotlib.image as mpimg


def get_player_id(firstname, lastname):
    player_index = playerindex.PlayerIndex().get_normalized_dict()['PlayerIndex']
    for player in player_index:
        if player['PLAYER_LAST_NAME'] == lastname and player["PLAYER_FIRST_NAME"] == firstname:
            return player['PERSON_ID']

def get_team_id(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()['CommonPlayerInfo'][0]
    return player_info['TEAM_ID']

def get_made_shots(player_id, team_id):
    shot_details = shotchartdetail.ShotChartDetail(team_id=team_id, player_id=player_id).get_normalized_dict()['Shot_Chart_Detail']
    # Filter only made shots
    made_shots_x = [shot['LOC_X'] for shot in shot_details if shot['SHOT_MADE_FLAG'] == 1]
    made_shots_y = [shot['LOC_Y'] for shot in shot_details if shot['SHOT_MADE_FLAG'] == 1]
    return made_shots_x, made_shots_y

def shot_chart(x, y, filename="static/shot_chart.png"):
    court_img = mpimg.imread("court.png")

    plt.figure(figsize=(10, 10))
    plt.xlim(-250, 250)
    plt.ylim(-50, 420)
    plt.imshow(court_img, extent=[-250, 250, -50, 420], zorder=0)
    plt.scatter(x, y, c='green', alpha=0.5, label='Made Shots')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return filename

def get_players():
    player_index = playerindex.PlayerIndex().get_normalized_dict()['PlayerIndex']
    players = [{"id": player['PERSON_ID'], "firstname": player['PLAYER_FIRST_NAME'], "lastname": player['PLAYER_LAST_NAME']} for player in player_index]
    return players



