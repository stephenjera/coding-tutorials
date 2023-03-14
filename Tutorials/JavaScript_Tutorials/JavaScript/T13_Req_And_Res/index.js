const http = require('http')

requestListener = (req, res) => {
  // req and res are streams
  console.dir(req, { depth: 0 })
  console.log()
  console.log(res, { depth: 0 })

  res.write('Hello World\n')
  res.end()
}

const server = http.createServer(requestListener)
server.on('request', requestListener)

server.listen(8080, () => {
  console.log('Server is running...')
})
