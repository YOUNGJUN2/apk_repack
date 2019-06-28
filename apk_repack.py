from subprocess import run
from sys import argv

file = argv[1]

apkTool = "C:\\APKTOOL\\"
signApk = "C:\\Users\\cortk\\Desktop\\SignApk\\"

run("java -jar %sapktool.jar b %s -o %s.apk" % (apkTool, file, file))
run("java -jar %ssignapk.jar %scertificate.pem %skey.pk8 %s.apk %s_sined.apk" % (signApk, signApk, signApk, file, file))
run("adb install %s_sined.apk" % (file))
