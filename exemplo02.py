import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    
    data_types = data['types']
    types_list = []
    
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    
    return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
    print(pegar_pokemon(1))
    print(pegar_pokemon(4))
    print(pegar_pokemon(7))
    print(pegar_pokemon(10))