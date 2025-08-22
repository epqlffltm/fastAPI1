from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

thing=Creature(
    name="yeti",
    country="CN",
    area="himalayas",
    description="himalayas",
    aka="himalayas"
)

print(thing.name)