# 💊 TrueMeds Medicine Scraper (Flask + Selenium)

This project is a web-based application that scrapes medicine data from [TrueMeds.in](https://www.truemeds.in) using **Selenium** and displays it through a **Flask** web interface.

---

## 📸 Features

- Input a search query (like `A`, `B`, or `Paracetamol`)
- Scrapes:
  - ✅ Medicine name
  - ✅ Manufacturer
  - ✅ Quantity
  - ✅ Price
  - ✅ Image link
- Displays results in a clean HTML table
- Built with Flask and runs headless in Selenium for dynamic JS content rendering

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/gautamdhw/web_scraper.git
cd web_scraper
```

### 2. Install Dependencies

Use pip to install the required packages:

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure Google Chrome is installed and matches the version of [ChromeDriver](https://sites.google.com/chromium.org/driver/).

### 3. Run the Flask App

```bash
python app.py
```

Once running, open your browser and go to:

```
http://127.0.0.1:5000
```

You can now search for medicines and view the scraped data.
