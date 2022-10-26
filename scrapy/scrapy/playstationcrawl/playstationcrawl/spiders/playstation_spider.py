import scrapy
from ..items import PlaystationcrawlItem

class PlaystationSpiderSpider(scrapy.Spider):
    name = 'playstation'
    page_number = 2
    start_urls = [
        'https://store.playstation.com/en-id/category/f44fdcbf-a390-4543-962b-ad929bbf213c/1'
    ]

    def parse(self, response, **kwargs):
        items = PlaystationcrawlItem()
        games_name = response.xpath("//span[@class='psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2']/text()").extract()
        games_price = response.css('span.psw-m-r-3::text').extract()

        items['games_name'] = games_name
        items['games_price'] = games_price

        yield items

        next_page = 'https://store.playstation.com/en-id/category/f44fdcbf-a390-4543-962b-ad929bbf213c/'+ str(PlaystationSpiderSpider.page_number)
        if PlaystationSpiderSpider.page_number <= 43 :
            PlaystationSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
# <a data-qa data-track="web:store:product-tile" data-track-click="web:store:product-tile" data-track-content="web:store:product-tile" data-telemetry-meta="{"id":"HP0102-PPSA09418_00-RE4RMAINGAME0000","index":0,"name":"Resident Evil 4 (English/Chinese/Korean/Japanese Ver.)","price":"Rp 831,000","titleId":"PPSA09418_00"}" id class="psw-link psw-content-link" aria-label type href="/en-id/product/HP0102-PPSA09418_00-RE4RMAINGAME0000" rel="noopener noreferrer" data-track-id="1">
# <span data-qa="ems-sdk-grid#productTile0#product-name" class="psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2">Resident Evil 4 (English/Chinese/Korean/Japanese Ver.)</span>
# <span data-qa="ems-sdk-grid#productTile0#price#display-price" aria-hidden="false" class="psw-m-r-3">Rp 831,000</span>
# <li class="psw-l-w-1/2@mobile-s psw-<ul data-qa class="psw-grid-list psw-l-grid">flexl-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max">flex