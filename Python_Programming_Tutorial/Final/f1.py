class Vehicle:
    """
    สร้าง abstract class ที่ทำหน้าที่เป็น super class ของ vehicle ทุกชนิด
    """

    def __init__(self, license_plate, brand, base_rate_per_day):
        self.license_plate = license_plate
        self.brand = brand
        self.base_rate_per_day = base_rate_per_day
        self.is_rented = False

    def rent_vehicle(self):
        """
        method สำหรับการเช่ารถ หากรถว่าง ให้เป็นสถานะเช่าแล้ว เเละเเสดงผล "ดำเนินการเรียบร้อย ทะเบียนรถ: {license_plate} ถูกเช่าแล้ว"
        หากรถถูกเช่าอยู่ ให้แสดงผล "ไม่สามารถดำเนินการได้ ทะเบียนรถ: {license_plate} ถูกเช่าอยู่"
        """
        if not self.is_rented:
            self.is_rented = True
            print(f"ดำเนินการเรียบร้อย ทะเบียนรถ: {self.license_plate} ถูกเช่าแล้ว")
        else:
            print(f"ไม่สามารถดำเนินการได้ ทะเบียนรถ: {self.license_plate} ถูกเช่าอยู่")

    def return_vehicle(self):
        """
        method สำหรับการคืนรถ หากรถถูกเช่าอยู่ ให้เป็นสถานะว่างเเละเเสดงผล "ดำเนินการเรียบร้อย ทะเบียนรถ: {license_plate} ถูกส่งคืน"
        """
        if self.is_rented:
            self.is_rented = False
            print(f"ดำเนินการเรียบร้อย ทะเบียนรถ: {self.license_plate} ถูกส่งคืน")
        else:
            print(f"ไม่สามารถดำเนินการได้ ทะเบียนรถ: {self.license_plate} ไม่ได้ถูกเช่า")

    def get_status(self):
        """
        method สำหรับการตรวจสอบสถานะของรถ เเสดงสถานะปัจจุบัน โดยเเสดงผล "สถานะปัจจุบัน: {status}" (ว่าง หรือ ถูกเช่า)
        """
        if self.is_rented:
            print("สถานะปัจจุบัน: ถูกเช่า")
        else:
            print("สถานะปัจจุบัน: ว่าง")

    def calculate_rental_fee(self, days):
        """
        abstract method สำหรับการคำนวณค่าธรรมเนียมการเช่ารถ
        """
        raise NotImplementedError("Subclass must implement this method")

    def display_detail(self):
        """
        abstract method สำหรับการแสดงรายละเอียดของรถ
        """
        raise NotImplementedError("Subclass must implement this method")


class Car(Vehicle):
    def __init__(self, license_plate, brand, base_rate_per_day, seat_capacity):
        super().__init__(license_plate, brand, base_rate_per_day)
        self.seat_capacity = seat_capacity

    def calculate_rental_fee(self, days):
        """เงื่อนไข ถ้ารถมีที่นั่งมากกว่า 5 ที่นั่ง คิดค่าบริการเพิ่ม 15% จากค่าเช่าพื้นฐาน เเละเเสดงผล "คำนวณ (รถขนาดใหญ่): [ค่าพื้นฐาน] (ราคาพื้นฐาน)+[ค่าบริการเพิ่ม] (ที่นั่ง>5)= [ยอดรวม] บาท" จากนั้นคืนค่า return ยอดรวมสุทธิ

        ถ้ารถมี 5 ที่นั่งหรือน้อยกว่า คิดค่าเช่าตามราคาพื้นฐาน เเละเเสดงผล "คำนวณ (ขนาดมาตรฐาน): [ค่าพื้นฐาน] บาท" จากนั้นคืนค่า return ยอดรวมสุทธิ
        """
        if self.seat_capacity > 5:
            total_fee = self.base_rate_per_day * days
            additional_fee = total_fee * 0.15
            print(
                f"คำนวณ (รถขนาดใหญ่): {total_fee} (ราคาพื้นฐาน)+{additional_fee} (ที่นั่ง>5)= {total_fee + additional_fee} บาท"
            )
            return total_fee + additional_fee
        else:
            total_fee = self.base_rate_per_day * days
            print(f"คำนวณ (ขนาดมาตรฐาน): {total_fee} บาท")
            return total_fee

    def display_detail(self):
        """เเสดงรายละเอียด โดยเเสดงผล "ทะเบียนรถ: {license_plate}, ยี่ห้อ: {brand}, ที่นั่ง: {seat_capacity}" """
        print(
            f"ทะเบียนรถ: {self.license_plate}, ยี่ห้อ: {self.brand}, ที่นั่ง: {self.seat_capacity}"
        )


def main():
    # 1
    print("---เเสดงข้อมูลรถในระบบ---")
    car1_large = Car("กข 1234", "Toyota", 1500, 7)
    # 2
    car2_small = Car("บบ 5678", "Honda", 1000, 4)

    # 3
    car1_large.display_detail()
    car1_large.get_status()
    car2_small.display_detail()
    car2_small.get_status()

    # 4
    print()
    print("---การเช่ารถ---")
    car1_large.rent_vehicle()
    car1_large.rent_vehicle()
    car1_large.get_status()

    # 5
    print()
    print("---คำนวณค่าเช่า---")
    print("คำนวณ กข 1234")
    fee1 = car1_large.calculate_rental_fee(3)

    # 6
    print("คำนวณ บบ 5678")
    fee2 = car2_small.calculate_rental_fee(3)
    total_fee = fee1 + fee2

    # 7
    print(f"ค่าธรรมเนียมรวมทั้งหมด: {total_fee} บาท")


if __name__ == "__main__":
    main()

# ---เเสดงข้อมูลรถในระบบ---
# ทะเบียนรถ: กข 1234, ยี่ห้อ: Toyota, ที่นั่ง: 7
# สถานะปัจจุบัน: ว่าง
# ทะเบียนรถ: บบ 5678, ยี่ห้อ: Honda, ที่นั่ง: 4
# สถานะปัจจุบัน: ว่าง

# ---การเช่ารถ---
# ดำเนินการเรียบร้อย ทะเบียนรถ: กข 1234 ถูกเช่าแล้ว
# ไม่สามารถดำเนินการได้ ทะเบียนรถ: กข 1234 ถูกเช่าอยู่
# สถานะปัจจุบัน: ถูกเช่า

# ---คำนวณค่าเช่า---
# คำนวณ กข 1234
# คำนวณ (รถขนาดใหญ่): 4500.00 (ราคาพื้นฐาน)+675.00 (ที่นั่ง>5)= 5175.00 บาท
# คำนวณ บบ 5678
# คำนวณ (ขนาดมาตรฐาน): 3000.00 บาท
# ค่าธรรมเนียมรวมทั้งหมด: 8175.00 บาท
