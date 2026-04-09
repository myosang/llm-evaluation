from fastapi import FastAPI
from llm_evaluation_gradio.api.routes import router

app = FastAPI()
app.include_router(router)