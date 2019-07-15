import json
import time
from model.thirdparty import findVCodeByPhone, delVCodeByDevice
from utils.content import devicesAndroid
from utils.creatPhone import randomPhone
from utils.requestUitls import doRequest

"""登录账户获取token"""


def login(mobile, password, device):
    method = "POST"
    url = "http://47.112.0.183:8801/base/user/login"
    jsons = {"password": password, "mobile": mobile, "appType": "2", "type": "2", "device": device}
    header = {}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    return json_str["data"]


# print(login("13367339376","123456",devicesAndroid)["id"])


"""获取短信验证码"""


def sendSmsMessage(mobile, type, device):
    method = "POST"
    url = "http://47.112.0.183:8801/web/thirdparty/sendSmsMessage"
    jsons = {"productName": "时光序", "mobile": mobile, "type": type, "device": device}
    header = {}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    if json_str["msg"] == "短信验证码发送成功":
        code = findVCodeByPhone(mobile)[0][5]
        return code
    else:
        print("短信验证码发送失败:" + json_str["msg"])


"""获取账户token"""


def getToken(mobile, device):
    method = "POST"
    url = "http://47.112.0.183:8801/base/user/getToken"
    jsons = {"mobile": mobile, "device": device}
    header = {"token": login(mobile, "123456", device)["token"]}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    return json_str["data"]["token"]


"""短信提醒"""


def smsRemind(mobile):
    method = "POST"
    url = "http://47.112.0.183:8801/base/thirdparty/smsRemind"
    jsons = {"mobile": mobile, "content": "测试短信提醒"}
    # header = {"token": login(mobile, "123456", device)["token"]}
    header = {}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    return json_str["msg"]


"""电话提醒"""


def voiceRemind(mobile):
    method = "POST"
    url = "http://47.112.0.183:8801/base/thirdparty/voiceRemind"
    jsons = {"mobile": mobile, "content": "测试电话提醒"}
    # header = {"token": login(mobile, "123456", device)["token"]}
    header = {}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    return json_str["msg"]


"""日程添加接口"""


def batchadd(count, todoTime, header):
    todoList = []
    currentTime = time.strftime('20%y%m%d%H%M', time.localtime())
    for key in range(count):
        shortTitle = "自动创建本地日程" + str(key) + currentTime
        localID = "-1560343" + time.strftime('20%y%m%d%H%M', time.localtime())
        todoJson = {"duration": 0, "importance": 2, "intervalType": 1, "localId": localID, "todoClassifyId": 1001,
                    "todoTime": todoTime, "shortTitle": shortTitle,
                    "title": shortTitle, "aheadType": [{"offset": 0}]}
        todoList.append(todoJson)
    method = "POST"
    url = "http://47.112.0.183:8801/base/plan/schedule/batchadd"
    jsons = {"todos": todoList}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    return json_str["data"]


#
#
# header = {"token": login('13367339376', "123456", devicesAndroid)["token"]}
# print(batchadd(1, '2019' + '0626' + '2055' + '00', header))

"""日程编辑"""


def scheduleEdit(counts, headers):
    # batchTodoTime = str(int(time.strftime('20%y%m%d%H%M', time.localtime())))+'00'
    batchTodoTime = '20190620142500'
    dataJson = batchadd(1, batchTodoTime, headers)
    shortTitle = dataJson['todos'][0]['shortTitle']
    importance = dataJson['todos'][0]['importance']
    intervalType = dataJson['todos'][0]['ruleInfo'][0]['intervalType']
    id = dataJson['todos'][0]['id']
    todoClassifyId = dataJson['todos'][0]['todoClassifyId']
    aheadType = dataJson['todos'][0]['aheadType']

    todoTime = str(int(time.strftime('20%y%m%d%H%M', time.localtime())) + 5) + '00'

    sonAddList = []
    # todoList = []
    for i in range(counts):
        jsonList = {"localId": int('-15610' + todoTime + str(i)), "grade": i, "todoTime": todoTime,
                    "title": todoTime + "子任务0" + str(i)}
        sonAddList.append(jsonList)

    editJson = {"duration": 0, "importance": importance, "intervalType": intervalType, "localId": id,
                "id": id,
                "todoClassifyId": todoClassifyId, "shortTitle": shortTitle, "title": shortTitle,
                "todoTime": batchTodoTime,
                "address": "", "city": "", "country": "", "district": "", "latitude": "", "longitude": "",
                "province": "", "remark": "",
                "aheadType": aheadType, "attachments": [],
                "sonAddList": sonAddList}
    # todoList.append(editJson)
    method = "POST"
    url = "http://47.112.0.183:8801/base/plan/schedule/edit"
    jsons = editJson
    datas = {}
    r = doRequest(method, url, datas, jsons, headers)
    json_str = json.loads(r)
    return json_str["data"]


#
# print(scheduleEdit(5, header))

"""倒数日提醒接口"""


def getelements():
    method = "POST"
    url = "http://47.112.0.183:8801/base/countdown/schedule/getelements"
    jsons = {"expires": "2019-06-14T09:37:56.221Z", "size": 1}
    header = {"token": login("13300000009", "123456", devicesAndroid)["token"]}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    print(json_str)


"""日程删除到回收站"""


def delPlan():
    method = "POST"
    url = "http://47.112.0.183:8801/base/plan/delete"
    jsons = {
        "deleteInfos": [
            {
                "id": 7665126565784591364,
                "todoTimes": [
                    20190617171400
                ]
            }
        ]
    }
    header = {"token": login("15217163726", "123456", devicesAndroid)["token"]}
    datas = {}
    r = doRequest(method, url, datas, jsons, header)
    json_str = json.loads(r)
    print(json_str)


"""注册账号"""


def regist(mobile, shorecode):
    method = "POST"
    header = {}
    datas = {}

    sendMessageUrl = 'http://47.112.0.183:8801/web/thirdparty/sendSmsMessage'
    sendMessageJson = {'device': devicesAndroid, 'mobile': mobile, 'productName': '时光序', 'type': 3}

    """清除验证码记录"""
    delVCodeByDevice("Meizu-16th Plus")

    sendMessageRe = doRequest(method, sendMessageUrl, datas, sendMessageJson, header)
    json_sendMessage = json.loads(sendMessageRe)
    print(json_sendMessage['msg'])

    registUrl = 'http://47.112.0.183:8801/base/user/register'

    if json_sendMessage['msg'] == '短信验证码发送成功':
        time.sleep(3)
        code = findVCodeByPhone(mobile)[0][5]
        registJson = {'appType': '2', 'code': code, 'device': devicesAndroid, 'mobile': mobile, 'password': '123456',
                      'shareCode': shorecode, 'type': 3}
        registRe = doRequest(method, registUrl, datas, registJson, header)
        json_regist = json.loads(registRe)
        if json_regist['code'] == 200 and json_regist['msg'] == '操作成功':
            print('注册成功')
        else:
            print('注册失败')
    else:
        print('注册失败')


"""批量注册"""


def bulkRegist(counts, shoreCode):
    count = 1
    for key in range(counts):
        mobile = randomPhone()
        regist(mobile, shoreCode)
        count = key + count
    print(count)

# bulkRegist(20)

# delPlan()

# print(str(int(time.strftime('20%y%m%d%H%M%S', time.localtime())) + 500) + "00")

# getelements()
#
#
# print(time.strftime('20%y%m%d%H%M', time.localtime()))
# print(voiceRemind("13367339376"))

# print(sendSmsMessage("13300000005", 2, devicesAndroid))
# print(getToken("13300000000", devicesAndroid))
