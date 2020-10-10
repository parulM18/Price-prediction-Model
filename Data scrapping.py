import scrapy

class flipkartcrawl(scrapy.Spider):
    name = 'flip'
    page_no=2
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=mobiles&page=1']

    def parse(self, response):

        print("procesing:"+response.url)
        product_name=response.css('._3wU53n::text').extract()
        price=response.css('._2rQ-NK::text').extract()
        rating=response.css('.hGSR34::text').extract()
        ram=response.css('.tVe95H:nth-child(1)::text').extract()
        product_dimention=response.css('.tVe95H:nth-child(2)::text').extract()
        camera=response.css('.tVe95H:nth-child(3)::text').extract()
        battery=response.css('.tVe95H:nth-child(4)::text').extract()
        processor=response.css('.tVe95H:nth-child(5)::text').extract()
    

        row_data=zip(product_name,price,rating,ram,product_dimention,camera,battery,processor)
        for item in row_data:
            scraped_info = {
                'page' :response.url,
                'product_name' : item[0],
                'price' : item[1],
                'rating' : item[2],
                'ram' : item[3],
                'product_dimention' : item[4],
                'camera' : item[5],
                'battery' : item[6],
                'processor' : item[7],
            }
            yield scraped_info

            NEXT_PAGE='https://www.flipkart.com/search?q=mobiles&page=' + str(flipkartcrawl.page_no) + ''
            if flipkartcrawl.page_no <= 460:
                flipkartcrawl.page_no+=1
                yield response.follow(NEXT_PAGE, callback=self.parse)


        
