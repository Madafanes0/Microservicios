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

## Despliegue en Kubernetes

### Prerrequisitos

1. Docker Desktop instalado con Kubernetes habilitado
2. kubectl instalado
3. Las imágenes Docker de los servicios construidas

### Pasos para el Despliegue

1. **Habilitar Kubernetes en Docker Desktop**
   - Abrir Docker Desktop
   - Ir a Settings (⚙️)
   - En la sección "Kubernetes", marcar la casilla "Enable Kubernetes"
   - Hacer clic en "Apply & Restart"

2. **Construir las imágenes Docker**
   ```bash
   ./build-images.sh
   ```

3. **Aplicar las configuraciones de Kubernetes**
   ```bash
   kubectl apply -f k8s/
   ```

4. **Verificar el estado de los pods**
   ```bash
   kubectl get pods
   ```

5. **Verificar los servicios**
   ```bash
   kubectl get services
   ```

### Acceso a los Servicios

Los servicios están expuestos a través de NodePort en los siguientes puertos:

- Suma: http://localhost:30001
- Resta: http://localhost:30002
- Ecuación: http://localhost:30003
- Storage: http://localhost:30004

### Ejemplos de Uso

1. **Servicio de Suma**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"a": 5, "b": 3}' http://localhost:30001/sumar
   ```

2. **Servicio de Resta**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"c": 10, "d": 4}' http://localhost:30002/restar
   ```

3. **Servicio de Ecuación**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"a": 2, "b": 3, "c": 4, "d": 1}' http://localhost:30003/resolver
   ```

4. **Servicio de Storage**
   ```bash
   curl http://localhost:30004/resultados
   ```

### Comandos Útiles

1. **Ver logs de un pod específico**
   ```bash
   kubectl logs <nombre-del-pod>
   ```

2. **Ver detalles de un pod**
   ```bash
   kubectl describe pod <nombre-del-pod>
   ```

3. **Escalar un deployment**
   ```bash
   kubectl scale deployment <nombre-deployment> --replicas=3
   ```

4. **Eliminar todo el despliegue**
   ```bash
   kubectl delete -f k8s/
   ```

### Estructura de Archivos

```
.
├── k8s/
│   ├── suma-deployment.yaml
│   ├── resta-deployment.yaml
│   ├── ecuacion-deployment.yaml
│   ├── storage-deployment.yaml
│   └── mysql-deployment.yaml
├── suma/
│   ├── Dockerfile
│   └── suma.py
├── resta/
│   ├── Dockerfile
│   └── resta.py
├── ecuacion/
│   ├── Dockerfile
│   └── ecuacionMulty.py
├── storage/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── storage.py
├── build-images.sh
└── README.md
```

### Notas Importantes

- Los servicios están configurados para usar NodePort en lugar de Ingress para simplificar el despliegue
- La base de datos MySQL está configurada como un servicio ClusterIP
- Los servicios se comunican entre sí usando los nombres de servicio de Kubernetes
- Los datos de MySQL se almacenan en un volumen emptyDir (se perderán al reiniciar el pod)
