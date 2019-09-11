# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, copy, scrapy
import re
from scrapy.pipelines.files import FilesPipeline
from ppt.settings import FILES_STORE as files_store

class PptPipeline(object):


	def process_item(self, item, spider):

		# replacedStr = re.sub("\d+", "222", inputStr)
		bclass = item['ppt_bclass']
		sclass = item['ppt_sclass']
		r_bclass = os.path.join(files_store, bclass)

		# 判断大类储存路径是否存在
		if not os.path.exists(r_bclass): 
			os.makedirs(r_bclass)
		#bookname = re.sub('[\/:*?"<>|]', '', book_name)
		
		r_sclass = os.path.join(r_bclass, sclass)
		# 判断小类储存路径是否存在
		if not os.path.exists(r_sclass): 
			os.makedirs(r_sclass)
		return item

class PptFilesPipeline(FilesPipeline):
	def get_media_requests(self, item, info):
		ppt_url = item['ppt_url']
		yield scrapy.Request(ppt_url, meta = {'item':copy.deepcopy(item)})

	def file_path(self, request, response=None, info=None):
		item = request.meta['item']
		ppt_name = item['ppt_name']

		# 去除文件名可能存在的非法字符
		ppt_name = re.sub('[\/:*?"<>|]','-',ppt_name)
		#folder_strip = folder.strip()
		#image_guid = request.url.split('/')[-1]
		bclass = item['ppt_bclass']
		sclass = item['ppt_sclass']
		ppt_url = item['ppt_url']
		# 去除下载最后可能出现的（\、/）
		ppt_url = ppt_url.rstrip("\\")
		ppt_url = ppt_url.rstrip("/")
		back_path = ppt_url[-4:]

		filename =bclass+"/"+sclass+"/"+ppt_name+back_path
		return filename