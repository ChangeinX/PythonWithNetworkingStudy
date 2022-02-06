from netmiko import ConnectHandler as ch

Network_Device = {
    "host": 'ip_address',
    "username": "cisco",
    "password": "bigdaddy",
    "device_type": "cisco_ios",
    "secret": "cisco1",
}

Connect = ch(**Network_Device)

Connect.enable()

command_1 = "sh ip int gi 1/0"

port_range_1 = 10
port_range_2 = 20

for port in range(port_range_1, port_range_2 + 1):
    print(Connect.send_command(command_1 + str(port)))
