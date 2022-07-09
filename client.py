import socket as so

c = so.socket()

c.connect(('13.233.174.49',7777))

hello = c.recv(1024).decode()
print(hello)

name = input("--->  ")
c.send(bytes(name,'utf-8'))

mess = c.recv(1024).decode()
print(mess)

chat_permission_mess = c.recv(1024).decode()
print(chat_permission_mess)

chat_permission = input("yes or no --->  ")

if chat_permission == 'yes' or chat_permission == 'no':
    c.send(bytes(chat_permission,'utf-8'))
    trigger = c.recv(1024)
    if trigger.decode() == 'yes':
        while True:
            text_c = input('--->  ')
            if text_c == 'exit':
                c.send(bytes(text_c, 'utf-8'))
                break
            c.send(bytes(text_c,'utf-8'))

            text_s = c.recv(1024)

            if text_s.decode() == 'exit':
                print('Chat session closed by the server')
                break
            else:
                print(text_s.decode())
    elif trigger.decode() == 'no':
        print('Thank u for connecting to our server please visit again!')

else:
    print("Invalid option")