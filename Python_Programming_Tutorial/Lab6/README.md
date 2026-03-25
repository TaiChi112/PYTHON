# Assignment 6

## Part A: Functions

### 1) ฟังก์ชัน `calculate_stats`
ให้นักศึกษาสร้างฟังก์ชันชื่อ `calculate_stats` ที่รับตัวเลขได้ไม่จำกัดจำนวน และทำงานดังนี้

1. รับค่าตัวเลขจำนวนเต็มหรือทศนิยมได้ไม่จำกัดจำนวน
2. คำนวณค่าสถิติ: ผลรวม (`sum`), ค่าเฉลี่ย (`average`), ค่ามากที่สุด (`max`), ค่าน้อยที่สุด (`min`)
3. คืนค่าเป็น `dict` ที่มี key: `'sum'`, `'average'`, `'max'`, `'min'`
4. หากไม่มีการส่งค่าเข้ามา ให้คืน `{'sum': 0, 'average': 0, 'max': 0, 'min': 0}`

ตัวอย่าง:
```python
print(calculate_stats(10, 20, 30, 40, 50))
print(calculate_stats(5, 5))
print(calculate_stats())
```

ผลลัพธ์ตัวอย่าง:
```python
{'sum': 150, 'average': 30.0, 'max': 50, 'min': 10}
{'sum': 10, 'average': 5.0, 'max': 5, 'min': 5}
{'sum': 0, 'average': 0, 'max': 0, 'min': 0}
```

### 2) ฟังก์ชัน `final_price`
ให้นักศึกษาสร้างฟังก์ชัน `final_price` เพื่อคำนวณราคาสุทธิ โดยรองรับคูปองหลายแบบ

พารามิเตอร์:

1. `price` (Positional Argument): ราคาสินค้าตั้งต้น
2. `tax_rate` (Default Argument): อัตราภาษีมูลค่าเพิ่ม ค่าเริ่มต้น `0.07`
3. `**discounts` (Arbitrary Keyword Arguments): ส่วนลดในรูปแบบ `coupon_name=value`

เงื่อนไขคูปอง:

1. `special_...`: ส่วนลดคูณ 2
2. `expired_...`: ไม่นับส่วนลด (คิดเป็น 0)
3. ชื่ออื่น ๆ: ใช้ส่วนลดตามปกติ

ขั้นตอนคำนวณ:

1. รวมส่วนลดที่ผ่านเงื่อนไข
2. คำนวณยอดหลังหักส่วนลด = `price - total_discount` (ถ้าติดลบให้เป็น 0)
3. คำนวณภาษีจากยอดคงเหลือ โดยคูณด้วย `(1 + tax_rate)`
4. คืนค่าผลลัพธ์ทศนิยม 2 ตำแหน่ง

ตัวอย่าง:
```python
print(f"Case 1: {final_price(1000, discount_nov=100, expired_dec=500)}")
print(f"Case 2: {final_price(2000, special_vip=200)}")
print(f"Case 3: {final_price(3000, promo=100, special_year=200, expired_old=1000)}")
print(f"Case 4: {final_price(500, special_clearance=300)}")
print(f"Case 5: {final_price(2000, tax_rate=0, member=500)}")
```

ผลลัพธ์ตัวอย่าง:
```text
Case 1: 963.0
Case 2: 1712.0
Case 3: 2675.0
Case 4: 0.0
Case 5: 1500.0
```

### 3) ฟังก์ชัน `power_recursive(base, exponent)`
ให้นักศึกษาสร้างฟังก์ชัน `power_recursive(base, exponent)` สำหรับหาค่า $base^{exponent}$ โดยมีเงื่อนไข

1. ห้ามใช้ตัวดำเนินการ `**` และห้ามใช้ `pow()`
2. ต้องใช้ Recursion เท่านั้น
3. `exponent` เป็นจำนวนเต็มบวกหรือศูนย์เสมอ

