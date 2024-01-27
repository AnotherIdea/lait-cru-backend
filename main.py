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
    name: str
    logo: str
    website: str
    address: str
    phone_number: str

markers = [
    Marker(lat=47.0243098215608, lng=-0.7580285865069062, name="Bernard Gaborit", logo="", website="https://www.bernardgaborit.fr/vente-a-la-ferme", address="La Grande Nillière Maulevrier 49360 France", phone_number="02 41 55 56 54"),
    Marker(lat=45.7640, lng=4.8357, name="Ferme de Kerheu", logo="", website="https://www.fermedekerheu.com/", address="Rte de Kerheu, 29510 Briec", phone_number="0188336185"),
    # Autres marqueurs
]

@app.get("/markers")
async def get_markers() -> List[Marker]:
    return markers
