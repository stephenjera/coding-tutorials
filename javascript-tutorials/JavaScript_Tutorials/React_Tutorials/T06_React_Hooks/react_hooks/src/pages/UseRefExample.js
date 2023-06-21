import { useState, useEffect, useRef } from 'react'

export default function Ref () {
  const [inputValue, setInputValue] = useState('')
  const previousInputValue = useRef('')

  useEffect(() => {
    previousInputValue.current = inputValue
  }, [inputValue])

  return (
    <>
      <label>Type something: </label>
      <input
        type='text'
        value={inputValue}
        onChange={e => setInputValue(e.target.value)}
      />
      <h2>Current Value: {inputValue}</h2>
      <h2>Previous Value: {previousInputValue.current}</h2>
      <hr />
    </>
  )
}
