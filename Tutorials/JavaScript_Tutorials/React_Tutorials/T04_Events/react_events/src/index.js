import React from 'react'
import ReactDOM from 'react-dom/client'

function Football () {
  const shoot = () => {
    alert('Great Shot!')
  }

  return <button onClick={shoot}>Take the shot!</button>
}

function FootballWithParameters () {
  const shoot = (a, b) => {
    alert(` ${a} from ${b.type}`)
    // 'b' represents the React event that triggered the function,
    // in this case the 'click' event
  }

  return (
    <button onClick={event => shoot('Goal!', event)}>
      Take the shot with parameters!
    </button>
  )
}

function MissedGoal () {
  return <h1>MISSED!</h1>
}

function MadeGoal () {
  return <h1>Goal!</h1>
}

function Goal (props) {
  const isGoal = props.isGoal
  return <div>{isGoal ? <MadeGoal /> : <MissedGoal />}</div>
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <div>
    <Football />
    <FootballWithParameters />
    <Goal isGoal={false} />
  </div>
)
