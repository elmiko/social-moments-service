# social-moments-service

This application deploys an HTTP server that will generate sentiment analysis
on all text that is sent. When deployed, sending a `POST` request to `/` with
the body containing sentences in English will cause the server to return an
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
1. access the server with curl
   `curl http://localhost:5000 -H "Content-Type: application/json" -d "I love applesauce!"`

If everything has worked you will see a result from the server
that looks similar to this:

```
[{"compound": 0.6696, "neg": 0.0, "neu": 0.182, "pos": 0.818}]
```
