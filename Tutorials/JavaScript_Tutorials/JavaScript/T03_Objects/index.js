const unknown = "meaning" 
const PI = Math.PI

// what properties objects support
const obj = {
    p1: 10,
    p2: 20,
    f1() {},
    f2: () => {},
    // dynamic properties not to be mistaken for an array
    [unknown]: 42, // meaning is evaluated to meaning
    'stringPI': PI,
    PI // same as above line, shorthand syntax
  };


const person = {
  firstName: 'John',
  lastName: 'Doe',
  id: 5566,
  fullName: function () {
    return this.firstName + ' ' + this.lastName
  }
}

console.log(`obj.unknown: ${obj.unknown}`)
console.log(`obj.meaning: ${obj.meaning}`)
console.log(`obj.PI: ${obj.PI}`)
console.log(`obj.stringPI: ${obj.stringPI}`)
console.log(`obj.f1: ${obj.f1}`)
console.log(`obj.f2: ${obj.f2}`)

console.log()

console.log(`First name: ${person.firstName}`)
console.log(`Last name: ${person.lastName}`)
console.log(`Full name: ${person.fullName()}`)
console.log(`Full name function: ${person.fullName}`)

let x = new String('John')
let y = new String('John')

console.log()
console.log('Comparing JS objects always results in false')
console.log(`(x == y): ${(x == y)}`)
console.log(`(x === y): ${(x === y)}`)
