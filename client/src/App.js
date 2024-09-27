import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [instances, setInstances] = useState([]);

  useEffect(() => {
    const fetchInstances = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/ec2');
        // console.log("API Response:", response.data);
        setInstances(response.data || []);
      } catch (error) {
        console.error("There was an error fetching data from the API!", error);
      }
    };

    const eventSource = new EventSource('http://localhost:5000/api/ec2');
    eventSource.onmessage = (event) => {
      // console.log(typeof JSON.parse(event.data));
      setInstances(JSON.parse(event.data) || []);
    }
    fetchInstances();
  }, []);

  // console.log(instances);

  return !instances || instances.length === 0 ? (
    <div>
      <h1>No instances available.</h1>
    </div>
  ) : (
    <div>
      <h1>Instances:</h1>
      <table>
        <thead>
          <tr>
            <th>Instance ID</th>
            <th>State</th>
            <th>Name</th>
            <th>Public IP</th>
            <th>Elastic IP</th>
          </tr>
        </thead>
        <tbody>
          {instances.map((instance) => (
            <tr key={instance.InstanceId}>
              <td>{instance.InstanceId}</td>
              <td>{instance.State}</td>
              <td>{instance.InstanceName}</td>
              <td>{instance.PublicIpAddress}</td>
              <td>{instance.PrivateIpAddress}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default App;
