import React, { useState } from 'react'
import Fullcalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { v4 as uuid } from 'uuid'
import 'bootstrap/dist/css/bootstrap.min.css'
import EditEvent from './EditEvent'
import EventItem from './EventItem'

const { stringify } = JSON

function Calendar () {
  const [events, setEvents] = useState([])
  const [modalShow, setModalShow] = React.useState(false)
  const handleDateClick = arg => {
    // bind with an arrow function
    console.log(`handleDateClick: ${stringify(arg)}`)
    setModalShow(true)
  }

  const handleSelect = info => {
    console.log(`info: ${stringify(info)}`)
    const { start, end } = info
    console.log(info)
    const eventNamePrompt = prompt('Enter, event name')
    if (eventNamePrompt) {
      setEvents([
        ...events,
        {
          start,
          end,
          title: eventNamePrompt,
          id: uuid()
        }
      ])
    }
  }

  return (
    <div>
      <div>
        <Fullcalendar
          plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
          initialView={'dayGridMonth'}
          headerToolbar={{
            start: 'today prev,next', // will normally be on the left. if RTL, will be on the right
            center: 'title',
            end: 'dayGridMonth,timeGridWeek,timeGridDay' // will normally be on the right. if RTL, will be on the left
          }}
          height='auto'
          contentHeight='auto'
          weekends={true}
          editable={false}
          selectable={true}
          select={handleSelect}
          dateClick={handleDateClick}
          events={events}
          eventContent={info => <EventItem info={info} />}
        />
        <EditEvent show={modalShow} onHide={() => setModalShow(false)} />
      </div>
    </div>
  )
}

export default Calendar
