import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const response = await axios.get('/api/hello');
        setMessage(response.data.message);
      } catch (error) {
        console.error("There was an error fetching data from the API!", error);
      }
    };

    fetchMessage();
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  );
}

export default App;
