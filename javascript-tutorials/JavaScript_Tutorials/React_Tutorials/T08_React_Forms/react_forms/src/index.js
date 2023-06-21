import { useState } from 'react'
import ReactDOM from 'react-dom/client'

function MyForm () {
  const [inputs, setInputs] = useState({})

  const handleChange = event => {
    const name = event.target.name
    const value = event.target.value
    setInputs(values => ({ ...values, [name]: value }))
  }

  const handleSubmit = event => {
    event.preventDefault()
    //alert(inputs)
    console.log(inputs)
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Enter your name:
        <input
          type='text'
          name='username'
          value={inputs.username || ''}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Enter your age:
        <input
          type='number'
          name='age'
          value={inputs.age || ''}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Email:
        <input
          type='email'
          name='email'
          placeholder='placeholder@mail.com'
          value={inputs.email || ''}
          onChange={handleChange}
          required
        />
      </label>
      <br />
      <label>
        Password:
        <input
          type='password'
          name='password'
          maxLength='25'
          value={inputs.password || ''}
          onChange={handleChange}
          required
        />
      </label>

      <br />
      <input type='submit' />
      <input type='reset' />
    </form>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<MyForm />)
