import os, random, string, datetime, base64, requests, pytz, PIL, re, json, io

## CORS functions
def imageToDataURL(image_url):
    response = requests.get(image_url)
    image = PIL.Image.open(io.BytesIO(response.content))
    buffer = io.BytesIO()
    image.save(buffer, "PNG")
    contents = buffer.getvalue()
    b64str = 'data:image/png;base64,'+str( base64.b64encode(contents).decode() )
    buffer.close()
    return b64str


##### List Processing Functions
def shuffleList(old_list):
    new_list = old_list.copy()
    random.shuffle(new_list)
    return new_list