import { BrowserRouter} from 'react-router-dom'
import { AuthContextProvider } from './AuthContext';
import RoutePaths from './RoutePaths';

const AppLogin = () => {
  return (
    <>
      <AuthContextProvider>
      <BrowserRouter>
          <RoutePaths />
      </BrowserRouter>
      </AuthContextProvider>
      
    </>
  )
}

export default AppLogin;
