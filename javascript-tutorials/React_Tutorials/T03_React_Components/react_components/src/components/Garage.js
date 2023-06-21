// Components in components
import CarFunc from './CarFunc'

export default function Garage () {
  const carName = { name: 'Ford', model: 'Mustang' }
  return (
    <div>
      <h1>Who lives in my garage?</h1>
      <CarFunc brand={carName.name} />
    </div>
  )
}
