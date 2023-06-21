// With require
const { readFile } = require('fs')

// const PI = Math.PI;
// const E = Math.E;
// const SQRT2 = Math.SQRT2;

const {stringify} = JSON
const { PI, E, SQRT2 } = Math // simplifies above code

const circle = {
  label: 'circleX',
  radius: 2
}

// get only required properties from objects
const circleArea = (
  { radius },
  { precision = 2 } = {} /* '=' makes precision optional*/
) => (PI * radius * radius).toFixed(precision)

console.log(circleArea(circle))
console.log(circleArea(circle, { precision: 4 }))

// Works with arrays too
const [first, second, , forth] = [1, 2, 3, 4] // skip the 3rd
const [number, ...rest] = [5, 6, 7, 8] // create new array for rest of elements

// filter objects
const data = {
  temp1: '001',
  temp2: '002',
  firstName: 'John',
  lastName: 'Doe'
}

// These are shallow copies so nested objects will be shared
const { temp1, temp2, ...person } = data
console.log(`person: ${stringify(person)}`)

const newArray = [...rest]
console.log(`newArray: ${newArray}`)

const newObject = {
  ...person
}
console.log(`newObj: ${stringify(newObject)}`)
