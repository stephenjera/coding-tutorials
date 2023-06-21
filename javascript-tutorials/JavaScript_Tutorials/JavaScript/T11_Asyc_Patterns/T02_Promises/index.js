// A JavaScript Promise object contains both the producing code and calls to the consuming code:
let myPromise = new Promise(function (resolve, reject) {
  // "Producing Code" (May take some time)

  resolve() // when successful
  reject() // when error
})

//Promise.then() takes two arguments, a callback for success and another for failure.
// "Consuming Code" (Must wait for a fulfilled Promise)
myPromise.then(
  function (value) {
    /* code if successful */
  },
  function (error) {
    /* code if some error */
  }
)

//Call back vs promise
setTimeout(function () {
  myFunction('I love You !!!')
}, 3000)

function myFunction (value) {
  console.log(value)
}

// Promise
let myPromise2 = new Promise(function (resolve, reject) {
  setTimeout(function () {
    resolve('I love You !!')
  }, 3000)
})

myPromise2.then(function (value) {
  console.log(value)
})
