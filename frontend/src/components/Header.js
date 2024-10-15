import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../context/AuthContext';  // Импортируем контекст
import { useNavigate } from 'react-router-dom';  // Хук для перенаправления

// Функция для получения CSRF-токена из куки
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function Header({ onLoginClick }) {
  const { logout } = useContext(AuthContext);  // Получаем функцию выхода
  const [isAuthenticated, setIsAuthenticated] = useState(false);  // Локальное состояние авторизации
  const navigate = useNavigate();  // Хук для перенаправления

  // Проверка сессии через запрос на сервер
  useEffect(() => {
    const checkSession = () => {
      fetch('http://localhost:8000/auth/check-session/', {
        method: 'GET',
        credentials: 'include',  // Отправляем куки
      })
      .then(response => {
        if (!response.ok) {
          console.error('Ошибка проверки сессии:', response.status);
          return { authenticated: false };
        }
        return response.json();
      })
      .then(data => {
        if (data.authenticated !== undefined && data.authenticated) {
          setIsAuthenticated(true);
        } else {
          setIsAuthenticated(false);
          logout();  // Вызываем функцию выхода из контекста
          navigate('/');  // Перенаправляем на главную страницу, если сессия истекла
        }
      })
      .catch(error => {
        console.error('Ошибка запроса:', error);
        setIsAuthenticated(false);
        logout();  // Вызываем функцию выхода
        navigate('/');  // Перенаправляем на главную страницу
      });
    };

    checkSession();  // Проверка сессии при первом рендере

    const intervalId = setInterval(checkSession, 30000);  // Проверяем сессию каждые 5 минут
    return () => clearInterval(intervalId);  // Очищаем интервал при размонтировании
  }, [logout, navigate]);

  const handleLogout = () => {
    const csrftoken = getCookie('csrftoken');  // Получаем CSRF-токен

    fetch('http://localhost:8000/auth/logout/', {
      method: 'POST',
      credentials: 'include',  // Отправляем сессионные куки
      headers: {
        'X-CSRFToken': csrftoken,  // Добавляем CSRF-токен в заголовок
      },
    })
    .then(response => {
      if (response.ok) {
        logout();  // Вызываем функцию выхода из контекста
        alert('Вы вышли из системы');
        setIsAuthenticated(false);  // Обновляем состояние, разлогинивая пользователя
        navigate('/');  // Перенаправляем на главную страницу
      } else {
        console.error('Ошибка выхода:', response.status);
      }
    })
    .catch(error => {
      console.error('Ошибка запроса выхода:', error);
    });
  };

  return (
    <header className="header">
      <div className="logo">Логотип</div>
      <nav className="nav">
        <ul>
          <li><a href="/">О нас</a></li>
          <li><a href="/services">Сервисы</a></li>
          <li><a href="/blog">Блог</a></li>
          {isAuthenticated ? (  // Если пользователь авторизован, показываем личный кабинет и кнопку выхода
            <>
              <li><a href="/dashboard">Мой кабинет</a></li>
              <li><button onClick={handleLogout}>Выйти</button></li>
            </>
          ) : (  // Если не авторизован, показываем кнопку Войти
            <li><button onClick={onLoginClick}>Войти</button></li>
          )}
        </ul>
      </nav>
    </header>
  );
}

export default Header;
