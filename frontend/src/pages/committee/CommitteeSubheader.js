import "../../css_files/header.css"
import ApiUrls from "../../components/ApiUrls";
import React,{useState,useRef,useContext} from 'react'
import { Link, Outlet, Navigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import { FaHome, FaMailBulk, FaHistory, FaPlusCircle } from "react-icons/fa";
import { CgProfile} from "react-icons/cg";
import { AuthContext } from "../../core";
import * as RiIcons from 'react-icons/ri';
import axios from 'axios';

const CommitteeSubheader=()=>{
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
                <Link to ='/committee/dashboard' className='link'> <FaHome/> Dashboard </Link>
                <Link to='/committee/inbox' className='link'> <FaMailBulk/> Inbox </Link>
                <Link to='/committee/transactions' className='link'> <FaHistory/> Transactions </Link>
                <Link to='/committee/budgetrequest' className='link'> <FaPlusCircle/> Create Budget Request </Link>
                <div className='dropdown'>
                   <button ref={dropdownRef} className='link'  onClick={()=>setmenuOpen(!menuopen)}> <CgProfile/> MyAccount <RiIcons.RiArrowDropDownFill/></button>
                   {
                      menuopen && (<div ref={menuRef} className='dropdown-menu'>
                      <Link to ='/committee/viewprofile' className='droplink'>Profile</Link>
                      <Link to ='/committee/changepassword' className='droplink'>change password</Link>
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

 export default CommitteeSubheader;
 