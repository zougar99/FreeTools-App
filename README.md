# 🛠️ FreeTools-App — 25 free Python utility tools: system info, file manager, network scanner, password generator, QR code creator, unit converter and more — all in one desktop app

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/zougar99/FreeTools-App/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/zougar99/FreeTools-App?style=social)](https://github.com/zougar99/FreeTools-App)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue)](https://github.com/zougar99/FreeTools-App)

> 25 free Python utility tools: system info, file manager, network scanner, password generator, QR code creator, unit converter and more — all in one desktop app.

---

## 📖 Table of Contents
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [FAQ](#-faq)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features
- ✔ **25+ Tools** — System info, file manager, network scanner, password generator, QR creator, unit converter, text tools, math tools, and more
- ✔ **Unified Interface** — All tools accessible from a single sidebar menu
- ✔ **Portable** — Single executable, no installation needed
- ✔ **Lightweight** — Runs on any Windows machine, < 50 MB RAM
- ✔ **Export** — Save tool outputs as TXT, CSV, or PDF
- ✔ **Search** — Quick tool search by name or category

---

## 🔮 How It Works

```
  Input ──► Processing Pipeline ──► Output
  ┌────────┐   ┌────────┐   ┌────────┐
  │ Data   │──►│ Engine │──►│ Result │
  │ Source │   │ Logic  │   │        │
  └────────┘   └────────┘   └────────┘
```

1. **Input** — Load data from file, API, or user input
2. **Process** — Core engine applies logic/analysis/transformation
3. **Output** — Results displayed in UI, saved to file, or sent via API

---

## 💻 Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.10+ |
| UI | CustomTkinter |
| Platform | Windows (portable) |
| Packaging | PyInstaller |

---

## 🚀 Installation

```bash
git clone https://github.com/zougar99/FreeTools-App.git
cd FreeTools-App
pip install -r requirements.txt
# Or download the portable exe from Releases
```

---

## 📄 Configuration

Create a `config.yaml` or `.env` file in the project root:

```yaml
# Application settings
debug: false
port: 8080
theme: dark
language: en
```

---

## 🧰 Usage Guide

1. Launch the app
2. Browse or search for a tool
3. Input your data
4. Get instant results
5. Export if needed

---

## 🖼 Screenshots

> *(Screenshots coming soon. PRs welcome!)*

---

## 🔄 Roadmap

- 🟢 Web dashboard
- 🟡 Mobile companion app
- ⚫ API access
- ⚫ Plugin system
- ⚫ Multi-language support

---

## ❓ FAQ

### Are all tools free?
Yes — 100% free, no ads, no premium tiers.

### Can I add my own tools?
Not yet — plugin system is on the roadmap.

---

## 🚧 Troubleshooting

| Problem | Solution |
|---------|----------|
| **App won't start** | Check Python version (3.10+); run `pip install -r requirements.txt` |
| **No output** | Check logs in `logs/` folder; enable debug mode in config |
| **Performance issues** | Close other applications; reduce batch size in config |
| **Dependency errors** | Create fresh venv: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📐 License
Distributed under the **MIT License**. See [`LICENSE`](https://github.com/zougar99/FreeTools-App/blob/main/LICENSE) for more information.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/zougar99">zougar99</a>
</p>
