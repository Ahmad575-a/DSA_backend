# DSA Heldenverwaltungssystem

Ein webbasiertes System zur Verwaltung von DSA-Helden. Dieses Projekt ist Teil der Ausbildungsaufgabe für Fachinformatiker Anwendungsentwicklung.

---

## 🚀 Schnellstart

### Voraussetzungen

* Docker & Docker Compose installiert
* Python 3.11+ (wenn ohne Docker verwendet)

---

## 📦 Setup mit Docker

1. **.env Datei anpassen (falls nötig)**

```env
DB_NAME=dsa_db
DB_USER=dsa_user
DB_PASSWORD=dein_passwort
DB_HOST=db
DB_PORT=3306
```

2. **Container starten**

```bash
docker-compose up --build
```

3. **Migrationen ausführen**

```bash
docker-compose exec web python manage.py migrate
```

4. **Superuser erstellen (für Admin-Oberfläche)**

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 🔐 Authentifizierung

### Registrierung

```
POST /api/register/
{
  "username": "dein_username",
  "password": "dein_passwort"
}
```

Antwort:

```json
{
  "token": "abcdef123456..."
}
```

### Token-Nutzung in Swagger

1. Swagger unter: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
2. Klicke auf **Authorize**
3. Gib im Feld ein:

```
Token dein_token_hier
```

4. Jetzt kannst du geschützte Endpunkte aufrufen

---

## 🧪 API-Endpunkte (Beispiele)

### Helden erstellen

```http
POST /api/helden/
Header: Authorization: Token dein_token
Body: {
  "name": "Gandalf",
  "rasse": "Mensch",
  "kultur": "Mittelreich",
  "profession": "Magier",
  "lebenspunkte": 30,
  "ausdauer": 40
}
```

### Eigene Helden anzeigen

```
GET /api/helden/
```

### Benutzer anzeigen (nur Admin)

```
GET /api/users/
```

---

## ⚙️ Weitere Befehle

### Shell-Zugang:

```bash
docker-compose exec web sh
```

### Testlauf:

```bash
docker-compose exec web python manage.py test
```

### Admin-Oberfläche:

[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 📁 Ordnerstruktur

```
dsa_backend/
|-- helden_app/
|-- dsa_project/
|-- requirements.txt
|-- docker-compose.yml
|-- Dockerfile
```

---