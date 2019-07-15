from model.userDao import findUserIdByPhone
from tools.commonApi import bulkRegist, login, batchadd
from utils.content import devicesAndroid, devicesIOS

'''UserId查询'''
def test_userId():
    moblie = "13610150696"
    print(str(findUserIdByPhone(moblie)))

'''批量注册'''
def test_bulkRegist():
    count = 5
    shoreCode = 'gBlPTM'
    bulkRegist(count, shoreCode)

'''日程添加'''
def test_batchadd():
    mobile = '13300010008'
    count = 66
    year = '2019'
    month = '07'
    day = '03'
    time = '1834'
    header = {"token": login(mobile, "123456", devicesAndroid)["token"]}
    print(batchadd(count, year + month + day + time + '00', header))

