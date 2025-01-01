from fastapi import FastAPI

app = FastAPI()


@app.get('/greet')
def read_root(name: str | None = 'World'):
    return {
        'message': f'Hello, {name}!'
    }

