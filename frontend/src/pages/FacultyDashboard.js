import React, { useContext } from 'react'
import { useState, useEffect } from 'react';
import { AuthContext } from '../core';

const FacultyDashboard = () => {
  const {user_type}=useContext(AuthContext);

  return (
    <div className='dashboard'>
      <h3>No pending Requests</h3>
    </div>
  );
};

export default FacultyDashboard;
      
      
      
      
  