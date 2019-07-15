from utils.dbUitls import MysqlHelper

mh = MysqlHelper('47.112.0.183', 'planadmin', 'pL%5^an3a$4in', 'user')


def findUserIdByPhone(params):
    sql = "SELECT * FROM user where mobile=%s"
    return mh.find(sql, params)[0][0]


def findUserIdLikePhone(params):
    sql = "SELECT * FROM user where mobile Like '%'+%s+'%'"
    return mh.find(sql, params)[0][0]


# print(findUserIdByPhone("13300001004"))
