import React, { useState } from 'react';
import './ChatWidget.css';

function ChatWidget() {
  const [messages, setMessages] = useState([
    { from: 'bot', text: 'Привет! Я чатбот. Чем могу помочь?' }
  ]);
  const [input, setInput] = useState('');

  const handleSend = (e) => {
    e.preventDefault();
    if (input.trim() !== '') {
      setMessages([...messages, { from: 'user', text: input }]);
      setInput('');
      // Здесь можно добавить логику отправки запроса к серверу или API чатбота
      setTimeout(() => {
        setMessages((prevMessages) => [
          ...prevMessages,
          { from: 'bot', text: 'Это пример ответа от чатбота.' }
        ]);
      }, 1000);  // Имитируем ответ через 1 секунду
    }
  };

  return (
    <div className="chat-widget">
      <div className="chat-header">
        <h3>Чат с ботом</h3>
      </div>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.from}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form className="chat-input" onSubmit={handleSend}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Напишите сообщение..."
        />
        <button type="submit">Отправить</button>
      </form>
    </div>
  );
}

export default ChatWidget;
