const express = require('express');
const app = express();
const dotenv = require('dotenv');
const cors = require('cors');

dotenv.config();

// Middleware para parsear JSON
app.use(express.json());

// Habilita CORS para todas las solicitudes
app.use(cors());

// Rutas
const emailRoutes = require('./app/routes/emailRoutes');
app.use('/notify', emailRoutes);

// Puerto
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor de notificaciones corriendo en el puerto ${PORT}`);
});
