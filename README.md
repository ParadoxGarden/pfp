## SVG clock generator
This is a script that I made to [draw](https://github.com/cduck/drawsvg) a SVG of an analog clockface at a specified time.
additionally there is a [fastapi](https://github.com/fastapi/fastapi) webserver which provides endpoints to get the clock image (at the current time) in various ways


## Requirements:

- Python 3.13.2 (version is just the one I used for development & testing, I'm sure other versions work also)



## Use:
```bash
    # Environment setup
    python -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt    
    # run the webserver
    .venv/bin/python -m fastapi run server.py
    # generate images
    .venv/bin/python makepfp.py


    # run docker container
    docker compose up -d
```
