# Oscar Nominees: 1928 to 2017
COE332 Final Project -  Felipe Martins Rocha (fm9252)

If you have already deployed your container, you are ready to curl routes and do operations in the Oscars database. If your Kubernetes clusters aren't deployed, go to [Deployment](https://github.com/felipemrocha/COE-322-fm9252/blob/main/final/documentation/deployment.md).

## 2. User

### 2.1. Starting up

To curl routes, you will first have to exec into the flask deployment:
```console
$ $ kubectl get pods -o wide
NAME                                              READY   STATUS    RESTARTS   AGE   IP              NODE                         NOMINATED NODE   READINESS GATES
frocha-oscars-flask-deployment-5fc88cf459-cs6hc   1/1     Running   0          46m   10.244.12.214   c12                          <none>           <none>
frocha-oscars-redis-deployment-586bcdddb4-p7jtk   1/1     Running   0          34h   10.244.15.98    c03                          <none>           <none>
frocha-oscars-worker-deployment-6cc798957-gpf2h   1/1     Running   0          46m   10.244.15.232   c03                          <none>           <none>
py-debug-deployment-5cc8cdd65f-lvfsg              1/1     Running   0          9h    10.244.10.126   c009.rodeo.tacc.utexas.edu   <none>           <none>

````
Copy the name of the flask-deployment and paste it in the following command with your unique debug pod number:
```console
$ kubectl exec -it py-debug-deployment-5cc8cdd65f-lvfsg  -- /bin/bash
```
This will take you to an environment where you'll be able to curl routes. The IP used should be the flask deployment IP you see when you get pods (see above). If this is the first time anyone is using this project, it might be necessary to apply the reset route. This will basically delete all of the keys currently in the database and reload the information from the original Academy database. All of the changes made will be erased.
```console
# curl 10.244.12.214:5000/reset
Data Reset
````

### 2.2. Create
Now that your JSON is loaded into the redis database, you can create your nominees by assigning them the following attributes: 
- Entity: Person or film nominated
- Category: Best Picture, Actor in a Supporting Role, etc. (in ALL CAPS)
- Year: Year of the nomination
- Winner: True or False

*Note: to use spaces in the attributes, use underscores*
```console
# curl "10.244.12.214:5000/create?entity="Parasite"&category="BEST_PICTURE"&year="2020"&winner="True""
{
  "category": "BEST PICTURE",
  "entity": "Parasite",
  "uid": "e0f80d81-e89c-404c-8dc9-a7d462fdf18c",
  "winner": "True",
  "year": "2020"
}
```

### 2.3. Read

There are multiple ways to read data in this project. For the first one, you can see all of the nominees from a certain year. To save space in this document only the first five results are being shown.
```console
# curl 10.244.12.214:5000/year/2011
{'uid': '0024ffba-7c15-4e4c-85b2-ddcfba829dcd', 'category': 'COSTUME DESIGN', 'entity': 'Anonymous', 'winner': 'False', 'year': '2011'}
{'uid': 'af162168-9b94-4aa0-930c-0c2df0e3cab0', 'category': 'CINEMATOGRAPHY', 'entity': 'Hugo', 'winner': 'True', 'year': '2011'}
{'uid': 'c223ef7b-6d3a-4f0c-9891-e046572a7f6f', 'category': 'BEST PICTURE', 'entity': 'Hugo', 'winner': 'False', 'year': '2011'}
{'uid': 'eb285688-c2eb-4910-b9f3-13a721e798fe', 'category': 'BEST PICTURE', 'entity': 'The Artist', 'winner': 'True', 'year': '2011'}
{'uid': 'b4337ffc-8046-4b25-83c7-74214ad81047', 'category': 'WRITING (Original Screenplay)', 'entity': 'Margin Call', 'winner': 'False', 'year': '2011'}
(...)
```
You can also get all of the nominees in a range of years by using this route. Again, only the top results are being shown since this returns a long list of nominees.

