import express from 'express'
import createTable from './database.js'
import { credentials } from './database.js'
import pg from 'pg'
import cors from 'cors'

const PORT = process.env.PORT || 3001
const { Pool } = pg
const pool = new Pool(credentials)
const app = express()

/* middleware */
app.use(express.json())
app.use(cors)

/* Routes */
// Get all events
app.get('/allEvents', async (req, res) => {
  try {
    console.log('running get all events')
    const allEvents = await pool.query('select * from events ')
    res.json(allEvents.rows)
  } catch (err) {
    console.error(err.message)
  }
})

// Get event
app.get('/events/:id', async (req, res) => {
  try {
    // const allEvents = await pool.query('select * from events ')

    const { id } = req.params
    const event = await pool.query('select * from events where id = $1', [id])
    res.json(event.rows[0])
    //console.log(req.params)
  } catch (err) {
    console.error(err.message)
  }
})

// Add event
app.post('/addEvent', async (req, res) => {
  try {
    //const { events } = req.body
    console.log(req.body)
    const newEvent = await pool.query(
      'insert into events (event) values($1) returning *',
      [req.body]
    )
    res.json(newEvent.rows)
  } catch (err) {
    console.error(err.message)
  }
})

// Update event
app.put('/events/:id', async (req, res) => {
  try {
    const { id } = req.params
    //const { description } = req.body
    console.log(req.body)
    const newEvent = await pool.query(
      'update events set event = $1 where id = $2',
      [req.body, id]
    )
    res.json('event was updated')
  } catch (err) {
    console.error(err.message)
  }
})

// Delete event
app.delete('/events/:id', async (req, res) => {
  try {
    const { id } = req.params
    const deleteEvent = await pool.query('delete from events where id = $1;', [
      id
    ])
    res.json('event was deleted')
  } catch (err) {
    console.error(err.message)
  }
})

createTable()

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`)
})
