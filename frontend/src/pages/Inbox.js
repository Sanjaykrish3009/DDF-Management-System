import { useState ,useEffect} from 'react';
import {Card} from '../components';
import axios from 'axios';
import { AuthContext } from '../core';
import React, { useContext } from 'react'
import { Loader, ErrorDisplay } from "../components";


const Inbox = () => {

  const [data, setData] = useState([]);
  const {user_type}=useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState(null); 


  useEffect(() => {
    console.log(user_type);
    axios.get('http://localhost:8000/'+user_type+'/previousrequests')
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
    <div className='dashboard'>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 

      {data ? (
         <div>
          { data.length===0?(
          <h3>No pendingrequests</h3>
          ):(
          <div>
            {data.map((item)=> ( !item.status &&
              <Card key={item.id} data={item} url={'requests/'+item.id}/>
            ))}
          </div>
          )}
        </div>
      ):(

          <Loader/>

      )}
      </div>
    );
}

export default Inbox