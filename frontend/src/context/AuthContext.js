import React, { createContext, useState, useEffect } from 'react';

// Создаём контекст
export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Проверка авторизации при загрузке компонента
  useEffect(() => {
    const sessionExists = localStorage.getItem('isLoggedIn') === 'true';
    setIsLoggedIn(sessionExists);
  }, []);

  const login = () => {
    setIsLoggedIn(true);
    localStorage.setItem('isLoggedIn', 'true');
  };

  const logout = () => {
    setIsLoggedIn(false);
    localStorage.setItem('isLoggedIn', 'false');
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
