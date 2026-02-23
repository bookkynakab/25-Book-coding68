""" 

เลือกโจทก์ : โปรแกรมทายตัวเลข 1-10
I  : ตัวเลข 1-10 
P  : สุ่มตัวเลข 1-10 จากโค้ด
o  : ถ้าทายตรงกับ Process จะถูก ถ้าไม่ตรง จะผิด
ตัวแปร : Secret_number,guess

"""

import random

print("   ยินดีต้อนรับเข้าสู่เกมทายเลข   ")
print("   ลองทายดูว่าผมคิดเลขอะไรอยู่    ")

secret_number = random.randint(1, 10) 
guess = 0                        

while guess != secret_number:      
    guess = int(input("ทายเลข (1-10): ")) 
    
    if guess == secret_number:     
        print("ทายถูกแล้ว!")  
        print("เครดิต นายณัฏฐวี นาคมอญ")
    else:
        print("ไม่เป็นไร ลองใหม่นะ")

