const express = require('express');
const app = express();
const dotenv = require('dotenv');
dotenv.config();

// Middleware para parsear JSON
app.use(express.json());

// Rutas
const emailRoutes = require('./app/routes/emailRoutes');
app.use('/api', emailRoutes);

// Puerto
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor de notificaciones corriendo en el puerto ${PORT}`);
});
