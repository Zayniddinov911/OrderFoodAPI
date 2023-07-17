from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Here will be your local DB
engine = create_engine('postgresql://postgres:0020@localhost/OrderPizza', echo=True)

Base = declarative_base()

Session = sessionmaker()
