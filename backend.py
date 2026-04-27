import os
import requests
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Konfigurácia databázy (z tvojich údajov)
DB_CONFIG = {
    "user": "time_cell_moon_palace_user",
    "password": "onC6pAWRuut5cZ5LDax4iJuKtLD0g0bJ",
    "host": "dpg-d7ng35bbc2fs738phvq0-a.frankfurt-postgres.render.com",
    "port": 5432,
    "database": "time_cell_moon_palace",
    "sslmode": "require"
}

def get_db_connection():
    # RealDictCursor zabezpečí, že výsledky budú vyzerať ako slovníky (dict), nie n-tice (tuples)
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)

@app.route('/api')
def get_students():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Vytiahneme všetkých študentov z tabuľky, ktorú sme vytvorili minule
        cur.execute("SELECT original_id as id, name, surname, nickname, image_url as image FROM students ORDER BY original_id;")
        students = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify({"students": students})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        api_key = os.environ.get("GROK_API_KEY")
        
        # Odpovedaj ako konkrétny spolužiak
        res = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "grok-2-1212", 
                "messages": [
                    {"role": "system", "content": f"Si spolužiak {data.get('nickname')}. Odpovedaj stručne a slovensky."},
                    {"role": "user", "content": data.get('message')}
                ]
            },
            timeout=10
        )
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": {"message": str(e)}}), 500

if __name__ == "__main__":
    # Render automaticky nastavuje premennú prostredia PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
