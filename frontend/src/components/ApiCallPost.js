import Cookies from 'js-cookie';
import axios from 'axios';

const ApiCallPost = ({api_url,setData,setErrorMessage,senddata}) => {

   
    axios.post(api_url,senddata,
    {
        headers:{
            'X-CSRFToken' :Cookies.get('csrftoken')
    }} )
    .then(response =>{ setData(response.data.data)
    
    if(response.data.success){
        setData(response.data.data);
    }
    else{
        setErrorMessage(response.data.error);
    }
    })
    .catch(error => setErrorMessage(error.message));

   
}

export default ApiCallPost


