import { useContext, useState } from "react";
import { Navigate } from "react-router-dom";


import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from "../core";

import '../css_files/forgotPassword.css';
import { Loader } from "../components";

const ForgotPassword = () => {
  const [otpverify, setOtpVerify] = useState(false);
  const [email,setEmail] =useState("");
  const {setEmailID} = useContext(AuthContext);
  const [isLoading,setIsLoading]=useState(false);


  const handleSubmit = (event) => {
    event.preventDefault();
    setEmailID(email);
    setIsLoading(true);
    axios.post(`http://localhost:8000/authentication/forgotpassword`,{
      'email':email,
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        setIsLoading(false);
        if(response.data.success)
        {
          setOtpVerify(true);
        }
      })
      .catch(error =>{
        console.log(error.response.data);
        
      });
  };

  if(otpverify)
  {
    return <Navigate to = "/otpverification"/>
  }

  return (
    <div>
    {isLoading?(
      // <div className="forgot_Loading">Loading...</div>
      <Loader/>
    ):(
    <div className="forgot_login-page">
      <form onSubmit={handleSubmit} className="forgot_login-form">
        <label htmlFor="email" className="forgotlogin_email">Forgot Password</label>
        <div className="forgot_email">
          <label htmlFor="email" >Please Enter Your Registered Email </label>
          <input type="email" id="email" value={email} onChange={(e)=>setEmail(e.target.value)} required />
        </div>
        <button type="submit" className="forgot_signUp">Reset Password</button>
      </form>
    </div>
    )}
    </div>
  );
};

export default ForgotPassword;
