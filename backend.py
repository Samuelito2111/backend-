from flask import Flask, jsonify
from flask_cors import CORS # Nezabudni: pip install flask-cors

app = Flask(__name__)
CORS(app) # Toto je kľúčové pre prepojenie s HTML!

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Databáza 10 študentov S FOTKAMI (vymeň URL za svoje!)
databaza = {
    "students": [
        {"id": 1, "name": "Janka", "surname": "Vargova", "nickname": "Dzejna", "image": "https://images-ext-1.discordapp.net/external/yeLMYDmagoC9SQhnO4ZNrtdkWuQ9zxNAcXAhBPZHi4c/https/i.pinimg.com/736x/27/00/24/2700247a1026dcda5effff4328dde1d5.jpg?format=webp"},
        {"id": 2, "name": "Samuel", "surname": "Haring", "nickname": "Samuelito", "image": "https://images-ext-1.discordapp.net/external/Yewp1yH-cpq8Fgygf-0kKWiGUwK4CUW6vrwM_5qPLwY/https/animehunch.com/wp-content/uploads/2023/01/Aki-Chainsawman.jpg?format=webp"},
        {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Moarari", "image": "https://i1.sndcdn.com/artworks-DCs5M8Xy0IYKVsqP-5O0ZyQ-t500x500.jpg"},
        {"id": 4, "name": "Matus", "surname": "Bucko", "nickname": "Kutik", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvyZyRob3RlZjvWGkUj5Fll7NAUPiEZYQakw&s"},
        {"id": 5, "name": "Tomas", "surname": "Jurcak", "nickname": "Jurcacik", "image": "https://s.yimg.com/ny/api/res/1.2/ITFAbxtzntLanHDJb7ABNw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTc3NTtjZj13ZWJw/https://media.zenfs.com/en/know_your_meme_909/e62f0fff99985de7d1a755c38d137e67"},
        {"id": 6, "name": "Adrian", "surname": "Cervenka", "nickname": "BigRed", "image": "https://cdn.discordapp.com/attachments/1465277883777024082/1469426348115099721/Screenshot_20260206_211508_Gallery.jpg?ex=69ca312e&is=69c8dfae&hm=3158bf91b369476112530358e31bf59d55d4fbbeae0799e264a9443f8efcf3a1&"},
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

@app.route('/')
def home():
    return jsonify({"message": "Vitajte v studentskom API s fotkami!"})

@app.route('/api')
def get_all_students():
    return jsonify(databaza)

@app.route("/api/student/<int:student_id>")
def get_one_student(student_id):
    # Vyhľadávanie podľa ID
    student = next((s for s in databaza["students"] if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student nenajdeny"}), 404

if __name__ == '__main__':
    # Spustíme na porte 5000
    app.run(port=5000, debug=True)
