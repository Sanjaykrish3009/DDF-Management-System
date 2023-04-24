import React,{useContext,useEffect,useState} from 'react'
import { AuthContext } from '../core';
import axios from 'axios';
import '../css_files/profile.css';
import { Loader } from "../components";
import { ErrorDisplay } from "../components";



const Profile = () => {
  const { user,setUser} = useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState(null); 

  useEffect(() => {
    axios.get('http://localhost:8000/user/profile')
      .then(response => 
        {
          if(response.data.success)
          {
            setUser(response.data.profile)

          }
          else{
            setErrorMessage(response.data.error);

          }
        })
      .catch(error => setErrorMessage(error.message));
  }, []);


  return (
    <div>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 

      {user ? (
        <div className="profile-section">
          <h2>USER DETAILS</h2>
          <div className="user details">
            <p>First Name: {user.firstname}</p>
            <p>Last Name: {user.lastname}</p>
            <p>Email ID: {user.email}</p>
          </div>
        </div>
      ) : (
        // <div className="loading-message ">
        //   <p>Loading user profile...</p>
        // </div>

          <Loader/>

        
      )}
    </div>
    
  )
}

export default Profile