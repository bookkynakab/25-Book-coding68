""" 

เลือกโจทก์ : โปรแกรมทายตัวเลข 1-10
I  : ตัวเลข 1-10 
P  : สุ่มตัวเลข 1-10 จากโค้ด
o  : ถ้าทายตรงกับ Process จะถูก ถ้าไม่ตรง จะผิด
ตัวแปร : Secret_number,guess

"""
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game ทายตัวเลข 1-10</title>
    <style>
        /* CSS สำหรับตกแต่งให้สวยงาม */
        body {
            font-family: 'Kanit', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #333;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
            width: 350px;
        }
        h1 { color: #764ba2; margin-bottom: 10px; }
        p { font-size: 0.9rem; color: #666; }
        input {
            width: 80%;
            padding: 10px;
            margin: 20px 0;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 1.2rem;
            text-align: center;
        }
        button {
            background: #764ba2;
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1rem;
            transition: 0.3s;
        }
        button:hover { background: #667eea; }
        #message { margin-top: 20px; font-weight: bold; min-height: 1.5em; }
        .credit { margin-top: 30px; font-size: 0.8rem; color: #aaa; border-top: 1px solid #eee; pt: 10px; }
    </style>
</head>
<body>

<div class="container">
    <h1>เกมทายเลข 🎮</h1>
    <p>ยินดีต้อนรับ! ลองทายเลข 1-10 ดูซิ</p>
    
    <input type="number" id="guessInput" min="1" max="10" placeholder="ใส่เลขที่นี่">
    <br>
    <button onclick="checkGuess()">ส่งคำตอบ</button>

    <div id="message"></div>

    <div class="credit">
        เครดิต นายณัฏฐวี นาคมอญ
    </div>
</div>

<script>
    // ส่วนของ Logic (เหมือน Python ที่คุณเขียน)
    let secretNumber = Math.floor(Math.random() * 10) + 1;

    function checkGuess() {
        const input = document.getElementById('guessInput');
        const message = document.getElementById('message');
        const userGuess = parseInt(input.value);

        if (isNaN(userGuess) || userGuess < 1 || userGuess > 10) {
            message.style.color = "orange";
            message.innerText = "กรุณาใส่เลข 1-10 เท่านั้นนะ!";
            return;
        }

        if (userGuess === secretNumber) {
            message.style.color = "green";
            message.innerText = "🎉 ยินดีด้วย! ทายถูกแล้ว";
            // สุ่มเลขใหม่หลังจากทายถูก (ทางเลือก)
            // setTimeout(() => location.reload(), 3000); 
        } else {
            message.style.color = "red";
            message.innerText = "❌ ไม่เป็นไร ลองใหม่นะ";
        }
        
        input.value = ""; // ล้างช่องใส่เลข
        input.focus();    // เอาเคอร์เซอร์ไปวางที่ช่องเดิม
    }
</script>

</body>
</html>

