from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from api.shot_chart import get_player_id, get_team_id, shot_chart, get_players, get_all_shots

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "NBA Shot Chart API is running."}

@app.get("/player")
def get_player(firstname: str = Query(...), lastname: str = Query(...)):
    player_id = get_player_id(firstname, lastname)
    if not player_id:
        raise HTTPException(status_code=404, detail="Player not found")
    team_id = get_team_id(player_id)
    all_shots = get_all_shots(player_id, team_id)
    made_x = [shot['LOC_X'] for shot in all_shots if shot['SHOT_MADE_FLAG'] == 1]
    made_y = [shot['LOC_Y'] for shot in all_shots if shot['SHOT_MADE_FLAG'] == 1]

    chart_path = shot_chart(made_x, made_y, all_shots, firstname, lastname)
    return FileResponse(chart_path, media_type="image/png")

@app.get("/players")
def get_players_names():
    """
    Get all players.
    """
    players = get_players()
    return {"players": players}
