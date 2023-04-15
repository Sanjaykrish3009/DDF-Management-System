import { useState ,useEffect} from 'react';
import { AuthContext } from '../core';
import React, { useContext } from 'react'

const Inbox = () => {
  const {user_type}=useContext(AuthContext);

  return (
    <div className='inbox'>
      <h3>Empty</h3>
    </div>
  );
};

export default Inbox