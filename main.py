import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import DSN
from models import create_tables, Publisher, Book, Shop, Stock, Sale

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

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




def find_data_by_name():
    pub_name = input("Имя издателя:")
    for books in session.query(Book.title, Publisher.name, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(
            Stock).join(Sale).join(Shop).filter(Publisher.name.like(pub_name)).all():
        print(' '.join(str(book) for book in books))


def find_data_by_id():
    pub_id = input("Id Издателя:")

    for books in session.query(Book.title, Publisher.name, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(
            Stock).join(Sale).join(Shop).filter(Publisher.id == pub_id).all():
        print(' '.join(str(book) for book in books))



def how_do_you_want_to_search():
    inputable_data = input('Вы хотите искать данные по имени издателя или по id?')
    if inputable_data == 'id':
        find_data_by_id()
    else:
        find_data_by_name()


how_do_you_want_to_search()

session.commit()

session.close()
