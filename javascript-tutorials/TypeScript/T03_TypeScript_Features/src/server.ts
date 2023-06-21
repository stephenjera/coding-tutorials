import { Calculator, log } from "./features"

// Defining an interface
interface Person {
  name: string
  age: number
  greet: (message: string) => void
}

// Implementing the interface
class Student implements Person {
  name: string
  age: number
  id: number

  constructor (name: string, age: number, id: number) {
    this.name = name
    this.age = age
    this.id = id
  }
  @log
  greet (message: string) {
    console.log(`${message}, ${this.name}`)
  }
}

// Using a generic type
function identity<T> (arg: T): T {
  return arg
}

let student = new Student('John Doe', 25, 1)
student.greet('Hello')

let output = identity<string>('myString')
console.log(output)


let calculator = new Calculator()
calculator.add(2, 3)

// Using a namespace
namespace MyMath {
  export function add (x: number, y: number): number {
    return x + y
  }
}

console.log(MyMath.add(2, 3))