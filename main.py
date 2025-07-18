from fastapi import FastAPI
from recomender_service import RecomenderService

app = FastAPI()

@app.get('/')
async def root():
  return {
    "message": "Recomender System Actived"
  }

@app.get('/recommend/{product_code}')
async def predict(product_code: str, n_items: int = 5):
  recomender = RecomenderService()
  recomendations: list[str] = recomender.recomendation(product_code, n_items)
  
  return {
    "recomendations": recomendations
  }
  
  
  
  
  
  