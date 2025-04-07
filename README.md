# 🏀 NBA Shot Chart Analysis

## 📌 Project Overview
This project is a fullstack web app that allows users to search for an NBA player by name and generate a **shot chart** based on real game data. The backend fetches player and shot data using the `nba_api`, and the frontend displays it as a visual court overlay with made/missed shots or density plots.

---

## 🚀 Features
- 🔍 Search by player name (e.g. *Stephen Curry*)
- 📡 Backend uses `nba_api` to fetch shot data
- 📈 Visualize shot locations using **scatter plots** or **density maps**
- 🏀 Overlay charts on a realistic half-court image
- 💻 Frontend built with React + Vite
- ⚙️ Backend powered by FastAPI

---

## 🧱 Tech Stack

### 🔹 Frontend
- React (Vite)
- Axios – API communication

### 🔹 Backend
- FastAPI – Lightweight Python web server
- nba_api – NBA data source
- matplotlib / seaborn – Visualization tools
- pandas / numpy – Data manipulation

---

## 🧪 How It Works

1. User enters a player's name in the React frontend.
2. The name is sent to the FastAPI backend.
3. Backend uses `nba_api` to fetch:
   - Player ID
   - Team ID
   - Shot chart data
4. Backend generates a chart and returns it (as image or data).
5. Frontend displays the result over a court.

---

## 📥 Installation

### 🔧 Backend Setup

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

### 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 🪪 License
This project is licensed under the [MIT License](LICENSE).
