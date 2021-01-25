from fastapi import FastAPI

app = FastAPI(docs_url=None)

@app.get('/')
async def get_root():
    return {"status":"ok"}