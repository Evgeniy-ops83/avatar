import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Хук useEffect для выполнения fetch-запроса
  useEffect(() => {
    fetch('http://localhost:8000/api/data/')  // URL вашего API (например, из Django REST Framework)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setData(data);  // Сохраняем полученные данные
        setLoading(false);  // Устанавливаем состояние загрузки в false
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);  // Пустой массив зависимостей означает, что этот код выполнится один раз при монтировании компонента

  // Обработка состояния загрузки и ошибок
  if (loading) return <p>Загрузка...</p>;
  if (error) return <p>Ошибка: {error.message}</p>;

  // Отображение полученных данных
  return (
    <div>
      <h2>Полученные данные:</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default DataFetcher;
