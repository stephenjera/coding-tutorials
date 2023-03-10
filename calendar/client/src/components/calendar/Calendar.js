import React, { useState } from 'react'
import Fullcalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { v4 as uuid } from 'uuid'

let handleDateClick = arg => {
  // bind with an arrow function
  console.log(arg.dateStr)
}

function Calendar () {
  const [events, setEvents] = useState([])

  const handleSelect = info => {
    const { start, end } = info
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
          weekends={false}
          editable={true}
          selectable={true}
          select={handleSelect}
          dateClick={handleDateClick}
          events={events}
        />
      </div>
    </div>
  )
}

export default Calendar
