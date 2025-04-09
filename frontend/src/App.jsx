import { useState, useEffect } from 'react'
import './App.css'
import CircularProgress from '@mui/material/CircularProgress';

function App() {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [players, setPlayers] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await fetch('/api/players')
        const data = await response.json()
        console.log('Fetched players:', data)
        setPlayers(data.players)
      } catch (error) {
        console.error('Error fetching players:', error)
      }
    }

    fetchPlayers()
  }, [])

  const handleGenerateChart = async (event) => {
    event.preventDefault()
    try {
      setLoading(true)
      const res = await fetch(`/api/player?firstname=${firstName}&lastname=${lastName}`)
      const blob = await res.blob()
      const url = URL.createObjectURL(blob)
      window.open(url) // or set state to render <img src={url} />
      setLoading(false)
    } catch (error) {
      console.error('Error:', error)
      setLoading(false)
    }
  }
  
  return (
    <div className='App'>
      <h1>NBA Shot Chart Analysis by Player</h1>
      <div style={{display: "flex", flexDirection: "column", gap: "2rem"}}>
        <select 
          onChange={(e) => {
            const selectedId = parseInt(e.target.value)
            const selectedPlayer = players.find(p => p.id === selectedId)
            if (selectedPlayer) {
              setFirstName(selectedPlayer.firstname)
              setLastName(selectedPlayer.lastname)
            }
          }}
          style={{padding: "0.5rem 0 0.5rem 0", fontSize: "1rem"}}
        >
          <option value=''>Select a player</option>
          {players.map((player) => (
            <option key={player.id} value={player.id}>
              {player.firstname} {player.lastname}
            </option>
          ))}
        </select>
        <button onClick={handleGenerateChart} style={{width: "180px", alignSelf: "center"}}>{loading ? <CircularProgress size={18}/> : "Generate"}</button>
      </div>
    </div>
  )
}

export default App
