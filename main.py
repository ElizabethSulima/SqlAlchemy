import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base
from models import create_tables, Publisher, Book, Stock, Sale, Shop

login = 'postgres'
password = ''
db_name = 'book_list_db'

Base = declarative_base()

DSN = f"postgresql://{login}:{password}@localhost:5432/{db_name}"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

pub_1 = Publisher(name="O\u2019Reilly")
pub_2 = Publisher(name="Pearson")
pub_3 = Publisher(name="Microsoft Press")
pub_4 = Publisher(name="No starch press")

session.add_all([pub_1, pub_2, pub_3, pub_4])
session.commit()

book_1 = Book(title="Programming Python, 4th Edition", id_publisher=1)
book_2 = Book(title="Learning Python, 4th Edition", id_publisher=1)
book_3 = Book(title="Natural Language Processing with Python", id_publisher=1)
book_4 = Book(title="Hacking: The Art of Exploitation", id_publisher=4)
book_5 = Book(title="Modern Operating Systems", id_publisher=2)
book_6 = Book(title="Code Complete: Second Edition", id_publisher=3)

session.add_all([book_1, book_2, book_3, book_4, book_5, book_6])
session.commit()

shop_1 = Shop(name="Labirint")
shop_2 = Shop(name="OZON")
shop_3 = Shop(name="Amazon")

session.add_all([shop_1, shop_2, shop_3])
session.commit()

stock_1 = Stock(id_shop=1, id_book=1, count=34)
stock_2 = Stock(id_shop=1, id_book=2, count=30)
stock_3 = Stock(id_shop=1, id_book=3, count=0)
stock_4 = Stock(id_shop=2, id_book=5, count=40)
stock_5 = Stock(id_shop=2, id_book=6, count=50)
stock_6 = Stock(id_shop=3, id_book=4, count=10)
stock_7 = Stock(id_shop=3, id_book=6, count=10)
stock_8 = Stock(id_shop=2, id_book=1, count=10)
stock_9 = Stock(id_shop=3, id_book=1, count=10)

session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7, stock_8, stock_9])
session.commit()

sale_1 = Sale(price="50.05", data_sale="2018-10-25T09:45:24.552Z", count=16, id_stock=1)
sale_2 = Sale(price="50.05", data_sale="2018-10-25T09:51:04.113Z", count=10, id_stock=3)
sale_3 = Sale(price="10.50", data_sale="2018-10-25T09:52:22.194Z", count=9, id_stock=6)
sale_4 = Sale(price="16.00", data_sale="2018-10-25T10:59:56.230Z", count=5, id_stock=5)
sale_5 = Sale(price="16.00", data_sale="2018-10-25T10:59:56.230Z", count=5, id_stock=9)
sale_6 = Sale(price="16.00", data_sale="2018-10-25T10:59:56.230Z", count=1, id_stock=4)

session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5, sale_6])
session.commit()

def publisher_list():
    publisher_name = str(input("Введите имя издателя: "))
    q = session.query(Publisher).join(Book.publisher).filter(Publisher.name == publisher_name)
    # print(q)
        #     print(f"{Book.title} | {Shop.name} | {Sale.price} | {Sale.data_sale}")

publisher_list()