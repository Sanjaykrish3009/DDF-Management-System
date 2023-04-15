import { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { AuthContext } from './AuthContext';
import {Header} from './header';
import {SignUp, ForgotPassword, OTP, Resetpwd} from '../pages';
import Loginpage from './Login-page'
import {Route, Routes} from 'react-router-dom';

const AuthStatus =() => {
  const {isAuthenticated, setIsAuthenticated, setUser_type} = useContext(AuthContext);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
        axios.get(`http://localhost:8000/authentication/authenticated`)
        .then(response => {
          setIsLoading(true);
          if(response.data.isAuthenticated==='success')
          {
              console.log(response.data.type)
              setIsAuthenticated(true);
              setUser_type(response.data.type);
          }
        })
        .catch(error => console.log(error))
        .finally(()=>{
          setIsLoading(false);}
        );    
  }, [setIsAuthenticated]);

  return (
    <div>    
    <Header/>
    {isLoading ? (
        <div>Loading...</div>
      ) : (
    
    <Routes>
      
      <Route path ="/" element={<Loginpage/>}/>
      <Route path ="/signup" element={<SignUp/>}/>
      <Route path ="/forgotpassword" element={<ForgotPassword/>}/>
      <Route path ="/otpverification" element={<OTP/>}/>
      <Route path = "/resetpassword" element={<Resetpwd/>}/>
      
    </Routes>
)}
    </div>

  );
}

export default AuthStatus;
