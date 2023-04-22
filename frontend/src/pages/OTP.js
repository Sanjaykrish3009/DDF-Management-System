import React, { useContext, useState } from 'react';
import { Navigate } from 'react-router-dom';
import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from '../core';

import '../css_files/otp.css';


const OTP = () => {
  const [otp, setOtp] = useState('');
  const [verify,setverify] = useState(false);
  const {emailID} =useContext(AuthContext);

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Submitting OTP: ${otp}`);
    axios.post(`http://localhost:8000/authentication/checkotp`,{
      'entered_otp':otp,
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        if(response.data.success)
        {
          setverify(true);
        }
      })
      .catch(error =>{
        console.log(error.response.data);
        
      });
  }

  const handleResend =()=>{
    axios.post(`http://localhost:8000/authentication/forgotpassword`,{
      'email':emailID,
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);

      })
      .catch(error =>{
        console.log(error.response.data);
        
      });
  }

  if(verify)
  {
    return (<Navigate to = "/resetpassword" />);
  }
  return (
    <div className="otp_login-page">
      <form onSubmit={handleSubmit} className="otp_login-form">
        <label htmlFor="otp">Enter your 6-digit OTP</label>
        <div className="otp_email">
          <input
            type="text"
            pattern="[0-9]*"
            inputMode="numeric"
            minLength="6"
            maxLength="6"
            id="otp"
            value={otp}
            onChange={(event) => setOtp(event.target.value)}
            required
          />
        </div>
        <div className="otp_buttons">
          <button type="submit" className="otp_submit">
            Submit OTP
          </button>
          <button onClick={handleResend} className="otp_resend">
            Resend OTP
          </button>
        </div>
      </form>
  </div>

  );
}

export default OTP;
