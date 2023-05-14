from models import create_tables, Publisher, Book, Shop, Stock, Sale
publisher1 = Publisher(name="Москва")
book1 = Book(title="Капитанская дочка", publisher=publisher1)
shop1 = Shop(name=" Буквоед")
stock1 = Stock(count=580, book=book1, shop=shop1)
sale1 = Sale(price=600, date_sale='09-11-2022', stock=stock1, count=1)

publisher2 = Publisher(name="Ленинград")
book2 = Book(title="Руслан и Людмила", publisher=publisher2)
stock2 = Stock(count=800, book=book2, shop=shop1)
sale2 = Sale(price=500, date_sale='08-11-2022', stock=stock2, count=55)

shop3 = Shop(name="Лабиринт")
stock3 = Stock(count=800, book=book1, shop=shop3)
sale3 = Sale(price=580, date_sale='05-11-2022', stock=stock3, count=5)

book4 = Book(title="Евгений Онегин", publisher=publisher2)
shop4 = Shop(name="Книжный дом")
stock4 = Stock(count=432, book=book4, shop=shop4)
sale4 = Sale(price=490, date_sale='02-11-2022', stock=stock4, count=500)

stock5 = Stock(count=580, book=book1, shop=shop1)
sale5 = Sale(price=600, date_sale='26-10-2022', stock=stock4, count=590)


session.add_all([publisher1,book1,shop1,stock1,sale1])
session.add_all([publisher2,book2,stock2,sale2])
session.add_all([shop3,stock3,sale3])
session.add_all([book4,shop4,stock4,sale4])
session.add_all([stock5,sale5])