import os


def dumpUiXMl():
    path = os.getcwd() + "\\dump\\1.xml"
    os.system("adb shell /system/bin/uiautomator dump")
    os.system("adb pull /sdcard/window_dump.xml " + path)


def str():
    out = os.popen("adb shell dumpsys activity com.duorong.smarttool").read()
    print(out[out.find("ACTIVITY") + 8:out.find("pid") - 8].strip())



def screenshot():
    os.popen("adb shell screencap -p /sdcard/01.png")
    # os.system("adb pull /sdcard/01.png G:\\testTask\sprint04-android\截图\\1.png")
dumpUiXMl()
