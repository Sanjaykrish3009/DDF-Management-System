import '../css_files/signUp.css'

import React, { useState,useContext} from "react";
import { Navigate } from "react-router-dom";
import { CSRFToken } from "../components";
import { AuthContext } from "../core";
import {ErrorDisplay} from '../components';

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassw] = useState("");
  const [re_password,setRePassw] =useState("");
  const [accountCreated,setAccountCreated] = useState(false);
  const [firstname,setFirstname] = useState("");
  const [lastname,setLastname] = useState("");
  const { isAuthenticated , signingUp} = useContext(AuthContext);
  const [passwordError, setPasswordError] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState("");
  const [errorMessage, setErrorMessage] = useState(null); 

  const handleSubmit = (event) => {
    event.preventDefault();

    setPasswordError("");
    setConfirmPasswordError("");

    if (password.length < 6) {
      setPasswordError("Password must be at least 6 characters.");
      return;
    }

    // check if passwords match
    if (password !== re_password) {
      setConfirmPasswordError("Passwords do not match.");
      return;
    }

    signingUp({firstname,lastname,email,password,re_password,setAccountCreated})
    .then(() => {
      console.log('Signup Successful')

    })
    .catch((error) => {
      console.log(error);
      setErrorMessage(error.message); 
    });
  };

  if(isAuthenticated)
  {
    return <Navigate to = '/dashboard'/>
  }
  else if(accountCreated)
  {
    return <Navigate to = "/"/>

  }

  return (
    <div>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/>        


    <div className="signup-page">
      <form onSubmit={handleSubmit} className="signup-form">
          <h1>Create Account</h1> 
        <div className="signup-details">
          <label htmlFor="firstname"  >First Name: </label>
          <input
            type="text"
            value={firstname}
            onChange={(e) => setFirstname(e.target.value)} 
          />
        </div>
        <div className="signup-details">
          <label htmlFor="lastname" >Last Name: </label>
          <input
            type="text"
            value={lastname}
            onChange={(e) => setLastname(e.target.value)} 
          />
        </div>
        <div className="signup-details">
          <label htmlFor="email" >Email: </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)} 
          />
        </div>
        <div className="signup-details">
          <label htmlFor="password" >Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassw(e.target.value)} 
          />
        </div>
        {passwordError && <p className='error-message'>{passwordError}</p>}
        <div className="signup-details">
          <label htmlFor="password" >Confirm Password: </label>
          <input
            type="password"
            value={re_password}
            onChange={(e) => setRePassw(e.target.value)} 
          />
        </div>
        {confirmPasswordError && <p className='error-message'>{confirmPasswordError}</p>}
        <CSRFToken/>
          <button type="submit" className="register-button" >Register</button>
      </form>
    </div>
    </div>
  );
}
