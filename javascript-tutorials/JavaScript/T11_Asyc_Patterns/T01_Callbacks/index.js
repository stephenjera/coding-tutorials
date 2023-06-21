function myDisplayer (some) {
  console.log(some)
}

function myCalculator (num1, num2) {
  let sum = num1 + num2
  // Cannot prevent the calculator function from displaying the result.
  myDisplayer(sum)
}

myCalculator(5, 5)

// Using a call back function
function myCalculatorCb (num1, num2, myCallback) {
  let sum = num1 + num2
  myCallback(sum)
}

myCalculatorCb(7, 5, myDisplayer)

// Create an Array
const myNumbers = [4, 1, -20, -7, 5, 9, -6]

// Call removeNeg with a callback
const posNumbers = removeNeg(myNumbers, (x) => x >= 0)

// Display Result
console.log(posNumbers)

// Keep only positive numbers
function removeNeg (numbers, callback) {
  const myArray = []
  for (const x of numbers) {
    if (callback(x)) {
      myArray.push(x)
    }
  }
  return myArray
}
