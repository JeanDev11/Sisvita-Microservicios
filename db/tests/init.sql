-- tests_service/init.sql
BEGIN;

DROP TABLE IF EXISTS public.test;
DROP TABLE IF EXISTS public.test_pregunta;
DROP TABLE IF EXISTS public.test_alternativa;
DROP TABLE IF EXISTS public.test_resultado;
DROP TABLE IF EXISTS public.nivel_test;

CREATE TABLE IF NOT EXISTS public.test
(
    test_id serial NOT NULL,
    descripcion character varying(255),
    rango_puntuacion integer,
    titulo character varying(100),
    CONSTRAINT test_pkey PRIMARY KEY (test_id)
);

CREATE TABLE IF NOT EXISTS public.test_pregunta
(
    pregunta_id serial NOT NULL,
    test_id integer,
    texto_pregunta character varying(255),
    orden integer,
    CONSTRAINT test_pregunta_pkey PRIMARY KEY (pregunta_id)
);

CREATE TABLE IF NOT EXISTS public.test_alternativa
(
    alternativa_id serial NOT NULL,
    pregunta_id integer,
    alternativa character varying(255),
    puntaje integer,
    CONSTRAINT test_alternativa_pkey PRIMARY KEY (alternativa_id)
);

CREATE TABLE IF NOT EXISTS public.test_resultado
(
    resultado_id serial NOT NULL,
    test_id integer,
    usuario_id integer,
    puntaje_obtenido integer,
    fecha_creacion timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    id_nivel integer,
    CONSTRAINT test_resultado_pkey PRIMARY KEY (resultado_id)
);

CREATE TABLE IF NOT EXISTS public.nivel_test
(
    id_nivel serial NOT NULL,
    min_puntos integer,
    max_puntos integer,
    descripcion character varying(255),
    test_id integer,
    semaforo character varying,
    CONSTRAINT niveles_ansiedad_pkey PRIMARY KEY (id_nivel)
);

ALTER TABLE IF EXISTS public.test_pregunta
    ADD CONSTRAINT test_pregunta_test_id_fkey FOREIGN KEY (test_id)
    REFERENCES public.test (test_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.test_alternativa
    ADD CONSTRAINT test_alternativa_pregunta_id_fkey FOREIGN KEY (pregunta_id)
    REFERENCES public.test_pregunta (pregunta_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.test_resultado
    ADD CONSTRAINT test_resultado_test_id_fkey FOREIGN KEY (test_id)
    REFERENCES public.test (test_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.test_resultado
    ADD CONSTRAINT test_resultado_usuario_id_fkey FOREIGN KEY (usuario_id)
    REFERENCES public.usuarios (usuario_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.test_resultado
    ADD CONSTRAINT fk_id_nivel FOREIGN KEY (id_nivel)
    REFERENCES public.nivel_test (id_nivel) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.nivel_test
    ADD CONSTRAINT fk_niveles_ansiedad_test FOREIGN KEY (test_id)
    REFERENCES public.test (test_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;
