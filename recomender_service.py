import pandas as pd
import joblib as jl
from typing import Any

class RecomenderService:
  
  path: str = './model/modelo.pkl'
    
  def __init__(self):
    self.model: pd.DataFrame = jl.load(self.path)
  
  def __str__(self) -> str:
    recomendations: list[str] = self.recomendation('falda-67012025', 5)
    
    return ",".join(recomendations)
    
  def recomendation(self, product_code: str, n: int = 5) -> list[str]:
    if not self._exists_product_code(product_code):
      return []

    relations: Any = self._get_relations(product_code, n)
    
    return self._get_recomendations(relations)
       
  def _get_relations(self, product_code: str, n: int = 5) -> Any:
    return self.model[product_code].sort_values(ascending=False).head(n)
  
  def _get_recomendations(self, relations: Any ) -> list[str]:
    recomendations: list = []
    for product, value in relations.items():
      recomendations.append(product)
      
    return recomendations
  
  def _exists_product_code(self, product_code: str) -> bool:
    return product_code in self.model.columns
    

