import "../../css_files/header.css"

import React,{useState,useRef,useContext} from 'react'
import { Link, Outlet, Navigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { FaHome, FaMailBulk, FaHistory, FaPlusCircle } from "react-icons/fa";
import { CgProfile} from "react-icons/cg";
import { AuthContext } from "../../core";
import * as RiIcons from 'react-icons/ri';
import axios from 'axios';
import ApiUrls from "../../components/ApiUrls";

const FacultySubheader=()=>{
    const [menuopen,setmenuOpen]=useState(false);
    const menuRef=useRef();
    const dropdownRef=useRef();
    const [islogout,setLogout]=useState(false);
    const { logout } = useContext(AuthContext);
    window.addEventListener('click',(e)=>{
       if(e.target!==menuRef.current&&e.target!==dropdownRef.current)
       {
          setmenuOpen(false);
       }
    });
 
    const Loggingout = () => {
       axios.post(ApiUrls.AUTHENTICATION_LOGOUT_URL,{
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

 export default FacultySubheader;
 