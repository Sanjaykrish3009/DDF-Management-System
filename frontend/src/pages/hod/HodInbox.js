import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const HodInbox = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.HOD_INBOX_URL}/>
  )
}

export default HodInbox