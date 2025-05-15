# Microservicios Matemáticos

Sistema de microservicios que realiza operaciones matemáticas básicas.

## Servicios

- Suma (8001)
- Resta (8002)
- Ecuación (8003)
- Storage (8004)
- MySQL (3306)

## Cómo Usar

1. Instalar Docker y Docker Compose
2. Ejecutar:
```bash
docker-compose up --build
```

## Endpoints

- Suma: POST `/sumar`
- Resta: POST `/restar`
- Ecuación: POST `/calcular`
- Storage: 
  - POST `/guardar`
  - GET `/resultados`
