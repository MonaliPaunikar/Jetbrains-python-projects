import sqlite3
import random


class Banking:

    def __init__(self):
        self.card_number = None
        self.pin_number = None
        self.balance = None
        self.conn = sqlite3.connect('bank.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS card (
            id INTEGER,
            number TEXT UNIQUE,
            pin TEXT,
            balance INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    @staticmethod
    def menu():
        print()
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')

    def create_account(self):
        while True:
            card_test = random.randint(400000000000000, 400000999999999)
            final_check = self.luhn_check(card_test)
            self.cur.execute("SELECT number FROM card WHERE number = (?)", (final_check,))
            self.conn.commit()
            collected_card = self.cur.fetchall()
            if len(collected_card) == 0:
                self.card_number = final_check
                self.pin_number = str(random.randint(0000, 9999))
                while len(self.pin_number) < 4:
                    self.pin_number = '0' + self.pin_number
                self.cur.execute("INSERT INTO card (number, pin) VALUES (?,?)", (self.card_number, self.pin_number))
                self.conn.commit()
                break
        print('Your card has been created')
        print('Your card number:')
        print(self.card_number)
        print('Your card PIN:')
        print(self.pin_number)

    @staticmethod
    def luhn_check(test_card):
        check_point = (str(test_card))[0:15]
        check_list = [int(i) for i in check_point]
        check_number = 0
        for number in range(0, 15, 2):
            check_list[number] = check_list[number] * 2
        for number in range(15):
            if check_list[number] > 9:
                check_list[number] = check_list[number] - 9
            check_number += check_list[number]
        for x in range(10):
            if (check_number + x) % 10 == 0:
                card_number = check_point + str(x)
                if len(str(test_card)) == 15:
                    return card_number
                else:
                    if card_number == str(test_card):
                        return True
        return False

    def log_account(self):
        print('Enter your card number:')
        self.card_number = input()
        print('Enter your PIN:')
        self.pin_number = input()
        self.cur.execute("SELECT pin FROM card WHERE number = (?) AND pin = (?)", (self.card_number, self.pin_number))
        data = self.cur.fetchall()
        self.conn.commit()
        if len(data) > 0:
            print('You have successfully logged in!')
            self.logged(self.card_number)
        else:
            print('Wrong card number or PIN!')

    @staticmethod
    def logged_menu():
        print()
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')

    def get_balance(self, card_number):
        self.cur.execute("SELECT balance FROM card WHERE number = (?)", (card_number,))
        data = self.cur.fetchall()
        self.conn.commit()
        balance = data[0][0]
        return balance

    def add_income(self, card_number, amount):
        balance = self.get_balance(card_number)
        self.balance = balance + amount
        self.cur.execute("UPDATE card SET balance = (?) WHERE number = (?)", (self.balance, card_number))
        self.conn.commit()

    def subtract_income(self, card_number, amount):
        balance = self.get_balance(card_number)
        self.balance = balance - amount
        self.cur.execute("UPDATE card SET balance = (?) WHERE number = (?)", (self.balance, card_number))
        self.conn.commit()

    def check_card(self, card_number):
        self.cur.execute("SELECT number FROM card WHERE number = (?)", (card_number,))
        data = self.cur.fetchall()
        if len(data) > 0:
            return True
        else:
            return False

    def transfer(self, user_card):
        print('Transfer')
        print('Enter card number:')
        sender_card = input()
        if user_card == sender_card:
            print("You can't transfer money to the same account!")
        elif self.luhn_check(sender_card) is not True:
            print("Probably you made a mistake in the card number. Please try again!")
        elif self.check_card(sender_card) is False:
            print("Such a card does not exist.")
        else:
            print("Enter how much money you want to transfer:")
            amount = float(input())
            balance = self.get_balance(user_card)
            if amount > balance:
                print("Not enough money!")
            else:
                self.subtract_income(user_card, amount)
                self.add_income(sender_card, amount)
                print("Success!")

    def close_account(self, card_number):
        self.cur.execute("DELETE FROM card WHERE number = (?)", (card_number,))
        self.conn.commit()

    def logged(self, card_number):
        while True:
            self.logged_menu()
            user_choice = input()
            print()

            if user_choice == '0':
                print('Bye!')
                self.conn.close()
                exit(1)

            elif user_choice == '1':
                # 1: Balance
                self.balance = self.get_balance(card_number)
                print(f'Balance: {self.balance}')

            elif user_choice == '2':
                # 2: Add income
                print('Enter income:')
                amount = float(input())
                self.add_income(card_number, amount)
                print('Income was added!')

            elif user_choice == '3':
                # 3: Do transfer
                self.transfer(card_number)

            elif user_choice == '4':
                # 4: close account
                self.close_account(card_number)
                print("The account has been closed!")

            elif user_choice == '5':
                print('You have successfully logged out!')
                break

            else:
                print("Incorrect choice!")

    def main(self):
        while True:
            self.menu()
            choice = input()
            print()
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.log_account()
            elif choice == '0':
                print('Bye!')
                self.conn.close()
                exit(1)
            else:
                print("Incorrect choice!")


bank_1 = Banking()
bank_1.main()
