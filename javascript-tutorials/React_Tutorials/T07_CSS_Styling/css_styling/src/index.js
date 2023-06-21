import React from 'react'
import ReactDOM from 'react-dom/client'
import styles from './styles.module.css'
import './index.css'
import './sass_styles.scss'

const Header = () => {
  return (
    <>
      <h1 className={styles.bigblue}>Hello Style!</h1>
      <p>Add a little style!.</p>
    </>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<Header />)
