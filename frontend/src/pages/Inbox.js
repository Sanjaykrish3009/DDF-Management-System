import { useState ,useEffect} from 'react';
import {Card} from '../components';
import axios from 'axios';
import { AuthContext } from '../core';
import React, { useContext } from 'react'

const Inbox = () => {

  const [data, setData] = useState([]);
  const {user_type}=useContext(AuthContext);

  useEffect(() => {
    console.log(user_type);
    axios.get('http://localhost:8000/'+user_type+'/previousrequests')
      .then(response => setData(response.data.data))
      .catch(error => console.log(error));
  }, []);
  return (
    <div className='dashboard'>
      {data ? (
         <div>
          { data.length===0?(
          <div>No pendingrequests</div>
          ):(
          <div>
            {data.map((item)=> ( !item.status &&
              <Card key={item.id} data={item} url={'requests/'+item.id}/>
            ))}
          </div>
          )}
        </div>
      ):(
        <p>Loading...</p>
      )}
      </div>
    );
}

export default Inbox