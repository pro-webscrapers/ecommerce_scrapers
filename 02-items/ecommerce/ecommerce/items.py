# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class EcommerceItem(Item):
    title = Field()
    url = Field()
    reduction = Field()
    new_price = Field()
