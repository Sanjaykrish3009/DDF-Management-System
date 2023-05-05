import React, { createContext, useState } from 'react';
export const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isValid, setValid] = useState(false);
  const [isValidOtp, setValidOtp] = useState(false);

  const [user, setUser] = useState(null);
  const [emailID,setEmailID] =useState('');
  const [user_type,setUser_type] =useState('');
  const [isValidEmail,setValidEmail] = useState(false);

  const login = () => {
    setIsAuthenticated(true);
  };

  const logout = () => {
    setIsAuthenticated(false);
  };
  
  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, setIsAuthenticated, user, setUser, emailID, setEmailID, user_type,setUser_type,isValid,setValid,isValidOtp,setValidOtp,isValidEmail,setValidEmail }}>
      {children}
    </AuthContext.Provider>
  );
};
