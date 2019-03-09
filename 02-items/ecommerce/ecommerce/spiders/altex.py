# -*- coding: utf-8 -*-
import scrapy
import logging

from ecommerce.items import EcommerceItem


class AltexSpider(scrapy.Spider):
    name = 'altex'
    allowed_domains = ['altex.ro']
    start_urls = ['https://altex.ro/cafetiere/cpl/']

    def parse(self, response):
        items = []
        items_xpath = response.xpath('//*[@class="Products-item"]')
        for item_xpath in items_xpath:
            item = EcommerceItem()
            title = item_xpath.xpath(
                './/*[@class="Product-list-right"]//@title'
            ).extract()
            url = item_xpath.xpath(
                './/*[@class="Product-list-right"]'
                '/*[@class="Product-nameHeading"]/a/@href'
            ).extract()
            reduction = item_xpath.xpath(
                './/*[@class="Badge-reducere"]/text()'
            ).extract()
            new_price = item_xpath.xpath(
                './/*[@itemprop="price"]/@content'
            ).extract()

            item['title'] = title
            item['url'] = url
            item['reduction'] = reduction
            item['new_price'] = new_price
            items.append(item)
        logging.info("parsing result: {item}".format(item=items))
        return items


class AltexYieldSpider(scrapy.Spider):
    name = 'altex_yield'
    allowed_domains = ['altex.ro']
    start_urls = ['https://altex.ro/cafetiere/cpl/']

    def parse(self, response):
        items_xpath = response.xpath('//*[@class="Products-item"]')
        for item_xpath in items_xpath:
            item = EcommerceItem()
            title = item_xpath.xpath(
                './/*[@class="Product-list-right"]//@title'
            ).extract()
            url = item_xpath.xpath(
                './/*[@class="Product-list-right"]'
                '/*[@class="Product-nameHeading"]/a/@href'
            ).extract()
            reduction = item_xpath.xpath(
                './/*[@class="Badge-reducere"]/text()'
            ).extract()
            new_price = item_xpath.xpath(
                './/*[@itemprop="price"]/@content'
            ).extract()

            item['title'] = title
            item['url'] = url
            item['reduction'] = reduction
            item['new_price'] = new_price
            logging.info("parsing result: {item}".format(item=item))
            yield item
