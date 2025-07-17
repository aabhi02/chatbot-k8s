# chatbot-k8s

pre-requisits for the project

install helm
install minikube
install kubectl

required to install few addons to see metrics
```shell
minikube addons enable metrics-server
```

install flux-system crd

```shell
helm repo add fluxcd https://fluxcd-community.github.io/helm-charts
helm repo update
helm install flux fluxcd/flux2 --create-namespace --namespace flux-system
```


install ingress crd

```shell
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress --create-namespace
```


install grafana

```shell
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana --namespace grafana --create-namespace
```


install prometheus

```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install kube-prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```


install ollama with helm with default model(deepseek-r1) downloaded

```shell
helm install ollama otwld/ollama --namespace ollama --create-namespace --set ollama.models.pull="{deepseek-r1:1.5b}"
```


install the custom application helm chart

`Note: if your git repo and image registry is not public make sure to create a secret to avoid deployment failures`

Command to create docker secret

```
kubectl create secret docker-registry dockersecret --docker-username=username --docker-password=password -o yaml > docker-secret.yaml
```


