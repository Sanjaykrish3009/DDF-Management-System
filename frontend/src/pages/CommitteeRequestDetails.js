import React, { useContext, useState } from 'react'
import { useParams,useLocation } from 'react-router-dom';
import axios from 'axios';
import { Navigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { AuthContext } from '../core';
import { ErrorDisplay } from '../components';
import "../css_files/CommitteeRequestDetails.css"

const CommitteeRequestDetails = () => {
  const location=useLocation();
  const data=location.state;
  const [remarks,setRemarks]=useState('');
  const [redirect, setRedirect] = useState(false);
  const [errorMessage1, setErrorMessage1] = useState(null); 
  const [errorMessage2, setErrorMessage2] = useState(null); 

  const {user_type} = useContext(AuthContext);
  const handleRemarksChange = (event) => {
    setRemarks(event.target.value);
  };

  const RequestApproval = (id) =>{
    
    ApproveRequest({id})
    .then(() => {
      console.log('Approval Successful')
    })
    .catch((error) => {
      console.log(error);
      setErrorMessage1(error.message); 
      console.log(errorMessage1);
    });
  }

  const ApproveRequest = ({id})=>{
    const response=axios.post('http://localhost:8000/'+user_type+'/approve',{
      'request_id':id,
       'committee_review':remarks,
     
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
        throw new Error(response.data.error);
      }
    })
    .catch(error =>{
      throw error;
    })
    return response;

  }


  const RequestDisApproval = (id) =>{
    
    DisapproveRequest({id})
    .then(() => {
      console.log('Approval UnSuccessful')
    })
    .catch((error) => {
      console.log(error);
      setErrorMessage2(error.message); 
      console.log(errorMessage2);
    });
  }

  const DisapproveRequest = ({id})=>{
    const response=axios.post('http://localhost:8000/'+user_type+'disapprove',{
      'request_id':id,
       'committee_review':remarks,
     
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
        // console.log("Disapproving Request Failed");
        throw new Error(response.data.error);
      }
    })
    .catch(error =>{
      throw error;
    })
    return response;
  }


  if (redirect) {
    return <Navigate to="/committee/dashboard" />;
}

  return (
    <div>
      <ErrorDisplay errormessage={errorMessage1} seterrormessage={setErrorMessage1}/> 
      <ErrorDisplay errormessage={errorMessage2} seterrormessage={setErrorMessage2}/> 
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
          <button onClick={()=>RequestApproval(data.id)} className="committee_approve">Approve</button>
          <button onClick={()=>RequestDisApproval(data.id)} className="committee_disapprove">Disapprove</button>
        </div>
      </div>
    </div>
    </div>
  )
}



export default CommitteeRequestDetails