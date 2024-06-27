import requests
from PIL import Image
from io import BytesIO
def GetCard():
    url="https://api.scryfall.com/cards/random?format=image&q=t%3Asorcery+or+t%3Ainstant+or+t%3Acreature+or+t%3Aartifact+or+t%3Aenchantment+or+t%3Aplaneswalker+or+t%3Abattle"
    response = requests.get(url)
    card=Image.open(BytesIO(response.content))
    card.show()
    card.save("Random_Card.png")
GetCard()