import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const HodDashboard = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.HOD_DASHBOARD_URL}/>
  )
}

export default HodDashboard