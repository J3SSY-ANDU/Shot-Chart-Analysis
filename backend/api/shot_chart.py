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

def get_all_shots(player_id, team_id):
    response = shotchartdetail.ShotChartDetail(
        team_id=team_id,
        player_id=player_id,
        season_type_all_star='Regular Season',
        context_measure_simple='FGA'
    )
    shots = response.get_normalized_dict()['Shot_Chart_Detail']
    print(f"Fetched total shots: {len(shots)}")
    made = [s for s in shots if s['SHOT_MADE_FLAG'] == 1]
    print(f"Made shots: {len(made)}")
    return shots

def shot_chart(x, y, all_shots, firstname, lastname):
    filename = f"static/{firstname.lower()}_{lastname.lower()}_shot_chart.png"
    court_img = mpimg.imread("court.png")

    plt.figure(figsize=(10, 10))
    plt.xlim(-250, 250)
    plt.ylim(-50, 420)
    plt.imshow(court_img, extent=[-250, 250, -50, 420], zorder=0)
    plt.scatter(x, y, c='green', alpha=0.5, label='Made Shots')

    # FG%
    fg_percentage = round((len(x) / len(all_shots)) * 100, 1) if all_shots else 0

    # Annotations
    plt.text(-230, 400, f'{firstname} {lastname}', fontsize=14, color='white', backgroundcolor='black')
    plt.text(-230, 375, f'FG%: {fg_percentage}%', fontsize=12, color='white', backgroundcolor='black')

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return filename

def get_players():
    player_index = playerindex.PlayerIndex().get_normalized_dict()['PlayerIndex']
    players = [{"id": player['PERSON_ID'], "firstname": player['PLAYER_FIRST_NAME'], "lastname": player['PLAYER_LAST_NAME']} for player in player_index]
    return players


