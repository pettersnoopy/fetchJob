# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem

class FetchteacherjobsPipeline(object):
    def process_item(self, item, spider):
        return item

class InfoItemWriterPipeline(object):

	def __init__(self):
		self.file = codecs.open('jobs.json', 'a', encoding='utf-8')

	def process_item(self, item, spider):
		drop = True
		for cat in item['category']:
			if ("英语" in cat):
				drop = False
				break
		if (drop) :
			raise DropItem("Missing English %s" % item)
		else :
			line = json.dumps(dict(item), ensure_ascii=False, encoding='utf-8') + "\n"
			self.file.write(line)
			return item

	def close_item(self, spider):
		self.file.close
