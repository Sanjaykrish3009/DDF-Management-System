import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import React from 'react';
import { Loader ,ErrorDisplay} from '../../components';
import '../../css_files/transactions.css';
import ApiUrls from '../../components/ApiUrls';
import ApiCallGet from '../../components/ApiCallGet';


const CommitteeTransactions = () => {
  const [data, setData] = useState([]);
  const [errorMessage, setErrorMessage] = useState(null);
 
  useEffect(() => {
    const senddata ={};
    const api_url = ApiUrls.COMMITTEE_TRANSACTIONS_URL;
    ApiCallGet({api_url,setData,setErrorMessage,senddata});
  }, []);
  
  return (
    <div className='dashboard'>
      <ErrorDisplay errormessage={errorMessage} seterrormessage={setErrorMessage} />
      <div className='transactions-wrapper'>
        
        {data? (
          <div>
          <div className='transactions-header'>
          <h2>Transactions</h2>          
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
                          <Link to={`/committee/inbox/requests/${item.request.id}`}>
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

export default CommitteeTransactions;
