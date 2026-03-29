Rozumiem, tu je osekané a vecné README.md, ktoré sa sústredí len na to, čo aplikácia robí a ako vyzerajú jej dáta.

🎓 Študentský Dashboard
Moderná webová aplikácia na prehľadnú správu a zobrazovanie zoznamu študentov. Projekt prepája Python (Flask) backend ako zdroj dát a HTML/CSS/JS frontend s responzívnym rozhraním.

🚀 Hlavné funkcie
Automatická synchronizácia: Dáta sa načítavajú priamo z API hneď po štarte stránky.

Inteligentné vyhľadávanie: Integrovaný filter umožňujúci okamžité hľadanie podľa mena, priezviska alebo prezývky.

4-stĺpcový Grid: Optimalizované rozloženie kariet pre maximálnu prehľadnosť na širokých monitoroch.

Responzivita: Plná podpora pre mobilné zariadenia a tablety (automatická zmena počtu stĺpcov).

Záložné avatary: Ak je odkaz na fotografiu neplatný alebo expirovaný, systém automaticky vygeneruje vizuálny avatar s iniciálkami študenta.

📂 Štruktúra dát (JSON)
Aplikácia spracováva od backendu nasledujúce polia pre každého študenta:

id: Číselný identifikátor.

name: Krstné meno.

surname: Priezvisko.

nickname: Používateľská prezývka.

image: URL adresa profilového obrázka.

⚠️ Dôležité upozornenia
CORS Policy: Pre správne fungovanie komunikácie musí byť v Python skripte povolený CORS(app).

Konfigurácia portov: Webová stránka komunikuje s portom 5000. Ak v backende dôjde k zmene portu, je potrebné túto zmenu vykonať aj vo funkcii fetchData v súbore index.html.