import React from 'react'
import { useState, useEffect } from 'react';
import axios from 'axios';
import {Card} from '../components';
import '../css_files/dashboard.css';
import { Loader } from "../components";


const HodDashboard = () => {

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/hod/pendingrequests')
      .then(response => setData(response.data.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div className='dashboard'>
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

export default HodDashboard;