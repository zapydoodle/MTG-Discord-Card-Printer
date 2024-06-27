import requests
from PIL import Image
from io import BytesIO
url="https://api.scryfall.com/cards/random?format=image"
response = requests.get(url)
card=Image.open(BytesIO(response.content))
card.show()