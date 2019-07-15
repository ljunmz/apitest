from utils.dbUitls import MysqlHelper

mh = MysqlHelper('47.112.0.183', 'planadmin', 'pL%5^an3a$4in', 'thirdparty')

def findVCodeByDevice(params):
    sql = "SELECT * FROM verification_code where device_model=%s"
    return mh.find(sql, params)

def findVCodeByPhone(params):
    sql = "SELECT * FROM verification_code where mobile=%s order by created desc limit 1"
    return mh.find(sql, params)


def delVCodeByDevice(params):
    sql = "DELETE FROM verification_code WHERE device_model=%s"
    return mh.cud(sql, params)

def delVCodeByPhone(params):
    sql = "DELETE FROM verification_code WHERE mobile=%s"
    return mh.cud(sql, params)

# print(findVCodeByPhone('14827327046')[0][5])
# print(findVCodeByDevice("iphone 7"))

# delVCodeByDevice("Meizu-16th Plus")
# delVCodeByDevice("Meizu-16th")
# delVCodeByDevice("iphone 7")

