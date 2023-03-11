import express from 'express'
import createTable from './db.js'
import { credentials } from './db.js'
import pg from 'pg'

const PORT = process.env.PORT || 3001
const { Pool } = pg
const app = express()

/* middleware */
app.use(express.json())

/* Routes */

// Add event
app.post('/addEvent', async (req, res) => {
  try {
    const pool = new Pool(credentials)
    const { description } = req.body
    console.log(req.body)
    const newEvent = await pool.query(
      "INSERT INTO events (event) values($1) returning *", [req.body]
    )
    res.json(newEvent.rows)
  } catch (err) {
    console.error(err.message)
  }
})

// Update event

// Delete event

createTable()

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`)
})
