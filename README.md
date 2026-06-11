# SOC Lab Launcher

## 🇬🇧 English

SOC Lab Launcher is a Python project that automatically prepares a personal SOC (Security Operations Center) lab environment.

The launcher checks VirtualBox virtual machines, starts them if needed, launches selected applications, opens Splunk Web, and writes activity logs.

### Features

* Check VirtualBox VM status
* Start virtual machines automatically
* Launch desktop applications
* Open Splunk Web interface
* Activity logging
* Startup time measurement
* Modular project structure

### Technologies

* Python
* VirtualBox
* Splunk
* subprocess
* logging

### Project Structure

```text
SOC_Lab_launcher/
│
├── main.py
├── config_example.py
├── vm_manager.py
├── app_launcher.py
├── file_checker.py
├── logger.py
├── ui.py
│
├── logs/
│
└── README.md
```

### Quick Start

1. Clone the repository.

2. Rename:

```text
config_example.py
```

to:

```text
config.py
```

3. Open `config.py` and replace the example paths with paths from your system.

Example:

```python
OBSIDIAN_PATH = r"C:\Path\To\Obsidian.exe"
CHROME_PATH = r"C:\Path\To\chrome.exe"
VBOXMANAGE_PATH = r"C:\Path\To\VBoxManage.exe"
```

4. Run:

```bash
python main.py
```

### Example Output

```text
=== HELLIX'S SOC LAB LAUNCHER ===

Windows 10 is already running
kali is already running

Started: chrome.exe
Opened: http://localhost:8000

SOC Lab Ready in 0.59 seconds
```

### Notes

This project was created as a personal learning project for SOC analyst internship preparation and Python automation practice.

---

## 🇷🇺 Русский

SOC Lab Launcher — это Python-проект для автоматической подготовки собственной лаборатории SOC (Security Operations Center).

Программа проверяет виртуальные машины VirtualBox, запускает их при необходимости, открывает нужные приложения, запускает веб-интерфейс Splunk и ведёт журнал действий.

### Возможности

* Проверка состояния виртуальных машин VirtualBox
* Автоматический запуск виртуальных машин
* Запуск приложений Windows
* Открытие веб-интерфейса Splunk
* Ведение логов
* Подсчёт времени запуска
* Модульная структура проекта

### Используемые технологии

* Python
* VirtualBox
* Splunk
* subprocess
* logging

### Структура проекта

```text
SOC_Lab_launcher/
│
├── main.py
├── config_example.py
├── vm_manager.py
├── app_launcher.py
├── file_checker.py
├── logger.py
├── ui.py
│
├── logs/
│
└── README.md
```

### Быстрый запуск

1. Склонируйте репозиторий.

2. Переименуйте файл:

```text
config_example.py
```

в:

```text
config.py
```

3. Откройте `config.py` и замените примерные пути на пути вашей системы.

Пример:

```python
OBSIDIAN_PATH = r"C:\Путь\К\Obsidian.exe"
CHROME_PATH = r"C:\Путь\К\chrome.exe"
VBOXMANAGE_PATH = r"C:\Путь\К\VBoxManage.exe"
```

4. Запустите программу:

```bash
python main.py
```

### Пример вывода

```text
=== HELLIX'S SOC LAB LAUNCHER ===

Windows 10 уже запущена
kali уже запущена

Запущено: chrome.exe
Открыт: http://localhost:8000

SOC Lab готов за 0.59 секунды
```

### Примечание

Проект создан в учебных целях для подготовки к стажировке SOC Analyst и практики автоматизации на Python.
