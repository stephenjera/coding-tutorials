// '*' used to denote generator function
function* generatorFunction () {
  console.log('generator is running')

  let x = 5
  yield x // yield returns value then pauses execution until resumed
  // starts here on next call
  x++

  y = yield x
  console.log(`value of x ${x} value of y ${y}`)
  return x + y
}

let iterator = generatorFunction() // returns a generator object
console.log(iterator)

// lazy evaluation unless next method is used
console.log(iterator.next())
// function exits here because return was used not yield
console.log(iterator.next())

// the value of y is the 4 passed as the argument
console.log(iterator.next(4))

console.log('All done')
