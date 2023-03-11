import React, { useState, useCallback } from 'react'
import Fullcalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { v4 as uuid } from 'uuid'
import EventItem from './EventItem'

const { stringify } = JSON

function Calendar () {
  //const [events, setEvents] = useState([])
  const [events, setEvents] = useState([
    {
      start: new Date(2023, 3, 14, 8, 0),
      end: new Date(2023, 3, 12, 17, 0),
      title: 'My First Event'
    },
    {
      start: new Date(2020, 2, 18, 9, 0),
      end: new Date(2020, 2, 20, 13, 0),
      title: 'My Second Event'
    }
  ])
  const addEvent = useCallback(() => {
    const newEvent = {
      id: uuid(),
      start: new Date(2023, 2, 18, 9, 0),
      end: new Date(2023, 2, 20, 13, 0),
      title: 'My New Event'
    }
    setEvents([...events, newEvent])
    console.log('event added')
  }, [events])

  const deleteEvent = useCallback(
    eventId => {
      // Create a copy of the event array
      const newEvents = [...events]
      // Find the index of the event to be deleted
      const index = events.indexOf(
        events.filter(event => event.id === eventId)[0]
      )
      // Remove the event from the array
      newEvents.splice(index, 1)
      // Pass the new array to the calendar
      setEvents(newEvents)
    },
    [events]
  )

  const updateEvent = useCallback(
    updatedEvent => {
      const index = events.indexOf(
        events.filter(event => event.id === updatedEvent.id)[0]
      )
      events[index] = updatedEvent
      // Create a copy of the event array
      setEvents([...events])
    },
    [events]
  )

  const handleDateClick = arg => {
    // bind with an arrow function
    console.log(`handleDateClick: ${stringify(arg)}`)
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
          weekends={true}
          editable={false}
          selectable={true}
          //*select={handleSelect}
          dateClick={addEvent}
          events={events}
          eventContent={info => <EventItem info={info} />}
        />
      </div>
    </div>
  )
}

export default Calendar