```console
# curl "10.244.12.214:5000/year/range?start=2005&end=2010"
{'uid': '659740d4-888a-40f0-9e86-ad7f54c881a5', 'category': 'SHORT FILM (Animated)', 'entity': 'Logorama', 'winner': 'True', 'year': '2009'}
{'uid': '017d6c78-3321-4b3f-92b4-bc279a1a3f4b', 'category': 'MUSIC (Original Score)', 'entity': 'Up', 'winner': 'True', 'year': '2009'}
{'uid': '20a2723b-5cc6-45f5-b4f0-218d59e0d785', 'category': 'WRITING (Adapted Screenplay)', 'entity': 'The Constant Gardener', 'winner': 'False', 'year': '2005'}
{'uid': 'ffdc252b-76b9-45db-af70-03a0d9a6ae6b', 'category': 'ANIMATED FEATURE FILM', 'entity': 'WALL-E', 'winner': 'True', 'year': '2008'}
{'uid': 'd1019119-7d4a-44ac-a965-5bef9231c6f6', 'category': 'ACTOR IN A SUPPORTING ROLE', 'entity': 'Matt Damon', 'winner': 'False', 'year': '2009'}
{'uid': '0340fd3e-da05-4271-a4c6-a519733c32e0', 'category': 'MUSIC (Original Song)', 'entity': 'Once', 'winner': 'True', 'year': '2007'}
{'uid': '70b7ba1b-6664-4eb4-be8d-d32d71b9f3d9', 'category': 'FOREIGN LANGUAGE FILM', 'entity': 'Outside the Law (Hors-la-loi)', 'winner': 'False', 'year': '2010'}
```
Next, you can be more specific and check the movies nominated in specific categories in the year.
```CONSOLE
# curl 10.244.12.214:5000/year/2017/category/ACTOR_IN_A_SUPPORTING_ROLE
[
  {
    "category": "ACTOR IN A SUPPORTING ROLE",
    "entity": "Willem Dafoe",
    "uid": "8b46f190-7c32-4155-b8cb-0e4d73e69887",
    "winner": "False",
    "year": "2017"
  },
  {
    "category": "ACTOR IN A SUPPORTING ROLE",
    "entity": "Sam Rockwell",
    "uid": "48658f7d-2717-47e6-98c4-dfdd1b31f1b9",
    "winner": "True",
    "year": "2017"
  },
  {
    "category": "ACTOR IN A SUPPORTING ROLE",
    "entity": "Christopher Plummer",
    "uid": "2928e97e-c23f-4a2f-b3f1-b81e45193029",
    "winner": "False",
    "year": "2017"
  },
  {
    "category": "ACTOR IN A SUPPORTING ROLE",
    "entity": "Richard Jenkins",
    "uid": "1d2409eb-a8e2-4ea7-afed-156f87dec631",
    "winner": "False",
    "year": "2017"
  },
  {
    "category": "ACTOR IN A SUPPORTING ROLE",
    "entity": "Woody Harrelson",
    "uid": "f4bef306-2b4a-48c0-b35b-0864a1bfc4cd",
    "winner": "False",
    "year": "2017"
  }
]

```
Now, using the unique ID, you can get the nomination that it is attributed to.

```console
# curl 10.244.12.214:5000/uid/75c27e55-9746-450e-8827-ef8c9ad5e376
{
  "category": "FILM EDITING",
  "entity": "City of God",
  "uid": "75c27e55-9746-450e-8827-ef8c9ad5e376",
  "winner": "False",
  "year": "2003"
}

```
Finally, you'll be able to see every nomination a certain entity has. This could either mean you'll get all of the nominations a movie had in one year, or every nomination a person has gotten until 2015.
```console
# curl 10.244.12.214:5000/entity/The_Social_Network
[
  {
    "category": "MUSIC (Original Score)",
    "entity": "The Social Network",
    "uid": "712c3aa3-f061-4977-9b17-9128f4e5d8aa",
    "winner": "True",
    "year": "2010"
  },
  {
    "category": "DIRECTING",
    "entity": "The Social Network",
    "uid": "dde5cda7-aced-46c4-bf28-2375101798c4",
    "winner": "False",
    "year": "2010"
  },
  {
    "category": "WRITING (Adapted Screenplay)",
    "entity": "The Social Network",
    "uid": "5e387d5b-291a-462e-b752-6179d081697c",
    "winner": "True",
    "year": "2010"
  },
  {
    "category": "FILM EDITING",
    "entity": "The Social Network",
    "uid": "906a8fb9-81e5-4d82-8365-c61df4fa8572",
    "winner": "True",
    "year": "2010"
  },
  {
    "category": "BEST PICTURE",
    "entity": "The Social Network",
    "uid": "259f1758-6487-44ae-aef8-7cd96248ff32",
    "winner": "False",
    "year": "2010"
  },
  {
    "category": "CINEMATOGRAPHY",
    "entity": "The Social Network",
    "uid": "650bd539-923d-4878-a7ee-0fd37fef234b",
    "winner": "False",
    "year": "2010"
  },
  {
    "category": "SOUND MIXING",
    "entity": "The Social Network",
    "uid": "ecf00a8b-398e-49bd-adbd-b93b0e53d06a",
    "winner": "False",
    "year": "2010"
  }
]
```

