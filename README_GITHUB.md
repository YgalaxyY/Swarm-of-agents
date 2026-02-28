# 🚀 Swarm Agents - AI Agent Swarm Framework

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Node.js](https://img.shields.io/badge/Node.js-24.12+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Swarm Agents** - это фреймворк для создания и управления роем AI-агентов, работающих вместе для решения сложных задач.

## ✨ Особенности

- 🤖 **Multi-Agent System**: Supervisor, Architect, Coder, Tester, Researcher
- 🧠 **Shared Memory**: Единая база знаний для всех агентов
- 🔄 **Handoff Protocol**: Логированная передача задач между агентами
- 🛠️ **MCP Integration**: Model Context Protocol серверы для расширенных возможностей
- 📝 **Auto-Documentation**: Автоматическое создание документации
- 🎯 **Role-Based**: Четкое разделение обязанностей между агентами

## 🚀 Быстрый старт

### Требования
- Python 3.13+
- Node.js 24.12+
- Windsurf IDE или Roo Code

### Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/swarm-agents.git
   cd swarm-agents
   ```

2. **Запустите развертывание:**
   ```bash
   python deploy_swarm_complete2.0.py
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения:**
   ```bash
   cp .env.example .env
   # Добавьте ваши API ключи в .env файл
   ```

5. **Перезапустите IDE** (Windsurf/Roo Code)

## 🎭 Как работает рой

### 1. Инициализация
Откройте проект в Windsurf/Roo Code, выберите режим **Supervisor** и напишите:
```
Supervisor, инициализируй проект. Прочитай active_state.md и скажи, что делать.
```

### 2. Структура агентов

| Агент | Роль | Основные задачи |
|-------|------|-----------------|
| 👑 **Supervisor** | Менеджер | Распределение задач, контроль качества |
| 🏗️ **Architect** | Архитектор | Проектирование, выбор технологий |
| 💻 **Coder** | Разработчик | Написание кода, реализация |
| 🧪 **Tester** | Тестировщик | Поиск багов, написание тестов |
| 🔍 **Researcher** | Исследователь | Поиск информации, анализ |

### 3. Цикл работы
```
READ Context → THINK (Sequential) → ACT → UPDATE Log
```

## 📁 Структура проекта

```
swarm-agents/
├── src/                    # Основной код проекта
├── tests/                   # Тесты
├── docs/                    # Документация
├── scripts/                 # Скрипты автоматизации
├── tools/                   # Инструменты агентов
│   ├── clean_memory.py      # Очистка памяти
│   ├── web_search.py        # Веб-поиск
│   ├── update_state.py      # Обновление статуса
│   └── mcp-servers/         # MCP серверы
├── .swarm_memory/           # 🧠 Мозг роя
│   ├── active_state.md      # Текущее состояние
│   ├── handoff_log.md       # Лог передачи задач
│   ├── architecture.md      # Архитектурные решения
│   ├── specifications.md   # Технические задания
│   ├── qa_checklist.md      # Чек-лист QA
│   └── archive/             # Архив состояний
├── .roo/                    # Конфигурация Roo Code
│   └── mcp.json            # MCP серверы
├── .windsurfrules          # Правила Windsurf
├── AGENTS_ROLES.md          # Описание ролей агентов
├── deploy_swarm_complete.py     # Скрипт развертывания v1
├── deploy_swarm_complete2.0.py  # Скрипт развертывания v2
└── README.md               # Документация
```

## 🛠️ Доступные инструменты

### Встроенные скрипты
- `deploy_swarm_complete2.0.py` - Основной скрипт развертывания
- `deploy_swarm_complete.py` - Упрощенная версия

### Инструменты агентов
- `tools/clean_memory.py` - Очистка памяти роя
- `tools/web_search.py` - Умный веб-поиск
- `tools/update_state.py` - Быстрое обновление статуса

### MCP Серверы
- **filesystem**: Работа с файловой системой
- **memory**: Управление памятью
- **sequentialthinking**: Последовательное мышление

## 📖 Пример использования

### Создание веб-приложения
```
User: Supervisor, создай простое веб-приложение на Flask с CRUD операциями для задач

Supervisor: [Planning] [Next Agent]: Architect
Architect: Проектирую архитектуру Flask приложения...
Supervisor: [Delegating] [Next Agent]: Coder  
Coder: Реализую Flask приложение с моделями...
Supervisor: [Reviewing] [Next Agent]: Tester
Tester: Пишу тесты и проверяю функциональность...
Supervisor: [Complete] Приложение готово к использованию!
```

## 🔧 Конфигурация

### MCP Серверы
Конфигурация находится в `.roo/mcp.json`:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "memory": {
      "command": "npx", 
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "sequentialthinking": {
      "command": "node",
      "args": ["./tools/mcp-servers/src/sequentialthinking/dist/index.js"]
    }
  }
}
```

### Переменные окружения
Создайте `.env` файл:
```env
# API ключи
OPENAI_API_KEY=sk-your-openai-key
TAVILY_API_KEY=tvly-your-tavily-key

# Другие ключи
ANTHROPIC_API_KEY=your-anthropic-key
GOOGLE_API_KEY=your-google-key
```

## 🧪 Тестирование

Запустите тесты:
```bash
# Базовые тесты
python -m pytest tests/ -v

# С покрытием
python -m pytest tests/ --cov=src
```

## 🤝 Вклад в проект

1. Fork проекта
2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📝 Документация

- [AGENTS_ROLES.md](./AGENTS_ROLES.md) - Подробное описание ролей агентов
- [Примеры использования](./docs/examples/) - Реальные кейсы
- [API Reference](./docs/api/) - Техническая документация

## 🐛 Troubleshooting

### Частые проблемы

**Q: MCP серверы не запускаются**
A: Убедитесь что Node.js установлен и перезапустите IDE

**Q: Агенты не видят память роя**  
A: Проверьте что `.swarm_memory` папка существует и не пуста

**Q: Ошибка при развертывании**
A: Запустите с флагом `--cleanup` и попробуйте снова:
```bash
python deploy_swarm_complete2.0.py --cleanup
python deploy_swarm_complete2.0.py
```

## 📄 Лицензия

Этот проект лицензирован под MIT License - см. [LICENSE](LICENSE) файл для деталей.

## 🙏 Благодарности

- Model Context Protocol (MCP) за стандарт взаимодействия
- Windsurf IDE за поддержку агентов
- Сообществу open-source за вдохновение

---

**⭐ Если проект вам понравился, поставьте звезду!**

📧 Для вопросов и предложений: [your-email@example.com](mailto:your-email@example.com)
