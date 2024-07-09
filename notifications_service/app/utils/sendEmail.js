const nodemailer = require('nodemailer');
require('dotenv').config();

async function sendEmail(toEmail, nombrePaciente, nombreEspecialista, nombreTest, recomendaciones, mensaje) {
    const transporter = nodemailer.createTransport({
        host: "smtp.office365.com",
        port: 587,
        service: process.env.MAIL_SERVICE_PROVIDER,
        auth: {
            user: process.env.MAIL_USERNAME,
            pass: process.env.MAIL_PASSWORD
        }
    });

    const mailOptions = {
        from: process.env.MAIL_DEFAULT_SENDER,
        to: toEmail,
        // subject: 'Notificación de Sisvita',
        subject: `Resultados del test ${nombreTest} para ${nombrePaciente}`,
        html: `
            <p>Hola ${nombrePaciente},</p>
            <p>Es un placer saludarte. Soy <strong>${nombreEspecialista}</strong>, tu especialista a cargo. Como parte de nuestro compromiso contigo en <strong><em>SISVITA</em></strong>, hemos revisado cuidadosamente tus resultados del test ${nombreTest}. Basándome en estos resultados, quiero compartir contigo algunas recomendaciones que considero importantes para tu bienestar y desarrollo personal:</p>
            <p style="white-space: pre-wrap;margin-left: 30px;">${recomendaciones}</p>
            <p>Así mismo, me gustaría indicarte que:</p>
            <p style="white-space: pre-wrap;margin-left: 30px;">${mensaje}</p>
            <p>Saludos cordiales, ${nombreEspecialista}.</p>
            <p>—————————————————————</p>
            <p><em>&#8194;&#8194;&#8194;&#8194;&#8194;&#8194;Equipo SISVITA - FISI - UNMSM</em></p>
            <p>—————————————————————</p>
        `
    };

    await transporter.sendMail(mailOptions);
}

module.exports = sendEmail;
