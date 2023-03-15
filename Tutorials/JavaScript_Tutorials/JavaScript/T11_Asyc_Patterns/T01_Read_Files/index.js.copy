const fs = require('fs')
const util = require('util')

// get readFile to default to promises
// const { readFile } = require('fs').promises

// Synchronous method: get data when function is called
const data = fs.readFileSync(__filename)

console.log('File data is', data)
console.log('TEST1')

// Using a callback goes through event loop
// readfile ran and asked for data then in first event loop
// callback ran in next event loop
fs.readFile(__filename, function cb1 (err, data) {
  // callback must me nested if they depend on each other
  fs.writeFile(__filename + '.copy', data, function cb2 (err) {
    // Nest more callbacks here...
  })
})

console.log('TEST2')

//
const readFile = util.promisify(fs.readFile)

async function main () {
  const data = await readFile(__filename)
  console.log('File data is', data)
}

main()

console.log('TEST3')


//const fs = require('fs').promises <- replace above require to stop error

// async function main () {
//   const data = await fs.readFile(__filename)
//   await fs.writeFile(__filename + '.copy', data)
//   // More awaits here...
// }

// main()
console.log('TEST4')
