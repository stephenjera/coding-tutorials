// Components can be passed as props, which stands for properties.
// Props are like function arguments, and you send them into the component as attributes.
export default function CarProps (props) {
  return (
    <h2>
      I am a {props.color} Car! Made with ❤️ from functions and
      properties(props)
    </h2>
  )
}
