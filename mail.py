#coding=utf-8
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from models import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, html_body):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.html = html_body
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr