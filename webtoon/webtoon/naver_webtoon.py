import requests
import bs4
from .models import Webtoon


def webtoon(day):
    html = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=' + day)

    bs_object = bs4.BeautifulSoup(html.text, 'html.parser')
    webtoon_list = bs_object.find('ul', {'class': 'img_list'})

    for webtoon in webtoon_list.findAll('li'):
        webtoon_detail = webtoon.find('dt')

        webtoon_model = Webtoon()
        webtoon_model.webtoon_id = "naver_" + webtoon_detail.find('a')['title']
        webtoon_model.site_name = "naver"
        webtoon_model.webtoon_name = webtoon_detail.find('a')['title']
        webtoon_model.webtoon_author = webtoon.find('dd').find('a').text
        webtoon_model.webtoon_img_url = webtoon.find('img')['src']

        webtoon_model.save()


def webtoon_all():
    week_day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in week_day:
        webtoon(day)


