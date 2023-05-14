import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import DSN
from models import create_tables, Publisher, Book, Shop, Stock, Sale

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

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
