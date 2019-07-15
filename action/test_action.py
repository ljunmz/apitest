import json

import pytest

from model.thirdparty import delVCodeByDevice
from tools.commonApi import *
from utils.excelUitls import getTestCase
from utils.requestUitls import doRequest


# 运行在每个方法之前
def setup_function():
    print()
    print('========================== Test Start ===========================')


# 运行在每个方法之后
def teardown_function():
    print('========================== Test End ===========================')
    print()


# 测试用例


# 手机号判断接口
@pytest.mark.parametrize('caseInfo', getTestCase("test_validateUserNewOrOld", 'apitest'))
def test_validateUserNewOrOld(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    print("请求参数" + caseInfo["json"])
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = json.loads(caseInfo["header"])
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 发送验证码接口（未登录）
@pytest.mark.parametrize('caseInfo', getTestCase("test_sendSmsMessage", 'apitest'))
def test_sendSmsMessage(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = json.loads(caseInfo["header"])
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """清除验证码记录"""
    delVCodeByDevice("Meizu-16th Plus")
    delVCodeByDevice("Meizu-16th")

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 登录接口
@pytest.mark.parametrize('caseInfo', getTestCase("test_login", 'apitest'))
def test_login(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = json.loads(caseInfo["header"])
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 退出接口
@pytest.mark.parametrize('caseInfo', getTestCase("test_logout", 'apitest'))
def test_logout(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 提交意见反馈接口
@pytest.mark.parametrize('caseInfo', getTestCase("test_addAdvice", 'apitest'))
def test_addAdvice(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# qq授权登录-未绑定手机号
@pytest.mark.parametrize('caseInfo', getTestCase("test_qqLogin", 'apitest'))
def test_qqLogin(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取用户信息
@pytest.mark.parametrize('caseInfo', getTestCase("test_getUserInfo", 'apitest'))
def test_getUserInfo(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取用户配置
@pytest.mark.parametrize('caseInfo', getTestCase("test_appConfig", 'apitest'))
def test_appConfig(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取用户习惯列表
@pytest.mark.parametrize('caseInfo', getTestCase("test_customList", 'apitest'))
def test_customList(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取分类列表
@pytest.mark.parametrize('caseInfo', getTestCase("test_multiClassify", 'apitest'))
def test_multiClassify(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取业务同步版本
@pytest.mark.parametrize('caseInfo', getTestCase("test_getBusinessSyncVersion", 'apitest'))
def test_getBusinessSyncVersion(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取龙猫未读
@pytest.mark.parametrize('caseInfo', getTestCase("test_totoroUnread", 'apitest'))
def test_totoroUnread(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 所有分类列表接口
@pytest.mark.parametrize('caseInfo', getTestCase("test_classifyListAll", 'apitest'))
def test_classifyListAll(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 传入日期获取当月或者当年的休息假期
@pytest.mark.parametrize('caseInfo', getTestCase("test_getCalendar", 'apitest'))
def test_getCalendar(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code


# 获取小程序列表
@pytest.mark.parametrize('caseInfo', getTestCase("test_indexAppletList", 'apitest'))
def test_indexAppletList(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {"token": login("13300000000", "123456", devicesAndroid)["token"]}
    method = caseInfo["method"]
    msg = caseInfo["msg"]
    code = caseInfo["code"]

    """接口请求"""
    r = doRequest(method, url, datas, jsons, header)
    print("接口返回值：" + r)
    re = json.loads(r)

    """结果校验"""
    assert re["msg"] == msg
    assert re["code"] == code
