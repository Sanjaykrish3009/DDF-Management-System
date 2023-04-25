import React from 'react'
import { useState, useEffect } from 'react';
import axios from 'axios';
import {Card} from '../components';
import '../css_files/dashboard.css';
import { Loader } from "../components";
import {ErrorDisplay} from '../components';

const CommitteeDashboard = () => {

  const [errorMessage, setErrorMessage] = useState(null); 
  const [data, setData] = useState([]);
  
  useEffect(() => {
    axios.get('http://localhost:8000/committee/pendingrequests')
      .then(response =>{ setData(response.data.data)
      
        if(response.data.success){
          setData(response.data.data);
        }
        else{
          setErrorMessage(response.data.error);
        }
      })
      .catch(error => setErrorMessage(error.message));
      
  }, []);

  return (
    <div className='dashboard'>
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

export default CommitteeDashboard;