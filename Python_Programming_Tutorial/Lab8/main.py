class PhoneBattery:
    def __init__(self) -> None:
        self.__percent = 100

    def use_battery(self, amount: float) -> None:
        self.__percent = max(0, self.__percent - amount)

    def charge_battery(self, amount: float) -> None:
        self.__percent = min(100, self.__percent + amount)

    def get_percent(self) -> float:
        return self.__percent


class BankAccount:
    def __init__(self, account_number: str, balance: float = 0) -> None:
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"ฝาก {amount} บัญชี {self.account_number} ยอด {self._balance}")
        else:
            print("จำนวนเงินต้องมากกว่า 0")

    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"ถอน {amount} บัญชี {self.account_number} ยอด {self._balance}")
        else:
            print("ยอดเงินไม่พอหรือจำนวนเงินไม่ถูกต้อง")

    def get_balance(self) -> float:
        return self._balance


class SavingsAccount(BankAccount):
    interest_rate = 0.015

    def __init__(self, account_number: str, balance: float = 0) -> None:
        super().__init__(account_number, balance)

    def add_interest(self) -> None:
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"เพิ่มดอกเบี้ย {interest:.2f} บัญชี {self.account_number}")


def test_phone_battery() -> None:
    print("=== ทดสอบ PhoneBattery ===")
    phone = PhoneBattery()
    print(f"แบตเตอรี่เริ่มต้น: {phone.get_percent()}%")

    phone.use_battery(30)
    print(f"ใช้แบตเตอรี่ 30% คงเหลือ: {phone.get_percent()}%")

    phone.use_battery(90)
    print(f"ใช้แบตเตอรี่ 90% คงเหลือ: {phone.get_percent()}%")

    phone.charge_battery(20)
    print(f"ชาร์จแบตเตอรี่ 20% คงเหลือ: {phone.get_percent()}%")

    phone.charge_battery(200)
    print(f"ชาร์จแบตเตอรี่ 200% คงเหลือ: {phone.get_percent()}%")


def test_savings_account() -> None:
    print("\n=== ทดสอบ SavingsAccount ===")
    account = SavingsAccount("123-456-789")
    account.deposit(10000)
    account.add_interest()
    account.withdraw(2000)
    print(f"ยอดเงินคงเหลือสุดท้าย: {account.get_balance()}")


def main() -> None:
    test_phone_battery()
    test_savings_account()


if __name__ == "__main__":
    main()
