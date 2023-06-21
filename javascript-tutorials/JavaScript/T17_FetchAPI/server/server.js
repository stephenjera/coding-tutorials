import express from 'express'
import cors from 'cors'

const server = express()
server.use(
  cors({
    origin: '*'
  })
)
server.use(express.json())

server.get('/', async (req, res) => {
  res.send('Hello world')
})

server.post('/', async (req, res) => {
  console.log('request received')
  console.log(req.body)
})

server.listen(3000, () => {
  console.log(`Server listening on ${3000}`)
})
