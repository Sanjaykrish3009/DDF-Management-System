import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const FacultyDashboard = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.FACULTY_DASHBOARD_URL}/>
  )
}

export default FacultyDashboard