import requests
import time
from .models import Webtoon


def get_artists(artists):
   artist = ''
   for i in artists:
       artist += i.get('name') + '/'

   return artist[:-1]


def webtoon(day):
   json = requests.get('http://webtoon.daum.net/data/pc/webtoon/list_serialized/' + day + '?timeStamp=' + str(int(time.time()))).json()

   for webtoon in json.get('data'):
       webtoon_model = Webtoon()
       webtoon_model.webtoon_id = "daum_" + webtoon.get('title')
       webtoon_model.site_name = "daum"
       webtoon_model.webtoon_name = webtoon.get('title')
       webtoon_model.webtoon_author = get_artists(webtoon.get('cartoon').get('artists'))
       webtoon_model.webtoon_img_url = webtoon.get('thumbnailImage2').get('url')

       webtoon_model.save()


def webtoon_all():
    week_day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in week_day:
        webtoon(day)


