# 🛠️ Free Tools Application

A comprehensive collection of **25 free utility tools** for everyday tasks.  
All tools are Python-based CLI scripts with a unified menu launcher.

---

## ✨ Features

### 🖥️ System Tools
| # | Tool | Description |
|---|------|-------------|
| 1 | **System Info** | OS, hostname, Python version, CPU, memory |
| 16 | **Stats** | Directory statistics & file type analysis |
| 20 | **Updater** | Check for latest version on GitHub |

### 📁 File Management
| # | Tool | Description |
|---|------|-------------|
| 2 | **File Manager** | Navigate, create, delete files & directories |
| 5 | **Archive Extractor** | Extract ZIP, TAR, GZ, BZ2, XZ archives |
| 11 | **CSV Viewer** | Display CSV file contents |
| 12 | **Image Info** | Get image metadata (dimensions, format, ratio) |
| 18 | **Config Editor** | Edit configuration files |

### 🌐 Network Tools
| # | Tool | Description |
|---|------|-------------|
| 3 | **Scanner** | Port scanner & local file scanner |
| 4 | **Web Server** | Simple HTTP file server |
| 7 | **URL Checker** | Check URL reachability & status |
| 24 | **Domain Checker** | Domain IP lookup & WHOIS info |

### 🔒 Security Tools
| # | Tool | Description |
|---|------|-------------|
| 6 | **Password Generator** | Generate cryptographically secure passwords |
| 10 | **Hash Generator** | MD5, SHA1, SHA256, SHA512 hashes |

### 📊 Data Tools
| # | Tool | Description |
|---|------|-------------|
| 8 | **JSON Formatter** | Format & validate JSON data |
| 9 | **Base64 Tool** | Encode / Decode Base64 |
| 19 | **Validators** | Validate email, phone, URL, IP address |

### 📝 Productivity
| # | Tool | Description |
|---|------|-------------|
| 13 | **Notes** | Multi-line notes manager |
| 14 | **Contact Manager** | Add, list, delete contacts |
| 15 | **Automation** | Schedule & run shell commands |
| 17 | **Logger** | Application logging with levels |

### 🧰 Utilities
| # | Tool | Description |
|---|------|-------------|
| 21 | **Wordlist Generator** | Generate character combination wordlists |
| 22 | **Weather** | Check weather via OpenWeatherMap API |
| 23 | **Text Tools** | Uppercase, lowercase, reverse, count |
| 25 | **QR Code Generator** | Generate QR codes (PNG or terminal text) |

---

## 🚀 Installation

```bash
cd FreeTools-App
pip install -r requirements.txt
```

Or install individual dependencies:

```bash
pip install rich          # 👑 Colored UI (recommended)
pip install pillow        # 🖼️ Image tools
pip install python-whois  # 🌐 Domain checker
pip install qrcode[pil]   # 📱 QR Code Generator
```

## 🎮 Usage

```bash
python main.py
```

Select a tool by entering its number from the interactive menu.

### 🎨 With Rich UI
If `rich` is installed, the menu displays with **colors**, **tables**, and **category grouping**.

### 📟 Without Rich UI
If `rich` is not installed, the app falls back to a clean plain-text menu automatically.

---

## ⚠️ Notes

- **Weather** tool requires setting `OWM_API_KEY` environment variable (get a free key at https://openweathermap.org/api)
- **QR Code Generator** needs `pip install qrcode[pil]`
- **Domain Checker** needs `pip install python-whois`
- All config files (`tasks.txt`, `contacts.json`, `notes.txt`, `app.log`) are saved in the current working directory

---

## 📦 Requirements

| Package | Version | Used By |
|---------|---------|---------|
| Python | 3.7+ | Core |
| rich | ≥13.0 | UI (optional) |
| pillow | ≥10.0 | Image Info, QR Code (optional) |
| python-whois | ≥0.9 | Domain Checker (optional) |
| qrcode[pil] | latest | QR Code Generator (optional) |

---

## 📄 License

Free to use - MIT License
