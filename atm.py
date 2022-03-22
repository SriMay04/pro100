class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print("your balance is 50000")
    def withdrawal(self,amount):
        new_amount=50000-amount
        print("you have withdrawn amount"+str(amount)+".your remaining balance is"+str(new_amount))
def main():
    Card_number=input("insert your card number")
    pin_number=input("enter your pin number")
    new_user=Atm(Card_number,pin_number)
    print("choose your activity")
    print("1. balnce enquiry 2.withdrawel")
    activity=int(input("enter acivity number"))
    
    if (activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        new_user.withdrawal(amount)
    else:
        print("enter the valued number")

main()
    