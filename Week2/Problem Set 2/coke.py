def main():
    amount_due = 50 #default amount due
    print("Amount Due:", amount_due) #notifying user amount due

    while amount_due > 0:
        coin = int(input("Insert Coin: ")) #prompt for coin input
        if coin in [5, 10, 25]:
            amount_due -= coin
            if amount_due > 0:
                print("Amount Due:", amount_due)
        else:
            print("Amount Due:", amount_due)
            continue

    if amount_due < 0:
        print("Change Owed:", abs(amount_due))
    else:
        print("Change Owed: 0")

main()
