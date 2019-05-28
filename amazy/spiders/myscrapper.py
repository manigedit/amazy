import scrapy

class myscrapper(scrapy.Spider):
    name = "mobiles"
    
    def start_requests(self):
        urls = [ "https://www.amazon.in/s?k=mobiles&lo=list&page=2" ]
        
        for url in urls:
            yield scrapy.Request( url=url, callback = self.parse )



            
    def parse(self, response):
        page = response.url.split("=")[2][0]
        filename = "mobiles-%s.html" %page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("saved the file %s"%filename)

        main_key = "sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 AdHolder sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"
        #all the inner css elements before product name
        main_a = "div.sg-col-inner"
        main_b = "div.s-include-content-margin s-border-bottom"
        main_c = "div.a-section a-spacing-medium"
        main_d = "div.sg-row"
        main_e = "div.sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"
        main_f = "div.sg-col-inner"
        main_g = "div.sg-row"

        name_in_a = "div.sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-32 sg-col-12-of-20 sg-col-12-of-36 sg-col sg-col-12-of-24 sg-col-12-of-28"
        name_in_b = "div.sg-col-inner"
        name_in_c = "div.a-section a-spacing-none"
        name_in_d = "h2.a-size-mini a-spacing-none a-color-base s-line-clamp-2"
        name_in_e = "a.a-link-normal a-text-normal"
        name_final = "span.a-size-medium a-color-base a-text-normal::text"
        

        price_in_a = "div.sg-col-4-of-12 sg-col-6-of-20 sg-col-4-of-16 sg-col sg-col-6-of-36 sg-col-6-of-28 sg-col-6-of-32 sg-col-6-of-24"
        price_in_b = "div.sg-col-inner"
        price_in_c = "div.a-section a-spacing-none a-spacing-top-small"
        price_in_d = "div.a-row a-size-base a-color-base"
        price_in_e = "div.a-row"
        price_in_f = "a.a-size-base a-link-normal s-no-hover a-text-normal"
        price_in_g = "span.a-price"
        price_final = "span.a-icon-alt::text"

        #all the inner css elements before rating
        rating_in_a = "div.sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-32 sg-col-12-of-20 sg-col-12-of-36 sg-col sg-col-12-of-24 sg-col-12-of-28"
        rating_in_b = "div.sg-col-inner"
        rating_in_c = "div.a-section a-spacing-none a-spacing-top-micro"
        rating_in_d = "div.a-row a-size-small"
        rating_in_e = "span.mobiles_rating_two"
        rating_in_f = "a.a-popover-trigger a-declarative"
        rating_in_g = "i.a-icon a-icon-star-small a-star-small-4 aok-align-bottom"
        rating_final = "span.a-offscreen::text"




        prods = response.css(main_key)

        for product in prods:
            main_subframe = product.css(main_a).css(main_b).css(main_c).css(main_e).css(main_f).css(main_g)

            name = main_subframe.css(name_in_a).css(name_in_b).css(name_in_c).css(name_in_e).css(name_final).get()

            price = main_subframe.css(price_in_a).css(price_in_b).css(price_in_c).css(price_in_d).css(price_in_e).css(price_in_f).css(price_in_g).css(price_final).get()

            ratings = main_subframe.css(rating_in_a).css(rating_in_b).css(rating_in_c).css(rating_in_d).css(rating_in_e).css(rating_in_f).css(rating_in_g).css(rating_final)

            yield {
                    "Mobile Phone":name,
                    "Price ":price,
                    "Ratings ":ratings,
            }


        if int(page) < 8:
            url = "https://www.amazon.in/s?k=mobiles&lo=list&page=" + str(int(page)+1)
            yield scrapy.Request(url=url, callback=self.parse)





