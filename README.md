# 🤖 Swarm Agents - AI Agent Swarm Framework

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **🚀 Мульти-агентная система на базе Roo Code + Ollama для локальной разработки**

## 🎯 Концепция

**Swarm Agents** - это фреймворк для создания роев AI-агентов, работающих на **локальных моделях Ollama** через расширение **Roo Code**. Система позволяет нескольким специализированным агентам совместно решать сложные задачи с единым контекстом и координацией.

## 🏗️ Архитектура

### 🧠 Технологический стек

| Компонент | Технология | Назначение |
|-----------|------------|------------|
| **IDE** | **Roo Code** | Расширение для VS Code с поддержкой агентов |
| **LLM** | **Ollama Models** | Локальные модели (llama3, mistral, codellama) |
| **Координация** | **Handoff Protocol** | Передача контекста между агентами |
| **Память** | **Markdown Files** | Единая база знаний роя |
| **Интеграция** | **MCP Servers** | Model Context Protocol для инструментов |

### 🔄 Архитектурные паттерны

```
┌─────────────────────────────────────────────────────────────┐
│                    ROO CODE IDE                             │
├─────────────────────────────────────────────────────────────┤
│  👑 Supervisor  🏗️ Architect  💻 Coder  🧪 Tester  🔍 Researcher  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    🧠 SHARED MEMORY                         │
│  ┌─────────────────┬─────────────────┬─────────────────┐    │
│  │ active_state.md │ handoff_log.md  │ architecture.md │    │
│  └─────────────────┴─────────────────┴─────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  🦙 OLLAMA LLM SERVER                        │
│  ┌─────────────────┬─────────────────┬─────────────────┐    │
│  │    llama3       │    mistral      │   codellama     │    │
│  └─────────────────┴─────────────────┴─────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 🎭 Агенты роя

### 👑 **Supervisor** - Менеджер проекта
- **Роль**: Распределение задач и контроль качества
- **Навыки**: Проектный менеджмент, декомпозиция задач
- **Модель**: `llama3:instruct` (лучше всего подходит для планирования)

### 🏗️ **Architect** - Системный архитектор  
- **Роль**: Проектирование архитектуры и выбор технологий
- **Навыки**: System design, паттерны проектирования
- **Модель**: `mistral:instruct` (хорошо анализирует сложные системы)

### 💻 **Coder** - Разработчик
- **Роль**: Написание кода и реализация функционала
- **Навыки**: Программирование, рефакторинг, отладка
- **Модель**: `codellama:instruct` (специализированная для кода)

### 🧪 **Tester** - QA инженер
- **Роль**: Тестирование и поиск багов
- **Навыки**: Unit тесты, интеграционное тестирование
- **Модель**: `llama3:instruct` (детальный анализ)

### 🔍 **Researcher** - Исследователь
- **Роль**: Поиск информации и анализ технологий
- **Навыки**: Research, анализ данных, документация
- **Модель**: `mistral:instruct` (хорошо с большими объемами текста)

## 🚀 Быстрый старт

### 📋 Требования
- **Python 3.13+**
- **Ollama** с установленными моделями
- **Roo Code** расширение для VS Code

### ⚡ Установка Ollama

```bash
# Установка Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Загрузка моделей
ollama pull llama3:instruct
ollama pull mistral:instruct  
ollama pull codellama:instruct

