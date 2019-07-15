import pytest

from model.thirdparty import delVCodeByDevice
from tools.commonApi import *
from utils.excelUitls import getTestCase
from utils.requestUitls import doRequest


# 运行在每个方法之前
def setup_function():
    print()
    print('========================== Test Start =========================')


# 运行在每个方法之后
def teardown_function():
    print('========================== Test End ===========================')
    print()


# 测试用例


# 手机号判断接口
@pytest.mark.parametrize('caseInfo', getTestCase("test_validateUserNewOrOld", 'baseUser'))
def test_validateUserNewOrOld(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    print("请求参数" + caseInfo["json"])
    url = 'http://47.112.0.183:8801' + caseInfo["url"]
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


# 添加每日一句收藏
@pytest.mark.parametrize('caseInfo', getTestCase("test_everydayMottoInsert", 'baseUser'))
def test_everydayMottoInsert(caseInfo):
    print()
    print("测试项：" + caseInfo["title"])
    print("请求参数：" + caseInfo["json"])

    """参数组装"""
    url = 'http://47.112.0.183:8801' + caseInfo["url"]
    datas = json.loads(caseInfo["data"])
    jsons = json.loads(caseInfo["json"])
    header = {'token': login("13367339376", "123456", devicesAndroid)["token"]}
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

