Ex1.


|Test Num.|Test Objective|Test step|Expected result|
| :- | :- | :- | :- |
|1|<p>ทดสอบความถูกต้องของรายการสินค้าที่ซื้อ</p>|1. กดเลือกสินค้าที่ต้องการ|<p>แสดงรายการคำสั่งซื้อตรงกับสินค้าที่ต้องการ</p>|
|2|ทดสอบการรับเหรียญหรือธนบัตรที่ตู้เครื่องดื่มไม่รองรับ|<p>1. กดเลือกสินค้าที่ต้องการ</p><p>2. ชำระสินค้าด้วยเหรียญหรือธนบัตรที่ตู้ไม่รองรับ</p>|<p>ตู้เครื่องดื่มทำการคืนเหรียญหรือธนบัตรที่ไม่รองรับและแสดงหน้าจอให้ชำระเงินด้วยเหรียญหรือธนบัตรที่เครื่องรองรับเท่านั้น</p>|
|3|ทดสอบการทอนเงิน|<p>1. กดเลือกสินค้าที่ต้องการ</p><p>2. ใส่เงินให้มากกว่าราคาของสินค้า</p>|<p>ตู้เครื่องดื่มทอนเงินตามจำนวนที่มากกว่าราคาของสินค้า</p>|


Ex2.

1. ถามเกี่ยวกับ User story ให้ชัดเจนทั้งฝั่งผู้ซื้อและผู้ขาย

2. Functional และ Non-functional requirements

3. วิธีการชำระเงินของ user ผ่านช่องทางไหนได้บ้าง

4. กระบวนการคิดค่าจัดส่ง

5. Scope ในการเทสแต่ละครั้ง

Ex3


|Test Num.|Test Objective|Test step|Expected result|
| :- | :- | :- | :- |
|1|ทดสอบความถูกต้องของบัญชีปลายทาง|<p>1. ใส่ข้อมูล เลขบัญชีหรือธนาคารที่</p><p>ไม่ถูกต้อง</p>|แสดงหน้าจอ “เลขบัญชีหรือธนาคารไม่ถูกต้อง”|
|2|<p>ทดสอบยอดเงินคงเหลือ</p><p>ในบัญชีว่าเพียงพอต่อการทำ</p><p>ธุรกรรมหรือไม่</p>|<p>1. ใส่ข้อมูลเลขบัญชีหรือธนาคารที่ถูกต้อง</p><p>2. ใส่จำนวนเงินที่ต้องการโอนให้มากกว่าเงินคงเหลือในบัญชี</p><p>ของผู้โอน</p><p>3. กด ยืนยัน</p>|แสดงหน้าจอ “ยอดเงินไม่เพียงพอต่อการโอนเงิน”|
|3|<p>ทดสอบยอดเงินของผู้โอนและผู้รับหลังจากการโอนเงินสำเร็จ</p>|<p>1. ใส่ข้อมูลเลขบัญชีหรือธนาคารที่ถูกต้อง</p><p>2. ใส่จำนวนเงินที่ต้องการโอนให้น้อยกว่ากว่าเงินคงเหลือในบัญชีของผู้โอน</p><p>3. กด ยืนยัน</p>|<p>แสดงหน้าจอ “โอนเงินสำเร็จ”</p><p>และ </p><p>1. เงินคงเหลือของผู้โอนลดลงเท่ากับจำนวนเงินที่โอน</p><p>2. เงินคงเหลือของผู้รับเพิ่มขึ้นเท่ากับเงินที่ผู้โอนเงินโอนมา</p>|


