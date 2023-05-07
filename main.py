import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import HOST, PORT, USER, PASSWORD, DATABASENAME, DSN
from models import create_tables, Publisher, Book, Shop, Stock, Sale

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


publisher2 = Publisher(name="Maker up")
book1 = Book(title="Руслан и Людмила",publisher=publisher2)
shop1 = Shop(name="Буквоед")
stock1 = Stock(count= 500,book = book1, shop = shop1)
sale1 = Sale(price= 500,date_sale='08-11-2022',stock= stock1,count=1)



session.add(publisher2)
session.add(book1)
session.add(shop1)
session.add(stock1)
session.add(sale1)

session.commit()

session.close()
