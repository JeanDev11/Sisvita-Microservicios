# Sisvita - Microservicios

Este proyecto es una implementación de microservicios para la aplicación Sisvita, usando Docker y Docker Compose. Los microservicios se encargan de la gestión de usuarios, diagnósticos y tests.

## Prerrequisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Asegurarse de tener un archivo .env en la raíz del proyecto con las variables de entorno.

## Estructura del Proyecto

```plaintext
sisvita-microservicios/
├── usuarios_service/
├── diagnosticos_service/
├── tests_service/
├── db/
├── docker-compose.yml
└── .env
```

## Iniciar los Contenedores
Para construir y ejecutar los contenedores, abre Docker Desktop y ejecuta:
`docker-compose up --build`

## Acceder a los Servicios

 - Usuarios Service: http://localhost:5001
 - Diagnósticos Service: http://localhost:5002
 - Tests Service: http://localhost:5003

## Detener los Servicios
Para detener todos los servicios:
`docker-compose down`


# Ayuda adicional

## Ejecutar los Contenedores en Segundo Plano
Para ejecutar los contenedores en segundo plano, usa el flag -d:
`docker-compose up --build -d`