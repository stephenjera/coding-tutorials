import EditEvent from "./EditEvent"

const EventItem = ({ info }) => {
  const { event } = info
  return (
    <div>
      <p>{event.title}</p>
      <EditEvent/>
    </div>
  )
}

export default EventItem
