import socket as so

s = so.socket()
print("Socket created!!")

s.bind(('localhost',9999))

s.listen(8)
print("Waiting for connections.....")

while True:
    c, addr = s.accept()

    hello = "hello please enter your name:  "
    s.send(bytes(hello,'utf-8'))

    name = c.recv(1024)
    print(f"connected to {addr} ({name.decode()})")

    mess = 'Welcome to the first server where u can chat !!'.encode()
    c.send(mess)

    chat_permission_mess = "would u like to chat with us ??"
    c.send(bytes(chat_permission_mess,'utf-8'))

    chat_permission = c.recv(1024)
    print(chat_permission.decode())
    print("-----------||-------------")

    if chat_permission.decode() == 'yes':
        trigger = 'yes'
        c.send(bytes(trigger,'utf-8'))
    elif chat_permission.decode() == 'no':
        trigger = 'no'
        c.send(bytes(trigger,'utf-8'))
        continue
    else:
        continue

    while True:
        text_c = c.recv(1024)
        if text_c.decode() == 'exit':
            print('Chat session closed by the client')
            break
        else:
            print(text_c.decode())

            text_s = input("--->   ")
            if text_s == 'exit':
                c.send(bytes(text_s, 'utf-8'))
                break
            c.send(bytes(text_s, 'utf-8'))

    c.close()