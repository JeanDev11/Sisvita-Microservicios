-- usuarios_service/init.sql
BEGIN;

DROP TABLE IF EXISTS public.usuarios;
DROP TABLE IF EXISTS public.especialistas;
DROP TABLE IF EXISTS public.pacientes;
DROP TABLE IF EXISTS public.ubigeo;

CREATE TABLE IF NOT EXISTS public.usuarios
(
    usuario_id serial NOT NULL,
    nombres character varying(255) NOT NULL,
    apellidos character varying(255) NOT NULL,
    correo_electronico character varying(255) NOT NULL,
    contrasena character varying(255) NOT NULL,
    rol character(1) NOT NULL,
    es_paciente boolean DEFAULT false,
    telefono character varying(20) NOT NULL,
    fecha_nac date,
    sexo character(1),
    id_ubigeo integer,
    dni character varying(8),
    CONSTRAINT usuarios_pkey PRIMARY KEY (usuario_id),
    CONSTRAINT usuarios_correo_electronico_key UNIQUE (correo_electronico)
);

CREATE TABLE IF NOT EXISTS public.especialistas
(
    especialista_id serial NOT NULL,
    usuario_id integer NOT NULL,
    especialidad character varying(255) NOT NULL,
    nro_colegiado integer,
    direccion_consultorio character varying(255),
    CONSTRAINT especialistas_pkey PRIMARY KEY (especialista_id),
    CONSTRAINT especialistas_usuario_id_key UNIQUE (usuario_id)
);

CREATE TABLE IF NOT EXISTS public.pacientes
(
    paciente_id serial NOT NULL,
    usuario_id integer NOT NULL,
    ciclo integer,
    facultad character varying(255),
    carrera character varying(255),
    CONSTRAINT pacientes_pkey PRIMARY KEY (paciente_id),
    CONSTRAINT pacientes_usuario_id_key UNIQUE (usuario_id)
);

CREATE TABLE IF NOT EXISTS public.ubigeo
(
    id_ubigeo integer NOT NULL,
    departamento character varying,
    provincia character varying,
    distrito character varying,
    longitud numeric,
    latitud numeric,
    CONSTRAINT ubigeo_pkey PRIMARY KEY (id_ubigeo)
);

-- Load data from CSV
COPY public.ubigeo (id_ubigeo, distrito, provincia, departamento, latitud, longitud)
FROM '/docker-entrypoint-initdb.d/ubigeo.csv'
DELIMITER ';'
CSV HEADER;

ALTER TABLE IF EXISTS public.usuarios
    ADD CONSTRAINT fk_ubigeo FOREIGN KEY (id_ubigeo)
    REFERENCES public.ubigeo (id_ubigeo) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.especialistas
    ADD CONSTRAINT especialistas_especialista_id_fkey FOREIGN KEY (especialista_id)
    REFERENCES public.usuarios (usuario_id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.pacientes
    ADD CONSTRAINT pacientes_paciente_id_fkey FOREIGN KEY (paciente_id)
    REFERENCES public.usuarios (usuario_id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;

END;
