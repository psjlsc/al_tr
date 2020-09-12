name = 'test1'
email = 'test2'
addr = 'test3'

def print_business_card(name, email, addr):
    print("-------------------")
    print('name: {}'.format(name))
    print('E-mail: {}'.format(email))
    print('office address: {}'.format(addr))
    print("-------------------")


print_business_card(name, email, addr)

def print_business_card_2(name, email, addr):
    print("-------------------")
    print("name: %s" %name)
    print("email: %s" %email)
    print("office address: %s" %addr)
    print("-------------------")

print_business_card_2(name, email, addr)