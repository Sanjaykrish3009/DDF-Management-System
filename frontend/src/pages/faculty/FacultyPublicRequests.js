import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const FacultyPublicRequests = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.FACULTY_PUBLICREQUESTS_URL}/>
  )
}

export default FacultyPublicRequests