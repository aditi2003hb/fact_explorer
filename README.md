# 📚 Random Fact Explorer

A beautifully interactive **web app** built with **FastAPI**, **SQLAlchemy**, and **Pydantic** on the backend, with a smooth, visually engaging frontend (HTML/CSS/JavaScript). Users can explore random facts by category, flip animated fact cards, and expand their knowledge!

---

## ✨ Features

- 🔍 Explore fun facts in categories: `Science`, `History`, `Tech`, `Life`
- 🎲 Click any category to fetch a **random fact**
- 📖 Card flip animation to show fact and category
- 📦 Facts stored and served using SQLite + SQLAlchemy
- 🧠 Backend validation powered by Pydantic models
- 🔗 Fully interactive frontend built with HTML, CSS, JS
- 🖥️ Runs entirely on **localhost** — no external services required

---

## 📸 Live Preview (Localhost)

> You’ll run this locally on your machine.

![Preview](https://dummyimage.com/700x400/e0f7fa/333&text=Random+Fact+Explorer+UI)

> *(Replace the above image with a real screenshot once running)*

---

## 🛠 Tech Stack

| Layer    | Tech Used                     |
|----------|-------------------------------|
| Backend  | FastAPI, SQLAlchemy, Pydantic |
| Frontend | HTML, CSS, JavaScript         |
| DB       | SQLite                        |
| Server   | Hypercorn (Python 3.13 safe)  |

---

## 🗂 Project Structure

```
fact_explorer/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

## 🔧 Installation & Run Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/aditi2003hb/random-fact-explorer.git
cd random-fact-explorer
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

> `requirements.txt`:
```
fastapi
sqlalchemy
pydantic
hypercorn
```

### 3️⃣ Run Backend Server

```bash
hypercorn backend.main:app
```

✅ Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

---

## 🌐 Open the Frontend

Open this file in your browser:

```bash
frontend/index.html
```

Or use VS Code's Live Server extension for real-time reloads.

---

## 🎉 Sample Categories & Facts

| Category | Example Fact |
|----------|--------------|
| Science  | "Octopuses have three hearts and blue blood." |
| History  | "Oxford University is older than the Aztec Empire." |
| Tech     | "The first computer virus was created in 1986 and called Brain." |
| Life     | "Honey never spoils — it's edible even after thousands of years." |

Add your own facts using the `/facts` POST endpoint in the docs!

---

## 📚 API Endpoints

| Method | Endpoint                    | Description                          |
|--------|-----------------------------|--------------------------------------|
| GET    | `/facts`                    | Get all facts                        |
| GET    | `/facts/random/{category}` | Get a random fact by category        |
| POST   | `/facts`                    | Add a new fact                       |
| DELETE | `/facts/{fact_id}`         | Delete a fact                        |

---

## 🧠 What You Learn From This Project

- How to build modular FastAPI apps with full CRUD
- Structuring Pydantic models and handling validation
- Building and querying with SQLAlchemy ORM
- Connecting a static frontend to FastAPI backend with `fetch()`
- Organizing full-stack Python web projects cleanly

---

## 🙋‍♀️ Author

Made with 💙 by [Aditi (aditi2003hb)](https://github.com/aditi2003hb)

---

## 📄 License

MIT License

