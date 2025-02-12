from controller import ClientController
import sys
import time
# -H <direccion_ip> -p <puerto> -n <nick> -c <comando> -a <argumento>"

test_input = sys.argv[1:]
print(test_input)
host,port,nickname,command,arg = test_input[1],int(test_input[3]),test_input[5],test_input[7].split('/'),test_input[9]
command = '/' + command[len(command) -1 ]
print(command)
# exit()
ircc = ClientController()
ircc.connect_to_server(host,port,nickname,False)
ircc.handle_user_input(command + ' ' + arg)
time.sleep(10)
ircc.disconnect_from_server()



# Traceback (most recent call last):
#   File "/home/runner/work/computer_networks_fall_2024/computer_networks_fall_2024/src/main.py", line 10, in <module>
#     ircc.handle_user_input(command + ' ' + arg)
#   File "/home/runner/work/computer_networks_fall_2024/computer_networks_fall_2024/src/controller.py", line 42, in handle_user_input
#     self.handle_user_command(input)
#   File "/home/runner/work/computer_networks_fall_2024/computer_networks_fall_2024/src/controller.py", line 56, in handle_user_command
#     self.send_message(command_name + " " + command_args)
#   File "/home/runner/work/computer_networks_fall_2024/computer_networks_fall_2024/src/controller.py", line 65, in send_message
#     self.server_interface.send_message(message)
#   File "/home/runner/work/computer_networks_fall_2024/computer_networks_fall_2024/src/server_interface.py", line 38, in send_message
#     self.socket.send((message + "\r\n").encode('utf-8'))
# BrokenPipeError: [Errno 32] Broken pipe