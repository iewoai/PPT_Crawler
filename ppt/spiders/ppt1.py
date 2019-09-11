# -*- coding: utf-8 -*-
import scrapy
import re, copy
from ppt.items import PptItem


class Ppt1Spider(scrapy.Spider):
	name = 'ppt1'
	# allowed_domains = ['1ppt.com']
	start_urls = ['http://www.1ppt.com/data/sitemap.html']
	server = 'http://www.1ppt.com'
	num = 0
# 获得ppt大类名、小类名和主链接
	def parse(self, response):
		item = PptItem()

		# 大类名
		bclass_pattern = re.compile(r'<h3>.*?<a.*?>(.*?)</a>', re.S)
		bclass = re.findall(bclass_pattern, response.text)

		# 大类所有链接
		class_urls_pattern = re.compile(r'<ul class="f6">(.*?)</ul>',re.S)
		class_urls = re.findall(class_urls_pattern, response.text)

		# 遍历所有大类获得所有小类链接并发送请求
		for i in range(1,2):
			item['ppt_bclass'] = bclass[i]
			sclass = re.findall(r"<li.*?href='(.*?)'.*?>(.*?)</a>", class_urls[i],re.S)
			# print(bclass[i])
			# 遍历所有小类
			for j in sclass:
				item['ppt_sclass'] = j[1]
				sclass_url = self.server + j[0]
		# 测试专用
		# test = 'http://www.1ppt.com/article/43411.html'
		# yield scrapy.Request(test,callback = self.parse_dl)
				yield scrapy.Request(sclass_url, callback = self.parse_sclass, meta = {'item':copy.deepcopy(item),'url':sclass_url})

# 获得小类中所有ppt链接
	def parse_sclass(self, response):
		item = response.meta['item']

		# 一页所有ppt名和链接
		url = response.meta['url']
		ppts = re.findall(r"<li>.*?<h2.*?href=\"(.*?)\".*?>(.*?)</a>.*?</li>", response.text, re.S)
		for ppt in ppts:
			ppt_url = self.server + ppt[0]
			item['ppt_name'] = ppt[1]
			yield scrapy.Request(ppt_url, callback = self.parse_dl, meta = {'item':copy.deepcopy(item)})
		next_page = re.findall(r'<ul class="pages">.*?href=\'(.*?)\'.*?</ul>', response.text, re.S)
		# 如果不存在下一页链接就停止递归
		if len(next_page) != 0:
			next_url = url + next_page[0]
			yield scrapy.Request(next_url, callback = self.parse_sclass, meta = {'item':copy.deepcopy(item),'url':url})

# 获得下载地址
	def parse_dl(self, response):
		item = response.meta['item']
		ppt_url = re.findall(r'<ul class="downurllist".*?href="(.*?)".*?</a>', response.text, re.S)
		item['ppt_url'] = ppt_url[0]
		self.num += 1
		print('正在下载第%s个任务：' %(str(self.num), ))
		
		yield item


