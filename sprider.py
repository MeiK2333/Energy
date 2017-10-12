#coding=utf-8
import requests
import sqlite3
import json
import math

LIMIT_DAY = 7

class User(object):

    def __init__(self, stu_id, email, room_id):
        self.stu_id = stu_id
        self.email = email
        self.room_id = room_id
        print stu_id, email, room_id

class Energy(object):

    query_url = 'http://api.dogest.cn/grade/energy/query?id={}&room={}'
    submit_url = 'http://127.0.0.1:5000/check_email/{}/'

    def __init__(self, user):
        self.user = user
        self.data = json.loads(requests.get(self.query_url.format(user.stu_id, user.room_id)).text)['data']
        self.less_day = math.floor(self.data['lastreading'] / (self.data['weekaverage'] if self.data['weekaverage'] > self.data['monthaverage'] else self.data['monthaverage']))

    def sub_mail(self):
        rst = json.loads(requests.post(self.submit_url.format(self.user.email), data=self.data).text)
        print 'submit mail to {}'.format(self.user.email)
        f = open('mail.log', 'a')
        f.write('submit mail to {}\n'.format(self.user.email))
        f.close()

def main():
    conn = sqlite3.connect('energy.db')
    c = conn.cursor()
    cursor = c.execute("SELECT stu_id, email, room_id from pools")
    for row in cursor:
        u = User(row[0], row[1], row[2])
        e = Energy(u)
        if e.less_day <= LIMIT_DAY:
            e.sub_mail()
    conn.close()

if __name__ == '__main__':
    main()
