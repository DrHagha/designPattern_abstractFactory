from client.clientCode import client_code
from factory.concreateFactory1 import ConcreateFactory1
from factory.concreateFactory2 import ConcreateFactory2


print("Client: Testing client code with the first factory type:")
client_code(ConcreateFactory1())

print("\n")

print("Client: Testing the same client code with the second factory type:")
client_code(ConcreateFactory2())