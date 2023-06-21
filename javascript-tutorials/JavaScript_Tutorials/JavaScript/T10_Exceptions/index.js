const path = require('path')
const fs = require('fs')

const files = ['example.txt', 'kjkjhh', '.npmrc']

files.forEach(file => {
  try {
    const filePath = path.resolve(file) // a way to get file paths not required here
    const data = fs.readFileSync(filePath, 'utf-8')
    console.log('File data is:', data)
  } catch (err) {
    if (err.code === 'ENOENT') {
      /* Error NO ENTry (or Error NO ENTity),*/
      console.log('File not found')
    } else {
      throw err
    }
  }
})
