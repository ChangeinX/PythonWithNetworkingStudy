import subprocess

Computer_List = ['ip1', 'ip2', 'ip3', 'etc...']

for computer in Computer_List:
    subprocess.getoutput("shutdown -m \\\\" + computer + "-f -s -t 0")
