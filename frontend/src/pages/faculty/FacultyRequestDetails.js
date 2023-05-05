import React, { useState } from 'react'
import { useParams, Link } from 'react-router-dom';
import "../../css_files/RequestDetails.css"
import { Loader,ErrorDisplay } from '../../components';
import axios from 'axios';
import Cookies from 'js-cookie';
import ApiUrls from '../../components/ApiUrls';
import { useEffect } from 'react';
import ApiCallGet from '../../components/ApiCallGet';
const FacultyRequestDetails = () => {

  const {id}=useParams();
  const [data,setData] = useState(null);
  const [errorMessage,setErrorMessage] = useState('');

  useEffect(() => {
    const senddata ={};
    senddata.request_id=id;
    const api_url = ApiUrls.REQUEST_REQUESTDETAILS_URL;
    ApiCallGet({api_url,setData,setErrorMessage,senddata});
  }, [id]);

  const handleFile =(file)=>{
    axios.get(ApiUrls.REQUEST_FILEDETAILS_URL,
    {
      params: {
        file_path: file
      },
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      responseType: 'arraybuffer'
    }).then(response => {
      // window.location.href = pdfUrl;
      const fileBlob = new Blob([response.data], { type: response.headers['content-type']});
      const fileUrl = URL.createObjectURL(fileBlob);
      window.open(fileUrl, '_blank');

    }).catch(error => console.log(error));

    
  }

  return (
    <div>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 

      {data ? (
    <div className='page'>
    <div className='mainbody'>
      <div className='titl'>RequestDetails</div>
        <div className='bod'>
          <div className='requesttype'>This is a {data.request_type}</div>

            <div className="row">
                <div className="col-head">Title</div>
                <div className="colon">:</div>
                <div className="col-body">{data.request_title}</div>
              </div>
              <div className="row">
                <div className="col-head">Description</div>
                <div className="colon">:</div>
                <div className="col-body">{data.request_description}</div>
              </div>
              <div className="row">
                <div className="col-head">Requested Amount</div>
                <div className="colon">:</div>
                <div className="col-body">{data.request_amount}</div>
              </div>
              <div className="row">
                <div className="col-head">Requested on</div>
                <div className="colon">:</div>
                <div className="col-body">{data.request_date}</div>
              </div>
              <div className="row">
                <div className="col-head">Requested By</div>
                <div className="colon">:</div>
                <div className="col-body">{data.user.email}</div>
              </div>
              <div className="row">
                <div className="col-head">Committee Decision Status</div>
                <div className="colon">:</div>
                <div className="col-body">{data.committee_approval_status}</div>
              </div>
              <div className="row">
                <div className="col-head">Committee Remarks</div>
                <div className="colon">:</div>
                <div className="col-body">{data.committee_review}</div>
              </div>
              <div className="row">
                <div className="col-head">Time</div>
                <div className="colon">:</div>
                <div className="col-body">{data.committee_review_date}</div>
              </div>
              <div className="row">
                <div className="col-head">HOD Decision Status</div>
                <div className="colon">:</div>
                <div className="col-body">{data.hod_approval_status}</div>
              </div>
              <div className="row">
                <div className="col-head">HOD Remarks</div>
                <div className="colon">:</div>
                <div className="col-body">{data.hod_review}</div>
              </div>
              <div className="row">
                <div className="col-head">Time</div>
                <div className="colon">:</div>
                <div className="col-body">{data.hod_review_date}</div>
              </div>
              <div className="row">
                <div className="col-head">Uploads</div>
                <div className="colon">:</div>
                <div className="col-body">
                  <Link onClick={() => handleFile(data.upload)}>{data.upload}</Link>
                </div>
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

export default FacultyRequestDetails;