import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [players, setPlayers] = useState([])

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

  const handleSubmit = async (event) => {
    event.preventDefault()
    try {
      const res = await fetch(`/api/player?firstname=${firstName}&lastname=${lastName}`)
      const blob = await res.blob()
      const url = URL.createObjectURL(blob)
      window.open(url) // or set state to render <img src={url} />
    } catch (error) {
      console.error('Error:', error)
    }
  }
  
  return (
    <div className='App'>
      <h1>NBA Shot Chart Analysis by Player</h1>
      <h2>Players</h2>
      <select 
        onChange={(e) => {
          const selectedId = parseInt(e.target.value)
          const selectedPlayer = players.find(p => p.id === selectedId)
          if (selectedPlayer) {
            setFirstName(selectedPlayer.firstname)
            setLastName(selectedPlayer.lastname)
          }
        }}
      >
        <option value=''>Select a player</option>
        {players.map((player) => (
          <option key={player.id} value={player.id}>
            {player.firstname} {player.lastname}
          </option>
        ))}
      </select>
      <button onClick={handleSubmit}>Submit</button>
    </div>
  )
}

export default App
