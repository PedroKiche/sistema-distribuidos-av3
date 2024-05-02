# saved as greeting-client.py
import Pyro5.api

name = input("mensagem")

node = Pyro5.api.Proxy("PYRONAME:lider")    # use name server object lookup uri shortcut
print(node.set_data(name))