
import React, { useContext, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from "../core";
import { ErrorDisplay } from "../components";

import '../css_files/login.css';


const Resetpwd = () => {

    const [newPassword, setNewPassword] = useState("");
    const [confirmNewPassword, setConfirmNewPassword] = useState("");
    const [passwordChange,setPasswordChange]=useState(false);
    const {logout,setValid,setValidOtp} = useContext(AuthContext);
    const [errorMessage, setErrorMessage] = useState(null); 
    const [confirmPasswordError, setConfirmPasswordError] = useState("");
    const [passwordError, setPasswordError] = useState("");

  
    const handleSubmit = (e) => {
      e.preventDefault();
      setConfirmPasswordError("");
      setPasswordError("");
      if (newPassword.length < 6) {
        setPasswordError("Password should have at least 6 characters.");
      } else if (newPassword !== confirmNewPassword) {
        setConfirmPasswordError("New password and confirm password fields should match.");
      } else {
        axios.post(`http://localhost:8000/authentication/resetpassword`,{
        'new_password':newPassword,
        're_new_password':confirmNewPassword,
      }
      ,{
        headers:{
          'X-CSRFToken' :Cookies.get('csrftoken')
        }
      })
    
        .then(response =>{
          console.log(response.data);
          if(response.data.success)
          {
            setPasswordChange(true);
          }
          else{
            setErrorMessage(response.data.error);
          }
          
        })
        .catch(error =>{
          setErrorMessage(error.message);

        });
      
      }
    };
  
    if(passwordChange)
    {
      setValid(false);
      setValidOtp(false);
      return <Navigate to = "/"/>
    }
  
    return (
      <div className="login-page">
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 

      <form onSubmit={handleSubmit}  className="login-form">
      <div className="login-title">Reset Password </div>
          
          <div className="login_details">
            <label>New Password</label>
            <input
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
          </div>
          {passwordError && <p className='error-message'>{passwordError}</p>}

          <div className="login_details">
            <label>Confirm New Password</label>
            <input
              type="password"
              value={confirmNewPassword}
              onChange={(e) => setConfirmNewPassword(e.target.value)}
            />
          </div>
          {confirmPasswordError && <p className='error-message'>{confirmPasswordError}</p>}

          <div>
          <button type="submit" className="submit">Submit</button>
          </div>
        </form>
      </div>
    );
}

export default Resetpwd

