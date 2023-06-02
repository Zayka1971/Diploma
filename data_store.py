import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from config import db_url_object

metadata = MetaData()
Base = declarative_base()


class Viewed(Base):
    __tablename__ = "vk_views"

    profile_id = sq.Column(sq.Integer, primary_key=True)
    viewed_id = sq.Column(sq.Integer, unique=True)

    engine = create_engine(db_url_object)


def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    to_bd = Viewed(profile_id='', viewed_id='')
    session.add(to_bd)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
    ##from_bd = session.quaery(Viewed).filter(Viewed.profile_id == 123).all()