### 2.4. Update
Any of the features listed below can be edited by the user in any nominee. All you need is their UID. Multiple attributes can be edited at once.
- Entity: Person or film nominated
- Category: Best Picture, Actor in a Supporting Role, etc. (in ALL CAPS)
- Year: Year of the nomination
- Winner: True or False

*Note: to use spaces in the attributes, use underscores*
```console
# curl 10.244.12.214:5000/uid/"f88dfa19-8bf0-47d8-a463-098643e042d2"/edit?winner=True
{
  "category": "ACTRESS IN A LEADING ROLE",
  "entity": "Fernanda Montenegro",
  "uid": "f88dfa19-8bf0-47d8-a463-098643e042d2",
  "winner": "True",
  "year": "1998"
}
```

### 2.5. Delete
Delete routes work similarly to read routes, but of course you remove the element from the database when you curl it.

You can use them to delete all nominees from a specific year.
```console
# curl 10.244.12.214:5000/year/1957/delete
Year Deleted: 95 items total
```
Or to delete nominees from a range of years.
```console
# curl "10.244.12.214:5000/year/range/delete?start=1927&end=1934"
Range Deleted: 326 items total
```
Or even from a specific category in a year
```console
# curl 10.244.12.214:5000/year/1989/category/CINEMATOGRAPHY/delete
Category Deleted: 5 items total

# curl 10.244.12.214:5000/year/1989/category/CINEMATOGRAPHY
[]
```
You can also use UIDs to delete a specific nomination
```console
# curl 10.244.12.214:5000/uid/"4811b706-1252-4f6e-83e8-fd0fabcfd3da"/delete
{
  "category": "ACTRESS IN A LEADING ROLE",
  "entity": "Gwyneth Paltrow",
  "status": "DELETED",
  "uid": "4811b706-1252-4f6e-83e8-fd0fabcfd3da",
  "winner": "True",
  "year": "1998"
}
```
Or an entity name to delete all nominations from a film or a person.
```console
# curl 10.244.12.214:5000/entity/Meryl_Streep/delete
Entity Deleted: 21 items total
```

### 2.6. Jobs

Now, you will be able to perform an analysis job in the data. For this project, you will analyze the average length of nominees' names in each year. By the end of the analysis, you will have a graph with a start and stopping year of your choice. Why would this be useful? Maybe someday you want to join the film industry but not sure what to name your movie. With this you can analyze trends and maximize your mathematical chances of getting an Oscar nomination by the length of your movie title.

To start, curl this route using your information:
```console
# curl -X POST -H "content-type: application/json" -d '{"start":"2000","end":"2010"}' 10.244.15.204:5000/jobs
{"id": "aaffab13-69a2-494d-8a66-98513620f2da", "status": "submitted", "start": "2000", "end": "2010"}
```
What is being returned is the dictionairy for your job request, so you will need to copy that ID to get your plot when the job is finalized. Now, there is more than one way to obtain your image. We'll go over two of them:

##### 2.6.1. Download Route

You can use a command to download the image to your current folder and later move it around your isp02 directory.
```console
# curl 10.244.13.225:5000/download/"5ad09127-7c00-48d3-9dfa-71075e2a95cd" >output.png
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 38173  100 38173    0     0  1863k      0 --:--:-- --:--:-- --:--:-- 2071k

# scp output.png yourusername@isp02.tacc.utexas.edu:~/
yourusername@isp02.tacc.utexas.edu's password:
output.png  
```
This will transfer the image to your home on isp02. From there, you can either use 'scp' again to move it to your computer, or push it somewhere you would like.

#### 2.6.2. Browser

A way that can be easier if you want to hava the file in your local computer directly is accessing the following url. It will download it automatically.
```
https://isp-proxy.tacc.utexas.edu/<yourusername>/download/<job-id>
```

#### 2.6.3. Image Examples
Below are some examples of plots that show the average length of Oscar Nominees' names across different time periods.

![2.6.3.1](https://github.com/felipemrocha/COE-322-fm9252/blob/main/final/documentation/5e45c6c4-be3e-4daf-b2ca-1a65675d9b1c.png)

![2.6.3.2](https://github.com/felipemrocha/COE-322-fm9252/blob/main/final/documentation/be1327ce-ccfe-429f-a585-b9010e7e0e44.png)
