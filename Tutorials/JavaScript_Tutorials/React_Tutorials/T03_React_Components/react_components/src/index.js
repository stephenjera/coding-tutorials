import React from 'react'
import ReactDOM from 'react-dom/client'
import CarClass from './components/CarClass'
import CarFunc from './components/CarFunc'
import CarProps from './components/CarProps'
import Garage from './components/Garage'



const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <div>
    <CarClass />
    <CarFunc />
    <CarProps color='blue' />
    <Garage/>
  </div>
)
