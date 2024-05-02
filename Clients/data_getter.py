# saved as greeting-client.py
import Pyro5.api

name = input("mensagem?")

greeting_maker = Pyro5.api.Proxy("PYRONAME:lider")    # use name server object lookup uri shortcut
print(greeting_maker.set_data(name))