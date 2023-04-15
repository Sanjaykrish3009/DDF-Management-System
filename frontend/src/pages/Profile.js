import React,{useContext,useEffect} from 'react'
import { AuthContext } from '../core';
import axios from 'axios';


const Profile = () => {
  const { user,setUser} = useContext(AuthContext);
  useEffect(() => {
    axios.get('http://localhost:8000/user/profile')
      .then(response => setUser(response.data.profile))
      .catch(error => console.log(error));
  }, []);


  return (
    <div>
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
        <div className="loading-message ">
          <p>Loading user profile...</p>
        </div>
        
      )}
    </div>
    
  )
}

export default Profile