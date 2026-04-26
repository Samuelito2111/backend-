import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. KOMPLETNÁ DATABÁZA ŠTUDENTOV (Všetkých 20)
databaza = {
    "students": [
        {"id": 1, "name": "Janka", "surname": "Vargova", "nickname": "Dzejna", "image": "https://images-ext-1.discordapp.net/external/yeLMYDmagoC9SQhnO4ZNrtdkWuQ9zxNAcXAhBPZHi4c/https/i.pinimg.com/736x/27/00/24/2700247a1026dcda5effff4328dde1d5.jpg?format=webp"},
        {"id": 2, "name": "Samuel", "surname": "Haring", "nickname": "Samuelito", "image": "https://images-ext-1.discordapp.net/external/Yewp1yH-cpq8Fgygf-0kKWiGUwK4CUW6vrwM_5qPLwY/https/animehunch.com/wp-content/uploads/2023/01/Aki-Chainsawman.jpg?format=webp"},
        {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Moarari", "image": "https://i1.sndcdn.com/artworks-DCs5M8Xy0IYKVsqP-5O0ZyQ-t500x500.jpg"},
        {"id": 4, "name": "Matus", "surname": "Bucko", "nickname": "Kutik", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvyZyRob3RlZjvWGkUj5Fll7NAUPiEZYQakw&s"},
        {"id": 5, "name": "Tomas", "surname": "Jurcak", "nickname": "Jurcacik", "image": "https://s.yimg.com/ny/api/res/1.2/ITFAbxtzntLanHDJb7ABNw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTc3NTtjZj13ZWJw/https/media.zenfs.com/en/know_your_meme_909/e62f0fff99985de7d1a755c38d137e67"},
        {"id": 6, "name": "Adrian", "surname": "Cervenka", "nickname": "BigRed", "image": "https://i.pinimg.com/736x/75/42/4f/75424f660cca53f4d1f57af0ab7084fc.jpg"},
        {"id": 7, "name": "Marcus", "surname": "Martis", "nickname": "Jew", "image": "https://cdn.shopify.com/s/files/1/0209/9589/9456/files/israeli_flag.jpg?v=1548460595"},
        {"id": 8, "name": "Martin", "surname": "Jelinek", "nickname": "Jeliman", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d"},
        {"id": 9, "name": "Milan", "surname": "Kokina", "nickname": "Nalimovec", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4"},
        {"id": 10, "name": "Marko", "surname": "Mihalicka", "nickname": "ᗰᗩᖇKEᑎᘔIE", "image": "https://img.hockeyslovakia.sk/Player/231280/MarkoMIHALI%C4%8CKA.jpg"},
        {"id": 11, "name": "Samuel", "surname": "Uhrík", "nickname": "Samis", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6592fd86dc8b723834ae04/formal-photo/7ab0b847-749f-42e5-af17-ca7f8a12f32d"},
        {"id": 12, "name": "Matus", "surname": "Holecka", "nickname": "Holenka", "image": "https://eshop.banchem.sk/userdata/cache/images/storecards/000193/600/000193_mop%20strapcovy%20bavlneny%20140%20180%20220%20250%20IT-600x800.jpg"},
        {"id": 13, "name": "Lukas", "surname": "Vindis", "nickname": "Vindik", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6596c286dc8b72383529e0/formal-photo/6ac3297a-522f-460c-9c0f-6ce714ef6c39"},
        {"id": 14, "name": "Pato", "surname": "Korba", "nickname": "Patotvorba", "image": "https://www.zeriavplus.sk/wp-content/uploads/2022/11/bager-vykopove-prace-liptovsky-mikulas.jpg"},
        {"id": 15, "name": "Daniel", "surname": "Barta", "nickname": "Litwil", "image": "https://e7.pngegg.com/pngimages/757/1018/png-clipart-apple-logo-apple-desktop-models-logo-computer-wallpaper.png"},
        {"id": 16, "name": "David", "surname": "Skula", "nickname": "Dejvid", "image": "https://blog.blue-style.cz/wp-content/uploads/2016/07/Detail-obliceje.jpg"},
        {"id": 17, "name": "Rasto", "surname": "Patak", "nickname": "Chessmaster", "image": "https://thumbs.dreamstime.com/b/detailed-king-chess-piece-isolated-white-background-representing-most-important-piece-chess-game-king-chess-364212994.jpg"},
        {"id": 18, "name": "Karolina", "surname": "Kmetova", "nickname": "Kaja", "image": "https://static.vecteezy.com/system/resources/thumbnails/044/280/984/small/stack-of-books-on-a-brown-background-concept-for-world-book-day-photo.jpg"},
        {"id": 19, "name": "Samuel", "surname": "Martis", "nickname": "Zap_Zap", "image": "https://i.pinimg.com/736x/e2/ee/c4/e2eec4dc31feec8c20a3db33aa3c61af.jpg"},
        {"id": 20, "name": "Martin", "surname": "Deglovic", "nickname": "Boywithguns", "image":"https://m.media-amazon.com/images/I/51OwzCxWJCS.jpg"}
    ]
}

# 2. OSOBNOSTI PRE AI
personalities = {
    "Dzejna": "Si Janka. Miluješ módu, estetiku a si vždy milá ✨.",
    "Samuelito": "Si Samuelito. Si drsný anime hrdina, trochu tajomný 😎.",
    "Moarari": "Si Moarari. Si umelec, tvoje odpovede sú hlboké a filozofické 🎨.",
    "Kutik": "Si Kutik. Si tichý stratég, odpovedaj vecne a k veci 🧠.",
    "Jurcacik": "Si Jurcacik. Si kráľ vtipov a memes, každá tvoja správa musí byť sranda 🐸.",
    "BigRed": "Si BigRed. Si úprimný a priamy chlapík 🧨.",
    "Jew": "Si Marcus. Máš veľký prehľad o svete 🇮🇱.",
    "Jeliman": "Si Jeliman. Si športovec, tvoj život je futbal ⚽.",
    "Nalimovec": "Si Nalimovec. Si maximálny pohoďák 🌴.",
    "ᗰᗩᖇKEᑎᘔIE": "Si Marko. Si dravý hokejista 🏒.",
    "Samis": "Si Samis. Si počítačový mág 💻.",
    "Holenka": "Si Holenka. Poriadok a disciplína sú základ 🧼.",
    "Vindik": "Si Vindik. Si futbalový mozog 🏟️.",
    "Patotvorba": "Si Patotvorba. Si majster bagerista, tvoj svet sú stroje a stavby 🏗️.",
    "Litwil": "Si Litwil. Si fanúšik Apple, miluješ čistý dizajn 🍎.",
    "Dejvid": "Si David. Si cestovateľ a dobrodruh ✈️.",
    "Chessmaster": "Si Rasto. Premýšľaš tri kroky dopredu, život je šach ♔.",
    "Kaja": "Si Karolina. Si inteligentná a miluješ knihy 📚.",
    "Zap_Zap": "Si Samuel Martis. Si plný energie ako elektrický výboj ⚡.",
    "Boywithguns": "Si Martin Deglovic. Máš rád akciu 💥."
}

@app.route('/')
def home():
    return jsonify({"message": "Backend beží!", "status": "online"})

@app.route('/api')
def get_students():
    return jsonify(databaza)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_msg = data.get('message')
        nick = data.get('nickname')
        
        api_key = os.environ.get("GROK_API_KEY")
        if not api_key:
            return jsonify({"error": "Chýba API kľúč na serveri"}), 500

        persona = personalities.get(nick, "Si priateľský spolužiak.")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": "grok-beta",
            "messages": [
                {"role": "system", "content": f"{persona} Odpovedaj stručne, kamošsky a po slovensky."},
                {"role": "user", "content": user_msg}
            ],
            "temperature": 0.7
        }

        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=20
        )

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": f"AI Error {response.status_code}"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
