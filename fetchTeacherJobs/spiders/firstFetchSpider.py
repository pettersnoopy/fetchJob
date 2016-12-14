# -*- coding: utf-8 -*- 
import scrapy
import sys
from fetchTeacherJobs.items import InfoItem

reload(sys)
sys.setdefaultencoding('UTF-8')

class MySpider(scrapy.Spider):
	name = "jiaoshizhaopin.net"
	allowed_domains = [
		'jiaoshizhaopin.net'
	]
	start_urls = [
		'http://www.jiaoshizhaopin.net/guangdong',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=2',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=3',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=4',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=5',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=6',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=7',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=8',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=9',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=9',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=10',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=11',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=12',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=13',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=14',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=15',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=16',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=17',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=18',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=19',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=20',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=21',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=22',
		'http://www.jiaoshizhaopin.net/guangdong/?City=&page=23',

	]

	def parse(self, response):
		sel = scrapy.Selector(response)
		a_contains = response.xpath('//li[@class="article"]')
		for a in a_contains:
			title = a.xpath('.//div[@class="list_item_title"]/a/text()').extract()
			herf = a.xpath('.//div[@class="list_item_title"]/a/@href').extract();
			content = a.xpath('.//p[@class="content"]/text()').extract()
			category = a.xpath('.//ul[@class="jobs_list_ul"]//span[@class="job_name"]/text()').extract()
			count = a.xpath('.//ul[@class="jobs_list_ul"]//span[@class="job_amount"]/text()').extract()
			time = a.xpath('.//p[@class="middle_text"]/text()').extract()
			item = InfoItem()
			item['title'] = title
			item['herf'] = herf
			item['content'] = content
			item['category'] = category
			item['count'] = count
			item['time'] = time
			yield item

		# i = 0;
		# for url in response.xpath('//a/@href').extract():
		# 	if (i < 100) :
		# 		yield scrapy.Request(response.urljoin(url), callback=self.parse)
		# 		i = i + 1
		# 	else :
		# 		break


