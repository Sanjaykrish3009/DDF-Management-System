import React, { useContext } from 'react'
import { useState, useEffect } from 'react';
import {Card} from '../components';
import axios from 'axios';
import { AuthContext } from '../core';
import "../css_files/RequestDetails.css"
import { Loader } from "../components";
import { ErrorDisplay } from "../components";



const Transactions = () => {
  const [data, setData] = useState([]);
  const [errorMessage, setErrorMessage] = useState(null); 

  useEffect(() => {
    axios.get('http://localhost:8000/faculty/publicrequests')
      .then(response => 
        {
          if(response.data.success)
          {
            setData(response.data.data)

          }
          else{
            setErrorMessage(response.data.error);
          }
        })
      .catch(error => setErrorMessage(error.message));
  }, []);

  return (
    <div className='publicrequests'>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 

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

          <Loader/>

      )}
    </div>
  );
};

export default Transactions;
      
      
      
      
  