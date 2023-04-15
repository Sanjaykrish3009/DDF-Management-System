import '../css_files/signUp.css'

import React, { useState,useContext} from "react";
import { CSRFToken } from "../components";
import { AuthContext } from "../core";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassw] = useState("");
  const [re_password,setRePassw] =useState("");
  const [accountCreated,setAccountCreated] = useState(false);
  const [firstname,setFirstname] = useState("");
  const [lastname,setLastname] = useState("");
  const { isAuthenticated , signingUp} = useContext(AuthContext);

  const handleSubmit = (event) => {
    event.preventDefault();
    signingUp({firstname,lastname,email,password,re_password,setAccountCreated});
  };

  return (
    <div className="signup-page">
      <form onSubmit={handleSubmit} className="signup-form">
          <h1>Register</h1> 
        <div className="signup-details">
          <label htmlFor="firstname"  >First Name: </label>
          <input
            type="text"
            value={firstname}
            onChange={(e) => setFirstname(e.target.value)} className="details"
          />
        </div>
        <div className="signup-details">
          <label htmlFor="lastname" >Last Name: </label>
          <input
            type="text"
            value={lastname}
            onChange={(e) => setLastname(e.target.value)} className="details"
          />
        </div>
        <div className="signup-details">
          <label htmlFor="email" >Email: </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)} className="details"
          />
        </div>
        <div className="signup-details">
          <label htmlFor="password" >Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassw(e.target.value)} className="details"
          />
        </div>
        <div className="signup-details">
          <label htmlFor="password" >Confirm Password: </label>
          <input
            type="password"
            value={re_password}
            onChange={(e) => setRePassw(e.target.value)} className="details"
          />
        </div>
        <CSRFToken/>
          <button type="submit" className="register-button" >Register</button>
      </form>
    </div>
  );
}
