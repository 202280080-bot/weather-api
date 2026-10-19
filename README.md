# 🌦️ Weather App

A simple, web-based Weather App built with **Python and Flask** that allows users to check weather information for their selected city. The project also includes **Progressive Web App (PWA)** features, allowing users to install the app through a supported browser.

## 📌 Project Overview

The Weather App provides a user-friendly interface for checking weather information. It uses a Flask backend to process requests and serves the web interface through HTML, CSS, JavaScript, and static assets.

The application includes a web app manifest, a service worker, and app icons to support installation as a PWA.

## ✨ Features

- 🌤️ Check weather information for a city.
- 🔎 Search for weather information through the app interface.
- 📱 Responsive web interface.
- 💻 Python Flask backend.
- 📲 Progressive Web App (PWA) installation support.
- 🎨 Custom app icons and theme colors.
- ⚙️ Web app manifest for app name, display mode, and icons.
- 🚀 Service worker for caching and basic offline support.

> **Note:** Offline functionality depends on what the service worker caches. Weather data that requires an online weather API may not be available without an internet connection.

## 🛠️ Technologies Used

- **Python** — backend programming language
- **Flask** — web framework
- **HTML** — web page structure
- **CSS** — interface styling
- **JavaScript** — client-side functionality
- **JSON** — PWA manifest configuration
- **Service Worker** — caching and PWA support
- **Git and GitHub** — version control and project hosting

## 📂 Project Structure

```text
weather-api/
├── static/
│   ├── icons/
│   │   ├── weather-192.png
│   │   └── weather-512.png
│   ├── screenshots/
│   ├── manifest.json
│   ├── service-worker.js
│   └── weather-icon.svg
├── templates/
│   └── index.html
├── venv/
├── app.py
├── README.md
└── requirements.txt
```

*The structure above represents the expected project layout. Your actual files may differ.*

## ⚙️ Installation and Setup

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/).

During installation on Windows, enable **Add Python to PATH** if the installer offers that option.

### 2. Clone the Repository

If the project is hosted on GitHub, open PowerShell and run:

```powershell
git clone YOUR_GITHUB_REPOSITORY_URL
cd weather-api
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

Alternatively, open your existing project folder.

### 3. Create a Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 6. Run the Application

```powershell
python app.py
```

### 7. Open the App

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Keep the terminal running while using the locally hosted app.

## 📲 Installing the App as a PWA

1. Run the Flask application.
2. Open `http://127.0.0.1:5000/` in Google Chrome.
3. Check the browser menu or address bar for the installation option.
4. Select **Install page as app** or the available installation option.
5. Confirm the installation.

The exact installation option may vary by Chrome version and browser conditions.

The app's PWA configuration is located in `static/manifest.json`. It defines the app name, display mode, theme colors, and icon paths.

## 🔧 Troubleshooting

**The app does not start**

- Make sure Python is installed.
- Activate the virtual environment.
- Install dependencies using `pip install -r requirements.txt`.
- Check the terminal for error messages.

**The PWA installation option is missing**

- Confirm that the manifest is linked correctly in `templates/index.html`.
- Confirm that the service worker is registered.
- Check the browser's Developer Tools for manifest, icon, and service worker errors.
- Ensure the app is served from a supported secure context. Localhost is generally supported for development.

**The app icons do not appear**

Check that these files exist:

```text
static/icons/weather-192.png
static/icons/weather-512.png
```

Then test these URLs while the Flask server is running:

```text
http://127.0.0.1:5000/static/icons/weather-192.png
http://127.0.0.1:5000/static/icons/weather-512.png
```

**Weather information does not load**

Check your internet connection and verify the weather API configuration, if your implementation uses an external API.

## 🔒 Security Notes

- Do not commit API keys, passwords, or other secrets to GitHub.
- Use environment variables for sensitive configuration.
- Do not upload your `venv/` folder to GitHub.
- Ensure `requirements.txt` contains the packages needed to run the project.

## 🚀 Future Improvements

- Improve the app's responsive design.
- Add weather forecasts for upcoming days.
- Display additional weather details such as humidity, wind speed, and feels-like temperature.
- Improve offline access to previously cached app content.
- Add clearer loading indicators and error messages.
- Improve the PWA installation experience with suitable screenshots.

## 👨‍💻 Author

**Project:** Weather App  
**Framework:** Python Flask  
**Purpose:** To provide a simple and accessible way to check weather information through a web application with PWA installation support.

## 📄 License

This project is available for educational and personal use. Add a specific open-source license if you intend to distribute it under particular terms.
