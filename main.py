import pygame, random, cv2, mediapipe as mp
import numpy as np
import os, json

# ================= INIT =================
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beer Catcher AI - Vietnam Story")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

BASE_DIR = os.path.dirname(__file__)
ASSETS = os.path.join(BASE_DIR, "assets")

# ================= HIGH SCORE =================
SAVE_FILE = os.path.join(BASE_DIR, "highscore.json")

def load_highscore():
    if os.path.exists(SAVE_FILE):
        return json.load(open(SAVE_FILE))["highscore"]
    return 0

def save_highscore(score):
    json.dump({"highscore": score}, open(SAVE_FILE, "w"))

highscore = load_highscore()

# ================= MUSIC =================
music_path = os.path.join(ASSETS, "music.mp3")
if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)

# ================= LOAD IMAGE =================
def load_img(name, size):
    path = os.path.join(ASSETS, name)
    try:
        return pygame.transform.scale(pygame.image.load(path), size)
    except:
        surf = pygame.Surface(size)
        surf.fill((200, 0, 200))
        return surf

bg_game = load_img("bg_beer.png", (WIDTH, HEIGHT))
bg_menu = load_img("bg_beermenu.png", (WIDTH, HEIGHT))
beer_img = load_img("beer.png", (40, 60))
gold_img = load_img("gold.png", (40, 60))
toxic_img = load_img("toxic.png", (40, 60))

# ================= CAMERA =================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)
cap = cv2.VideoCapture(0)

smooth_x = WIDTH // 2

def get_hand():
    global smooth_x
    ret, frame = cap.read()
    if not ret:
        return None

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    x = None

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        x = int(hand.landmark[8].x * WIDTH)
        smooth_x = int(smooth_x * 0.7 + x * 0.3)

    return smooth_x

# ================= GAME VAR =================
player = pygame.Rect(350, 450, 80, 20)
drops = []

hp = 100
score = 0

# ================= INTRO (VIETNAMESE STORY) =================
def intro_story():
    story = [
        "NĂM 2145...",
        "HỆ THỐNG AI ĐÃ MẤT KIỂM SOÁT",
        "NHÀ MÁY SẢN XUẤT ĐỒ UỐNG BỊ LỖI DỮ LIỆU",
        "BIA - VÀNG - ĐỘC RƠI KHÔNG KIỂM SOÁT",
        "BẠN LÀ NGƯỜI DUY NHẤT CÒN SỐNG",
        "NHIỆM VỤ: HỨNG VÀ SINH TỒN"
    ]

    frame = 0

    while True:
        screen.fill((0,0,0))

        for i, line in enumerate(story):
            text = font.render(line, 1, (255,255,255))
            screen.blit(text, (80, 120 + i*40))

        screen.blit(font.render("NHẤN SPACE / CLICK ĐỂ BẮT ĐẦU",1,(255,200,0)),(180,520))

        pygame.display.update()
        frame += 1

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return True
            if e.type == pygame.MOUSEBUTTONDOWN:
                return True

        if frame > 720:
            return True

# ================= MENU =================
def menu():
    while True:
        screen.blit(bg_menu, (0,0))

        btn = pygame.Rect(300, 300, 200, 60)
        pygame.draw.rect(screen, (200,150,0), btn)

        screen.blit(font.render("START",1,(0,0,0)),(360,320))
        screen.blit(font.render(f"HIGH SCORE: {highscore}",1,(255,255,255)),(250,400))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if btn.collidepoint(e.pos):
                    return True

# ================= PAUSE =================
def pause():
    while True:
        screen.fill((0,0,0))

        screen.blit(font.render("TẠM DỪNG",1,(255,255,255)),(350,200))

        resume = pygame.Rect(300,260,200,50)
        quit_btn = pygame.Rect(300,330,200,50)

        pygame.draw.rect(screen,(0,200,0),resume)
        pygame.draw.rect(screen,(200,0,0),quit_btn)

        screen.blit(font.render("TIẾP TỤC",1,(0,0,0)),(350,275))
        screen.blit(font.render("THOÁT",1,(0,0,0)),(360,345))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"
            if e.type == pygame.MOUSEBUTTONDOWN:
                if resume.collidepoint(e.pos):
                    return "resume"
                if quit_btn.collidepoint(e.pos):
                    return "quit"

# ================= DROP =================
def create_drop():
    x = random.randint(0, WIDTH-40)
    t = random.choice(["beer", "gold", "toxic"])

    if t == "beer":
        return {"x":x,"y":0,"img":beer_img,"v":1}
    if t == "gold":
        return {"x":x,"y":0,"img":gold_img,"v":5}
    return {"x":x,"y":0,"img":toxic_img,"v":-20}

# ================= GAME =================
def game():
    global hp, score, highscore

    drops.clear()
    hp = 100
    score = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if pause() == "quit":
                        return

        x = get_hand()
        if x:
            player.x = x - 40

        if random.randint(1, 15) == 1:
            drops.append(create_drop())

        screen.blit(bg_game,(0,0))

        for d in drops[:]:
            d["y"] += 5

            rect = pygame.Rect(d["x"],d["y"],40,60)

            if player.colliderect(rect):
                score += d["v"]
                hp += d["v"]
                drops.remove(d)

        pygame.draw.rect(screen,(255,200,0),player)

        for d in drops:
            screen.blit(d["img"],(d["x"],d["y"]))

        screen.blit(font.render(f"Score: {score}",1,(255,255,255)),(10,10))
        screen.blit(font.render(f"HP: {hp}",1,(0,255,0)),(10,40))
        screen.blit(font.render(f"High: {highscore}",1,(255,255,0)),(10,70))

        pygame.display.update()
        clock.tick(60)

        if hp <= 0:
            break

    if score > highscore:
        highscore = score
        save_highscore(highscore)

# ================= LOOP =================
while True:
    if not menu():
        break
    if not intro_story():
        break
    game()

cap.release()
cv2.destroyAllWindows()
pygame.quit()