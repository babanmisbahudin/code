// src/pages/Display.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Display = () => {
  const [queue, setQueue] = useState({ kasir1: 0, kasir2: 0 });

  const getQueues = async () => {
    const k1 = await axios.get('http://localhost:3001/api/queue/1');
    const k2 = await axios.get('http://localhost:3001/api/queue/2');
    setQueue({ kasir1: k1.data.number, kasir2: k2.data.number });
  };

  useEffect(() => {
    getQueues();
    const interval = setInterval(getQueues, 3000); // auto refresh
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ textAlign: 'center', fontSize: '3em', marginTop: '50px' }}>
      <h1>LAYAR ANTRIAN</h1>
      <div>
        <p>Kasir 1: <strong>{queue.kasir1}</strong></p>
        <p>Kasir 2: <strong>{queue.kasir2}</strong></p>
      </div>
    </div>
  );
};

export default Display;
