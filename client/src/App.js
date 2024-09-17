import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [instances, setInstances] = useState([]);

  useEffect(() => {
    const fetchInstances = async () => {
      try {
        const response = await axios.get('/api/ec2/');
        setInstances(response.data.instances || []);
      } catch (error) {
        console.error("There was an error fetching data from the API!", error);
      }
    };

    fetchInstances();
  }, []);

  return (
    <div className="App">
    {instances.map((instance, index) => (
        <div key={index}>
          <p>{instance}</p>
          <div style={{ marginBottom: '1rem' }}></div>
        </div>
      ))}
    </div>
  );
}

export default App;
