# Froshims

A sports registration web app where users can register and deregister for intramural sports. Built with Python and Flask.

## Tech stack

- Python, Flask
- SQLAlchemy, SQLite

## Setup

1. Clone this repository

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-secret-key-here
   ```

5. Run the application:
   ```bash
   python app.py
   ```

Open `http://127.0.0.1:5000` in your browser.

> Note: Use `127.0.0.1:5000` rather than `localhost:5000` — Chrome may block the latter.
