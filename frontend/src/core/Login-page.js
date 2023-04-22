import "../css_files/login.css"

import React, { useState,useContext } from "react";
import { Link, Navigate,useNavigate } from "react-router-dom";
import { CSRFToken } from "../components";
import { AuthContext} from "./AuthContext";

export default function LoginPage() {

  const [email, setEmail] = useState("");
  const [password, setPassw] = useState("");
  const { isAuthenticated, loggingIn, user_type } = useContext(AuthContext);
  const history=useNavigate();

  const [errorMessage, setErrorMessage] = useState(null); 

  const handleSubmit = (event) => {
    event.preventDefault();

    loggingIn({ email, password })
      .then(() => {
        console.log('Login Successful')
      })
      .catch((error) => {
        console.log(error);
        setErrorMessage("Invalid email or password"); 
      });
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
    <div className="login-page">
      <form onSubmit={handleSubmit} className="login-form">
          <div className="login-title">Welcome! </div>
          <div className="error-message">{errorMessage}</div> 
        
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
  );
}
