// Defining an enum
enum Color {
  Red = 1, // chose starting point of enum
  Green,
  Blue
}

// Defining a tuple
let myTuple: [string, number]
myTuple = ['hello', 42]

// Using a union type
function printId (id: number | string) {
  console.log(`ID: ${id}`)
}

// Using an intersection type
interface Shape {
  area: number
}
interface Circle {
  radius: number
}
type CircleShape = Shape & Circle

// Using a type guard
function printLength (x: string | number) {
  if (typeof x === 'string') {
    console.log(x.length)
  } else {
    console.log(x)
  }
}

// Using a decorator
function log (
  target: Object,
  propertyKey: string,
  descriptor: TypedPropertyDescriptor<any>
) {
  let originalMethod = descriptor.value
  descriptor.value = function (...args: any[]) {
    console.log(`Arguments: ${args}`)
    let result = originalMethod.apply(this, args)
    console.log(`Result: ${result}`)
    return result
  }
}

class Calculator {
  @log
  add (x: number, y: number): number {
    return x + y
  }
}

export{
    Calculator,
    log,
    printLength
}