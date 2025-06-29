// src/pages/Admin.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Admin = () => {
  const [queue, setQueue] = useState({ kasir1: 0, kasir2: 0 });

  const getQueues = async () => {
    const k1 = await axios.get('http://localhost:3001/api/queue/1');
    const k2 = await axios.get('http://localhost:3001/api/queue/2');
    setQueue({ kasir1: k1.data.number, kasir2: k2.data.number });
  };

  const nextQueue = async (kasir) => {
    await axios.post(`http://localhost:3001/api/next/${kasir}`);
    getQueues();
  };

  useEffect(() => {
    getQueues();
  }, []);

  return (
    <div style={{ textAlign: 'center' }}>
      <h1>Panel Admin</h1>
      <div>
        <h2>Kasir 1: {queue.kasir1}</h2>
        <button onClick={() => nextQueue(1)}>Panggil Kasir 1</button>
      </div>
      <div>
        <h2>Kasir 2: {queue.kasir2}</h2>
        <button onClick={() => nextQueue(2)}>Panggil Kasir 2</button>
      </div>
    </div>
  );
};

export default Admin;
