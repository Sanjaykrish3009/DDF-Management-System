import React, { useContext } from 'react'
import { useState, useEffect } from 'react';
import {Card} from '../components';
import axios from 'axios';
import { AuthContext } from '../core';
import "../css_files/RequestDetails.css"


const Transactions = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:8000/faculty/publicrequests')
      .then(response => setData(response.data.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div className='publicrequests'>
      {data ? (
        <div classname="dash"> 
        { data.length===0?(
        <h3>No pending Requests</h3>
        ):(
          <div>
            {data.map((item, index,user_type)=> ( !item.status &&
                <Card key={item.id} url={'requests/'+item.id} data={item}/>
            ))}
          </div>
        )}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Transactions;
      
      
      
      
  