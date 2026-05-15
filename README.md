<h1 align="center">
🍺 GAME RÓT BIA AI - VIETNAM CYBER BAR
</h1>

<div align="center">
  <img src="README/logoDaiNam.png" alt="DaiNam University Logo" width="250">
</div>

<br>

<div align="center">

[![FIT DNU](https://img.shields.io/badge/-FIT%20DNU-28a745?style=for-the-badge)](https://fitdnu.net/)
[![DAINAM UNIVERSITY](https://img.shields.io/badge/-DAINAM%20UNIVERSITY-dc3545?style=for-the-badge)](https://dainam.edu.vn/vi)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![Pygame](https://img.shields.io/badge/Pygame-AI%20GAME-green?style=for-the-badge)](#)

</div>

<hr>

<h2 align="center">✨ Mô tả dự án</h2>

<p align="justify">

<strong>GAME RÓT BIA AI - VIETNAM CYBER BAR</strong> là trò chơi sinh tồn hiện đại sử dụng công nghệ <strong>Computer Vision</strong> và <strong>AI Hand Tracking</strong> để điều khiển gameplay bằng cử chỉ tay thông qua webcam.

Người chơi sẽ điều khiển khay hứng bia trong một thành phố Cyberpunk tương lai, nơi AI mang tên <strong>GLITCH CORE</strong> đã mất kiểm soát và tạo ra cơn mưa dữ liệu độc hại.

Dự án tích hợp:

- 🤖 Nhận diện tay bằng MediaPipe
- 📷 Camera Tracking Realtime
- 🍺 Hệ thống Beer / Toxic Beer / Gold Beer
- ⚡ Skill kích hoạt bằng gesture
- 🌈 Hiệu ứng Cyber Glitch
- 🔥 Gameplay phản xạ tốc độ cao
- 🎵 Voice Narration & Sound Effect
- 🏆 Hệ thống Mission & Boss Battle

</p>

<hr>

<h2 align="center">🚀 Cấu trúc dự án</h2>

<pre>
📂 BEER_AI_GAME
├── 📁 assets/                     # Thư mục tài nguyên game
│   ├── 🖼️ bg_beer.png             # Background gameplay
│   ├── 🖼️ bg_beermenu.png         # Background menu
│   ├── 🖼️ beer.png                # Beer thường
│   ├── 🖼️ gold.png                # Gold beer
│   ├── 🖼️ toxic.png               # Toxic beer
│   ├── 🖼️ player.png              # Player bar
│   ├── 🖼️ button.png              # Button UI
│   ├── 🎵 music.mp3               # Nhạc nền
│   ├── 🎵 catch.wav               # Âm thanh hứng beer
│   ├── 🎵 hit.mp3                 # Âm thanh toxic hit
│   ├── 🎵 miss.wav                # Âm thanh miss
│   └── 🎵 gameover.mp3            # Âm thanh game over
│
├── 📁 README/                     # Tài nguyên README
│   ├── 🖼️ logoDaiNam.png          # Logo Đại Nam
│   └── 🖼️ image1.png              # Gameplay preview
│
├── 📄 main.py                     # File game chính
├── 📄 score.json                  # Lưu điểm cao
├── 📄 requirements.txt            # Danh sách thư viện
└── 📘 README.md                   # Tài liệu dự án
</pre>

<hr>

<h2 align="center">🎬 Video Demo & Gameplay</h2>

<div align="center">
  <a href="#" target="_blank">
    <img src="README/image1.png" alt="Gameplay demo" width="70%">
  </a>

  <p>
    <i>
      Hệ thống điều khiển bằng AI Hand Tracking thông qua MediaPipe & OpenCV
    </i>
  </p>
</div>

<hr>

<h2 align="center">🛠️ Chuẩn bị</h2>

### 💻 Phần mềm & Thư viện sử dụng

<div align="center">

[![Python](https://img.shields.io/badge/-Python%203.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/-OpenCV%204.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](#)
[![MediaPipe](https://img.shields.io/badge/-MediaPipe-007ACC?style=for-the-badge)](#)
[![Pygame](https://img.shields.io/badge/-Pygame-ffd343?style=for-the-badge&logo=python&logoColor=black)](#)
[![NumPy](https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#)

</div>

<hr>

<h2 align="center">📦 Hướng dẫn cài đặt & Chạy</h2>

<p align="justify">

<strong>1. Cài đặt thư viện cần thiết:</strong>

<br><br>

<code>
pip install -r requirements.txt
</code>

<br><br>

<strong>2. Chạy game:</strong>

<br><br>

<code>
python main.py
</code>

<br><br>

<em>
Lưu ý:
Game yêu cầu Webcam hoạt động ổn định để nhận diện cử chỉ tay.
Khuyến nghị sử dụng Python 3.10 hoặc 3.11.
</em>

</p>

<hr>

<h2 align="center">🎮 Quy trình hoạt động của hệ thống</h2>

<p align="justify">

### 1️⃣ Intro Story & Voice Narration

- Khi khởi động, game hiển thị cốt truyện về AI <strong>GLITCH CORE</strong>.
- Voice narration sẽ đọc nội dung mở đầu.
- Người chơi có thể ✊ nắm tay để bỏ qua intro.

---

### 2️⃣ AI Hand Tracking System

- Camera webcam nhận diện bàn tay realtime.
- MediaPipe phân tích 21 điểm khớp tay.
- Người chơi di chuyển tay để điều khiển thanh hứng bia.

Áp dụng công thức làm mượt chuyển động:

:contentReference[oaicite:0]{index=0}

---

### 3️⃣ Hệ thống Skill bằng Gesture

Người chơi có thể kích hoạt kỹ năng bằng số ngón tay:

| Gesture | Skill |
|---|---|
| ☝️ 1 ngón | MAGNET |
| ✌️ 2 ngón | SHIELD |
| 🤟 3 ngón | SLOW TIME |
| 🖖 4 ngón | DOUBLE SCORE |

---

### 4️⃣ Hệ thống Mission & Level

Game gồm nhiều level với độ khó tăng dần:

- 🟡 Level 1: Rain Begins
- 🔴 Level 2: System Corruption
- ☠️ Level 3: AI Overload
- 💀 Level 4: Glitch Storm
- 🔥 Level 5: THE GLITCH CORE

Mỗi màn có nhiệm vụ riêng:

- Đạt điểm yêu cầu
- Né toxic beer
- Tạo combo
- Sống sót theo thời gian

---

### 5️⃣ Boss Battle — THE GLITCH CORE

Boss cuối tạo ra:

- Toxic Rain
- Fake Beer
- Glitch Effect
- Laser Attack
- Toxic Wave

Người chơi phải kết hợp skill + phản xạ để sống sót.

---

### 6️⃣ Hệ thống Glitch Effect

Áp dụng hiệu ứng:

- RGB Split
- Scanline
- Camera Corruption
- Flash Error

Tạo cảm giác Cyberpunk hiện đại.

</p>

<hr>

<h2 align="center">🏆 Hệ thống Skill</h2>

| Skill | Chức năng |
|---|---|
| 🍺 MAGNET | Hút beer & gold gần player |
| 🛡️ SHIELD | Chặn toxic beer |
| ⏱️ SLOW TIME | Giảm tốc độ toàn bộ object |
| 🔥 DOUBLE SCORE | Nhân đôi điểm số |

<hr>

<h2 align="center">🎯 Hệ thống Mission</h2>

| Level | Mission |
|---|---|
| 🟡 Level 1 | Đạt 10 điểm |
| 🔴 Level 2 | Sống sót 30 giây |
| ☠️ Level 3 | Né 20 toxic beer |
| 💀 Level 4 | Combo x5 |
| 🔥 Level 5 | Sống sót 60 giây |

<hr>

<h2 align="center">⚙️ Công nghệ sử dụng</h2>

| Công nghệ | Vai trò |
|---|---|
| Python | Ngôn ngữ chính |
| Pygame | Xây dựng gameplay |
| OpenCV | Camera xử lý ảnh |
| MediaPipe | AI nhận diện tay |
| NumPy | Tính toán dữ liệu |
| JSON | Lưu điểm |
| GitHub | Quản lý source |

<hr>

<h2 align="center">👨‍💻 Thông tin sinh viên</h2>

<div align="center">

| Thông tin | Nội dung |
|---|---|
| 👤 Họ tên | Bùi Duy Anh |
| 🎓 Lớp | CNTT 16-02 |
| 🏫 Trường | Đại Nam University |

</div>

<hr>

<div align="center">

# 🔥 AI BEER CATCHER — CYBER VIETNAM EDITION 🔥

</div>
