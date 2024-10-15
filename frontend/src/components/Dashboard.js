import React from 'react';
import Header from './Header';  // Импортируем компонент шапки

function Dashboard() {
  return (
    <div>
      <Header />  {/* Шапка будет отображаться и на странице ЛК */}
      <div className="dashboard-content">
        <h1>Добро пожаловать в Личный Кабинет!</h1>
        <p>Здесь вы можете управлять своим аккаунтом и ботами.</p>
      </div>
    </div>
  );
}

export default Dashboard;
