let text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let length = text.length
let start = 3
let end = 15

// All string methods return a new string 

console.log(text.slice(start, end))
console.log(text.slice(-12, -6)) // count backwards if negative
console.log(text.substring(start, end))
console.log(text.replace(text.slice(start, end), 'yes'))
console.log(text.replace(/abc/i, 'regex'))
console.log(text.toLocaleLowerCase())
console.log(text.concat(" ", text.toLowerCase()))
console.log(text.split(" "))
console.log(text.split(""))
console.log(`Text is unchanged: ${text}`)
