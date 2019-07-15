import xml.etree.ElementTree as ET


def parseXml():
    tree = ET.parse('H:\\code\\apitest\\report\\report.xml')
    testcase = tree.getiterator("testcase")
    failure = tree.getiterator("failure")
    testsuite = tree.getiterator("testsuite")
    failList = []
    passList = []
    for child in failure:
        failList.append(child.text)

    for child in testcase:
        passList.append(child.attrib["name"])

    xmlJson = {"errors": testsuite[0].attrib["errors"], "failures": testsuite[0].attrib["failures"],
               "tests": testsuite[0].attrib["tests"], "time": testsuite[0].attrib["time"], "failLog": failList,
               "passList": passList}
    return xmlJson


# print(parseXml()["tests"])