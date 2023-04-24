import { useState ,useEffect} from 'react';

import axios from 'axios';
import { AuthContext } from '../core';
import React, { useContext } from 'react'
import { Loader } from "../components";


const BudgetTransactions= () => {
  const [data, setData] = useState([]);
  const {user_type}=useContext(AuthContext);

  useEffect(() => {
    console.log(user_type);
    axios.get('http://localhost:8000/'+user_type+'/alltransactions')
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
            <div>
                  Transaction_id,Request_id,Amount,Type,Requested By,Date and Time,Remaining Balance
            </div>
            <div>
            
              {data.map((item)=> ( !item.status &&
                <div>{item.id},{item.request.id},{item.request.request_amount},{item.request.transaction_type},{item.request.user.email},{item.transaction_date},{item.remaining_budget}</div>

              ))}
            </div>
          </div>
        )}
        </div>
      ):(

          <Loader/>
      )}
      </div>
    );
}



export default BudgetTransactions