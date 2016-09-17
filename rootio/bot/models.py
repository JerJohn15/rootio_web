# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from coaster.sqlalchemy import BaseMixin, IdMixin
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy_utils import JSONType

from ..utils import STRING_LEN
from ..extensions import db


class ChatBotCmd(IdMixin, db.Model):
    __tablename__ = u'chatbotcodes'

    code = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    answer = db.Column(db.String(500), nullable=False)

    @classmethod
    def answerTocode(cls, code):
        return cls.query.filter(ChatBotCmd.code == code).first()

    @classmethod
    def answerTohelp(cls):
        return cls.query.all()
