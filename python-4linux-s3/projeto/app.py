import modulos.banco as banco
import threading

if __name__=='__main__':
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=banco.find_message)
        f.start()
    except Exception as e:
        print('Falha ao criar a thread: {}'.format(e))

    while f.is_alive:
        mens = input()
        banco.register_message(user, mens)
