import React, { useState, useContext } from 'react';
import './AuthModal.css';  // Подключаем стили
import { AuthContext } from '../context/AuthContext';  // Импортируем контекст
import { useNavigate } from 'react-router-dom';

function AuthModal({ closeModal }) {
  const { login } = useContext(AuthContext);  // Используем контекст для авторизации
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();  // Хук для перенаправления

  const handleLogin = (e) => {
    e.preventDefault();  // Предотвращаем перезагрузку страницы

    fetch('http://localhost:8000/auth/login/', {  // Убедитесь, что URL корректный
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'include',  // Для отправки сессионных куков
      body: JSON.stringify({ email, password }),  // Отправляем email и пароль в теле запроса
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        setError(data.error);  // Обработка ошибки
      } else {
        login();  // Вызываем функцию авторизации из контекста
        closeModal();  // Закрываем модальное окно после успешного входа
        navigate('/dashboard');
    }
    })
    .catch(() => {
      setError('Ошибка при отправке запроса на авторизацию');  // Обработка ошибок запроса
    });
  };

  return (
    <div className="modal-overlay">
      <div className="modal">
        <button className="close-btn" onClick={closeModal}>&times;</button>
        <h2>Войти</h2>
        <form onSubmit={handleLogin}>
          {error && <p className="error">{error}</p>}  {/* Отображаем ошибку при наличии */}
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <label>Пароль:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit" className="btn-primary">Войти</button>
        </form>
      </div>
    </div>
  );
}

export default AuthModal;
