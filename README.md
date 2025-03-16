## Profile picture generator:
This is a script that I made to generate a SVG of an analog clockface at a specified time

look right, surely it's more efficent to generate a bunch of images and pull the correct one for the correct time, but I thought it would be more fun to draw it dynamically and hook it up to a web endpoint for later use.

(maybe I'll even end up customizing the gradient over time and other fun stuff)

## Requirements:
(to run scripts)
Python 3.13.2
(automated use)
docker

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

you can also fill out a config.toml file to upload this generated pfp to various services (currently just bsky and discord).

## Built with:
- [DrawSVG](https://github.com/cduck/drawsvg)
- [fastapi](https://github.com/fastapi/fastapi)
- [atproto](https://github.com/MarshalX/atproto)
