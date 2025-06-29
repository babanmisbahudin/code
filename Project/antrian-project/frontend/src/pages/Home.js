// src/pages/Home.js
import React from 'react';
import axios from 'axios';

const Home = () => {
  const ambilNomor = async (kasir) => {
    await axios.post(`http://localhost:3001/api/next/${kasir}`);
    alert(`Nomor antrian kasir ${kasir} telah ditambahkan`);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Ambil Nomor Antrian</h1>
      <button onClick={() => ambilNomor(1)}>Kasir 1</button>
      <button onClick={() => ambilNomor(2)}>Kasir 2</button>
    </div>
  );
};

export default Home;
