import { BrowserRouter} from 'react-router-dom'
import { AuthContextProvider } from './AuthContext';
import AuthStatus from './AuthStatus';

const AppLogin = () => {
  return (
    <>
      <AuthContextProvider>
      <BrowserRouter>
          <AuthStatus />
      </BrowserRouter>
      </AuthContextProvider>
    </>
  )
}

export default AppLogin;
