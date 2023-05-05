import React from 'react'
import { useState, useEffect } from 'react';
import {Card, Loader} from '../components';
import '../css_files/dashboard.css';
import {ErrorDisplay} from '../components';
import SearchBar from '../components/SearchBar';
import ApiCallGet from './ApiCallGet';

const Dashboardcomponent = (props) => {
  const api_url = props.api_url;
  const [errorMessage, setErrorMessage] = useState(null); 
  const [data, setData] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');


  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchButtonClick = () => {

    const senddata = {};
    senddata.title = searchTerm;
    ApiCallGet({api_url,setData,setErrorMessage,senddata});
  };
  useEffect(() => {

    setSearchTerm('');
    const senddata = {};
    ApiCallGet({api_url,setData,setErrorMessage,senddata});
  }, [api_url]);

  return (
    <div className='dashboardpage'>
        <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage}/> 
        <SearchBar handleChange={handleSearchInputChange} handleClick={handleSearchButtonClick} />
        {data ? (
            <div classname="dashboardcomponent"> 
            { data.length===0?(
                <h3>No Pending Requests</h3>
                ):(
                <div>
                    {data.map((item)=> ( !item.status &&
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

export default Dashboardcomponent;
      
      
      
      
  