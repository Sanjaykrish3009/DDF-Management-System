import { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { AuthContext } from './AuthContext';
import {Header, FacultySubheader, CommitteeSubheader, HodSubheader} from './header';
import { CreateRequest, FacultyDashboard, Inbox, Transactions, Profile, ChangePassword,ForgotPassword,SignUp,RequestDetails,PublicRequest,PrivateRequest,OTP, Resetpwd,BudgetRequest,BudgetTransactions,CommitteeDashboard,CommitteeRequestDetails, HodRequestDetails, HodDashboard,FileDetails  } from '../pages';
import Loginpage from './Login-page';
import {Route, Routes} from 'react-router-dom';
import {FacultyPrivateRoute, CommitteePrivateRoute, HodPrivateRoute} from "../components/PrivateRoute";
import { Loader } from '../components';

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
        // <div>Loading...</div>
        <Loader/>
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
          <Route path = "history" element = {<Transactions/>}/>
          <Route path = "makerequest" element = {<CreateRequest/>}/>
          <Route path = "viewprofile" element = {<Profile/>}/>
          <Route path = "changepassword" element = {<ChangePassword/>}/>
          <Route path = "dashboard/requests/:id" element = {<RequestDetails/>}/>
          <Route path = "inbox/requests/:id" element = {<RequestDetails/>}/>
          <Route path = "history/requests/:id" element = {<RequestDetails/>}/>
          <Route path = "makerequest/publicrequest" element={<PublicRequest/>}/>
          <Route path = "makerequest/privaterequest" element={<PrivateRequest/>}/>
          <Route path = "filedetails" element={<FileDetails/>}/>
        </Route>
      </Route>

      <Route path = "/committee" element= {<CommitteeSubheader/>}>
        <Route element={<CommitteePrivateRoute/>}>
          <Route path = "dashboard" element={<CommitteeDashboard/>}/>
          <Route path = "inbox" element={<Inbox/>}/>
          <Route path = "transactions" element = {<BudgetTransactions/>}/>
          <Route path = "budgetrequest" element = {<BudgetRequest/>}/>
          <Route path = "viewprofile" element = {<Profile/>}/>
          <Route path = "changepassword" element = {<ChangePassword/>}/>
          <Route path = "dashboard/requests/:id" element = {<CommitteeRequestDetails/>}/>
          <Route path = "inbox/requests/:id" element = {<RequestDetails/>}/>
        </Route>
      </Route>

      <Route path = "/hod" element= {<HodSubheader/>}>
          <Route element={<HodPrivateRoute/>}>
            <Route path = "dashboard" element={<HodDashboard/>}/>
            <Route path = "inbox" element={<Inbox/>}/>
            <Route path = "transactions" element = {<BudgetTransactions/>}/>
            <Route path = "viewprofile" element = {<Profile/>}/>
            <Route path = "changepassword" element = {<ChangePassword/>}/>
            <Route path = "dashboard/requests/:id" element = {<HodRequestDetails/>}/>
            <Route path = "inbox/requests/:id" element = {<RequestDetails/>}/>
          </Route>
      </Route>
      
    </Routes>
)}
    </div>

  );
}

export default AuthStatus;
