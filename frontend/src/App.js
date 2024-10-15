import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';  // Импорт провайдера
import Header from './components/Header';
import HomePage from './components/HomePage';
import Dashboard from './components/Dashboard';
import AuthModal from './components/AuthModal';

function App() {

   // Функция для проверки статуса сессии
   const handleLoginStatus = () => {
    fetch('http://localhost:8000/api/check-session/', {
      method: 'GET',
      credentials: 'include',  // Включаем отправку сессионной куки
    })
    .then(response => {
      if (response.status === 401) {  // Если сессия истекла
        localStorage.setItem('isLoggedIn', 'false');
        alert('Ваша сессия истекла, пожалуйста, войдите снова.');
        window.location.href = '/login';  // Перенаправляем на страницу логина
      }
    })
    .catch(error => {
      console.error('Ошибка проверки сессии:', error);
    });
  };

  useEffect(() => {
    // Проверяем статус сессии каждые 5 минут
    const intervalId = setInterval(() => {
      handleLoginStatus();  // Проверяем сессию
    }, 300000);  // 300000 миллисекунд = 5 минут

    // Очищаем интервал при размонтировании компонента
    return () => clearInterval(intervalId);
  }, []);

  return (
    <AuthProvider>
      <Router>

        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/auth" element={<AuthModal />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
