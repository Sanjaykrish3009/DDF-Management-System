import React from 'react'
import { useState, useEffect } from 'react';
import axios from 'axios';
import {Card} from '../components';
import '../css_files/dashboard.css';
import { Loader } from "../components";
import {ErrorDisplay} from '../components';
import SearchBar from '../components/SearchBar';






const FacultyDashboard = () => {
  const [errorMessage, setErrorMessage] = useState(null); 
  const [data, setData] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchButtonClick = () => {
    // Perform search with searchTerm
    // console.log(`Searching for ${searchTerm}...`);

      axios.get('http://localhost:8000/faculty/pendingrequests',
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
    
    
  };
  useEffect(() => {
    setSearchTerm('');

    axios.get('http://localhost:8000/faculty/pendingrequests')
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
    <div className='dashboardpage'>
        <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 
        <SearchBar handleChange={handleSearchInputChange} handleClick={handleSearchButtonClick} />

      {data ? (
        <div classname="dashboardcomponent"> 
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

export default FacultyDashboard;
      
      
      
      
  