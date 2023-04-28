

import React, { useContext, useState } from 'react';
import { Navigate,useLocation } from 'react-router-dom';
import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from '../core';

import '../css_files/otp.css';
import { ErrorDisplay } from '../components';
import {Loader} from '../components';


const SignUpOtp = () => {
  const [otp, setOtp] = useState('');
  const [verify,setverify] = useState(false);
  const {emailID,setValidEmail} =useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState(null); 
  const [isLoading,setIsLoading]=useState(false);
  const location=useLocation();
  const data=location.state;


  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Submitting OTP: ${otp}`);
    data.entered_otp =otp;
    axios.post(`http://localhost:8000/user/checkemail`,
      data,
    {
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
        else{
          setErrorMessage(response.data.error);
        }
      })
      .catch(error =>{
          setErrorMessage(error.message);
        
      });
  }

  const handleResend =()=>{
    setIsLoading(true);
    setOtp("");
    axios.post(`http://localhost:8000/user/register`,data
    // {
    //   'email':emailID,
    // }
    ,{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);

        if(response.data.success)
        {
          setErrorMessage(response.data.success);
        }
        else{
          setErrorMessage(response.data.error);
        }
        setIsLoading(false);

      })
      .catch(error =>{
          setErrorMessage(error.message);
        setIsLoading(false);
      });
      
  }

  if(verify)
  {
    setValidEmail(false);
    return (<Navigate to = "/" />);
  }
  return (
    <div>
    {isLoading?(
      // <div className="forgot_Loading">Loading...</div>
      <Loader/>
    ):(
    <div>
    <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/>        

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
  </div>
  )}
  </div>

  );
}

export default SignUpOtp;
