# ⚙️ Orquestração de Microserviços com Flask, Docker e Kubernetes

Este projeto demonstra uma orquestração simples de dois microserviços Flask usando Docker e Kubernetes (via Minikube), onde um serviço cliente consome outro serviço de cálculo. Exemplo para demonstração do uso de kubernetes.

---

##  Objetivo

- Criar dois microserviços:
  - `api-calculadora`: fornece operações matemáticas simples.
  - `api-cliente`: consome a API da calculadora e retorna os resultados.
- Usar **Kubernetes** para orquestrar os serviços, garantindo comunicação entre eles.
- Utilizar o **Minikube** para simular um cluster local de desenvolvimento.

---

## 🗂️ Estrutura do Projeto

```

orquestracao-k8s/
├── api-calculadora/
│ ├── calculator.py
│ └── Dockerfile
├── api-cliente/
│ ├── cliente.py
│ └── Dockerfile
├── k8s/
│ ├── calculadora-deployment.yaml
│ ├── calculadora-service.yaml
│ ├── cliente-deployment.yaml
  └── cliente-service.yaml
```

---

## 🐳 Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## Como rodar o projeto

### 1. Inicie o Minikube e configure o Docker

```
minikube start
eval $(minikube docker-env)
```
2. Construa as imagens
```
docker build -t api-calculadora ./api-calculadora
docker build -t api-cliente ./api-cliente
```

3. Aplique os arquivos Kubernetes
```
kubectl apply -f k8s/
```
4. Verifique os pods
```
kubectl get pods
```
5. Acesse o serviço cliente via navegador

```
minikube service api-cliente-service
```