

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_books():
    return {'message': 'Hola mundo!'}
