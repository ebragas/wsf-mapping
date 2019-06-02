# wsf-mapping

Start a Jupyter Notebook Docker container, mapping the `./notebooks` directory as a volume:
```
docker run -p 8888:8888 -v ./notebooks:/home/jovyan jupyter/minimal-notebook
```

*Reference:* https://www.dataquest.io/blog/docker-data-science/
