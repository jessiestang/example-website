# BigQuery Release Radar

A modern, glassmorphic web dashboard built using **Python Flask** and **vanilla HTML/CSS/JS** to fetch, parse, and browse BigQuery Release Notes, with the ability to share individual updates directly to X (formerly Twitter).

## Features

- **Live Feed Parsing**: Fetches the official Google Cloud BigQuery release notes XML feed in real-time, parsing individual entries and categorization types dynamically.
- **Glassmorphic UI**: Beautiful dark theme design using CSS variables, custom typography (`Plus Jakarta Sans`), and vibrant, type-specific badges (Features, Announcements, Issues, Deprecations).
- **Search & Filter**: Fast client-side filtering by update types and text search through the release notes.
- **Share to X (Twitter)**: Interactive sharing modal mimicking a real tweet composer with a 280-character counter, allowing users to customize updates before posting using the Twitter Web Intent API.
- **Interactive Spinner & Loading States**: Clean visual feedback during feed refresh.

## Project Structure

- `app.py` - Flask backend that fetches the XML feed, splits items by tag, and serves the static assets.
- `templates/index.html` - Vanilla frontend client with advanced styling, modals, and dynamic rendering logic.
- `requirements.txt` - Backend Python dependencies.
- `.gitignore` - Standard Python and OS level ignore patterns.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jessiestang/example-website.git
   cd example-website
   ```

2. Create a virtual environment and activate it:
   ```bash
   # Windows:
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.
