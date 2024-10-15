import React from 'react';
import './Hero.css'; // Импортируем стили

function Hero() {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>Создавайте умные чатботы с нами</h1>
        <p>Решения для автоматизации взаимодействия с клиентами. Инновации и поддержка 24/7.</p>
        <a href="#services" className="btn-primary">Начать сейчас</a>
      </div>
    </section>
  );
}

export default Hero;
