import React from 'react'
import '../css_files/ErrorDisplay.css'

const ErrorDisplay = (props) => {
  const{errormessage,seterrormessage}=props;
  return (
    errormessage && (
        <div className="error-message-box">
          <div className="error-message">{errormessage}</div>
            <button className="close-button" onClick={() => seterrormessage(null)}>
              <span aria-hidden="true">&times;</span>
            </button>
        </div>
      )
  )
}

export default ErrorDisplay