const person = {
  firstName: 'John',
  lastName: 'Doe',
  id: 5566,
  fullName: function () {
    return this.firstName + ' ' + this.lastName
  }
}

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
