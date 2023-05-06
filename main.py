import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import HOST, PORT, USER, PASSWORD, DATABASENAME, DSN
from models import create_tables, Publisher, Book, Shop, Stock, Sale

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# def insert_publisher(publisher,publisher_name=input('input name:')):
#     publisher = Publisher(name=publisher_name)
#     session.add(publisher)

publisher1 = Publisher(name="Ленинград")
book1 = Book(name="Капитанская дочка")
shop1 = Shop(name="Буквоед")
stock1 = Stock(count=99)
sale1 = Sale(price=600,date_sale='09-11-2022',count=1)

session.add(publisher1,book1,shop1,stock1,sale1)

session.commit()
# print(publisher1.id)
session.close()
