from controller import ClientController
# -H <direccion_ip> -p <puerto> -n <nick> -c <comando> -a <argumento>"

test_input = input().replace('"','').split(' ')
print(test_input)
host,port,nickname,command,arg = test_input[1],int(test_input[3]),test_input[5],test_input[7],test_input[9]

ircc = ClientController()
ircc.connect_to_server(host,port,nickname,False)
ircc.handle_user_input(command + ' ' + arg)
# ircc.disconnect_from_server()