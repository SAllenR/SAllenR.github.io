import subprocess

print (subprocess.check_output('git init', shell=True))

print (subprocess.check_output('git commit -a -m "from python"', shell=True))
print (subprocess.check_output('git push origin master', shell=True))
