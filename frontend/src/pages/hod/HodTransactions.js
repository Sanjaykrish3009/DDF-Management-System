import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import React from 'react';
import { Loader } from '../../components';
import { ErrorDisplay } from '../../components';
import '../../css_files/transactions.css';
import Cookies from 'js-cookie';
import ApiUrls from '../../components/ApiUrls';
import ApiCallGet from '../../components/ApiCallGet';

const HodTransactions = () => {
  const [data, setData] = useState([]);
  const [errorMessage, setErrorMessage] = useState(null);
  const [loader,setloader] = useState(true);

  const sendEmail = () => {
    setloader(false);
    axios.post(ApiUrls.HOD_SENDEXCEL_URL,{

    }
    ,
    {
      headers:{
        'X-CSRFToken' :Cookies.get('csrftoken'),
      }
    })
    .then((response) => {
      setloader(true);
      if (response.data.success) {
       
        setErrorMessage(response.data.success);
      } else {
        setErrorMessage(response.data.error);
      }
    })
    .catch((error) =>
    {
      setloader(true);
      setErrorMessage(error.message)}
      );
    
  }

  useEffect(() => {
    const senddata ={};
    const api_url = ApiUrls.HOD_TRANSACTIONS_URL;
    ApiCallGet({api_url,setData,setErrorMessage,senddata});
  }, []);
  
  return (
    <div className='dashboard'>
     

      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage} />
      <div className='transactions-wrapper'>
        
        {data && loader? (
          <div>
          <div className='transactions-header'>
          <h2>Transactions</h2>
          <button className='Excel' onClick={()=>(sendEmail())}> Send To Admin </button>
          
          </div>
          <div>
          <table className='transaction-table'>
            <thead>
              <tr>
                <th>Transaction ID</th>
                <th>Request ID</th>
                <th>Amount</th>
                <th>Type</th>
                <th>Requested By</th>
                <th>Date and Time</th>
                <th>Remaining Balance</th>
              </tr>
            </thead>
            <tbody>
              {data.length === 0 ? (
                <tr>
                  <td className='no-transactions' colSpan={7}>
                    No Transactions
                  </td>
                </tr>
              ) : (
                data.map((item) => {
                  if (!item.status) {
                    
                    return (
                      <tr key={item.id}>
                        <td>{item.id}</td>
                        <td>
                          <Link to={`/hod/inbox/requests/${item.request.id}`}>
                            {item.request.id}
                          </Link>
                        </td>
                        <td>{item.request.request_amount}</td>
                        <td>
                          {item.request.transaction_type}
                          </td>
                        <td>{item.request.user.email}</td>
                        <td>{item.transaction_date}</td>
                        <td>{item.remaining_budget}</td>
                      </tr>
                    );
                  } else {
                    return null;
                  }
                })
              )}
            </tbody>
          </table>

          </div>
          </div>
        ) : (
          
            <Loader />
          
        )}
      </div>
    </div>
  );
};

export default HodTransactions;
