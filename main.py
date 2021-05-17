import socket
from playsound import playsound


server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'learndatasci'
token = 'oauth:n4n4rt5yjjm2n9mrvp0ioo54wiwrst'
channel = '#scratch_lol'

sock = socket.socket()

try:
    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    resp = sock.recv(2048).decode('utf-8')
    print("Creation socket reussie")
except:
    print("Erreur debut socket")

while 1:
    try :
        resp = sock.recv(2048).decode('utf-8')
        envoyeur = resp.split('!', 1)
        pseudo = envoyeur[0].split(':', 1)
        x = resp.split("#", 1)
        try:
            message = x[1].split(":", 1)
            #print(pseudo[1] + " : " + message[1])
            fichier = open("Commandes.txt")
            for x in fichier:
                commande = x.split(';')
                if message[1].startswith(commande[0]) :
                    reponse = "PRIVMSG " + channel + " :" + commande[1].replace('{pseudo}',pseudo[1]) + "\r\n"
                    sock.send(reponse.encode('ISO-8859-1'))
                    break
            fichier.close()
            fichier = open('CommandesAudio.txt')
            for x in fichier:
                if message[1].startswith('!' + x.strip()):
                    soundfile = x.strip() + '.wav'
                    playsound(soundfile)
                    break
            fichier.close()
        except :
            print("Erreur")
            try:
                sock.close()
                sock = socket.socket()
                sock.connect((server, port))
                sock.send(f"PASS {token}\n".encode('utf-8'))
                sock.send(f"NICK {nickname}\n".encode('utf-8'))
                sock.send(f"JOIN {channel}\n".encode('utf-8'))
                resp = sock.recv(2048).decode('utf-8')
            except:
                print("Erreur Correction de bug 1")
    except :
        try :
            sock.close()
            sock = socket.socket()
            sock.connect((server, port))
            sock.send(f"PASS {token}\n".encode('utf-8'))
            sock.send(f"NICK {nickname}\n".encode('utf-8'))
            sock.send(f"JOIN {channel}\n".encode('utf-8'))
            resp = sock.recv(2048).decode('utf-8')
        except :
            print("Erreur Correction de bug 2")
