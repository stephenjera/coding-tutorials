const func = function () {
  // "this" is th caller of x
}

const arrow = () => {
  // "this" here i not the caller of arrow
  // it is the same "this" in arrow's scope
}

// "this" here is "exports"

this.id = 'exports'

const testerObj = {
  func1: function () {
    console.log('func1', this)
  },

  func2: () => {
    console.log('func2', this)
  }
}

testerObj.func1() // "this" is the caller of x: testerObj
testerObj.func2() // "this" is the this in scope : 'exports'
