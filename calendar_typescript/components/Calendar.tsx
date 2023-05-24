'use client'
import FullCalendar from '@fullcalendar/react'
import { DateSelectArg, EventClickArg, EventDropArg } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { EventResizeDoneArg } from '@fullcalendar/interaction'
import { useState } from 'react'

const initialEvents = [
  { id: '1', title: 'Event 1', start: '2023-05-01', end: '2023-05-02' },
  { id: '2', title: 'Event 2', start: '2023-05-05', end: '2023-05-07' }
]

export default function Calendar () {
  const [events, setEvents] = useState(initialEvents)

  const handleSelect = (selectionInfo: DateSelectArg) => {
    const title = prompt('Please enter a title for your event')
    if (title) {
      const newEvent = {
        id: (events.length + 1).toString(),
        title,
        start: selectionInfo.startStr,
        end: selectionInfo.endStr
      }
      setEvents([...events, newEvent])
    }
  }

  const handleEventClick = (clickInfo: EventClickArg) => {
    const title = prompt('Please enter a new title for your event')
    if (title) {
      const updatedEvents = events.map(event => {
        if (event.id === clickInfo.event.id) {
          return { ...event, title }
        }
        return event
      })
      setEvents(updatedEvents)
    }
  }

  const handleEventDrop = (dropInfo: EventDropArg) => {
    const updatedEvents = events.map(event => {
      if (event.id === dropInfo.event.id) {
        return {
          ...event,
          start: dropInfo.event.start
            ? dropInfo.event.start.toISOString()
            : event.start,
          end: dropInfo.event.end ? dropInfo.event.end.toISOString() : event.end
        }
      }
      return event
    })
    setEvents(updatedEvents)
  }

  const handleEventResize = (resizeInfo: EventResizeDoneArg) => {
    const updatedEvents = events.map(event => {
      if (event.id === resizeInfo.event.id) {
        return {
          ...event,
          start: resizeInfo.event.start
            ? resizeInfo.event.start.toISOString()
            : event.start,
          end: resizeInfo.event.end
            ? resizeInfo.event.end.toISOString()
            : event.end
        }
      }
      return event
    })
    setEvents(updatedEvents)
  }

  return (
    <div className='w-full max-w-4xl mx-auto'>
      <FullCalendar
        plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
        initialView={'dayGridMonth'}
        headerToolbar={{
          start: 'today prev,next',
          center: 'title',
          end: 'dayGridMonth,timeGridWeek,timeGridDay'
        }}
        height='auto'
        contentHeight='auto'
        weekends={true}
        editable={true}
        selectable={true}
        droppable={true}
        eventDurationEditable={true}
        eventStartEditable={true}
        eventResizableFromStart={true}
        select={handleSelect}
        eventClick={handleEventClick}
        eventDrop={handleEventDrop}
        eventResize={handleEventResize}
        events={events}
        eventDisplay='block'
      />
    </div>
  )
}
