from fastapi import FastAPI
import src.generator as gen
import src.levelup as levelup
from postdata import LevelData


app = FastAPI()
cur_artifact = {}


@app.get('/')
def index():
    return {
        'message': 'API up and running',
        'endpoints': ['/get_artifact', '/cur_artifact', '/levelup']
    }


@app.get('/get_artifact')
def get_artifact():
    ret = gen.get_artifact()
    global cur_artifact
    cur_artifact = ret
    return ret


@app.get('/cur_artifact')
def get_cur_artifact():
    global cur_artifact
    return cur_artifact


@app.post('/levelup')
def get_job_details(data: LevelData):
    ret = data.dict()
    cur_artifact['levelup'] = ret['data']
    return levelup.Levelup(cur_artifact)


# uvicorn app:app --reload
# uvicorn app:app --host 0.0.0.0 --port 8000
