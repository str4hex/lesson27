import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson27.settings')
application = get_asgi_application()


import json
from ads.models import Ads
from ads.models import Cat

with open('ads.json', 'r', encoding='utf-8') as file_json:
    load = json.load(file_json)

    for load_db in range(len(load)):
        ads = Ads(Id=load[load_db]['Id'],
                  name=load[load_db]['name'],
                  author=load[load_db]['author'],
                  price=load[load_db]['price'],
                  description=load[load_db]['description'],
                  address=load[load_db]['address'],
                  is_published=load[load_db]['is_published'].title()
                  )
        ads.save()

with open('categories.json', 'r', encoding='utf-8') as file_json:
    load = json.load(file_json)

    for load_db in range(len(load)):
        cat = Cat(id=load[load_db]['id'],
                  name=load[load_db]['name'])
        cat.save()
