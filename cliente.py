# Programa Socket Cliente
# Programador: Nilton Barbosa Santos Filho
# Ver. : 2.01
# 09/08/2023
# Prof.: Messias
# Matyeira: Redes de Computadores


import socket # uso da biblioteca socket

endereco_servidor = ('192.168.0.110', 9876) # endereço do servidor
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET (IPV4), SOCK_DGRAN (Protocolo UTP),SOCK_STREAM (TCP)  

while True: #  Loop finito satisfazendo a condição FALSE
    mensagem = input("\n Digite a mensagem para enviar ao servidor (ou 'sair' para sair): ") # Se digitar "sair" encerra o loop
    if mensagem.lower() == 'sair':
        break
        
    socket_cliente.sendto(mensagem.encode(), endereco_servidor) # Envia a mensssagem para a porta no endereço do servidor
    print(f"\n Mensagem enviada para o servidor: {mensagem}") # confirmação de envio de menssagem do seridor

socket_cliente.close() # fechamento da porta de envio



