import React from 'react'
import {Card} from '../components';
import '../css_files/dashboard.css';


const CommitteeDashboard = () => {
  const [selectedCard, setSelectedCard] = useState(null);

  const handleViewDetails = (request_id) => {
    setSelectedCard(request_id);
    
  };

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/committee/pendingrequests')
      .then(response => setData(response.data.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div className='dashboard'>
      {data ? (
        <div>
          {data.map((item, index,user_type)=> ( !item.status &&
          <Card key={item.id}
                url={'requests/'+item.id}
                data={item}
              
                />
          ))}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default CommitteeDashboard;