# Проверка
ollama list
```

### 🔧 Настройка Roo Code

1. **Установите Roo Code** из маркетплейса VS Code
2. **Настройте Ollama** в настройках Roo Code:
```json
{
  "rooCode.modelProvider": "ollama",
  "rooCode.ollamaBaseUrl": "http://localhost:11434",
  "rooCode.defaultModel": "llama3:instruct"
}
```

3. **Создайте профили агентов** в Roo Code:
```json
{
  "profiles": {
    "supervisor": {
      "model": "llama3:instruct",
      "systemPrompt": "Ты - Supervisor. Ты управляешь роем агентов..."
    },
    "architect": {
      "model": "mistral:instruct", 
      "systemPrompt": "Ты - Architect. Ты проектируешь системы..."
    },
    "coder": {
      "model": "codellama:instruct",
      "systemPrompt": "Ты - Coder. Ты пишешь код..."
    }
  }
}
```

### 🎯 Развертывание роя

```bash
# Клонирование и запуск
git clone https://github.com/yourusername/swarm-agents.git
cd swarm-agents
python swarm_deploy.py
```

**❌ Ошибка развертывания?**
```bash
# Если что-то пошло не так, можно запустить очистку и развернуть заново
python swarm_cleanup.py --force
python swarm_deploy.py
```

### 🧹 Очистка проекта
После развертывания роя создается скрипт `swarm_cleanup.py` для полного удаления всех следов агентового роя:
```bash
python swarm_cleanup.py          # С подтверждением
python swarm_cleanup.py --force   # Без подтверждения
```

## 🔄 Протокол работы

### 📥 **Фаза 1: Инициализация**
```
User → Supervisor: "Создай CRUD приложение для задач"
Supervisor → .swarm_memory/active_state.md: "Проанализирован запрос..."
```

### 🧠 **Фаза 2: Планирование** 
```
Supervisor → Architect: "Спроектируй архитектуру Flask CRUD"
Architect → .swarm_memory/architecture.md: "Архитектура: MVC паттерн..."
```

### ⚡ **Фаза 3: Реализация**
```
Supervisor → Coder: "Реализуй Flask приложение по спецификации"
Coder → .swarm_memory/handoff_log.md: "Созданы models.py, routes.py..."
```

### 🔍 **Фаза 4: Тестирование**
```
Supervisor → Tester: "Протестируй CRUD функциональность"
Tester → .swarm_memory/qa_checklist.md: "Тесты пройдены, найдены баги..."
```

## 🛠️ Продвинутые техники

### 🧠 **Sequential Thinking**
Используйте MCP сервер `sequentialthinking` для сложных задач:
```python
# Интеграция с Ollama через MCP
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "node",
      "args": ["./tools/mcp-servers/src/sequentialthinking/dist/index.js"]
    }
  }
}
```

### 📊 **Оптимизация моделей**
- **llama3:instruct** - для планирования и менеджмента
- **mistral:instruct** - для архитектуры и исследований  
- **codellama:instruct** - для программирования
- **qwen:coder** - альтернатива для кода

### 🔄 **Handshake Protocol**
```markdown
## 🤝 HANDOFF LOG
**[Supervisor] → [Coder]:** Реализуй Flask CRUD по спецификации
**[Coder] → [Tester]:** Функционал готов в app.py, нужно тестирование
**[Tester] → [Supervisor]:** Найден баг в delete endpoint, исправьте
```

## 📖 Примеры использования

### 🌐 **Веб-приложение**
```
👤 User: Supervisor, создай блог на Django с авторизацией

🤖 Supervisor: [Planning] → Architect
🏗️ Architect: Спроектирую Django с JWT аутентификацией...
🤖 Supervisor: [Delegating] → Coder
💻 Coder: Создаю models.py, views.py, serializers.py...
🤖 Supervisor: [Reviewing] → Tester  
🧪 Tester: Пишу тесты для API endpoints...
🎉 Result: Готовое Django приложение!
```

### 📱 **Мобильное приложение**
```
👤 User: Supervisor, сделай React Native todo app

🤖 Supervisor: [Planning] → Architect
🏗️ Architect: Sproektiruyu React Native + Redux...
🤖 Supervisor: [Delegating] → Coder
💻 Coder: Sozdavayu components, screens, store...
🤖 Supervisor: [Reviewing] → Tester
🧪 Tester: Testiruyu na iOS i Android...
🎉 Result: Rabochee mobile app!
```

## ⚙️ Конфигурация

### 🦙 **Ollama модели**
```bash
# Рекомендуемые модели
ollama pull llama3:instruct      # 8B параметров, универсальная
ollama pull mistral:instruct     # 7B параметров, быстрая  
ollama pull codellama:instruct    # 7B параметров, для кода
ollama pull qwen:coder           # 7B параметров, альтернатива

# Для продвинутых пользователей
ollama pull llama3:70b-instruct  # 70B параметров, максимальное качество
```

### 🔧 **Roo Code настройки**
```json
{
  "rooCode": {
    "modelProvider": "ollama",
    "ollamaBaseUrl": "http://localhost:11434",
    "temperature": 0.7,
    "maxTokens": 4096,
    "contextWindow": 8192
  }
}
```

## 🐛 Troubleshooting

**❌ Ollama не отвечает?**
```bash
# Проверка статуса
ollama ps
ollama serve

# Перезапуск
sudo systemctl restart ollama
```

**❌ Roo Code не видит Ollama?**
- Проверьте настройки в VS Code
- Убедитесь что `http://localhost:11434` доступен
- Перезапустите VS Code

**❌ Модель работает медленно?**
- Используйте более маленькие модели (7B вместо 70B)
- Увеличьте RAM на сервере Ollama
- Используйте GPU ускорение

## 🎯 Лучшие практики

### 🏗️ **Архитектурные решения**
- **MVC паттерн** для веб-приложений
- **Microservices** для сложных систем  
- **Clean Architecture** для enterprise проектов
- **Serverless** для простых сервисов

### 🛠️ **Технологический выбор**
- **Python/Django** для сложных веб-систем
- **React/Next.js** для фронтенда
- **PostgreSQL** для реляционных данных
- **MongoDB** для гибких структур
- **Docker** для контейнеризации

### 📊 **Производительность**
- **Кэширование** с Redis
- **Асинхронность** с asyncio
- **Оптимизация запросов** к БД
- **CDN** для статики

## 📄 Лицензия

[MIT License](LICENSE)

## 🙏 Благодарности

- **Ollama** за локальные LLM модели
- **Roo Code** за расширение VS Code
- **Meta AI** за Llama 3
- **Mistral AI** за Mistral модели
- **Open-source сообществу**

---

**⭐ Если понравилось - поставьте звезду!** 🌟

📧 Вопросы: [your-email@example.com](mailto:your-email@example.com)
