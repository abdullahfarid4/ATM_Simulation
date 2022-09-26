
print("Welcome to the python ATM")
print("*" * 30)
balance = 5000
pin = 1234

def ATM_System(balance, pin):
    return balance, pin


def Deposit(balance, deposited_amount):
    new_balance = balance + deposited_amount
    print("Updated Balance is {}".format(balance))


def Withdraw(balance, withdrawn_amount):
    if withdrawn_amount < balance:
        balance -= withdrawn_amount
        print("Updated Balance is {}".format(balance))
    else:
        print("Your Balance isn't enough")

def Balance_Check():
    print("Your Balance is {}".format(balance))

def Deposit_Ar(balance, deposited_amount):
    balance += deposited_amount
    print("رصيدك الجديد هو {}".format(balance))

def Withdraw_Ar(balance, withdrawn_amount):
    if withdrawn_amount < balance:
        balance -= withdrawn_amount
        print("رصيدك الجديد هو {}".format(balance))
    else:
        print("رصيدك لا يكفي لسحب هذا الميلغ")
def Balance_Check_Ar(balance):
    print("رصيدك الحالي هو {}".format(balance))

# ---------------------------------------------------------------------
lang = str(input("Enter a language (English / العربية"))
if lang == "English":
    i = 5
    pin_entered = int(input("Enter Your Pin"))
    while i > 0:
        if pin_entered != pin:
            i = i - 1
            print("WRONG PIN_Re-enter:")
            if i == 0:
                print("Pin has been entered 5 times wrong__You are not allowed to use the ATM")
        elif pin_entered == pin:
            i = -1
        while True:
            print('''Choose a process:
        1) Deposit
        2) Withdraw
        3) Check Balance
        4) Exit
        ''')
            option = int(input("Enter an option"))
            if option == 1:
                deposited_amount = float(input("Enter the amount u wish to deposit."))
                Deposit(balance,deposited_amount)
            elif option == 2:
                withdrawn_amount = float(input("Enter the amount u wish to withdraw."))
                Withdraw(balance, withdrawn_amount)
            elif option == 3:
                Balance_Check()
            else:
                break
elif lang == "العربية":
    x = 5
    pin_entered = int(input("ادخل الرقم السري"))
    while x > 0:
        if pin_entered != pin:
            x = x - 1
            print("الرقم السري خاطئ _ حاول مرة أخرى")
            if x == 0:
                print("تم ادخال الرقم السري يشكل خاطئ خمس مرات غير مسموح لك باستخدام الصراف")
        elif pin_entered == pin:
            x = -1
        while True:
            print('''اخنر احد العمليات:
            1) إيداع
            2) سحب
            3) كشف عن الرصيد
            4) خروج
            ''')
            option = int(input("أدخل رقم العملية"))
            if option == 1:
                deposited_amount = float(input("أدخل المبلغ الذي تريد ايداعه"))
                Deposit_Ar(balance, deposited_amount)
            elif option == 2:
                withdrawn_amount = float(input("أدخل المبلغ الذي تريد سحبه"))
                Withdraw_Ar(balance, withdrawn_amount)
            elif option == 3:
                Balance_Check_Ar(balance)
            else:
                break

