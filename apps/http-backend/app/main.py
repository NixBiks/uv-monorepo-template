from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


class HTMLBody(BaseModel):
    html: str


@app.post("/html2text")
def html2text(request: HTMLBody):
    import html2text

    parser = html2text.HTMLToText()
    return {"text": parser.parse(request.html)}
