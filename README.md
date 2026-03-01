# 🚀 Swarm Agents - AI Agent Swarm Framework

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-24.12+-green.svg)](https://nodejs.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **🤖 Мульти-агентная система для совместной работы AI над сложными задачами**

## ✨ Возможности

- 🎭 **5 специализированных агентов**: Supervisor, Architect, Coder, Tester, Researcher
- 🧠 **Единая память роя**: `.swarm_memory/` для совместной работы
- 🔄 **Протокол передачи задач**: Логированная передача между агентами
- 🛠️ **MCP интеграция**: Model Context Protocol серверы
- 📝 **Авто-документация**: Самодокументирующаяся система
- 🎯 **Ролевая модель**: Четкое разделение обязанностей

## 🚀 Быстрый старт

### 📋 Требования
- Python 3.13+
- Node.js 24.12+
- Windsurf IDE или Roo Code

### ⚡ Установка

```bash
# 1. Клонирование
git clone https://github.com/yourusername/swarm-agents.git
cd swarm-agents

# 2. Развертывание
python swarm_deploy.py

# 3. Зависимости
pip install -r requirements.txt

# 4. Настройка
cp .env.example .env
# Добавьте API ключи в .env

# 5. Перезапустите IDE
```

## 🎭 Как работает рой

### 🎯 Инициализация
Откройте проект в Windsurf/Roo Code, выберите **Supervisor** и напишите:
```
Supervisor, инициализируй проект. Прочитай active_state.md и скажи, что делать.
```

### 👥 Агенты роя

| Агент | Роль | 🎯 Задачи |
|-------|------|-----------|
| 👑 **Supervisor** | 🧠 Менеджер | Распределение задач, контроль |
| 🏗️ **Architect** | 📐 Архитектор | Проектирование, технологии |
| 💻 **Coder** | ⌨️ Разработчик | Написание кода |
| 🧪 **Tester** | 🔍 Тестировщик | Поиск багов, тесты |
| 📚 **Researcher** | 🔬 Исследователь | Поиск информации |

### 🔄 Цикл работы
```
📥 READ Context → 🧠 THINK (Sequential) → ⚡ ACT → 📝 UPDATE Log
```

## 📁 Структура проекта

```
swarm-agents/
├── 📁 src/                    # Основной код
├── 📁 tests/                   # Тесты
├── 📁 docs/                    # Документация
├── 📁 tools/                   # 🛠️ Инструменты агентов
├── 📁 .swarm_memory/           # 🧠 Мозг роя
│   ├── 📄 active_state.md      # Текущее состояние
│   ├── 📄 handoff_log.md       # Лог передачи задач
│   ├── 📄 architecture.md      # Архитектурные решения
│   └── 📄 specifications.md   # Технические задания
├── 📁 .roo/                    # Конфигурация Roo Code
├── 📄 swarm_deploy.py          # 🚀 Скрипт развертывания
├── 📄 swarm_cleanup.py         # 🧹 Скрипт очистки
├── 📄 AGENTS_ROLES.md          # 📖 Роли агентов
└── 📄 README.md               # 📚 Документация
```

## 🛠️ Скрипты

### 🚀 Развертывание
```bash
python swarm_deploy.py
```
Создает полную инфраструктуру роя с MCP серверами

### 🧹 Очистка
```bash
python swarm_cleanup.py          # С подтверждением
python swarm_cleanup.py --force   # Без подтверждения
```
Полностью удаляет все следы роя из проекта

## 📖 Пример использования

### 🌐 Создание веб-приложения
```
👤 User: Supervisor, создай Flask приложение с CRUD для задач

🤖 Supervisor: [Planning] [Next Agent]: Architect
🏗️ Architect: Проектирую архитектуру Flask...
🤖 Supervisor: [Delegating] [Next Agent]: Coder  
💻 Coder: Реализую Flask приложение...
🤖 Supervisor: [Reviewing] [Next Agent]: Tester
🧪 Tester: Пишу тесты и проверяю...
🤖 Supervisor: [Complete] Приложение готово! 🎉
```

## ⚙️ Конфигурация

### 🔑 Переменные окружения (.env)
```env
# API ключи
OPENAI_API_KEY=sk-your-openai-key
TAVILY_API_KEY=tvly-your-tavily-key
ANTHROPIC_API_KEY=your-anthropic-key
```

### 🛠️ MCP Серверы
Конфигурация в `.roo/mcp.json`:
- **filesystem**: Работа с файлами
- **memory**: Управление памятью  
- **sequentialthinking**: Последовательное мышление

## 🧪 Тестирование
```bash
# Базовые тесты
python -m pytest tests/ -v

# С покрытием
python -m pytest tests/ --cov=src
```

## 🐛 Troubleshooting

**❌ MCP серверы не запускаются?**
- Установите Node.js
- Перезапустите IDE

**❌ Агенты не видят память роя?**
- Проверьте `.swarm_memory/` папку
- Перезапустите IDE

**❌ Ошибка развертывания?**
```bash
python swarm_cleanup.py --force
python swarm_deploy.py
```

## 📄 Лицензия
[MIT License](LICENSE)

## 🙏 Благодарности
- Model Context Protocol (MCP) 
- Windsurf IDE
- Open-source сообществу

---

**⭐ Если понравилось - поставьте звезду!** 🌟

📧 Вопросы: [your-email@example.com](mailto:your-email@example.com)
