#coding=utf-8
import json
import math
import sys
from config import Config

from flask import Flask, jsonify, render_template, request

from mail import send_email
from models import MAIL_TEMPLATE, mail, SUB_TEMPLATE, db, Pools, db

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config.from_object(Config)
mail.init_app(app)
db.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/check_email/<email>/', methods=['GET', 'POST'])
def send_check_email(email):
    try:
        data = json.loads(request.data)
    except ValueError:
        data = request.form
    datatime = data.get('datatime', '')
    lastreading = float(data.get('lastreading', '0'))
    monthaverage = float(data.get('monthaverage', '0'))
    weekaverage = float(data.get('weekaverage', '0'))
    roomname = data.get('roomname', '')
    userName = data.get('userName', '')
    if monthaverage < weekaverage:
        ave_less = monthaverage
        ave_more = weekaverage
    else:
        ave_more = monthaverage
        ave_less = weekaverage
    try:
        less_day = math.floor(lastreading / ave_more)
    except ZeroDivisionError, e:
        less_day = 0
    try:
        more_day = math.ceil(lastreading / ave_less)
    except ZeroDivisionError, e:
        more_day = 0
    html_body = MAIL_TEMPLATE.format(
        roomname, userName, lastreading, ave_less, ave_more, less_day, more_day, datatime
    )
    send_email(email, u'您的电量监控', html_body)
    return jsonify({'code': 0})

@app.route('/submit_email/<email>/', methods=['POST'])
def send_sub_email(email):
    data = json.loads(request.data)
    stu_id = data.get('id', None)
    room_id = data.get('room', None)
    if stu_id is None or room_id is None:
        return jsonify({'code': -1})
    pool = Pools(
        stu_id=stu_id, room_id=room_id, email=email
    )
    db.session.add(pool)
    db.session.commit()
    send_email(email, u'添加监控成功', SUB_TEMPLATE)
    return jsonify({'code': 0})

if __name__ == '__main__':
    app.run(debug=True)
