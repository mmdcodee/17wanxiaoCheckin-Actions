import time
import datetime
import json
import requests


check_url = "https://reportedh5.test01.com/sass/api/epmpics"

text = input()
deptId = eval(input())
address = input()
addtext = input()
code = input()
stuNum = input()
userName = input()
phoneNum = input()
userId = input()
emergency = input()
emergencyPhone = input()
sckey = input()


area = {'address': address, 'text': addtext, 'code': code}

areaStr = json.dumps(area, ensure_ascii=False)

jsons = {"businessType": "epmpics", "method": "submitUpInfo",
        "jsonData": {"deptStr": {"deptid": deptId, "text": text},
                     "areaStr": areaStr,
                     "reportdate": round(time.time()*1000), "customerid": "786", "deptid": deptId, "source": "alipay",
                     "templateid": "pneumonia", "stuNo": stuNum, "username": userName, "phonenum": phoneNum,
                     "userid": userId, "updatainfo": [{"propertyname": "bodyzk", "value": "36.5"},
                                                          {"propertyname": "istouchcb", "value": "自己家中"},
                                                          {"propertyname": "sfwz2", "value": "内地学生"},
                                                          {"propertyname": "symptom", "value": "无"},
                                                          {"propertyname": "homehealth", "value": "无"},
                                                          {"propertyname": "isConfirmed", "value": "无"},
                                                          {"propertyname": "ownbodyzk", "value": "良好"},
                                                          {"propertyname": "ishborwh", "value": "无"},
                                                          {"propertyname": "outdoor", "value": "绿色"},
                                                          {"propertyname": "isContactFriendIn14", "value": "没有"},
                                                          {"propertyname": "ownPhone", "value": phoneNum},
                                                          {"propertyname": "emergencyContact", "value": emergency},
                                                          {"propertyname": "mergencyPeoplePhone",
                                                           "value": emergencyPhone}], "gpsType": 0}}

response = requests.post(check_url, json=jsons)
res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)


SCKEY = sckey

now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00','%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days

test_day=datetime.datetime.strptime('2020-09-15 00:00:00','%Y-%m-%d %H:%M:%S')
date2 =(test_day - bj_time).days
desp = f"""
------
### 打卡时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
```
{res}
```
### 开学倒计时（盲猜9月15？）:
```
{date2}天
```

### 考研倒计时:
```
{date}天
```
### 加油！！！！！

"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"每日完美校园自动健康打卡",
    "desp": desp
}
    
# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
        print("Server酱推送服务成功")
else:
        print("Something Wrong")
