from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = 'Zapflow com gemini'
    produto2 = 'Zapflow com Chatgpt'
    produto3 = 'Zapflow com Llama3.0'

class Vendas(BaseModel):
    email: EmailStr
    data: datetime    
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum


  