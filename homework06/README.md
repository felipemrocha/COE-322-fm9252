#Homework 06

Felipe Martins Rocha (fm9252)

## Step 1:
[frocha-test-redis-container.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework06/frocha-test-redis-container.yaml)
```console
$ kubectl apply -f frocha-test-redis-container.yaml
  persistentvolumeclaim/frocha-test-redis-container created
```

## Step 2:
[frocha-test-redis-database.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework06/frocha-test-redis-database.yaml)
```console
$ kubectl apply -f frocha-test-redis-database.yaml
  deployment.apps/frocha-test-redis-database created
```

## Step 3:
[frocha-test-redis-service.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework06/frocha-test-redis-service.yaml)
```console
$ kubectl apply -f frocha-test-redis-service.yaml
  service/frocha-test-redis-service created
```

## Step 4:
[frocha-test-flask-deployment.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework06/frocha-test-redis-deployment.yaml)
```console
$ kubectl apply -f frocha-test-redis-deployment.yaml
  deployment.apps/frocha-test-flask-deployment created
```

## Step 5:
[frocha-test-flask-service.yaml](https://github.com/felipemrocha/COE-322-fm9252/blob/main/homework06/frocha-test-redis-service.yaml)
```console
$ kubectl apply -f frocha-test-redis-service.yaml
  service/frocha-test-flask-service created
```
