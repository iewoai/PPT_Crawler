# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	ppt_url = scrapy.Field()
	ppt_name = scrapy.Field()
	ppt_sclass = scrapy.Field()
	ppt_bclass = scrapy.Field()

