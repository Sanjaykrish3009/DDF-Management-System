import { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { AuthContext } from './AuthContext';
import Header from './header';
import {Route, Routes} from 'react-router-dom';
import {FacultyPrivateRoute, CommitteePrivateRoute, HodPrivateRoute, SecurePrivateRoute, SecurePasswordPrivateRoute, SecureVerificationPrivateRoute} from "../components/PrivateRoute";
import { Loader } from '../components';
import { FacultyDashboard, FacultyInbox , FacultyPublicRequests, CreateRequest, PrivateRequest, PublicRequest, FacultyRequestDetails, FacultySubheader} from '../pages/faculty';
import { CommitteeDashboard, CommitteeInbox, CommitteeTransactions, CreateBudgetRequest, CommitteeRequestDetails, CommitteeSubheader  } from '../pages/committee';
import { HodDashboard, HodInbox, HodTransactions, HodRequestDetails, HodSubheader } from '../pages/hod';
import { Profile, ChangePassword,ForgotPassword,SignUp,OTP, Resetpwd,SignUpOtp ,LoginPage } from '../pages';
import ApiUrls from '../components/ApiUrls';


const RoutePaths =() => {
  const {setIsAuthenticated, setUser_type} = useContext(AuthContext);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
        axios.get(ApiUrls.AUTHENTICATION_AUTHENTICATED_URL)
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
  }, [setIsAuthenticated,setUser_type]);

  return (
    <div>    
    <Header/>
    {isLoading ? (
        // <div>Loading...</div>
        <Loader/>
      ) : (
    
    <Routes>
      
      <Route path ="/" element={<LoginPage/>}/>
      <Route path ="/signup" element={<SignUp/>}/>
      <Route path ="/forgotpassword" element={<ForgotPassword/>}/>
      <Route element= {<SecurePrivateRoute/>}>
        <Route path ="/otpverification" element={<OTP/>}/>
      </Route>
      <Route element={<SecurePasswordPrivateRoute/>}>
        <Route path = "/resetpassword" element={<Resetpwd/>}/>
      </Route>
      <Route element={<SecureVerificationPrivateRoute/>}>
        <Route path = "/signupverification" element={<SignUpOtp/>}/>
      </Route>
      
      <Route path = "/faculty" element= {<FacultySubheader/>}>
        <Route element={<FacultyPrivateRoute/>}>
          <Route path = "dashboard" element={<FacultyDashboard/>}/>
          <Route path = "inbox" element={<FacultyInbox/>}/>
          <Route path = "history" element = {<FacultyPublicRequests/>}/>
          <Route path = "makerequest" element = {<CreateRequest/>}/>
          <Route path = "viewprofile" element = {<Profile/>}/>
          <Route path = "changepassword" element = {<ChangePassword/>}/>
          <Route path = "dashboard/requests/:id" element = {<FacultyRequestDetails/>}/>
          <Route path = "inbox/requests/:id" element = {<FacultyRequestDetails/>}/>
          <Route path = "history/requests/:id" element = {<FacultyRequestDetails/>}/>
          <Route path = "makerequest/publicrequest" element={<PublicRequest/>}/>
          <Route path = "makerequest/privaterequest" element={<PrivateRequest/>}/>
        </Route>
      </Route>

      <Route path = "/committee" element= {<CommitteeSubheader/>}>
        <Route element={<CommitteePrivateRoute/>}>
          <Route path = "dashboard" element={<CommitteeDashboard/>}/>
          <Route path = "inbox" element={<CommitteeInbox/>}/>
          <Route path = "transactions" element = {<CommitteeTransactions/>}/>
          <Route path = "budgetrequest" element = {<CreateBudgetRequest/>}/>
          <Route path = "viewprofile" element = {<Profile/>}/>
          <Route path = "changepassword" element = {<ChangePassword/>}/>
          <Route path = "dashboard/requests/:id" element = {<CommitteeRequestDetails/>}/>
          <Route path = "inbox/requests/:id" element = {<FacultyRequestDetails/>}/>
        </Route>
      </Route>

      <Route path = "/hod" element= {<HodSubheader/>}>
          <Route element={<HodPrivateRoute/>}>
            <Route path = "dashboard" element={<HodDashboard/>}/>
            <Route path = "inbox" element={<HodInbox/>}/>
            <Route path = "transactions" element = {<HodTransactions/>}/>
            <Route path = "viewprofile" element = {<Profile/>}/>
            <Route path = "changepassword" element = {<ChangePassword/>}/>
            <Route path = "dashboard/requests/:id" element = {<HodRequestDetails/>}/>
            <Route path = "inbox/requests/:id" element = {<FacultyRequestDetails/>}/>
          </Route>
      </Route>
      
    </Routes>
)}
    </div>

  );
}

export default RoutePaths;
