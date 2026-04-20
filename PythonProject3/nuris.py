class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount}. Баланс: {self.balance}")
        else:
            print("Ошибка: сумма должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снято: -{amount}. Остаток: {self.balance}")
        else:
            print("Ошибка: недостаточно средств или неверная сумма")
    def get_info(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"


accounts = {}
current_account = None

while True:
    print(f"\n     МЕНЮ (Текущий счет: {current_account.owner if current_account else 'Не выбран'})")
    print("1. Создать новый счет")
    print("2. Выбрать счет (войти)")
    print("3. Пополнить")
    print("4. Снять")
    print("5. Показать баланс")
    print("6. Список всех счетов")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя владельца: ")
        if name in accounts:
            print("Ошибка: счет с таким именем уже существует")
        else:
            summa = float(input("Начальный баланс: "))
            accounts[name] = BankAccount(name, summa)
            print(f"Счет для {name} создан")

    elif choice == "2":
        name = input("Введите имя владельца: ")
        if name in accounts:
            current_account = accounts[name]
            print(f"Вы переключились на счет: {name}")
        else:
            print("Счет не найден")

    elif choice == "3":
        if current_account:
            val = float(input("Сумма пополнения: "))
            current_account.deposit(val)
        else:
            print("Сначала выберите счет (пункт 2)")

    elif choice == "4":
        if current_account:
            val = float(input("Сумма снятия: "))
            current_account.withdraw(val)
        else:
            print("Сначала выберите счет (пункт 2)")

    elif choice == "5":
        if current_account:
            print(current_account.get_info())
        else:
            print("Счет не выбран")

    elif choice == "6":
        if not accounts:
            print("Счетов еще нет")
        for acc in accounts.values():
            print(acc.get_info())

    elif choice == "0":
        break
    else:
        print("Неверный ввод")