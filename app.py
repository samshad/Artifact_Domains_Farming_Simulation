from fastapi import FastAPI
import src.generator as gen
import src.levelup as levelup
from postdata import LevelData
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return {
        'message': 'API up and running',
        'endpoints': ['/get_artifact', '/levelup']
    }


@app.get('/get_artifact')
def get_artifact():
    ret = gen.get_artifact()
    global cur_artifact
    cur_artifact = ret
    # print(cur_artifact)
    return ret


@app.post('/levelup')
def get_job_details(data: LevelData):
    ret = data.dict()
    print(ret)
    return levelup.Levelup(ret)


# uvicorn app:app --reload
# uvicorn app:app --reload --host 0.0.0.0 --port 8000
