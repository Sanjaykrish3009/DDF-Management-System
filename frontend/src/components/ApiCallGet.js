import axios from "axios";
const ApiCallGet = ({api_url,setData,setErrorMessage,senddata}) => {

    if(senddata)
    {
        axios.get(api_url,{
            params: 
              senddata
            })
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
    else{
        axios.get(api_url)
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
   
}

export default ApiCallGet