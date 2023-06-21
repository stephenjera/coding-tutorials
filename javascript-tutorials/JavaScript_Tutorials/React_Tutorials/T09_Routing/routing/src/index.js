import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './pages/Layout'
import Home from './pages/Home'
import MyForm from './pages/Form'
import NoPage from './pages/NoPage'

export default function App () {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />}>
          {/* index is the home page and point to '/' */}
          <Route index element={<Home />} />
          {/* '*' catches all pages */}
          <Route path='*' element={<NoPage />} />
          <Route path='form' element={<MyForm />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<App />)
