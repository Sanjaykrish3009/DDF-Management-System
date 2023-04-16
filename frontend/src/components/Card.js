
import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../css_files/card.css';

const Card = (props) => {
  const { data, url } = props;
  const history = useNavigate();

  const handlebutton = (event, data, url) => {
    event.preventDefault();
    history(url, { state: data });
  };

  return (
    <div className="card-container">
      <div className="card">
        <div className="card-header">
          <div className='card-title'>{data.request_title}</div>
          <div>{data.request_date}</div>
        </div>
        <div className="card-body">
          <div className="status-bar">
            <div className={`status-dot ${data.request_generated ? "green" : "green"}`}></div>
            <div className="status-text">
              Request generated
            </div>
            <div className="status-line"></div>
            <div className={`status-dot ${data.committee_approval_status === "Approved" ? "green" : data.committee_approval_status === "Disapproved" ? "red" : "gray"}`}></div>
            <div className="status-text">
              Committee decision
            </div>
            <div className="status-line"></div>
            <div className={`status-dot ${data.hod_approval_status === "Approved" ? "green" :data.hod_approval_status === "Disapproved" ? "red" : "gray"}`}></div>
            <div className="status-text">
              HOD decision
            </div>
          </div>
        
        <div className="card-footer">
          <button
            className="btn btn-primary"
            onClick={(event) => handlebutton(event, data, url)}
          >
            View Details
          </button>
        </div>
      </div>
      </div>
    </div>
  );
};

export default Card;
