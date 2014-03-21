Deployment
==========

Deployment
----------

As well as packaging code for sharing with others, we want to be able to get
our code onto somewhere where it will actually be used: either onto a
supercomputer to run simulations, or onto a web server to make a web-based tool.

Doing it wrong
--------------

If you manually shell into a remote supercomputer when you deploy
into production you are doing it wrong.

Tools exist to help you manage deployment.

Repetition
----------

* Repetition leads to boredom
* Boredom leads to horrifying mistakes
* Horrifying mistakes lead to God-I-wish-I-was- still-bored
-- [Will Larson](http://lethain.com/deploying-django-with-fabric/)

DevOps
------

"Systems administration" should be treated with the same respect as development.

This is systems programming. (Aka dev ops.)

Fabric
------

```bash
cat ~/devel/myproject/fabfile.py
fab deploy
```

```python
from fabric.api import local
env.host = 'gauss.chem.ucl.ac.uk'
env.repo = 'ssh://hg@myserver/myrepo'

env.remote_path='/var/www/www.myapp.com/'

@task
def deploy():
  with cd(env.remote_path)
    run('git clone {repo}'.format(**env))
```

Sshing, cloning or syncing of files, all gets absorbed into tasks
Fabric tasks are just python functions decorated with @task

Fabric with supercomputers
--------------------------

* Maintain list of different remotes
* Maintain templates for jobscripts
* Define modules to load in fabfile, not in remote bashrc.

Fabric to build code
--------------------

```python
@task
def build(*configurations,**extras):

    with cd(env.build_path):
        with prefix(env.build_prefix):
            run("rm -f {build_path}".format(**env))
            run("cmake {repository_path} {cmake_flags}".format(**env))
```

Using fabric with multiple remotes
----------------------------------

``` bash
cd devel/projects/hemelb
fab hector cold
fab tianhe send_geometry:cylinder
fab archer hemelb:cylinder
fab dirac wait_on_run
fab legion steer
fab stampede fetch_results
```

Use a config file to describe machines
--------------------------------------

```bash
cat ~/devel/hemelb/deploy/machines.yml
```
``` yaml
hector:
  remote: "login.hector.ac.uk"
  username: jamespjh
  job_dispatch: "qsub"
  run_command: "aprun -n $cores -N
            $coresusedpernode"
  batch_header: pbs
  max_job_name_chars: 15
  make_jobs: 4
legion:
  ...
```
