from account import Account

def transfer_money(a1, a2):
    successful = a1.transferTo(5, a2)

    if successful:
        print('Successful')
    else:
        print('Unsuccessful')

    print("%s has $%d") %(a1.getOwner(), a1.getBalance())
    print("%s has $%d") %(a2.getOwner(), a2.getBalance())

if __name__ == "__main__":
    a1 = Account('Jane')
    a2 = Account('John')

    a1.deposit(100)
    a2.deposit(20)

    transfer_money(a1, a2)