ตัวอย่าง:
```python
print(f"2^3 = {power_recursive(2, 3)}")
print(f"5^0 = {power_recursive(5, 0)}")
print(f"5^2 = {power_recursive(5, 2)}")
```

ผลลัพธ์ตัวอย่าง:
```text
2^3 = 8
5^0 = 1
5^2 = 25
```

หมายเหตุ: ฟังก์ชันทุกข้อให้เขียน Docstring อธิบายหน้าที่ พารามิเตอร์ (Args) และค่าที่คืน (Returns)

## Part B: Modules and Packages

### 1) โมดูลวิเคราะห์ข้อความ

1. สร้างไฟล์ `text_utils.py`
2. สร้างฟังก์ชันดังนี้
	- `count_words(text)`
	- `count_vowels(text)`
	- `clean_text(text)`
	- `highlight(text)`
3. ใน `main.py`
	- import โมดูล
	- ใช้ข้อความตัวอย่าง: `" Python is Amazing "`
	- เรียกใช้ฟังก์ชันทั้ง 4 ตัวและแสดงผล

ผลลัพธ์ตัวอย่าง:
```text
Raw text: ' Python is Amazing '
1. Cleaned: 'python is amazing'
2. Word count: 3
3. Vowel count: 5
4. Highlighted: *** python is amazing ***
```

### 2) Package ระบบ E-commerce อย่างง่าย

1. สร้าง package ชื่อ `ecommerce` และโมดูล `cart.py`
2. ภายใน `ecommerce/cart.py` สร้างฟังก์ชัน
	- `add_item(cart_list, item_name, price)`
	- `remove_item(cart_list, item_name)`
	- `calculate_total(cart_list)`
	- `apply_discount(total_price, percent)`
3. ใน `main.py`
	- สร้าง `my_cart = []`
	- ใช้ `from ... import ...`
	- เพิ่มสินค้า Mouse (500), Keyboard (1500), Monitor (4000)
	- ลบ Mouse
	- สรุปราคารวมและหักส่วนลด 10%

ผลลัพธ์ตัวอย่าง:
```text
--- เริ่มการช้อปปิ้ง ---
เพิ่ม Mouse ราคา 500 บาท
เพิ่ม Keyboard ราคา 1500 บาท
เพิ่ม Monitor ราคา 4000 บาท
--- เปลี่ยนใจ ---
ลบ Mouse ออกแล้ว
--- สรุปยอด ---
ราคารวม: 5500 บาท
ราคาหลังหักส่วนลด 10%: 4950.0 บาท
```

### 3) โมดูลแปลงหน่วย

1. สร้างไฟล์ `converter.py`
2. สร้างฟังก์ชัน
	- `cm_to_inch(cm)`
	- `inch_to_cm(inch)`
	- `kg_to_lbs(kg)`
	- `lbs_to_kg(lbs)`
	- `celsius_to_kelvin(c)`
3. ใน `converter.py` ใส่ส่วน `if __name__ == "__main__":` เพื่อทดสอบทุกฟังก์ชัน
4. ใน `main.py` import โมดูลและใช้แปลงน้ำหนักตัวเองจาก kg เป็น lbs

สูตรที่ใช้:

1. นิ้ว = เซนติเมตร / 2.54
2. ปอนด์ = กิโลกรัม * 2.20462
3. เคลวิน = เซลเซียส + 273.15

ผลลัพธ์ตัวอย่างเมื่อรัน `converter.py`:
```text
=== TEST MODE Checking Formulas ===
2.54 cm to Inch: 1.0
1 Inch to cm: 2.54
10 kg to lbs: 22.05
0 C to Kelvin: 273.15
=== End of Tests ===
```

ผลลัพธ์ตัวอย่างเมื่อรัน `main.py`:
```text
น้ำหนักผม 70 กิโลกรัม เท่ากับ 154.32 ปอนด์
```