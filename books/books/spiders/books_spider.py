import scrapy
# from ..items import BooksItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    page_number = 2
    start_urls = [
        'https://booksmandala.com/search?name=jiwan&page=1'
    ]

    def parse(self, response):
        # items = BooksItem()
        all_div_books = response.css("div.card-search")

        # print(all_div_books)
        for books in all_div_books:
            title = books.css('.card-title a').xpath("@href").extract()
            author = books.css('.card-text::text').extract()
            price = books.css('span .priceOfTheBook::text').extract()

            yield {
                'Title': title,
                'Author': author,
                'Price': price
            }

            # items['title'] = title
            # items['author'] = author
            # items['price'] = price
            # yield items

        next_page = 'https://booksmandala.com/search?name=jiwan&page=' + str(BooksSpider.page_number)
        if BooksSpider.page_number <= 4:
            BooksSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)



