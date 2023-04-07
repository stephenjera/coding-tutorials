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

  const handleSelect = info => {
    console.log(`info: ${stringify(info)}`)
    setModalShow(true)
    const { start, end } = info
    console.log(info)
    setEvents([
      ...events,
      {
        start,
        end,
        title: 'Enter Title',
        id: uuid()
      }
    ])
    //const eventNamePrompt = prompt('Enter, event name')
    // if (eventNamePrompt) {
    //   setEvents([
    //     ...events,
    //     {
    //       start,
    //       end,
    //       title: eventNamePrompt,
    //       id: uuid()
    //     }
    //   ])
    // }
  }
  const onSubmitForm = async e => {
    console.log('onSubmitForm called')
    e.preventDefault()
    try {
      setEvents(previousState => {
        // update only the colour and not overwrite previous data
        return { ...previousState, title: 'blue' }
      })

      const body = events
      const response = await fetch('http://localhost:3001/addEvent', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: stringify(body)
      })
      const responseData = await response.json()
      console.log(responseData)
    } catch (err) {
      console.error(err.message)
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
          events={events}
          eventDisplay='block'
          eventContent={events => <EventItem info={events} />}
        />
        <EditEvent
          onSubmitForm={onSubmitForm}
          events={events}
          show={modalShow}
          onHide={() => setModalShow(false)}
        />
      </div>
    </div>
  )
}

export default Calendar
