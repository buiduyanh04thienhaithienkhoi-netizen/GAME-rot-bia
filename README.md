🚀 GAME RÓT BIA AI - VIETNAM CYBER BAR
<div align="center"> <img width="220" src="https://github.com/user-attachments/assets/77fe0fd1-2e55-4032-be3c-b1a705a1b574"/>








</div>
📖 1. Giới thiệu dự án

GAME RÓT BIA AI - VIETNAM CYBER BAR là game sinh tồn kết hợp AI nhận diện tay bằng camera webcam.

Người chơi sẽ điều khiển khay hứng bia bằng cử chỉ tay để sống sót giữa cơn mưa dữ liệu lỗi do AI gây ra.

Game kết hợp:

🎮 Pygame
🤖 AI Hand Tracking
📷 OpenCV + MediaPipe
🔥 Hiệu ứng Glitch Cyberpunk
🍺 Gameplay phản xạ tốc độ cao
🌌 2. Cốt truyện
💀 “THE GLITCH CORE”

Năm 2145...

Một AI quản lý nhà máy bia tự động mang tên GLITCH CORE bị lỗi sau cuộc tấn công dữ liệu bí ẩn.

Hệ thống sản xuất bắt đầu tạo ra:

🍺 Beer thường
🟡 Gold Beer
☠️ Toxic Beer

Toàn bộ thành phố chìm trong cơn mưa dữ liệu độc hại.

Bạn là bartender AI cuối cùng còn hoạt động.

🎯 Nhiệm vụ:

Hứng beer để sống sót
Né toxic beer
Kích hoạt skill bằng tay
Đánh bại GLITCH CORE
🎮 3. Gameplay
✋ Điều khiển bằng AI Hand Tracking
Di chuyển tay trái/phải để điều khiển khay
Camera nhận diện ngón tay
Gesture để kích hoạt skill
🧠 4. Hệ thống Skill AI
Skill	Gesture	Hiệu ứng
🍺 MAGNET	☝️ 1 ngón	Hút beer + gold
🛡️ SHIELD	✌️ 2 ngón	Chặn toxic
⏱️ SLOW TIME	🤟 3 ngón	Làm chậm game
🔥 DOUBLE SCORE	🖐️ 4 ngón	Nhân đôi điểm
⚡ 5. Điều kiện mở Skill

Skill không dùng vô hạn.

Người chơi phải:

Thu thập Gold Beer
Tạo combo
Hoàn thành nhiệm vụ

UI Skill hiển thị:

Tên skill
Số lượng còn lại
Cooldown
Điều kiện kích hoạt
🏆 6. Hệ thống Mission
🟡 Level 1 — “Rain Begins”
Môi trường:
Mưa bia nhẹ
AI ổn định
Mission:

✅ Đạt 10 điểm

🔴 Level 2 — “System Corruption”
Môi trường:
Toxic beer xuất hiện nhiều
Camera bắt đầu nhiễu glitch
Mission:

✅ Sống sót 30 giây

☠️ Level 3 — “AI Overload”
Môi trường:
Mưa dữ liệu hỗn loạn
Tốc độ cực nhanh
HP tụt nhanh
Mission:

✅ Né 20 toxic beer

💀 Level 4 — “Glitch Storm”
Môi trường:
Fake beer xuất hiện
Toxic tăng mạnh
Màn hình glitch liên tục
Mission:

✅ Combo x5

🔥 Level 5 — “THE GLITCH CORE”
👾 FINAL BOSS

Boss AI tạo ra toàn bộ toxic beer.

Boss Mechanics:
Toxic rain tốc độ cực cao
Fake beer đánh lừa người chơi
Màn hình nhiễu glitch
Boss laser
Toxic wave
Mission:

✅ Sống sót 60 giây

✨ 7. Tính năng nổi bật
🎥 AI Camera Tracking
Nhận diện bàn tay realtime
Gesture control
Finger counting
🎵 Voice Narration
Giọng đọc mở đầu cốt truyện
Voice warning khi boss xuất hiện
AI voice system
🌈 Cyber Glitch Effect
RGB Split
Scanline
Flash Error
Camera corruption
🎯 Combo System
Combo x2 x3 x5
Multiplier bonus
Perfect Catch
🧠 Dynamic Difficulty
AI tăng độ khó theo điểm
Spawn toxic thông minh
⚙️ 8. Công nghệ sử dụng
Công nghệ	Vai trò
Python	Ngôn ngữ chính
Pygame	Engine game
OpenCV	Camera
MediaPipe	AI nhận diện tay
NumPy	Tính toán
JSON	Lưu điểm
GitHub	Quản lý source
📂 9. Cấu trúc dự án
beer_ai_game/
│
├── assets/
│   ├── beer.png
│   ├── toxic.png
│   ├── gold.png
│   ├── bg_beer.png
│   ├── bg_beermenu.png
│   ├── player.png
│   ├── button.png
│   ├── music.mp3
│   ├── catch.wav
│   ├── hit.mp3
│   ├── miss.wav
│   ├── gameover.mp3
│
├── main.py
├── score.json
├── requirements.txt
└── README.md
▶️ 10. Cách chạy game
1️⃣ Cài thư viện
pip install -r requirements.txt
2️⃣ Chạy game
python main.py
📦 11. requirements.txt
pygame==2.6.1
numpy==1.26.4
opencv-python==4.8.0.76
mediapipe==0.10.9
🎬 12. Intro Story mở đầu
📖 STORY INTRO
NĂM 2145...

GLITCH CORE ĐÃ THỨC TỈNH

HỆ THỐNG NHÀ MÁY BIA
BỊ AI KIỂM SOÁT

TOXIC BEER ĐANG RƠI KHẮP THÀNH PHỐ

BẠN LÀ BARTENDER CUỐI CÙNG

HÃY SỐNG SÓT...

🎮 Người chơi:

Nắm tay để bỏ qua intro
Hoặc chờ narration chạy xong
🧠 13. Hệ thống Gesture
Gesture	Skill
✊ Nắm tay	Skip Story
☝️ 1 ngón	Magnet
✌️ 2 ngón	Shield
🤟 3 ngón	Slow Time
🖖 4 ngón	Double Score
🎨 14. UI Game
HUD hiển thị:
❤️ HP
🏆 Score
⚡ Combo
🎯 Mission
🧠 Skill slots
📷 Camera status
🔥 Current Level
💀 15. Win / Lose Ending
🏆 GOOD ENDING

Bạn phá hủy GLITCH CORE.

Hệ thống bia được phục hồi.

Nhân loại sống sót.

☠️ BAD ENDING

AI kiểm soát toàn bộ thành phố.

TOXIC BEER lan rộng toàn cầu.

GAME OVER.

🚀 16. Hướng phát triển tương lai
🌐 Multiplayer Online
📱 Android APK
🎮 Controller Support
🤖 AI Difficulty System
🧠 Voice Command
🏅 Leaderboard Online
☁️ Cloud Save
👨‍💻 17. Thông tin sinh viên
Họ tên: Bùi Anh Tuấn
Lớp: CNTT 16-03
Trường: Đại Nam University
<div align="center">

🔥 AI BEER CATCHER — CYBER VIETNAM EDITION 🔥

</div>
