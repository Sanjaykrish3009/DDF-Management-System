import React,{useState} from 'react'
import { Navigate } from 'react-router';
import axios from 'axios';
import Cookies from 'js-cookie';

import '../css_files/publicrequest.css';

function PrivateRequest() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [fundAmount, setFundAmount] = useState("");
  const [documents, setDocuments] = useState(null);
  const [redirect, setRedirect] = useState(false);

 

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    const reader = new FileReader();
    formData.append('request_title',title);
    formData.append('request_description',description);
    formData.append('request_amount',fundAmount);  
    formData.append('file',documents);

    // reader.readAsDataURL(documents);
    // reader.onload=(readerEvent)=>{
    //   formData.append("file",readerEvent.target.result);
    // }
    console.log(documents);
    console.log(formData);
    console.log(formData.get('request_title'));

    axios.post(`http://localhost:8000/request/createprivaterequest`,
      formData
    ,{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken'),
        'Content-Type':'multipart/form-data',
      }
    })
    .then(response =>{
      console.log(response.data);
      
      if(response.data.success){
        setRedirect(true);
      }
      else{
        console.log("Creating Private Fund Request Failed");
      }
    })
    .catch(error =>{
      console.log(error.response.data);
    })
    
  };

  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    setDocuments(uploadedFile);
  };

  if (redirect) {
        return <Navigate to="/faculty/dashboard" />;
  }

  return (
    <div className="request-page">
      <form onSubmit={handleSubmit} className="request-form" encType='multipart/form-data'>
          Public Request
        <div className="title">
          <label htmlFor="title">Title *</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            required
          />
        </div>
        <div className="title">
          <label htmlFor="reason">Description *</label>
          <textarea
            type="text"
            id="reason"
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            required
          />
        </div>

        <div className="title">
          <label htmlFor="fundAmount">Fund amount *</label>
          <input
            type="number"
            id="fundAmount"
            value={fundAmount}
            onChange={(event) => setFundAmount(event.target.value)}
            required
          />
        </div>
        <div className="title">
          <label htmlFor="documents">Upload Documents *</label>
          <input
            type="file"
            id="documents"
            onChange={handleFileUpload}
            required
          />
        </div>
        <button type="submit" className="done">Submit</button>
      </form>
    </div>
  );
}

export default PrivateRequest