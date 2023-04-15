import React, { useContext } from 'react'
import { AuthContext } from '../core';

const CommitteeDashboard = () => {
  const {user_type}=useContext(AuthContext);

  return (
    <div className='dashboard'>
    </div>
  );
};

export default CommitteeDashboard;