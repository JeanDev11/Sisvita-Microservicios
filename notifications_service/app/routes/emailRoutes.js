const express = require('express');
const router = express.Router();
const sendEmail = require('../utils/sendEmail');

// Endpoint para enviar un correo electrónico
router.post('/send-email', async (req, res) => {
    const { to_email, nombre_del_paciente, nombre_de_la_especialista, nombre_del_test, recomendaciones, mensaje } = req.body;

    try {
        await sendEmail(to_email, nombre_del_paciente, nombre_de_la_especialista, nombre_del_test, recomendaciones, mensaje);
        res.status(200).json({ message: 'Email enviado correctamente' });
    } catch (error) {
        console.error('Error al enviar el correo:', error);
        res.status(500).json({ error: 'Error al enviar el correo' });
    }
});

module.exports = router;
