import "../css_files/login.css"

import React, { useState,useContext } from "react";
import { Link, Navigate} from "react-router-dom";
import { CSRFToken } from "../components";
import { AuthContext} from "../core/AuthContext";
import {ErrorDisplay} from "../components";
import ApiUrls from "../components/ApiUrls";
import Cookies from "js-cookie";
import axios from "axios";
const LoginPage = () =>{

  const [email, setEmail] = useState("");
  const [password, setPassw] = useState("");
  const { isAuthenticated, user_type, setIsAuthenticated, setUser_type } = useContext(AuthContext);

  const [errorMessage, setErrorMessage] = useState(null); 
 
  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post(ApiUrls.AUTHENTICATION_LOGIN_URL,{
      'email':email,
      'password':password,
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        
        if(response.data.success){
          setIsAuthenticated(true);
          setUser_type(response.data.user_type);
        }
        else{
          setErrorMessage(response.data.error); 
        }
      })
      .catch(error =>{
        setErrorMessage(error.message);
      })
  };

  if(isAuthenticated)
  {
    if(user_type==="faculty")
    {
      return <Navigate to = '/faculty/dashboard'/>
    }
    else if(user_type==="committee")
    {
      return <Navigate to = '/committee/dashboard'/>
    }
    else if(user_type==="hod")
    {
      return <Navigate to = '/hod/dashboard'/>
    }
    else{
      console.log("Unknown User");
    }
  }

  return (
    <div>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/>        

      <div className="login-page">
        <form onSubmit={handleSubmit} className="login-form">
            <div className="login-title">Welcome! </div>
          <div className="login_details">
            <label htmlFor="email" >Email: </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="login_details">
            <label htmlFor="password" >Password: </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassw(e.target.value)}
            />
          </div>
          <CSRFToken/>
          <div className="login_forgot-Password">
            <Link to='/forgotpassword'> Forgot Password?</Link>
          </div>
          <div>
            <button type="submit" className="submit" >LOG IN</button>
          </div>

          <div className="signup-link"> 
            <Link to='/SignUp'> Register or SignUp</Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
