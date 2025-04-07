from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

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
def get_player(name: str = Query(..., description="Player full name, e.g. Stephen Curry")):
    return {"player": name, "status": "request received"}
