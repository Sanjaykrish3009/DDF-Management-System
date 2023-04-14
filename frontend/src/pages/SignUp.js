import React, { useState,useContext} from "react";
import { Navigate } from "react-router-dom";
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
    <div className="login-page">
      <form onSubmit={handleSubmit} className="login-form">
          <h1>Register</h1> 
        <div className="register">
          <label htmlFor="firstname"  >First Name: </label>
          <input
            type="text"
            value={firstname}
            onChange={(e) => setFirstname(e.target.value)} className="details"
          />
        </div>
        <div className="register">
          <label htmlFor="lastname" >Last Name: </label>
          <input
            type="text"
            value={lastname}
            onChange={(e) => setLastname(e.target.value)} className="details"
          />
        </div>
        <div className="register">
          <label htmlFor="email" >Email: </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)} className="details"
          />
        </div>
        <div className="register">
          <label htmlFor="password" >Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassw(e.target.value)} className="details"
          />
        </div>
        <div className="register">
          <label htmlFor="password" >Confirm Password: </label>
          <input
            type="password"
            value={re_password}
            onChange={(e) => setRePassw(e.target.value)} className="details"
          />
        </div>
        <CSRFToken/>
          <button type="submit" className="signUp3" >Register</button>
      </form>
    </div>
  );
}
