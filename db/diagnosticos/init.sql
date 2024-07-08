-- diagnosticos_service/init.sql
BEGIN;

DROP TABLE IF EXISTS public.diagnostico;
DROP TABLE IF EXISTS public.evaluacionpaciente;
DROP TABLE IF EXISTS public.tratamiento;
DROP TABLE IF EXISTS public.tiposdiagnostico;
DROP TABLE IF EXISTS public.tipostratamiento;

CREATE TABLE IF NOT EXISTS public.diagnostico
(
    id_diagnostico serial NOT NULL,
    id_tipo_diagnostico integer,
    fundamentacion_cientifica character varying,
    CONSTRAINT diagnostico_pkey PRIMARY KEY (id_diagnostico)
);

CREATE TABLE IF NOT EXISTS public.evaluacionpaciente
(
    id_evaluacion integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    id_diagnostico integer,
    especialista_id integer,
    resultado_id integer,
    fecha_evaluacion timestamp with time zone,
    CONSTRAINT evaluacionpaciente_pkey PRIMARY KEY (id_evaluacion)
);

CREATE TABLE IF NOT EXISTS public.tratamiento
(
    id_tratamiento serial NOT NULL,
    id_tipo_tratamiento integer,
    id_diagnostico integer,
    CONSTRAINT tratamiento_pkey PRIMARY KEY (id_tratamiento)
);

CREATE TABLE IF NOT EXISTS public.tiposdiagnostico
(
    id_tipo_diagnostico serial NOT NULL,
    nombre_diagnostico character varying(100),
    CONSTRAINT tiposdiagnostico_pkey PRIMARY KEY (id_tipo_diagnostico)
);

CREATE TABLE IF NOT EXISTS public.tipostratamiento
(
    id_tipo_tratamiento serial NOT NULL,
    nombre_tratamiento character varying(100),
    CONSTRAINT tipostratamiento_pkey PRIMARY KEY (id_tipo_tratamiento)
);

ALTER TABLE IF EXISTS public.diagnostico
    ADD CONSTRAINT diagnostico_id_tipo_diagnostico_fkey FOREIGN KEY (id_tipo_diagnostico)
    REFERENCES public.tiposdiagnostico (id_tipo_diagnostico) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.evaluacionpaciente
    ADD CONSTRAINT evaluacionpaciente_id_diagnostico_fkey FOREIGN KEY (id_diagnostico)
    REFERENCES public.diagnostico (id_diagnostico) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.tratamiento
    ADD CONSTRAINT tratamiento_id_diagnostico_fkey FOREIGN KEY (id_diagnostico)
    REFERENCES public.diagnostico (id_diagnostico) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.tratamiento
    ADD CONSTRAINT tratamiento_id_tipo_tratamiento_fkey FOREIGN KEY (id_tipo_tratamiento)
    REFERENCES public.tipostratamiento (id_tipo_tratamiento) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;
