#coding=utf-8
from flask_mail import Mail
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
db = SQLAlchemy()

class Pools(db.Model):
    __tablename__ = 'pools'
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(16)) # 学号
    email = db.Column(db.String(128)) # 邮箱
    room_id = db.Column(db.String(16)) # 房间号
    date_time = db.Column(db.DateTime(), default=datetime.now) # 添加日期

MAIL_TEMPLATE = '''
<table ngcontent-c0="" class="table table-hover table-bordered" style=" box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; width: 523px; max-width: 100%; margin-bottom: 0px; border: 1px solid rgb(221, 221, 221); color: rgb(51, 51, 51) ; ; ; ; ">
    <tbody ngcontent-c0="" style="box-sizing: border-box;">
        <tr ngcontent-c0="" class="" style="box-sizing: border-box;">
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">房间</td>
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">
                <span ngcontent-c0="" style="box-sizing: border-box; font-weight: 700;">{}</span>
            </td>
        </tr>
        <tr ngcontent-c0="" class="" style="box-sizing: border-box;">
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">姓名</td>
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">{}</td>
        </tr>
        <tr ngcontent-c0="" class="" style="box-sizing: border-box;">
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">余量</td>
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">
                <span ngcontent-c0="" class="label label-success" style="box-sizing: border-box; display: inline; padding: 0.2em 0.6em 0.3em; font-size: 12px; font-weight: 700; line-height: 1; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25em; background-color: rgb(92, 184, 92);">{} kW·h</span>
            </td>
        </tr>
        <tr ngcontent-c0="" class="" style="box-sizing: border-box;">
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">日均用电</td>
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">
                <span ngcontent-c0="" style="box-sizing: border-box; font-weight: 700;">{}~{}</span>&nbsp;kW·h</td>
        </tr>
        <tr ngcontent-c0="" class="" style="box-sizing: border-box;">
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">预计可使用</td>
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">
                <span ngcontent-c0="" style="box-sizing: border-box; font-weight: 700;">{}~{}</span>&nbsp;天</td>
        </tr>
        <tr ngcontent-c0="" class="" style="box-sizing: border-box;">
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">更新时间</td>
            <td ngcontent-c0="" style="box-sizing: border-box; padding: 8px; line-height: 1.42857; vertical-align: top; border: 1px solid rgb(221, 221, 221);">
                <span style="border-bottom:1px dashed #ccc;" t="5" times=" 20:32">{}</span></td>
        </tr>
    </tbody>
</table>
'''

SUB_TEMPLATE = '''
<div _ngcontent-c0="" class="alert alert-info alert-dismissible" role="alert">在您宿舍剩余电量可用不足7天时会向您发送提醒邮件</div>
'''
