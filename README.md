# AI Podcast Generator

## Project Structure
```
podcast-app/
├── app.py                  # Flask backend (main server)
├── .env                    # API keys (never commit this!)
├── .env.example            # Template for .env
├── requirements.txt        # Python dependencies
├── static/
│   └── (served automatically by Flask)
├── templates/
│   └── index.html          # Main frontend SPA
└── instance/
    └── (SQLite fallback, if MongoDB unavailable)
```

## Setup Instructions

### 1. Store API Keys in VS Code (.env file)

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_key_here
ELEVENLABS_API_KEY=your_elevenlabs_key_here
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/podcastai
JWT_SECRET=some_random_secret_string_here
FLASK_SECRET_KEY=another_random_secret_string
```

**IMPORTANT:** Add `.env` to your `.gitignore` — never commit API keys!

In VS Code, install the **"Python Dotenv"** extension for auto-loading.
The `python-dotenv` package loads `.env` automatically when the app starts.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

For OCR support (scanned PDFs):
```bash
# macOS
brew install tesseract poppler

# Ubuntu/Debian
sudo apt-get install -y tesseract-ocr poppler-utils

# Windows: download installers from GitHub
# Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
# Poppler: https://github.com/oschwartz10612/poppler-windows
```

### 3. Run the Server
```bash
python app.py
```

App will be available at: http://localhost:5000

### 4. MongoDB Atlas Setup
1. Go to https://cloud.mongodb.com
2. Create a free cluster
3. Create a database user
4. Whitelist your IP (or use 0.0.0.0/0 for dev)
5. Get the connection string and paste into `.env` as MONGO_URI
