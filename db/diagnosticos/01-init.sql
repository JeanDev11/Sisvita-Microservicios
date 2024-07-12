-- diagnosticos_service/01-init.sql

CREATE TABLE IF NOT EXISTS diagnostico (
    id_diagnostico INT AUTO_INCREMENT PRIMARY KEY,
    id_tipo_diagnostico INT,
    fundamentacion_cientifica VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS evaluacionpaciente (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_diagnostico INT,
    especialista_id INT,
    resultado_id INT,
    fecha_evaluacion TIMESTAMP,
    FOREIGN KEY (id_diagnostico) REFERENCES diagnostico(id_diagnostico)
);

CREATE TABLE IF NOT EXISTS tratamiento (
    id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    id_tipo_tratamiento INT,
    id_diagnostico INT,
    FOREIGN KEY (id_diagnostico) REFERENCES diagnostico(id_diagnostico)
);

CREATE TABLE IF NOT EXISTS tiposdiagnostico (
    id_tipo_diagnostico INT AUTO_INCREMENT PRIMARY KEY,
    nombre_diagnostico VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS tipostratamiento (
    id_tipo_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tratamiento VARCHAR(100)
);

ALTER TABLE diagnostico
    ADD CONSTRAINT FOREIGN KEY (id_tipo_diagnostico)
    REFERENCES tiposdiagnostico(id_tipo_diagnostico);

ALTER TABLE tratamiento
    ADD CONSTRAINT FOREIGN KEY (id_tipo_tratamiento)
    REFERENCES tipostratamiento(id_tipo_tratamiento);
