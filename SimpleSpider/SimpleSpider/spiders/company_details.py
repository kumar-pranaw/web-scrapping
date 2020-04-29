# -*- coding: utf-8 -*-
import scrapy


class CompanyDetailsSpider(scrapy.Spider):
    name = 'company_details'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/sector/ms_technology']

    def parse(self, response):
        company_names_list =  response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[2]/text()').extract()
        compnay_price_list = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/text()').extract()
        
        countCompanyName = len(company_names_list)
        countCompanyList = len(compnay_price_list)
        print('Total count is : ', countCompanyName)
        print('Total count is : ', countCompanyList)
        
        # for i in range(0, count):
        #     print(company_names_list[i])