import { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { AuthContext } from './AuthContext';
import {Header, FacultySubheader, CommitteeSubheader, HodSubheader} from './header';
import {SignUp, ForgotPassword, OTP, Resetpwd, FacultyDashboard, CommitteeDashboard, HodDashboard, Inbox,ChangePassword,CreateRequest,Profile,PublicRequest,PrivateRequest} from '../pages';
import Loginpage from './Login-page';
import {Route, Routes} from 'react-router-dom';
import {FacultyPrivateRoute, CommitteePrivateRoute, HodPrivateRoute} from "../components/PrivateRoute";

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

      <Route path = "/faculty" element= {<FacultySubheader/>}>
        <Route element={<FacultyPrivateRoute/>}>
        <Route path = "dashboard" element={<FacultyDashboard/>}/>
        <Route path = "inbox" element={<Inbox/>}/>
        <Route path = "makerequest" element = {<CreateRequest/>}/>
        <Route path = "makerequest/publicrequest" element={<PublicRequest/>}/>
        <Route path = "makerequest/privaterequest" element={<PrivateRequest/>}/>
        <Route path = "viewprofile" element = {<Profile/>}/>
        <Route path = "changepwd" element = {<ChangePassword/>}/>
        </Route>
      </Route>

      <Route path = "/committee" element= {<CommitteeSubheader/>}>
        <Route element={<CommitteePrivateRoute/>}>
        <Route path = "dashboard" element={<CommitteeDashboard/>}/>
        <Route path = "inbox" element={<Inbox/>}/>
        <Route path = "viewprofile" element = {<Profile/>}/>
        <Route path = "changepwd" element = {<ChangePassword/>}/>
        </Route>
      </Route>

      <Route path = "/hod" element= {<HodSubheader/>}>
          <Route element={<HodPrivateRoute/>}>
          <Route path = "dashboard" element={<HodDashboard/>}/>
          <Route path = "inbox" element={<Inbox/>}/>
          <Route path = "viewprofile" element = {<Profile/>}/>
          <Route path = "changepwd" element = {<ChangePassword/>}/>
          </Route>
      </Route>
      
    </Routes>
)}
    </div>

  );
}

export default AuthStatus;
