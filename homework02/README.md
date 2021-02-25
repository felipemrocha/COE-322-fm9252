# Animal Breeding - Felipe Rocha

Contains files that allow you to generate a JSON with 20 unique animals with different heads, bodies, and number of arms, legs, and tails inside a container. This code also allows you to breed two of those animals and generate an "offspring" containing the head of one of their parents, a body formed by two of the four animals that formed their parents' bodies, and legs, arms, and tails formed by the mean of the number of each limb both parents had. A unit test is also provided outside a container.

## Download

Clone this repository to your terminal and navigate to the **homework02** subdirectory.

```bash
git clone https://github.com/felipemrocha/COE-322-fm9252
cd COE-322-fm9252/
cd homework02
```

## Building an image with the Dockerfile

```bash
cd dockerfile
docker build -t <dockerhubusername>/homework02:1.0 .
```
Use your own docker hub username.

## Running the scripts inside a container
There are two ways to run the code: interactively and non-interactively. Running it interactively requires you to go inside the container and use commands from there:
```bash
docker run --rm -it <dockerhubusername>/homework02:1.0 /bin/bash
cd /home
generate_animals.py test.json
read_animals.py test.json
exit
```
Running it non-interactively requires you to create a subdirectory and go there to execute the commands:
```bash
mkdir running
cd running
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) <dockerhubusername>/homework02:1.0 generate_animals.py /data/animals.json
docker run --rm -v $PWD:/data <dockerhubusername>/homework02:1.0 read_animals.py /data/animals.json
```
Both of these get you the same final result: the "offspring" of two random animals generated in the JSON file. This result will be printed as a dictionary with its features.

## Running the unit test
This next part should be tested outside the dockerfile folder. In the subdirectory, run the **test_read_animals.py** file with the following command.
```bash
python3 test_read_animals.py
```
This will check that the breeding function is only working for appropriate dictionaries that have been labeled correctly. It will also make sure the offspring for a test "parent" is returned as expected.

### Felipe Martins Rocha (fm9252) - Homework 2