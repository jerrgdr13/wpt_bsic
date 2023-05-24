from fastapi import FastAPI, Path
import requests
import json
import modules.wpt as wptdata

test_id = ''


app = FastAPI()

@app.get("/")
def index():
    pass


@app.get("/create-wpt/{test_id}")
def create_wpt(test_id: str):
    datwpt = wptdata.create_wpt(test_id)
    return datwpt
