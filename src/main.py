from controller import ClientController
# -H <direccion_ip> -p <puerto> -n <nick> -c <comando> -a <argumento>"

def main():
    host = input("Ingrese la dirección del host: ")
    port = int(input("Ingrese la dirección del puerto: "))
    nickname = input("Ingrese su nick: ")

    print(host)
    print(port)
    print(nickname)
    ircc = ClientController()
    ircc.connect_to_server(host,port,nickname,False)
    
    while True:
        user_input = input()
        
    ircc.handle_user_input(command + ' ' + arg)
    # ircc.disconnect_from_server()

main()