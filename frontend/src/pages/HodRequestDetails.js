import React, { useContext, useState } from 'react'
import { useParams,useLocation } from 'react-router-dom';
import axios from 'axios';
import { Navigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { AuthContext } from '../core';
import "../css_files/CommitteeRequestDetails.css"


const HodRequestDetails = () => {
  const location=useLocation();
  const data=location.state;
  const [remarks,setRemarks]=useState('');
  const [redirect, setRedirect] = useState(false);
  const {user_type} = useContext(AuthContext);
  const handleRemarksChange = (event) => {
    setRemarks(event.target.value);
  };
  const ApproveRequest = (id)=>{
    axios.post('http://localhost:8000/'+user_type+'/approve',{
      'request_id':id,
       'hod_review':remarks,
     
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
    .then(response =>{
      console.log(response.data);
      
      if(response.data.success){
        setRedirect(true);
      }
      else{
        console.log("Approving Request Failed");
      }
    })
    .catch(error =>{
      console.log(error.response.data);
    })


  }

  const DisapproveRequest = (id)=>{
    axios.post('http://localhost:8000/'+user_type+'disapprove',{
      'request_id':id,
       'hod_review':remarks,
     
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
    .then(response =>{
      console.log(response.data);
      
      if(response.data.success){
        setRedirect(true);
      }
      else{
        console.log("Disapproving Request Failed");
      }
    })
    .catch(error =>{
      console.log(error.response.data);
    })
}
  if (redirect) {
    return <Navigate to="/hod/dashboard" />;
}

  return (
    <div className='committee_page'>
      <div className='committee_mainbody'>
        <div className='committee_titl'>RequestDetails: </div>
        <div className='committee_bod'>
          <div className='requesttype'>This is a {data.request_type}</div>
          <div>Title:{data.request_title}</div>
          <div>Description:{data.request_description}</div>
          <div>Requested Amount: {data.request_amount}</div>
          <div>Requested on :{data.request_date}</div>
      {/* <div>Committee Decision Status: {data.committee_approval_status}</div>
      <div>Committee Remarks: {data.committee_review}, Time: {data.committee_review_date}</div>
      <div>HOD Decision Status: {data.hod_approval_status}</div>
      <div>HOD Remarks: {data.hod_review}, Time: {data.hod_review_date}</div> */}
          <label className="committee_title">
              Remarks:
              <textarea value={remarks} onChange={handleRemarksChange} />
            </label>
          <button onClick={()=>ApproveRequest(data.id)} className="committee_approve">Approve</button>
          <button onClick={()=>DisapproveRequest(data.id)} className="committee_disapprove">Disapprove</button>
        </div>
      </div>
    </div>
  )
}



export default HodRequestDetails