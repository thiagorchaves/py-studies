import paramiko

client = paramiko.client.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#  Conexão
client.connect('127.0.0.1', username= "", password="")

# Executando comandos

stdin,stdout,stderr = client.exec_command('ls -la')

if stdout.channel.recv_exit_status() ==0:
    print(stdout.read().decode("utf-8"))
else:
    print(stderr.read().decode("utf-8"))

# Executando comandos com input

stdin,stdout,stderr = client.exec_command('read variavel \n echo $variavel')

stdin.write("Valor da variavel\n")
stdin.flush()

print(stdout.read().decode("utf-8"))