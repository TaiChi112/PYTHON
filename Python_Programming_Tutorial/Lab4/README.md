# COS2210 Assignment 3

## 1) การตัดไพ่และกรีดไพ่
จงเขียนโปรแกรมรับลำดับไพ่ในสำรับ (จำนวนไพ่เป็นจำนวนคู่แน่นอน) แล้วทำการ

1. ตัดไพ่ (Cut)
2. กรีดไพ่ (Riffle)

นิยาม:

- ตัดไพ่: แบ่งสำรับเป็น 2 กองเท่า ๆ กัน แล้วนำกองหลังมาวางทับกองหน้า
- กรีดไพ่: แบ่งสำรับเป็น 2 กองเท่า ๆ กัน แล้วนำไพ่จากกองหลังมาแทรกทีละใบกับกองหน้า

ตัวอย่าง:

- สำรับ: A 2 3 4 5 6 7 8 9 10 J Q
- ตัดไพ่: 7 8 9 10 J Q A 2 3 4 5 6
- กรีดไพ่: A 7 2 8 3 9 4 10 5 J 6 Q

## 2) List Comprehension จาก list ของ tuple
กำหนด

```python
points = [(5, 2), (3, 8), (4, 4), (3, 9), (25, 5), (10, 1), (2, 4), (9, 3)]
```

จงเขียนโปรแกรมโดยใช้ List Comprehension เพื่อสร้าง list ใหม่ตามเงื่อนไขต่อไปนี้

1. สลับ (x, y) เป็น (y, x) สำหรับทุกคู่
2. เลือกคู่ที่ x > y
3. เลือกคู่ที่ x < y
4. เลือกคู่ที่ x == y
5. เลือกคู่ที่ x^2 == y
6. เลือกคู่ที่ y^2 == x

## 3) ระบบจัดการข้อมูลนักศึกษา (Dictionary)
จงเขียนโปรแกรมที่เก็บข้อมูลนักศึกษาใน Dictionary โดย

- key = รหัสนักศึกษา (Student ID)
- value = ชื่อ-นามสกุล (Full Name)

และทำงานแบบวนลูปไม่รู้จบ พร้อมเมนูดังนี้

1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. View All Students
6. Exit

เงื่อนไขข้อความสำคัญ:

- เพิ่มสำเร็จ: `Student added successfully.`
- รหัสซ้ำ: `Student ID already exists.`
- ไม่พบรหัส: `Student ID not found.`
- แก้ไขสำเร็จ: `Student data updated successfully.`
- ออกจากโปรแกรม: `Exiting program. Goodbye!`
- เลือกเมนูไม่ถูกต้อง: `Invalid option. Please try again.`

## 4) วิเคราะห์นักศึกษาที่ลงทะเบียนวิชาเลือกด้วย Set
มีรายชื่อนักศึกษาในวิชา Python, Java และ C++ ดังนี้

- Python: SUPANAT, TEERAPON, KAWINWAT, KIDSAKORN, PHON, SURACHAD
- Java: PAWARIS, SUPANAT, PONGSAKORN, RATTANACHAT, PHON, SURACHAD
- C++: SUPANAT, TEERAPON, KAWINWAT, RATTANACHAT, SURACHAD, MATCHAKAN

จงเขียนโปรแกรมเพื่อหาจำนวนและรายชื่อของนักศึกษาที่อยู่ในเงื่อนไขต่อไปนี้

1. เรียนครบทั้ง 3 วิชา
2. เรียนเฉพาะ Python อย่างเดียว
3. เรียนเฉพาะ Java อย่างเดียว
4. เรียนเฉพาะ C++ อย่างเดียว
5. เรียน Python และ Java เท่านั้น (ไม่เรียน C++)
6. เรียน Python และ C++ เท่านั้น (ไม่เรียน Java)
7. เรียน Java และ C++ เท่านั้น (ไม่เรียน Python)
8. เรียนอย่างน้อย 2 วิชาขึ้นไป
