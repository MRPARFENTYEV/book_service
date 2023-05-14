import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class Publisher(Base):
    __tablename__ = "publisher"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50), unique=True)
    # books = relationship("Book", back_populates='publisher')
    def __str__(self):
        return f'{self.id}:{self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    id_publisher = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("publisher.id"))
    publisher = relationship(Publisher,backref="books")
    def __str__(self):
        return f"Название книги: \n{self.title}"

class Shop(Base):
    __tablename__ = "shop"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50), unique=True)

    def __str__(self):
        return f"Название магазина: {self.name}"


class Stock(Base):
    __tablename__ = "stock"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("book.id"))
    id_shop = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("shop.id"))
    count = sqlalchemy.Column(sqlalchemy.Integer)
    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="shops")

class Sale(Base):
    __tablename__ = "sale"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    price = sqlalchemy.Column(sqlalchemy.Float)
    date_sale = sqlalchemy.Column(sqlalchemy.Date)
    id_stock = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("stock.id"))
    count = sqlalchemy.Column(sqlalchemy.Integer)
    stock = relationship(Stock, backref="sales")
    def __str__(self):
        return f"Cтоимость покупки:{self.price}, дата покупки: {self.date_sale} "

def create_tables(engine):
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)

