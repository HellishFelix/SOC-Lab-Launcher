# SOC Lab Launcher
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Windows](https://img.shields.io/badge/Platform-Windows-blue)
![Vosk](https://img.shields.io/badge/Speech-Vosk-green)
![VirtualBox](https://img.shields.io/badge/VirtualBox-Automation-orange)
![Splunk](https://img.shields.io/badge/Splunk-SIEM-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Voice-Activated SOC Lab Automation Tool

Automatically launches VirtualBox VMs, applications, and Splunk with a single command or voice activation using Vosk.

---

🇬🇧 English | [🇷🇺 Русский](#-русский)

---

## Features

- Start VirtualBox virtual machines
- Launch required applications
- Open Splunk dashboard automatically
- Startup logging
- Voice activation using Vosk
- Configurable microphone selection
- Lightweight and beginner-friendly codebase
- Pre-launch environment validation
- Cloudflare WARP detection

---

## Project Structure

```text
SOC-Lab-Launcher/
│
├── main.py
├── voice_listener.py
├── vm_manager.py
├── app_launcher.py
├── logger.py
├── config_example.py
├── list_microphones.py
│
├── models/
│   └── vosk-model-small-ru-0.22
│
├── logs/
│   └── .gitkeep
│
└── README.md
```

---

## Requirements

- Python 3.12+
- VirtualBox
- Splunk
- Google Chrome
- Vosk

Install dependencies:

```bash
py -m pip install vosk sounddevice
```

---

## Environment Validation

Before launching the SOC Lab, the application performs environment validation checks.

Current validation includes:

* Cloudflare WARP detection
* Prevention of launching Splunk in known problematic network configurations

If Cloudflare WARP is detected, the launcher displays a warning message and terminates automatically.


---

## Vosk Setup

Voice activation requires a Vosk speech recognition model.

Recommended model:

```text
vosk-model-small-ru-0.22
```

Download the model and place it into:

```text
SOC-Lab-Launcher/
└── models/
    └── vosk-model-small-ru-0.22
```

---

## Configuration

Rename:

```text
config_example.py
```

to:

```text
config.py
```

Then edit:

```python
OBSIDIAN_PATH = r"PATH_TO_OBSIDIAN"
CHROME_PATH = r"PATH_TO_CHROME"
VBOXMANAGE_PATH = r"PATH_TO_VBOXMANAGE"
```

---

## Voice Activation

Default wake phrase:

```text
просыпайся папочка вернулся
```

Microphone configuration:

```python
MICROPHONE_ID = None
```

To find your microphone ID:

```bash
py list_microphones.py
```

---

## Quick Start

Start SOC Lab manually:

```bash
py main.py
```

Start voice listener:

```bash
py voice_listener.py
```

Say:

```text
просыпайся папочка вернулся
```

SOC Lab will launch automatically.

---

## Example Output

```text
[VOICE] Wake phrase detected
[VOICE] Starting SOC Lab...

=== HELIX'S SOC LAB LAUNCHER ===

Windows 10 is already running
kali is already running

Started: Obsidian.exe
Started: chrome.exe

Opened: http://localhost:8000

SOC Lab Ready in 0.67 seconds
```

---

## License

This project is licensed under the MIT License.

---

# 🇷🇺 Русский

[🇬🇧 English](#soc-lab-launcher)

---

## Возможности

- Запуск виртуальных машин VirtualBox
- Автоматический запуск приложений
- Автоматическое открытие Splunk
- Ведение логов запуска
- Голосовая активация через Vosk
- Настройка микрофона
- Простая структура проекта
- Проверка окружения перед запуском
- Обнаружение Cloudflare WARP

---

## Требования

- Python 3.12+
- VirtualBox
- Splunk
- Google Chrome
- Vosk

Установка зависимостей:

```bash
py -m pip install vosk sounddevice
```

---

## Проверка окружения

Перед запуском SOC Lab приложение выполняет проверку окружения.

На данный момент реализованы:

* Обнаружение Cloudflare WARP
* Предотвращение запуска Splunk в заведомо проблемной сетевой конфигурации

Если обнаружен активный Cloudflare WARP, лаунчер выводит предупреждение и автоматически завершает работу.


---

## Настройка Vosk

Для голосовой активации необходимо скачать модель Vosk.

Рекомендуемая модель:

```text
vosk-model-small-ru-0.22
```

После скачивания поместите её в папку:

```text
SOC-Lab-Launcher/
└── models/
    └── vosk-model-small-ru-0.22
```

---

## Настройка проекта

Переименуйте:

```text
config_example.py
```

в:

```text
config.py
```

и укажите свои пути:

```python
OBSIDIAN_PATH = r"PATH_TO_OBSIDIAN"
CHROME_PATH = r"PATH_TO_CHROME"
VBOXMANAGE_PATH = r"PATH_TO_VBOXMANAGE"
```

---

## Голосовая активация

Фраза по умолчанию:

```text
просыпайся папочка вернулся
```

Для поиска микрофона выполните:

```bash
py list_microphones.py
```

После этого укажите нужный ID:

```python
MICROPHONE_ID = 2
```

или используйте:

```python
MICROPHONE_ID = None
```

для микрофона по умолчанию.

---

## Быстрый запуск

Ручной запуск:

```bash
py main.py
```

Голосовой запуск:

```bash
py voice_listener.py
```

После произнесения:

```text
просыпайся папочка вернулся
```

лаборатория будет запущена автоматически.

---

## Лицензия

Проект распространяется по лицензии MIT.