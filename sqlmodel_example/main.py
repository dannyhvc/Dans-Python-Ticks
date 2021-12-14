from typing import Optional
from sqlmodel import SQLModel, create_engine, Field
from sqlmodel.orm.session import Session
from sqlmodel.sql.expression import select

ENGINE = create_engine("sqlite:///database.db")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


def add_hero_s(*args):
    with Session(ENGINE) as session:
        for x in args:
            session.add(x)
        session.commit()


def get_all_heros():
    with Session(ENGINE) as session:
        hero = session.exec(select(Hero)).all()
        for h in hero:
            print(h)


def delete_all_heros():
    with Session(ENGINE) as session:
        hero = session.exec(select(Hero)).all()
        for h in hero:
            session.delete(
                session.exec(
                    select(Hero).where(Hero.id == h.id)
                ).one()
            )
            session.commit()


def main():
    SQLModel.metadata.create_all(ENGINE)  # start the engine

    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    #add_hero_s(hero_1, hero_2, hero_3)
    # get_all_heros()
    # delete_all_heros()


if __name__ == '__main__':
    main()
