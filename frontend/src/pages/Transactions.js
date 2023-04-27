import React, { useContext } from 'react'
import { useState, useEffect } from 'react';
import {Card} from '../components';
import axios from 'axios';
import { AuthContext } from '../core';
import "../css_files/dashboard.css"
import { Loader } from "../components";
import { ErrorDisplay,SearchBar } from "../components";



const Transactions = () => {
  const [data, setData] = useState([]);
  const [errorMessage, setErrorMessage] = useState(null); 
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchButtonClick = () => {
    // Perform search with searchTerm
    // console.log(`Searching for ${searchTerm}...`);

      axios.get('http://localhost:8000/faculty/publicrequests',
      {
      params: {
        title: searchTerm
      }
      })
        .then(response =>{ setData(response.data.data)
        
          if(response.data.success){
            setData(response.data.data);
          }
          else{
            setErrorMessage(response.data.error);
          }
        })
        .catch(error => setErrorMessage(error.message));
    
  }
    

  useEffect(() => {
    setSearchTerm('');
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
    <div className='dashboardpage'>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 
      <SearchBar handleChange={handleSearchInputChange} handleClick={handleSearchButtonClick} />

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
      
      
      
      
  