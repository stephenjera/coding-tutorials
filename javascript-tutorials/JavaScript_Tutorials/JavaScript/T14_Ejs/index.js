const express = require('express')

const server = express()

server.set('view engine', 'ejs')

server.get('/', (req, res) => {
  // use render instead of send (render ejs template)
  // searches view by default
  res.render('index')
})

server.get('/about', (req, res) => {
  res.render('about')
})

server.listen(8080, () => {
  console.log('Express Server is running...')
})
