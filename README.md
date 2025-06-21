# Historias CMC

> **Historias CMC** is a Django‐powered web application for managing electronic clinical histories (historias clínicas), patients and related medical documents. The project was born as an internal tool for small clinics and individual practitioners who need a lightweight, secure and cloud‑hosted solution without the complexity—and price tag—of the typical EMR.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
   * [Environment Variables](#environment-variables)
   * [Running Locally](#running-locally)
4. [Project Structure](#project-structure)
5. [Deployment Guide](#deployment-guide)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

* **Patient & Clinical History CRUD** – register patients, record consultations, attach files and generate printable reports.
* **Authentication & Authorization** – Django’s built‑in auth plus per‑object permissions (🎯 *coming soon*).
* **DigitalOcean Spaces Storage** – media files are stored off‑site using `django‑storages` + S3 API.
* **PostgreSQL Database** – configured via `DATABASE_URL`; easy to swap for SQLite for quick local prototyping.
* **Responsive UI** – Bootstrap‑based templates ready for desktop & mobile.
* **Docker‑free Deployment** – works out‑of‑the‑box on [Render](https://render.com), Heroku or any cheap VPS with Gunicorn + Nginx.
* **100 % Python** – no JavaScript build step required (unless you want it).

> *Got ideas for more features? Open an issue or send a pull request!*

---

## Tech Stack

| Layer            | Choice                                                              |
| ---------------- | ------------------------------------------------------------------- |
| **Language**     | Python 3.11+                                                        |
| **Framework**    | Django 4.1                                                          |
| **Database**     | PostgreSQL 15 (fallback: SQLite for dev)                            |
| **Storage**      | DigitalOcean Spaces (S3‑compatible) via `boto3` & `django‑storages` |
| **Web Server**   | Gunicorn                                                            |
| **Static Files** | WhiteNoise middleware                                               |
| **Host**         | Render.com (example) / Any WSGI host                                |

All Python deps are pinned in [`requirements.txt`](requirements.txt).

---

## Getting Started

### Prerequisites

* **Python 3.11** or newer
* **PostgreSQL** (locally or cloud)
* `virtualenv` (recommended) or `conda`

### Installation

```bash
# 1. Clone
$ git clone https://github.com/josecouzo/historias_cmc.git
$ cd historias_cmc

# 2. Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
(venv)$ pip install --upgrade pip
(venv)$ pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file (or set them in your hosting dashboard) with **at least**:

```bash
DEBUG=False
SECRET_KEY="change-me"          # Django secret key

# Database
DATABASE_URL="postgres://user:pass@localhost:5432/cmc"

# S3 / DigitalOcean Spaces
AWS_ACCESS_KEY_ID="<your‑access‑key>"
AWS_SECRET_ACCESS_KEY="<your‑secret‑key>"
AWS_STORAGE_BUCKET_NAME="cmc"
OBJECT_STORAGE_REGION="nyc3"
```

> **Tip:** Never commit real secrets—use env vars!  The keys in `settings.py` are placeholders and should be overridden.

### Running Locally

```bash
# Apply migrations
(venv)$ python manage.py migrate

# Create a superuser
(venv)$ python manage.py createsuperuser

# Collect static files (optional for dev)
(venv)$ python manage.py collectstatic --noinput

# Start the dev server
(venv)$ python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) and log in with the superuser credentials.

---

## Project Structure

```
historias_cmc/
├─ cmc/                 # Django project config
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ historias/           # App: clinical histories
├─ mainapp/             # App: landing pages & common views
├─ templates/           # Global Django templates
├─ static/              # Global static assets (collected by WhiteNoise)
├─ requirements.txt
└─ README.md
```

---

## Deployment Guide (Render example)

1. Push your fork or clone to GitHub.
2. In Render, click **“New ➜ Web Service”** and connect the repo.
3. **Build & Runtime:**

   * **Environment:** Python
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn cmc.wsgi:application`
4. Add the environment variables shown in the [Environment Variables](#environment-variables) section.
5. Click **Create Web Service** and let Render build & deploy.  🎉

*Alternative hosts:* Railway.app, Heroku (via `Procfile`), or any VPS with Docker.

---

## Contributing

1. Fork the repo and create your branch: `git checkout -b feature/awesome`
2. Commit your changes: `git commit -m "feat: add awesome feature"`
3. Push and open a Pull Request.

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for tidy history.

---

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

---

*© 2025 Jose Couzo & contributors*
