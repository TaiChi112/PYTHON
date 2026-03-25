# Lab 6

## 1. Robot Movement จากไฟล์คำสั่ง
จงเขียนโปรแกรมที่รับตำแหน่งเริ่มต้น `(x, y)` (โดย `x` และ `y` เป็นจำนวนเต็ม) จากผู้ใช้ แล้วอ่านลำดับคำสั่งการเคลื่อนที่ของหุ่นยนต์จากไฟล์ `move<n>.txt`

- `L` = ไปซ้าย 1 หน่วย
- `R` = ไปขวา 1 หน่วย
- `U` = ขึ้นบน 1 หน่วย
- `D` = ลงล่าง 1 หน่วย

เมื่ออ่านคำสั่งครบแล้ว ให้แสดงว่าหุ่นยนต์หยุดที่ตำแหน่งใด

ถ้าพบคำสั่งที่ไม่ใช่ `L, R, U, D` ให้แสดง `Invalid command`

ตัวอย่างการทำงาน:

ไฟล์ `move1.txt`
```
L
L
U
U
D
R
R
U
U
L
L
```

```
Choose your movefile: move1.txt
Initial position : 10,20
Robot stops at 8,23
```

ไฟล์ `move2.txt`
```
L
L
X
U
D
Z
R
```

```
Choose your movefile: move2.txt
Initial position : 10,20
Invalid command
```

## 2. Vector Dot Product
จงเขียนโปรแกรมที่อ่านเวกเตอร์ 2 เวกเตอร์จากไฟล์ `vector<n>.txt` แล้วตรวจสอบว่ามีขนาดเท่ากันหรือไม่

- ถ้าไม่เท่ากัน แสดง `Incompatible size`
- ถ้าเท่ากัน ให้หา dot product ของเวกเตอร์ทั้งสอง

ต้องมีฟังก์ชันดังนี้:

- `is_equal(v1, v2)` ตรวจสอบว่าเวกเตอร์ยาวเท่ากันหรือไม่ (คืนค่า `True/False`)
- `dot(v1, v2)` คืนค่าผลรวม dot product
- `convert_to_float(v)` แปลงสมาชิกในลิสต์เป็น `float`
- `read_file_vector(filename)` อ่านไฟล์และคืนค่า `v1, v2` เป็นลิสต์

ตัวอย่างการทำงาน:

ไฟล์ `vector1.txt`
```
6 4 9 6 -4 7
3 7 -3 9 -5 1
```

```
Choose your vector file: vector1.txt
v1 = [6.0, 4.0, 9.0, 6.0, -4.0, 7.0]
v2 = [3.0, 7.0, -3.0, 9.0, -5.0, 1.0]
v1*v2 = 100.0
```

ไฟล์ `vector2.txt`
```
6 4 9 6 -4 7
3 7 -3
```

```
Choose your vector file: vector2.txt
v1 = [6.0, 4.0, 9.0, 6.0, -4.0, 7.0]
v2 = [3.0, 7.0, -3.0]
Incompatible size
```

ไฟล์ `vector3.txt`
```
5.5 4.5 9.5 6 -4 7
3 7.1 -3.5 5 6 9
```

```
Choose your vector file: vector3.txt
v1 = [5.5, 4.5, 9.5, 6.0, -4.0, 7.0]
v2 = [3.0, 7.1, -3.5, 5.0, 6.0, 9.0]
v1*v2 = 84.2
```

ไฟล์ `vector4.txt`
```
5.5 4 -9 6 -4
3 -7.1 0
```

```
Choose your vector file: vector4.txt
v1 = [5.5, 4.0, -9.0, 6.0, -4.0]
v2 = [3.0, -7.1, 0.0]
Incompatible size
```

## 3. สมการกำลังสอง
จงเขียนฟังก์ชัน `quad1` และ `quad2` ที่รับค่าสัมประสิทธิ์ `a, b, c` ของสมการ

$$
ax^2 + bx + c = 0, \quad a \neq 0
$$

โดย

- `quad1(a, b, c)` คืนค่า

$$
x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
$$

- `quad2(a, b, c)` คืนค่า

$$
x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}
$$

ให้เขียนโปรแกรมอ่านข้อมูลจากไฟล์ `problem<n>.txt` ซึ่งเก็บค่า `a, b, c` ในแต่ละบรรทัด แล้วตรวจสอบว่าสมการนั้นหาคำตอบจำนวนจริงได้หรือไม่

- ถ้าได้ ให้เรียก `quad1` และ `quad2` แล้วแสดงผลลัพธ์
- ถ้าไม่ได้ ให้แสดง `Invalid problem`

หมายเหตุ (ไม่ต้องส่ง): ลองเขียนผลลัพธ์ลงไฟล์ `solutions.txt`

ตัวอย่างการทำงาน:

ไฟล์ `problem1.txt`
```
1 -2 1
3 -7 2
5 -7 2
5 9 2
```

```
Choose your problem file: problem1.txt
1.0 1.0
2.0 0.33333333333333333
1.0 0.4
-0.2596875762567151 -1.540312423743285
```

ไฟล์ `problem2.txt`
```
1 1 2
1 4 3
5 -7 2
0 1 5
```

```
Choose your problem file: problem2.txt
Invalid problem
-1.0 -3.0
1.0 0.4
Invalid problem
```