# Flink/Docker/Python example
## https://github.com/kkolman/flink-docker-python

## Git create a new repository on the command line
	echo "# flink-python-code" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git branch -M master
	git remote add origin https://github.com/dkolpakov2/flink-python-code.git
	git push -u origin master
## …or push an existing repository from the command line
	git remote add origin https://github.com/dkolpakov2/flink-python-code.git
	git branch -M master
	git push -u origin master

## Exclude dependency jars duplications:
 mvn dependency:tree -Ddetail=true

## Using Python DataStream API requires installing PyFlink, which is available on PyPI and can be easily installed using pip.
	$ python -m pip install apache-flink
## LOG:
	...nrt -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\cppwinrt /Tc_configtest.c /Fo_configtest.obj
        error:
        [end of output]
     
        note: This error originates from a subprocess, and is likely not a problem with pip.
      error: legacy-install-failure
     
      Encountered error while trying to install package.
     
      numpy
     
      note: This is an issue with the package mentioned above, not pip.
      hint: See above for output from the failure.
##
	  

$ python -m pip install apache-flink
## (Optional) Choose Flink docker image
```
export FLICK_DOCKER_IMAGE_NAME=flink-alpine
```

## Start Flink cluster
Execute
```
docker-compose up
```
and check Flink Dashboard at http://localhost:8081 (or whatever ip is assigned - see `docker-machine ip`).

- Two nodes are started - JobManager & TaskManager.
- Project folder is mapped as */app/* to both nodes.


## Trigger hello_world.py Flink job
Running
```
./trigger_helloworld.sh
```
will start a Flink job that outputs "Hello World" into a timestamped file in *out* folder.

```
$ ./trigger_helloworld.sh
Starting execution of program
Program execution finished
Job with JobID af08dc721ea929cdb45cdd2f3cee949d has finished.
Job Runtime: 4542 ms

$ ls out
helloworld_1539091504.366000

$ cat out/helloworld_1539091504.366000
Hello World
```

For simplicity `pyflink-stream.sh` is triggered from within job manager node without an additional "detached launcher" node.