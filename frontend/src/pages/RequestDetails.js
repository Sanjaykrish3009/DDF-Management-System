import React, { useState } from 'react'
import { useParams,useLocation, Link } from 'react-router-dom';
import "../css_files/RequestDetails.css"
import { Loader } from '../components';
import axios from 'axios';
import Cookies from 'js-cookie';

import { useEffect } from 'react';

const RequestDetails = () => {

  
  const {id}=useParams();
  const location=useLocation();
  // const data=location.state;
  const [data,setData] = useState(null);

  useEffect(() => {
    axios.post('http://localhost:8000/request/requestdetails',
    {
      'request_id':id,
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response => {
        
        if(response.data.success)
        {
          setData(response.data.data)
        }
      })
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      {data ? (
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
          <div>
              Uploads: <Link to = '/filedetails'> {data.upload} </Link>
          </div>
        </div>
      </div>
    </div>
     ) : (
        <Loader/>
    )}
  </div>
  )
}

export default RequestDetails;