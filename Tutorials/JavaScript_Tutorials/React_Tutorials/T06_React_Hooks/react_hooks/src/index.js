import { useState, useEffect } from 'react'
import ReactDOM from 'react-dom/client'

// The React useState Hook allows us to track state in a function component.
// State generally refers to data or properties that need to be tracking in an application.

function Car () {
  // useState returns current state and function to change state
  const [car, setCar] = useState({
    brand: 'Ford',
    model: 'Mustang',
    year: '1964',
    color: 'red'
  })

  const updateColor = () => {
    setCar(previousState => {
      // update only the colour and not overwrite previous data
      return { ...previousState, color: 'blue' }
    })
  }

  return (
    <>
      <h1>My {car.brand}</h1>
      <p>
        It is a {car.color} {car.model} from {car.year}.
      </p>
      <button type='button' onClick={updateColor}>
        Blue
      </button>
    </>
  )
}


function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    let timer = setTimeout(() => {
    setCount((count) => count + 1);
  }, 1000);
  // clean up timer to prevent memory leaks (uses return)
  return () => clearTimeout(timer)
  }, []); // run only when dependencies change [] = run once

  return <h1>I've rendered {count} times!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <>
    <Car /> 
    <Timer />
  </>
)
