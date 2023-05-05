import React from 'react'
import { Dashboardcomponent } from '../../components'
import ApiUrls from '../../components/ApiUrls'

const CommitteeInbox = () => {
  return (
    <Dashboardcomponent api_url = {ApiUrls.COMMITTEE_INBOX_URL}/>
  )
}

export default CommitteeInbox