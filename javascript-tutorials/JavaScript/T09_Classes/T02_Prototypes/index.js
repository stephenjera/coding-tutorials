// Using constructor functions and prototypes

//Person constructor function that takes
//two arguments: firstName and lastName.
function Person (firstName, lastName) {
  this.firstName = firstName
  this.lastName = lastName
}

// Define a method called greet
// on the Person.prototype object
Person.prototype.greet = function () {
  console.log(`Hello, ${this.firstName} ${this.lastName}!`)
}

// Using class syntax
class Person {
  constructor (firstName, lastName) {
    this.firstName = firstName
    this.lastName = lastName
  }
  // Define a method called greet
  // on the Person.prototype object
  greet () {
    console.log(`Hello, ${this.firstName} ${this.lastName}!`)
  }
}

// When we create new instances of Person using the
// new keyword (e.g., person1 and person2),
// these objects inherit from Person.prototype
const person1 = new Person('John', 'Doe')
person1.greet() // logs "Hello, John Doe!"

const person2 = new Person('Jane', 'Doe')
person2.greet() // logs "Hello, Jane Doe!"
