import React from 'react'
import { useParams,useLocation } from 'react-router-dom';

const RequestDetails = () => {
  const {id}=useParams();
  const location=useLocation();
  const data=location.state;
  return (
    <div className='page'>
      <div className='mainbody'>
        <div className='titl'>RequestDetails: </div>
        <div className='bod'>
          <div className='requesttype'>This is a {data.request_type}</div>
          <div>Title:{data.request_title}</div>
          <div>Description:{data.request_description}</div>
          <div>Requested Amount: {data.request_amount}</div>
          <div>Requested on :{data.request_date}</div>
          <div>Committee Decision Status: {data.committee_approval_status}</div>
          <div>Committee Remarks: {data.committee_review}, Time: {data.committee_review_date}</div>
          <div>HOD Decision Status: {data.hod_approval_status}</div>
          <div>HOD Remarks: {data.hod_review}, Time: {data.hod_review_date}</div>
        </div>
      </div>
    </div>
  )
}

export default RequestDetails;