import React, { useContext, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
import { AuthContext } from "../core";
import '../css_files/login.css'


function ChangePassword() {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmNewPassword, setConfirmNewPassword] = useState("");
  const [passwordChange,setPasswordChange]=useState(false);
  const {logout} = useContext(AuthContext);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newPassword !== confirmNewPassword) {
      alert("New password and confirm password fields should match.");
    } else if (newPassword.length < 6) {
      alert("Password should have at least 6 characters.");
    } else {
      axios.post(`http://localhost:8000/user/changepassword`,{
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
        console.log(response.data);
        if(response.data.success)
        {
          logout();
          setPasswordChange(true);
          
        }
        
      })
      .catch(error =>{
        console.log(error.response.data);
        
      });
    
    }
  };

  if(passwordChange)
  {
    return <Navigate to = "/"/>
  }

  return (
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
        <div className="login_details">
          <label>Confirm New Password</label>
          <input
            type="password"
            value={confirmNewPassword}
            onChange={(e) => setConfirmNewPassword(e.target.value)}
          />
        </div>
        <button type="submit" className="submit">Submit</button>
      </form>
    </div>
  );
}

export default ChangePassword;
