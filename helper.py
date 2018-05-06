import subprocess

msg = 'from python'

print (subprocess.check_output('git init', shell=True))

print (subprocess.check_output('git commit -a -m msg', shell=True))
print (subprocess.check_output('git push origin master', shell=True))
