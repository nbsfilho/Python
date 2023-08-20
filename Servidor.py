# Programa Socket Servidor
# Programador: Nilton Barbosa Santos Filho
# Ver. : 2.01
# 09/08/2023
# Prof.: Messias
# Matyeira: Redes de Computadores

import socket # biblioteca para uso das funçoes do socket

def main():
    endereco_servidor = ('192.168.0.110', 9876) # endereço IP do servidor
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET (IPV4), SOCK_DGRAN (Protocolo UTP),SOCK_STREAM (TCP)  
    socket_servidor.bind(endereco_servidor) # Deixa a porta no aguardo de menssagem do cliente
    
    print(f"\n Servidor esperando mensagens na porta {endereco_servidor[1]}...") # menssagem de espera
    
    while True: # loop infinito para aguardar menssagens
        dados, endereco_cliente = socket_servidor.recvfrom(1024) # Qunatidade de bytes da menssagem
        mensagem = dados.decode()
        print(f"\nMensagem recebida do cliente {endereco_cliente}: {mensagem}") # impressão da messagem junto com ip do cliente

if __name__ == "__main__":
    main()

