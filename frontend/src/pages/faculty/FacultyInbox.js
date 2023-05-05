import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const FacultyInbox = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.FACULTY_INBOX_URL}/>
  )
}

export default FacultyInbox