import { useContext } from "react";
import { Route, Redirect, Navigate ,Outlet} from "react-router-dom";
import { AuthContext } from "../core";


const FacultyPrivateRoute = () => {
  const {isAuthenticated,user_type} =useContext(AuthContext);
  return isAuthenticated && user_type==='faculty'? <Outlet/> : <Navigate to="/" />;
};

const CommitteePrivateRoute = () => {
  const {isAuthenticated,user_type} =useContext(AuthContext);
  return isAuthenticated && user_type==='committee'? <Outlet/> : <Navigate to="/" />;
};

const HodPrivateRoute = () => {
  const {isAuthenticated,user_type} =useContext(AuthContext);
  return isAuthenticated && user_type==='hod'? <Outlet/> : <Navigate to="/" />;
};

export {FacultyPrivateRoute,CommitteePrivateRoute,HodPrivateRoute};