# Mizzou Campus Life App

A Flask web app that helps new and returning University of Missouri students explore campus life. Browse category guides for dining, housing, transportation, academics, student organizations, events, and health services, use an interactive campus map, or ask the built-in Claude chatbot questions about anything not covered in the guides.

## Prerequisites

- **Python 3.9 or newer** (Flask 3.x requires Python 3.9+)
- **Anthropic API key** for the chatbot feature:
  1. Create an account at [console.anthropic.com](https://console.anthropic.com/).
  2. Open **API Keys** in the dashboard.
  3. Create a new key and copy it — you will add it to your `.env` file during setup.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/mizzou-campus-life-app-claude.git
   cd mizzou-campus-life-app-claude
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy the example env file and fill in your values:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set at minimum:

   ```env
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   FLASK_ENV=development
   SECRET_KEY=change_this_to_a_random_secret_key
   ```

   Do not commit `.env` — it contains secrets.

## How to Run

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## What to Expect

When the app is running, you get a local web site with a home page and navigation to each section.

**Browsing the guides**

- From the home page, click a category card (Dining, Housing, Transportation, Academics, Student Orgs, Events, Health) or use the nav bar.
- **Input:** Click links and scroll through the page — no forms required.
- **Output:** Static guide content loaded from JSON (hours, locations, tips, links, and similar campus-life info).

**Campus map**

- Go to **Map** in the navigation.
- **Input:** Click landmarks on the map.
- **Output:** Details for each campus location (name, description, and related info from `data/map.json`).

**Chatbot**

- Click **Ask a Question** on the home page or open **Chatbot** in the nav.
- **Input:** Type a question about Mizzou campus life (e.g. “Where can I eat on campus late at night?” or “How do I join a student org?”) and press send. You can ask follow-up questions in the same conversation.
- **Output:** A text reply from Claude, tailored as a Mizzou campus guide. If `ANTHROPIC_API_KEY` is missing or invalid, the chatbot returns a configuration or API error message instead of a normal answer.

The category pages and map work without an API key; only the chatbot requires a valid Anthropic key.
