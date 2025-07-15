# 🎵 Django Music Player

A simple yet functional music player website built using the Django web framework. This music player allows users to stream and control playback of randomly selected music tracks, with basic navigation controls including **Next**, **Previous**, and **Stop**.

## 🚀 Features

- 🎼 Play random music from a predefined list
- ⏭️ Navigate between tracks with Next and Previous buttons
- ⏹️ Stop playback anytime
- 🔄 Auto-refresh playlist options (optional future update)
- 🎧 Clean and minimal UI for smooth interaction

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Audio Playback**: HTML5 `<audio>` element
- **Database**: SQLite (default Django DB)

## 📸 Screenshots

*(Add screenshots here once available)*

## 🧑‍💻 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-music-player.git
   cd django-music-player
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations and run the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
5. Open your browser and go to http://127.0.0.1:8000/ to use the player.


Adding Music Files
Place your .mp3 or audio files in the media/music/ directory (you may need to create this).

Make sure the Django project is configured to serve media files in development.


📂 Project Structure
django-music-player/
├── musicplayer/          # Main Django app
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
├── media/
│   └── music/            # Your audio files go here
├── manage.py
└── requirements.txt

📌 To-Do
 Add playlist support

 Add volume control

 Add user login & personal playlists

 Improve mobile responsiveness

 Deploy to Heroku or Render

📃 License
This project is open-source and available under the MIT License.

 
