from io import BytesIO
from PIL import Image
from requests import get

def get_raw(url, **kwargs):
    return get(url, stream=True, **kwargs).content

def get_image(url, **kwargs):
    raw = get_raw(url, **kwargs)
    return Image.open(BytesIO(raw))