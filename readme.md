# wsf-mapping

## Setup
Start a Jupyter Notebook Docker container, mapping the `./notebooks` directory as a volume:
```
docker run -p 8888:8888 -v ./notebooks:/home/jovyan jupyter/minimal-notebook
```

*Reference:* https://www.dataquest.io/blog/docker-data-science/


## Feature Ideas:
* Run Flask web app container instead of `crond -f`. Pull data from API, expose logs via app, and enable CSV download via button.
