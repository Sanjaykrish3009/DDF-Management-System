import React, { createContext, useState } from 'react';
import axios from "axios";
import Cookies from 'js-cookie';

export const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const [emailID,setEmailID] =useState('');
  const [user_type,setUser_type] =useState('');
  

  const login = () => {
    setIsAuthenticated(true);
  };

  const logout = () => {
    setIsAuthenticated(false);
  };

  const loggingIn = ({email,password}) => {

    axios.post(`http://localhost:8000/authentication/login`,{
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
          throw new Error("Login failed"); 
        }
      })
      .catch(error =>{
        throw error; 
      })
  };

  const signingUp = ({firstname,lastname,email,password,re_password,setAccountCreated}) => {
      
    axios.post(`http://localhost:8000/user/register`,{
      'first_name':firstname,
      'last_name':lastname,
      'email':email,
      'password':password,
      're_password':re_password,
    },{
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        setAccountCreated(true);
      })
      .catch(error =>{
        console.log(error.response.data);
        
      });
  }
  
  
  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, setIsAuthenticated, user, setUser, loggingIn, signingUp, emailID, setEmailID, user_type,setUser_type }}>
      {children}
    </AuthContext.Provider>
  );
};
