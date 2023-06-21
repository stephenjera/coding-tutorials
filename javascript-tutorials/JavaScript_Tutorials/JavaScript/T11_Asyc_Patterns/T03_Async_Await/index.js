// The keyword async before a function makes the function return a promise:
async function myFunction () {
  return 'Hello'
}
myFunction().then(
  function (value) {
    /* code if successful */
  },
  function (error) {
    /* code if some error */
  }
)

// same as above code
function myFunction2 () {
  return Promise.resolve('Hello')
}
myFunction2().then(
  function (value) {
    /* code if successful */
  },
  function (error) {
    /* code if some error */
  }
)

// The await keyword can only be used inside an async function.
// The await keyword makes the function pause the execution and wait for a resolved promise before it continues:
async function myDisplay () {
  let myPromise = new Promise(function (resolve) {
    setTimeout(function () {
      resolve('I love You !!')
    }, 3000)
  })
  console.log(await myPromise)
}

myDisplay()
