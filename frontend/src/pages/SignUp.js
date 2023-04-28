import '../css_files/signUp.css'

import React, { useState,useContext} from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { CSRFToken } from "../components";
import { AuthContext } from "../core";
import {ErrorDisplay,Loader} from '../components';
import axios from 'axios';
import Cookies from 'js-cookie';

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassw] = useState("");
  const [re_password,setRePassw] =useState("");
  const [OtpSent,setOtpSent] = useState(false);
  const [firstname,setFirstname] = useState("");
  const [lastname,setLastname] = useState("");
  const { isAuthenticated,setValidEmail} = useContext(AuthContext);
  const [passwordError, setPasswordError] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState("");
  const [errorMessage, setErrorMessage] = useState(null); 
  const [isLoading,setIsLoading]=useState(false);

  const history = useNavigate();

  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    password: '',
    re_password: ''
  });
  const handleSubmit = (event) => {
    event.preventDefault();

    setPasswordError("");
    setConfirmPasswordError("");

    if (formData.password.length < 6) {
      setPasswordError("Password must be at least 6 characters.");
      return;
    }

    // check if passwords match
    if (formData.password !== formData.re_password) {
      setConfirmPasswordError("Passwords do not match.");
      return;
    }

    setIsLoading(true);
    axios.post(`http://localhost:8000/user/register`,formData
    // {
      // 'first_name':firstname,
      // 'last_name':lastname,
      // 'email':email,
      // 'password':password,
      // 're_password':re_password,

    // }
    ,{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        setIsLoading(false);
        if(response.data.success)
        {
          setOtpSent(true);
        }
        else 
        {
          setErrorMessage(response.data.error); 
        }
        
      })
      .catch(error =>{
        // console.log(error.response.data);
        setIsLoading(false);
        setErrorMessage(error.message); 
      });

    // signingUp({firstname,lastname,email,password,re_password,setAccountCreated})
    // .then((response) => {
      

    // })
    // .catch((error) => {
    //   console.log(error);
    //   setErrorMessage(error.message); 
    // });
  };

  function handleInputChange(event) {
    const { name, value } = event.target;
    setFormData(prevFormData => ({ ...prevFormData, [name]: value }));
  }

  if(isAuthenticated)
  {
    return <Navigate to = '/dashboard'/>
  }
  else if(OtpSent)
  {
    setValidEmail(true);
    history('/signupverification', { state: formData });

  }

  return (
    <div>
    {isLoading?(
      // <div className="forgot_Loading">Loading...</div>
      <Loader/>
    ):(
    <div>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/>        


    <div className="signup-page">
      <form onSubmit={handleSubmit} className="signup-form">
          <h1>Create Account</h1> 
        <div className="signup-details">
          <label htmlFor="firstname"  >First Name: </label>
          <input
            type="text"
            // value={firstname}
            // onChange={(e) => setFirstname(e.target.value)} 
            name="first_name"
            value={formData.first_name}
            onChange={handleInputChange} 
          />
        </div>
        <div className="signup-details">
          <label htmlFor="lastname" >Last Name: </label>
          <input
            type="text"
            // value={lastname}
            // onChange={(e) => setLastname(e.target.value)} 
            name="last_name"
            value={formData.last_name}
            onChange={handleInputChange} 
          />
        </div>
        <div className="signup-details">
          <label htmlFor="email" >Email: </label>
          <input
            type="email"
            // value={email}
            // onChange={(e) => setEmail(e.target.value)} 
            name="email"
            value={formData.email}
            onChange={handleInputChange} 
          />
        </div>
        <div className="signup-details">
          <label htmlFor="password" >Password: </label>
          <input
            type="password"
            // value={password}
            // onChange={(e) => setPassw(e.target.value)}
            name="password"
            value={formData.password}
            onChange={handleInputChange} 
          />
        </div>
        {passwordError && <p className='error-message'>{passwordError}</p>}
        <div className="signup-details">
          <label htmlFor="password" >Confirm Password: </label>
          <input
            type="password"
            // value={re_password}
            // onChange={(e) => setRePassw(e.target.value)} 
            name="re_password"
            value={formData.re_password}
            onChange={handleInputChange} 
          />
        </div>
        {confirmPasswordError && <p className='error-message'>{confirmPasswordError}</p>}
        <CSRFToken/>
          <button type="submit" className="register-button" >Register</button>
      </form>
    </div>
    </div>
    )}
    </div>
  );
}
