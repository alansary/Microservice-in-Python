# Microservice in Python

1. Installing Python 3.X<br/>
Documentation - https://www.python.org
2. Creating Python Virtual Environment<br/>
Documentation - https://docs.python.org/3/library/venv.html
    ```bash
    $ python3 -m venv ./microservices-in-python
    $ source microservices-in-python/bin/activate
    $ pip list
    ```
3. Installing Python VS Code Extension
4. Sample Flask Application<br/>
Documentation - https://flask.palletsprojects.com/en/2.1.x/installation/
    ```bash
    $ pip install Flask
    $ pip list
    ```
    Documentation - https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application
5. Using Pip to Freeze Python Dependencies
    ```bash
    $ pip freeze > requirements.txt
    ```
6. Building the docker image using Dockerfile
Start Minikube cluster
    ```bash
    $ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
    $ sudo install minikube-darwin-arm64 /usr/local/bin/minikube
    $ minikube start --driver docker
    $ minikube status
    $ kubectl get node
    ```
    Get docker containers running inside Minikube
    ```bash
    $ minikube docker-env
    $ export DOCKER_TLS_VERIFY="1"
    $ export DOCKER_HOST="tcp://127.0.0.1:60287"
    $ export DOCKER_CERT_PATH="/Users/alansary/.minikube/certs"
    $ export MINIKUBE_ACTIVE_DOCKERD="minikube"
    $ docker ps
    ```
    Create Dockerfile
    ```bash
    $ touch Dockerfile
    $ touch .dockerignore
    ```
    Build docker image
    ```bash
    $ docker build -t microservices-in-python-webapp:1.0 .
    ```
    Run the container
    ```bash
    $ docker run -d -p 80:5000 --name microservices-in-python-webapp microservices-in-python-webapp:1.0
    $ docker ps
    $ minikube ip
    ```
    Remove the container
    ```bash
    $ docker ps -a
    $ docker rm -f microservices-in-python-webapp
    ```
    Remove the image
    ```bash
    $ docker image ls
    $ docker rmi -f IMAGE_ID
    ```
    You man need to close the services that use port 80 first
    ```bash
    $ sudo lsof -i:80
    $ brew services stop httpd
    ```
    Documentation - https://docs.docker.com/compose/<br/>
    Create docker-compose.yml
    ```bash
    $ touch docker-compose.yml
    $ docker-compose build
    $ docker-compose up -d
    ```
7. Writing Kubernetes Manifest files for the application
    Documentation - https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
    Documentation - https://kubernetes.io/docs/concepts/services-networking/service/
    ```bash
    $ mkdir Kubernetes
    $ touch Kubernetes/deployment.yml
    $ touch Kubernetes/service.yml
    $ cd Kubernetes
    $ kubectl apply -f deployment.yml
    $ kubectl get po
    $ kubectl apply -f service.yml
    $ kubectl get po,svc
    $ minikube ip
    ```
    Uninstall deployment and service
    ```bash
    $ kubectl delete -f .
    $ kubectl get po,svc
    ```