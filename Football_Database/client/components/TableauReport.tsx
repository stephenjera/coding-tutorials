'use client'

import React, { useEffect } from 'react'
import Image from 'next/image'

interface TableauReportProps {
  reportId: string
}

const TableauReport: React.FC<TableauReportProps> = ({ reportId }) => {
  useEffect(() => {
    const divElement = document.getElementById(reportId)
    const vizElement = divElement!.getElementsByTagName('object')[0]!

    const resizeReport = () => {
      if (divElement!.offsetWidth > 800) {
        vizElement!.style.width = '100%'
        vizElement!.style.height = window.innerHeight + 'px' //`${divElement!.offsetWidth * 0.75}px`
      } else if (divElement!.offsetWidth > 500) {
        vizElement!.style.width = '100%'
        vizElement!.style.height = window.innerHeight + 'px' //`${divElement!.offsetWidth * 0.75}px`
      } else {
        vizElement!.style.width = '100%'
        vizElement!.style.height = '927px'
      }
    }

    resizeReport()

    const scriptElement = document.createElement('script')
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'
    vizElement!.parentNode!.insertBefore(scriptElement, vizElement)

    window.addEventListener('resize', resizeReport)

    return () => {
      window.removeEventListener('resize', resizeReport)
    }
  }, [reportId])

  return (
    <div
      className='tableauPlaceholder'
      id={reportId}
      style={{ position: 'relative' }}
    >
      <noscript>
        <a href='#'>
          <Image
            alt='Football Dashboard'
            src='https://public.tableau.com/static/images/An/AnalysingFootballData/Dashboard1/1_rss.png'
            style={{ border: 'none' }}
          />
        </a>
      </noscript>
      <object className='tableauViz' style={{ display: 'none' }}>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='AnalysingFootballData/Dashboard1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param
          name='static_image'
          value='https://public.tableau.com/static/images/An/AnalysingFootballData/Dashboard1/1.png'
        />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-GB' />
      </object>
    </div>
  )
}

export default TableauReport
