from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
# Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les headers
)

class Marker(BaseModel):
    lat: float
    lng: float
    popup: str

markers = [
    Marker(lat=48.8566, lng=2.3522, popup="Marqueur à Paris"),
    Marker(lat=45.7640, lng=4.8357, popup="Marqueur à Lyon"),
    # Autres marqueurs
]

@app.get("/markers")
async def get_markers() -> List[Marker]:
    return markers
