# Oscar Nominees: 1928 to 2017
COE332 Final Project -  Felipe Martins Rocha (fm9252)
## 1. Deployment

Once you are in the main folder (/final), go to the *deployments* folder and start applying your Kubernetes Redis files.

```console
$ kubectl apply -f frocha-oscars-redis-pvc.yaml
  persistentvolumeclaim/frocha-oscars-redis-pvc created

$ kubectl apply -f frocha-oscars-redis-deployment.yaml
  deployment.apps/frocha-oscars-redis-deployment created

$ kubectl apply -f frocha-oscars-redis-service.yaml
  service/frocha-oscars-redis-service created

$ kubectl get services --selector "project=final"
  NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
  frocha-oscars-redis-service   ClusterIP   10.110.194.121   <none>        6379/TCP   20h
```
This last command is important and you will need to copy the CLUSTER-IP for the redis service (it will not be the same as the one shown here). With that IP, you will need to edit some of the .yaml files. First, open frocha-oscars-flask-deployment.yaml and change the following:
```yaml
spec:
  containers:
    - name: frocha-oscars-flask-deployment
      imagePullPolicy: Always
      image: felipemrocha/oscars:latest
      env:
        - name: FLASK_APP_FINAL
          value: "app.py"
        - name: REDIS_IP
          value: "CLUSTER-IP" # Paste that value here
```
In the value for REDIS_IP, change the IP to the one from the redis service. Save your file and repeat the same process for the frocha-oscars-worker-deployment.yaml (the two files have a very similar structure, so just make sure you're making the same change).

With all of those changes made, kubectl apply the remaining .yaml files

```console
$ kubectl apply -f frocha-oscars-flask-deployment.yaml
  deployment.apps/frocha-oscars-flask-deployment created

$ kubectl apply -f frocha-oscars-worker-deployment.yaml
  deployment.apps/frocha-oscars-worker-deployment created

$ kubectl apply -f frocha-oscars-flask-service.yaml 
  service/frocha-oscars-flask-service created

$ kubectl apply -f python-debug.yaml
  deployment.apps/python-debug-deployment created
```

You're all set! When you exec into the flask deployment you should be able to use all the routes in the database. For more information go to: [User](google.com).



