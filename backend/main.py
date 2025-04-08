from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from api.shot_chart import get_player_id, get_team_id, get_made_shots, shot_chart

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
def get_player(firstname: str = Query(..., description="Player firstname, e.g. Stephen"), 
               lastname: str = Query(..., description="Player lastname, e.g. Curry")):
    """
    Get the shot chart for a player.
    """
    player_id = get_player_id(firstname, lastname)
    team_id = get_team_id(player_id)
    made_shots_x, made_shots_y = get_made_shots(player_id, team_id)
    shot_chart(made_shots_x, made_shots_y)
    return {"player": f"{firstname} + {lastname}", "status": "request received"}
