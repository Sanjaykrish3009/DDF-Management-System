import { useState } from 'react';
import { Link } from 'react-router-dom';

function CreateRequest() {
  const [showButtons, setShowButtons] = useState(false);

  const handleMakeRequestClick = () => {
    setShowButtons(!showButtons);
  };

  return (
    <div className="container">
      <button className="make-request" onClick={handleMakeRequestClick}>
        Make Request
      </button>
      {showButtons && (
        <div className="slide-container">
          <div className="private-button">
            <Link to="privaterequest">Private Request</Link>
          </div>
          <div className="public-button">
            <Link to="publicrequest">Public Request</Link>
          </div>
        </div>
      )}
    </div>
  );
}

export default CreateRequest;

