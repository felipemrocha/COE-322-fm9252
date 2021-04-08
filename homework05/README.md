#Homework 05

Felipe Martins Rocha (fm9252)

## A.
### 1. Include the yaml file used and the command issued to create the pod.
[hw5a.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework05/hw5a.yaml)
```console
$ kubectl apply -f hw5a.yaml
  pod/hello created
```

### 2. Issue a command to get the pod using an appropriate selector. Copy and paste the command used and the output.
```console
$ kubectl get pods --selector "greeting=personalized"
  NAME    READY   STATUS    RESTARTS   AGE
  hello   1/1     Running   0          92s
```

### 3. Check the logs of the pod. What is the output? Is that what you expected?
```console
$ kubectl logs hello
  Hello, !
```
This is not the output I expected, not even the $NAME part is visible.

### 4. Delete the pod. What command did you use?
```console
$ kubectl delete pods hello
  pod "hello" deleted
```
## B.
### 1. Include the yaml file used and the command issued to create the pod.
[hw5b.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework05/hw5b.yaml)
```console
$ kubectl apply -f hw5b.yaml
  pod/hello created
```
### 2. Check the logs of the pod. What is the output? Copy and paste the command used and the output.
```console
$ kubectl logs hello
  Hello, Felipe!
```
### 3. Delete the pod. What command did you use?
```console
$ kubectl delete pods hello
  pod "hello" deleted
```
## C.
### 1. Include the yaml file used to create a deployment with 3 replica pods, and include the command issued to create the deployment.
[hw5c.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework05/hw5c.yaml)
```console
$ kubectl apply -f hw5c.yaml
deployment.apps/hello-deployment configured
```
### 2. First, use kubectl to get all the pods in the deployment and their IP address. Copy and paste the command used and the output.
```console
$ kubectl get pods -o wide
  NAME                                READY   STATUS    RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
  hello-deployment-7bc6f55c8d-t2crb   1/1     Running   0          8m16s   10.244.7.142   c05    <none>           <none>
  hello-deployment-7bc6f55c8d-x6cq7   1/1     Running   0          108s    10.244.6.174   c03    <none>           <none>
  hello-deployment-7bc6f55c8d-xbw2f   1/1     Running   0          8m11s   10.244.3.192   c01    <none>           <none>
```
### 3. Now, check the logs associated with each pod in the deployment. Does it match what you got in 2? Copy and paste the commands and the output.
All of the IPs match what I got on 2.
```console
$ kubectl logs hello-deployment-7bc6f55c8d-t2crb
  Hello, Felipe from IP 10.244.7.142!

$ kubectl logs hello-deployment-7bc6f55c8d-x6cq7
  Hello, Felipe from IP 10.244.6.174!

$ kubectl logs hello-deployment-7bc6f55c8d-xbw2f
  Hello, Felipe from IP 10.244.3.192!
```
