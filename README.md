## Tok's Profile Picture generator:
This is a script that I made to generate a SVG / PNG of an analog clockface at a specified time

Currently generates a png at ./test.png

look right, surely it's more efficent to generate a bunch of PFPs and pull the correct one for the correct time, but I thought it would be more fun to create a function to dynamically provide the time, that way if I *want* to generate the images I can use it, or if I want I an hook this up to an HTTP endpoint and go nuts.

## Requirements:
Python 3.13.2

## Use:
``` bash
    python -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    .venv/bin/python makepfp.py
```