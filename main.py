import requests
from flask import Flask, render_template, jsonify, request # Добавили request здесь

app = Flask(__name__)

# --- НАСТРОЙКИ ---
TELEGRAM_TOKEN = '8646189146:AAHD6mhNNDRF3CwSTaPkXeppWSccHFgW9g0'
YOUR_CHAT_ID = '1931263730'

def send_telegram_msg(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {"chat_id": YOUR_CHAT_ID, "text": text}
        requests.get(url, params=params)
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")

# --- МАРШРУТЫ (ROUTES) ---

@app.route('/visit', methods=['POST'])
def visit_api():
    send_telegram_msg("Твоя сладость открыла сайт! Она начала смотреть... 🤫✨")
    return jsonify({"status": "seen"})

@app.route('/video_watched', methods=['POST'])
def video_watched_api():
    # Важно: используем request.json от Flask
    data = request.get_json()
    video_name = data.get('video_name', 'Видео')
    send_telegram_msg(f"✅ Она досмотрела видео до конца: {video_name}")
    return jsonify({"status": "success"})

@app.route('/celebrate', methods=['POST'])
def celebrate_api():
    send_telegram_msg("Она нажала кнопку 'ДА'! Пора идти на Космос! 🌹❤️")
    return jsonify({"status": "success"})

@app.route('/')
def index():
    moments = [
        {"image": "1.jpg", "text": "Наш самый первый букет... Я помню, как волновался, когда дарил его тебе и буду чаще дарить цветы, чтобы порадовать свою сладость 🌹"},
        {"image": "2.jpg", "text": "Две принцессы на одном фото. ✨"},
        {"image": "4.jpg", "text": "Наш поцелуй... ❤️"},
        {"image": "5.jpg", "text": "Твои обнимашки — это самое теплое и безопасное место на земле для меня. Я хочу каждую секунду чувствовать твое тепло."},
        {"image": "6.jpg", "text": "Боулинг, картинг и знакомство с братом и его женой. Ты очень крутая! 🏎️"},
        {"image": "7.jpg", "text": "Наше первое свидание... "},
        {"image": "8.jpg", "text": "Помнишь, как я завязывал тебе шнурки? Я готов каждый раз их завязывать 👟"}
    ]

    videos = [
        {"file": "вальс.MOV", "title": "Наш первый удачный тренд ✨"},
        {"file": "3.mp4", "title": "Наше общее видео... ❤️"},
        {"file": "обнимашки.MOV", "title": "Самые милые обнимашки"}
    ]
    return render_template('index.html', moments=moments, videos=videos)

# --- ЗАПУСК ---
if __name__ == '__main__':
    print("Отправляю тестовое сообщение в Telegram...")
    send_telegram_msg("Бот запущен! Система слежения за видео активирована. ✅")
    app.run(debug=True, port=5000)