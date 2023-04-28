import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { AuthContext } from '../core';
import React, { useContext } from 'react';
import { Loader } from '../components';
import { ErrorDisplay } from '../components';
import '../css_files/transactions.css';
import Cookies from 'js-cookie';


const BudgetTransactions = () => {
  const [data, setData] = useState([]);
  const { user_type } = useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState(null);
  const [loader,setloader] = useState(true);

  const sendEmail = () => {
    setloader(false);
    axios.post(`http://localhost:8000/hod/sendexcelsheet`,{

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
    console.log(user_type);
    axios
      .get('http://localhost:8000/' + user_type + '/alltransactions')
      .then((response) => {
        if (response.data.success) {
         
          setData(response.data.data);
         
        } else {
          setErrorMessage(response.data.error);
        }
      })
      .catch((error) => setErrorMessage(error.message));
  }, []);
  
  return (
    <div className='dashboard'>
      <button className='Excel' onClick={()=>(sendEmail())}> Send To Admin </button>

      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage} />
      <div className='transactions-wrapper'>
        <div className='transactions-header'>
          <h2>Transactions</h2>
        </div>
        {data && loader? (
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
                          <Link to={`/${user_type}/inbox/requests/${item.request.id}`}>
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
        ) : (
          
            <Loader />
          
        )}
      </div>
    </div>
  );
};

export default BudgetTransactions;
