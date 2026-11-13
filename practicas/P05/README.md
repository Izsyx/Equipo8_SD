# Práctica 5 — Actividades 2 y 3

## Actividad 2. Contenedores

Los ejemplos se ejecutan desde la raíz del repositorio. Los puertos 18081, 18082 y 18083 se usan para evitar conflictos y quedan accesibles solo desde la computadora local.

```sh
docker run -d -p 127.0.0.1:18082:80 --name sd-p05-nginx nginx:alpine
docker build -t sd-p05-web:v1 practicas/P05/actividad2/web
docker run -d -p 127.0.0.1:18083:80 --name sd-p05-web-estatica sd-p05-web:v1
docker build -t sd-p05-hola:single -f practicas/P05/actividad2/multistage/Dockerfile.single practicas/P05/actividad2/multistage
docker build -t sd-p05-hola:multi practicas/P05/actividad2/multistage
docker images sd-p05-hola
docker run --rm sd-p05-hola:single
docker run --rm sd-p05-hola:multi
docker inspect sd-p05-web-estatica
docker logs sd-p05-web-estatica
docker stats --no-stream sd-p05-web-estatica
docker compose -p sd-p05 -f practicas/P05/actividad2/compose/docker-compose.yml up -d --build
```

Abrir `http://localhost:18082` para nginx, `http://localhost:18083` para la página personalizada y `http://localhost:18081` para el contador de visitas. La contraseña de PostgreSQL es exclusivamente para esta práctica local.

Para detener solo estos contenedores, sin afectar otros proyectos:

```sh
docker rm -f sd-p05-nginx sd-p05-web-estatica
docker compose -p sd-p05 -f practicas/P05/actividad2/compose/docker-compose.yml down
```

El volumen `sd-p05_datos` conserva las visitas. `docker compose down -v` también lo elimina. No se ejecuta `docker system prune -a`, pues afecta recursos de otros proyectos.

## Actividad 3. Kubernetes

Con Kind y kubectl instalados, desde la raíz del repositorio:

```sh
kind create cluster --name sd-p05 --config practicas/P05/actividad3/kind-config.yaml --kubeconfig /tmp/sd-p05-kubeconfig --wait 180s
export KUBECONFIG=/tmp/sd-p05-kubeconfig
kubectl get nodes
kubectl apply -f practicas/P05/actividad3/deployment.yaml -f practicas/P05/actividad3/service.yaml
kubectl rollout status deployment/mi-app
kubectl get pods,service -o wide
kubectl scale deployment mi-app --replicas=5
kubectl rollout status deployment/mi-app
kubectl get pods -o wide
kubectl scale deployment mi-app --replicas=1
kubectl rollout status deployment/mi-app
kubectl get pods -o wide
kubectl delete pod <nombre-del-pod>
kubectl get pods -w
kubectl set image deployment/mi-app nginx=nginx:1.27-alpine
kubectl rollout status deployment/mi-app
kubectl rollout undo deployment/mi-app
kubectl rollout status deployment/mi-app
```

El Service NodePort se publica en `http://localhost:18080`. Para eliminar solo el clúster de la práctica: `kind delete cluster --name sd-p05`. El archivo de configuración separado evita cambiar el contexto habitual de Kubernetes.

## Reporte y estado

El archivo `reporte.tex` es el documento principal y se compila desde la raíz del repositorio con pdfLaTeX. Las actividades 2 a 5 están redactadas; la actividad 1 está pendiente. El código y las capturas del navegador se encuentran en esta carpeta. Se conservaron las salidas y las capturas originales de las pruebas; las versiones recortadas se usan en el reporte para facilitar su lectura. La salida `actividad3-salida.txt` identifica un primer intento inválido de recuperación; la prueba válida está en `recuperacion.txt`. No se ha verificado la compilación LaTeX en este equipo.
