from fastapi import FastAPI
import src.generator as gen


app = FastAPI()


@app.get('/')
def index():
    return {
        'message': 'API up and running',
        'endpoints': ['/get_artifact']
    }


@app.get('/get_artifact')
def get_artifact():
    ret = gen.get_artifact()
    return ret

# uvicorn app:app --reload
