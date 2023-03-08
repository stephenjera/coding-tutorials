const theOne = delay => {
  console.log(`${delay} seconds has passed`)
}

setTimeout(theOne, 4 * 1000, 4)
setTimeout(theOne, 8 * 1000, 8)

setInterval(() => console.log("2 seconds have passed"), 2*1000)

const timerId = setTimeout(() => console.log('a timer was lost today'),0)
console.log(timerId)
clearTimeout(timerId)


// Print once a second 5 times then end 
let counter = 0 
const intervalId = setInterval(() => {
    console.log("Hello Moto")
    counter += 1

    if (counter == 5) {
        console.log("Done")
        clearInterval(intervalId)
    }
}, 1000) 

