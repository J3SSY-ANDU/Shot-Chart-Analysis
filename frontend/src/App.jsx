import { useState, useEffect } from 'react'
import './App.css'
import CircularProgress from '@mui/material/CircularProgress';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

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
        setPlayers(() => data.players.map(player => ({
          label: `${player.firstname} ${player.lastname}`,
          firstname: player.firstname,
          lastname: player.lastname,
          id: player.id
        })))
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
      <div style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
        <Autocomplete
          disablePortal
          id="combo-box-demo"
          options={players}
          renderInput={(params) => <TextField {...params} label="Player Name"
            sx={{
              input: { color: 'white' },
              label: { color: 'white' },
              '& .MuiOutlinedInput-root': {
                '& fieldset': { borderColor: 'white' },
                '&:hover fieldset': { borderColor: '#646cff' },
                '&.Mui-focused fieldset': { borderColor: '#646cff' },
              },
            }}
            InputProps={{
              ...params.InputProps,
              sx: {
                '& .MuiInputBase-input': {
                  color: 'white', // input text
                },
                '& .MuiSvgIcon-root': {
                  color: 'white', // dropdown icon
                },
              },
            }} />}
          onChange={(event, value) => {
            if (value) {
              setFirstName(value.firstname)
              setLastName(value.lastname)
            } else {
              setFirstName('')
              setLastName('')
            }
          }}
        />

        <button onClick={handleGenerateChart} style={{ width: "180px", alignSelf: "center" }}>{loading ? <CircularProgress size={18} /> : "Generate"}</button>
      </div>
    </div>
  )
}

export default App
