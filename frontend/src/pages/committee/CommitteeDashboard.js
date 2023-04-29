import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const CommitteeDashboard = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.COMMITTEE_DASHBOARD_URL}/>
  )
}

export default CommitteeDashboard