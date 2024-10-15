import React, { useState } from 'react';
import './HomePage.css';
import Header from './Header';  // Импортируем компонент Header
import AuthModal from './AuthModal'; // Импортируем модальное окно
import ChatWidget from './ChatWidget';  // Импортируем компонент чатбота

function HomePage() {
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);  // Управление модальным окном

  return (
    <div className="homepage">
      {/* Шапка сайта */}
      <Header onLoginClick={() => setIsAuthModalOpen(true)} />  {/* Передаем обработчик открытия модалки */}
      
      {/* Основное содержимое страницы */}
      <div className="main-content">
        <div className="left-content">
          <h1>Наш чатбот</h1>
          <p>Этот виджет демонстрирует возможности нашего чатбота. Вы можете встроить такой виджет на свой сайт, чтобы автоматизировать общение с клиентами.</p>
          <p>Наши чатботы помогут вам:</p>
          <ul>
            <li>Отвечать на часто задаваемые вопросы</li>
            <li>Автоматизировать запросы клиентов</li>
            <li>Улучшить взаимодействие с клиентами</li>
          </ul>
        </div>

        <div className="right-content">
          <ChatWidget />  {/* Виджет с демонстрацией чатбота */}
        </div>
      </div>

      {/* Отображаем модальное окно только при открытии */}
      {isAuthModalOpen && <AuthModal closeModal={() => setIsAuthModalOpen(false)} />}
    </div>
  );
}

export default HomePage;
