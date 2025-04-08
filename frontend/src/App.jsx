import { useState } from 'react'
import './App.css'

function App() {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()
    console.log('Submitting:', { firstName, lastName })
    try {
      await fetch(`/api/player?firstname=${firstName}&lastname=${lastName}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <div>
      <input type='text' placeholder='First Name' value={firstName} onChange={(e) => setFirstName(e.target.value)} />
      <input type='text' placeholder='Last Name' value={lastName} onChange={(e) => setLastName(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  )
}

export default App
