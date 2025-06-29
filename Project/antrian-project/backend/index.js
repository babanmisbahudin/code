const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

// Dua antrian berbeda
let queueKasir1 = 1;
let queueKasir2 = 1;

// Ambil antrian masing-masing kasir
app.get('/api/queue/:loket', (req, res) => {
  const loket = req.params.loket;
  if (loket === '1') {
    return res.json({ number: queueKasir1 });
  } else if (loket === '2') {
    return res.json({ number: queueKasir2 });
  } else {
    return res.status(400).json({ error: 'Loket tidak dikenali' });
  }
});

// Geser ke nomor berikutnya
app.post('/api/next/:loket', (req, res) => {
  const loket = req.params.loket;
  if (loket === '1') {
    queueKasir1++;
    return res.json({ number: queueKasir1 });
  } else if (loket === '2') {
    queueKasir2++;
    return res.json({ number: queueKasir2 });
  } else {
    return res.status(400).json({ error: 'Loket tidak dikenali' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
