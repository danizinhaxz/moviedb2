import uuid
from tokenize import String

from sqlalchemy import Column, Uuid, String, Integer, Boolean, Text, DECIMAL

from moviedb.models.mixins import BasicRepositoryMixin
from moviedb import db

class Filme(db.Model, BasicRepositoryMixin):
    __tablename__ = 'Filmes'
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo_original = Column(String(256), nullable=False)
    titulo_nacional = Column(String(256), nullable=True)
    ano_lancamento = Column(Integer, nullable=False, default=0)
    lancado = Column(Boolean, nullable=False, default=False)
    duracao = Column(Integer, nullable=True, default=0)
    sinopse = Column(Text, nullable=True)
    orcamento = Column(DECIMAL(precision=2), nullable=True)
    faturamento_lancamento = Column(DECIMAL(precision=2), nullable=True)
    poster_principal = Column(Text, nullable=True)
    link_trailer = Column(String(256), nullable=True)

