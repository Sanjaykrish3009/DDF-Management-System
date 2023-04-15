import React,{useState} from 'react'
import { Navigate } from 'react-router';
import axios from 'axios';
import Cookies from 'js-cookie';

function PrivateRequest() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [fundAmount, setFundAmount] = useState("");
  const [redirect, setRedirect] = useState(false);


  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post(`http://localhost:8000/faculty/createprivatefundrequest`,{
      'request_title':title,
      'request_description':description,
      'request_amount':fundAmount,
     
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
        console.log("Creating Private Fund Request Failed");
      }
    })
    .catch(error =>{
      console.log(error.response.data);
    })
    
  };

  if (redirect) {
        return <Navigate to="/faculty/dashboard" />;
  }

  return (
    <div className="request-page">
      <form onSubmit={handleSubmit} className="request-form">
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
        <button type="submit" className="done">Submit</button>
      </form>
    </div>
  );
}

export default PrivateRequest