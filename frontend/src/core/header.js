import "../css_files/header.css"

import React,{useState,useRef,useContext} from 'react'
import { Link, Outlet, Navigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { FaHome, FaMailBulk, FaHistory, FaPlusCircle } from "react-icons/fa";
import { CgProfile} from "react-icons/cg";
import { AuthContext } from "./AuthContext";
import * as RiIcons from 'react-icons/ri';
import axios from 'axios';

const Header= () => {
  return (
     <div >
         <div className='header'>
            <div className="headtitle">
            Department Fund Management system
            </div>
         </div>
         
      
     </div>
     
  )
};


const FacultySubheader=()=>{
   const [menuopen,setmenuOpen]=useState(false);
   const menuRef=useRef();
   const dropdownRef=useRef();
   const [islogout,setLogout]=useState(false);
   const [showProfile,setShowProfile] = useState(false);
   const { setUser, logout } = useContext(AuthContext);
   window.addEventListener('click',(e)=>{
      if(e.target!==menuRef.current&&e.target!==dropdownRef.current)
      {
         setmenuOpen(false);
      }
   });

   const Loggingout = () => {
      axios.post(`http://localhost:8000/authentication/logout`,{
         'withCredentials':true
      },
      {
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        setLogout(true);
        logout();

      })
      .catch(error =>{
        console.log(error.response.data);
      });

   }

   if(islogout)
   {
      return <Navigate to = '/'/>
   }
    return (
        <div >
            {}
            <div className="subheader">
               <Link to ='/faculty/dashboard' className='link'> <FaHome/> Dashboard </Link>
               <Link to='/faculty/inbox' className='link'> <FaMailBulk/> Inbox </Link>
               <Link to='/faculty/history' className='link'> <FaHistory/> Public Requests </Link>
               <Link to='/faculty/makerequest' className='link'> <FaPlusCircle/> Create Fund Request </Link>
               <div className='dropdown'>
                  <button ref={dropdownRef} className='link'  onClick={()=>setmenuOpen(!menuopen)}> <CgProfile/> MyAccount <RiIcons.RiArrowDropDownFill/></button>
                  {
                     menuopen && (<div ref={menuRef} className='dropdown-menu'>
                     <Link to ='/faculty/viewprofile' className='droplink'>Profile</Link>
                     <Link to ='/faculty/changepassword' className='droplink'>change password</Link>
                     <button className='droplink' onClick={Loggingout}>Logout</button>     
                  </div>) 
                  }
                  
               </div>
               
            </div>
            <Outlet/>
            {}
        </div>
     )
};


const CommitteeSubheader=()=>{
   const [menuopen,setmenuOpen]=useState(false);
   const menuRef=useRef();
   const dropdownRef=useRef();
   const [islogout,setLogout]=useState(false);
   const [showProfile,setShowProfile] = useState(false);
   const { setUser, logout } = useContext(AuthContext);
   window.addEventListener('click',(e)=>{
      if(e.target!==menuRef.current&&e.target!==dropdownRef.current)
      {
         setmenuOpen(false);
      }
   });

 
   const Loggingout = () => {
      axios.post(`http://localhost:8000/authentication/logout`,{
         'withCredentials':true
      },
      {
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        setLogout(true);
        logout();

      })
      .catch(error =>{
        console.log(error.response.data);
      });

   }

   if(islogout)
   {
      return <Navigate to = '/'/>
   }
    return (
        <div >
            {}
            <div className="subheader">
               <Link to ='/committee/dashboard' className='link'> <FaHome/> Dashboard </Link>
               <Link to='/committee/inbox' className='link'> <FaMailBulk/> Inbox </Link>
               <Link to='/committee/transactions' className='link'> <FaHistory/> Transactions </Link>
               <Link to='/committee/budgetrequest' className='link'> <FaPlusCircle/> Create Budget Request </Link>
               <div className='dropdown'>
                  <button ref={dropdownRef} className='link'  onClick={()=>setmenuOpen(!menuopen)}> <CgProfile/> MyAccount <RiIcons.RiArrowDropDownFill/></button>
                  {
                     menuopen && (<div ref={menuRef} className='dropdown-menu'>
                     <Link to ='/committee/viewprofile' className='link'>Profile</Link>
                     <Link to ='/committee/changepassword' className='link'>change password</Link>
                     <button className='link' onClick={Loggingout}>Logout</button>     
                  </div>) 
                  }
                  
               </div>
               
            </div>
            <Outlet/>
            {}
        </div>
     )
};


const HodSubheader=()=>{
   const [menuopen,setmenuOpen]=useState(false);
   const menuRef=useRef();
   const dropdownRef=useRef();
   const [islogout,setLogout]=useState(false);
   const [showProfile,setShowProfile] = useState(false);
   const { setUser, logout } = useContext(AuthContext);
   window.addEventListener('click',(e)=>{
      if(e.target!==menuRef.current&&e.target!==dropdownRef.current)
      {
         setmenuOpen(false);
      }
   });

 
   const Loggingout = () => {
      axios.post(`http://localhost:8000/authentication/logout`,{
         'withCredentials':true
      },
      {
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken')
      }
    })
      .then(response =>{
        console.log(response.data);
        setLogout(true);
        logout();

      })
      .catch(error =>{
        console.log(error.response.data);
      });

   }

   if(islogout)
   {
      return <Navigate to = '/'/>
   }
    return (
        <div >
            {}
            <div className="subheader">
               <Link to ='/hod/dashboard' className='link'> <FaHome/> Dashboard </Link>
               <Link to='/hod/inbox' className='link'> <FaMailBulk/> Inbox </Link>
               <Link to='/hod/transactions' className='link'> <FaHistory/> Transactions </Link>
               <div className='dropdown'>
                  <button ref={dropdownRef} className='link'  onClick={()=>setmenuOpen(!menuopen)}> <CgProfile/> MyAccount <RiIcons.RiArrowDropDownFill/></button>
                  {
                     menuopen && (<div ref={menuRef} className='dropdown-menu'>
                     <Link to ='/hod/viewprofile' className='link'>Profile</Link>
                     <Link to ='/hod/changepassword' className='link'>Change password</Link>
                     <button className='link' onClick={Loggingout}>Logout</button>     
                  </div>) 
                  }
                  
               </div>
               
            </div>
            <Outlet/>
            {}
        </div>
     )
};



export {Header,FacultySubheader,CommitteeSubheader, HodSubheader};
