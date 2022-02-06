import subprocess

from netmiko import ConnectHandler as ch


def Username():
    Position_Counter = 0
    Result = subprocess.getoutput("whoami")
    for words in Result:
        if words == "\\":
            Position = Position_Counter
            break
        Position_Counter += 1
    return Result[Position + 1:]

Local_Computer_Username = Username()
print(Local_Computer_Username)

Network_Device = {
    "host": 'ip_address',
    "username": "cisco",
    "password": "bigdaddy",
    "device_type": "cisco_ios",
    "secret": "cisco1",
}

Connect = ch(**Network_Device)
Connect.enable()

command_1 = "sh env all"
command_1_output = Connect.send_command(command_1)

folder = "C:\\Users\\userd\\OneDrive\\Desktop\\Python-Tests\\output.txt"
with open(folder, "w") as f:
    f.write("device_name" + command_1)
    f.write("\n")
    f.write(Connect.send_command(command_1))
    f.write("\n")
    f.write("\nEnd of File")
    
print(command_1_output)
print('\n')
print('Completed')
