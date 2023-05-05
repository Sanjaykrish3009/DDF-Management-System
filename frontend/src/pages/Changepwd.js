import React, { useContext, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from "../core";
import '../css_files/login.css'
import { ErrorDisplay,Loader } from "../components";
import ApiUrls from "../components/ApiUrls";

function ChangePassword() {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmNewPassword, setConfirmNewPassword] = useState("");
  const [passwordChange,setPasswordChange]=useState(false);
  const [passwordError, setPasswordError] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState("");
  const {logout} = useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState(null); 
  const [isLoading,setIsLoading]=useState(false);


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
      axios.post(ApiUrls.USER_CHANGEPASSWORD_URL,{
      'old_password':oldPassword,
      'new_password':newPassword,
      're_new_password':confirmNewPassword,
    }
    ,{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
  
      .then(response =>{
        setIsLoading(false);

        if(response.data.success)
        {
          logout();
          setPasswordChange(true);
          
        }
        else{
          setErrorMessage(response.data.error);
        }  
      })
      .catch(error =>{
        setIsLoading(false);
        setErrorMessage(error.message);
      });
    
    }
  };

  if(passwordChange)
  {
    return <Navigate to = "/"/>
  }

  return (
    <div>
    {isLoading?(
      // <div className="forgot_Loading">Loading...</div>
      <Loader/>
    ):(
    <div>
    <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 

    <div className="login-page">

      <form onSubmit={handleSubmit} className="login-form">
      <div className="login-title">Change Password </div>
        <div className="login_details">
          <label>Old Password</label>
          <input
            type="password"
            value={oldPassword}
            onChange={(e) => setOldPassword(e.target.value)}
          />
        </div>
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

        <button type="submit" className="submit">Submit</button>
      </form>
    </div>
    </div>
     )}
     </div>
  );
}

export default ChangePassword;
