import { useState, createContext, useContext } from 'react'

const UserContext = createContext()

export default function Component1 () {
  const [user, setUser] = useState('Jesse Hall')

  return (
    <UserContext.Provider value={user}>
      <h1>{`Hello ${user}!`}</h1>
      {<Component2 />}
    </UserContext.Provider>
  )
}

function Component2 () {
  return (
    <>
      <h2>Component 2</h2>
      <Component3 />
    </>
  )
}

function Component3 () {
  return (
    <>
      <h2>Component 3</h2>
      <Component4 />
    </>
  )
}

export function Component4 () {
  return (
    <>
      <h2>Component 4</h2>
      <Component5 />
    </>
  )
}

// state only used by component 5
export function Component5 () {
  const user = useContext(UserContext)

  return (
    <>
      <h1>Component 5</h1>
      <h2>{`Hello ${user} again!`}</h2>
    </>
  )
}
