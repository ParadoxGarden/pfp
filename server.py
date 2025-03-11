from fastapi import FastAPI
from starlette.responses import Response
import drawsvg as dw
from .makepfp import draw_default_clock

app:FastAPI = FastAPI()
@app.get("/")
def get_pfp_png():
    clock:dw.Drawing= draw_default_clock()
    resp:Response  = Response(clock.as_svg(), media_type="image/svg+xml")
    return resp
