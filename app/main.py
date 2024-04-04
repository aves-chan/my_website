from fastapi import FastAPI
from fastapi.responses import FileResponse
from uvicorn import run


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("app/frontend/index.html")


if __name__ == "__main__":
    run(app=app, host="0.0.0.0", port=80)