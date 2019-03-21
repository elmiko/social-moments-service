# social-moments-service

This service deploys an HTTP server that will generate sentiment analysis
on all text that is sent. When deployed, sending a `POST` request to `/` with
the body containing sentences in English will cause the service to return an
array of sentiment scores corresponding to the sentences.

## quickstart

**prerequisites**
* a shell with Python 3.4+ available.
* access to the `pip` command available.
* access to the `curl` command available.
* _(optional)_ a
  [Python Virtual Environment](https://virtualenv.pypa.io/en/stable/)
  available.

**procedure**
1. clone this repository and change directory into the cloned location
1. install the dependencies with `pip install -r requirements.txt`
1. start the server with `FLASK_APP=app.py flask run`
1. access the service with curl

   `curl http://localhost:5000 -H "Content-Type: application/json" -d "I love applesauce!"`

If everything has worked you will see a result from the service
that looks similar to this:

```
[{"compound": 0.6696, "neg": 0.0, "neu": 0.182, "pos": 0.818}]
```

## launch on openshift

This repository has been designed to be deployable on OpenShift using the
[source-to-image](https://docs.okd.io/latest/creating_images/s2i.html#creating-images-s2i)
workflow. As such, you can directly deploy this code into a container on
OpenShift.

**prerequisites**
* access to an OpenShift cluster available.
* a shell with access to the `oc` command available.

**procedure**
1. login to your OpenShift account and select, or create, a project.
1. build and deploy the service.

   `oc new-app centos/python-36-centos7~https://github.com/elmiko/social-moments-service`
1. expose a route to your service.

   `oc expose service/social-moments-service`
1. access the service with curl.

   ```curl http://`oc get routes/social-moments-service --template='{{.spec.host}}'` \
        -H "Content-Type: application/json" \
        -d "I love applesauce!"```

If everything has worked you will see a result similar to one in the previous
example.
