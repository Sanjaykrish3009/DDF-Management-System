
import React, { useContext, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from "../core";
import { ErrorDisplay,Loader } from "../components";
import ApiUrls from "../components/ApiUrls";
import '../css_files/login.css';


const Resetpwd = () => {

    const [newPassword, setNewPassword] = useState("");
    const [confirmNewPassword, setConfirmNewPassword] = useState("");
    const [passwordChange,setPasswordChange]=useState(false);
    const {setValid,setValidOtp} = useContext(AuthContext);
    const [errorMessage, setErrorMessage] = useState(null); 
    const [confirmPasswordError, setConfirmPasswordError] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [isLoading,setIsLoading] =useState(false);
  
    const handleSubmit = (e) => {
      e.preventDefault();
      setConfirmPasswordError("");
      setPasswordError("");
      if (newPassword.length < 6) {
        setPasswordError("Password should have at least 6 characters.");
      } else if (newPassword !== confirmNewPassword) {
        setConfirmPasswordError("New password and confirm password fields should match.");
      } else {
        setIsLoading(true);
        axios.post(ApiUrls.AUTHENTICATION_RESETPASSWORD_URL,{
        'new_password':newPassword,
        're_new_password':confirmNewPassword,
      }
      ,{
        headers:{
          'X-CSRFToken' :Cookies.get('csrftoken')
        }
      })
    
        .then(response =>{
          
          if(response.data.success)
          {
            setPasswordChange(true);
          }
          else{
            setErrorMessage(response.data.error);
          }
          setIsLoading(false);
        })
        .catch(error =>{
          setIsLoading(false);
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
      <div>
      {isLoading?(
        // <div className="forgot_Loading">Loading...</div>
        <Loader/>
      ):(
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
       )}
       </div>
    );
}

export default Resetpwd

