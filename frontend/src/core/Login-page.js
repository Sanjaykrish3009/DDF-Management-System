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
    try {
      loggingIn({ email, password });
    } catch (error) {
      console.log("done");
      setErrorMessage("Invalid email or password"); 
    }
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
          Sign in
        <div className="email">
          <label htmlFor="email" >Email: </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="password">
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
          <button type="submit" className="submit" >Sign in</button>
        </div>
        <div className="error-message">{errorMessage}</div> 
        
        <div className="signUp3"> 
          <Link to='/SignUp'> Register or SignUp</Link>
        </div>
      </form>
    </div>
  );
}
