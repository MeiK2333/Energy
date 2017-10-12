#coding=utf-8
import os

basedir = os.path.abspath('./')

class Config:
    SECRET_KEY = 'QAQrz'

    MAIL_SERVER = 'pop.stumail.sdut.edu.cn'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '15110572023@stumail.sdut.edu.cn'
    MAIL_PASSWORD = 'xxxxxx'
    FLASKY_MAIL_SUBJECT_PREFIX = 'Energy'
    FLASKY_MAIL_SENDER = '15110572023@stumail.sdut.edu.cn'
    FLASKY_ADMIN = 'Energy'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'energy.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
