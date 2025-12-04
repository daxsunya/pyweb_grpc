from sqlalchemy.orm import Session
import models


def get_terms(db: Session):
    return db.query(models.Term).all()


def get_term_by_keyword(db: Session, keyword: str):
    return db.query(models.Term).filter(
        models.Term.keyword == keyword
    ).first()


def create_term(db: Session, keyword: str, description: str):
    db_term = models.Term(
        keyword=keyword,
        description=description,
    )
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term


def update_term(db: Session, db_term: models.Term, description: str):
    db_term.description = description
    db.commit()
    db.refresh(db_term)
    return db_term


def delete_term(db: Session, db_term: models.Term):
    db.delete(db_term)
    db.commit()
    return True
