function doAsyncWork (resolve, reject) {
  // do work
}

// using named function
let myPromise = new Promise(doAsyncWork)

// using anonymous function (arrow function)
let anotherPromise = new Promise((resolve, reject) => {})

methodThatReturnsPromise()
  .then(data => console.log(data)) // called when resolved
  .catch(error => console.log(error)) // called when rejected
  .finally(() => console.log('All done')) // called when everything is done
