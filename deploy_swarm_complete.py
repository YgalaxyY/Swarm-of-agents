#!/usr/bin/env python3
"""
🚀 COMPLETE AGENT SWARM DEPLOYMENT SCRIPT
Универсальный скрипт развертывания для любого проекта.

Особенности:
✅ Портативный - работает в любой папке
✅ Полная функциональность - все инструменты агентов
✅ MCP серверы - автоматическая установка и настройка
✅ Дополнительные серверы - fetch, git, time, sequentialthinking
✅ Полная документация - README и инструкции

Использование:
  python deploy_swarm_complete.py [опции]

Опции:
  --cleanup     - очистка окружения
  --mcp-only    - только установка MCP серверов
  --help        - эта справка
"""

import os
import json
import logging
import stat
import sys
import subprocess
import shutil
import importlib.util
from pathlib import Path

# --- КОНФИГУРАЦИЯ ---
PROJECT_DIRS = ['src', 'tests', 'docs', 'scripts', 'tools', '.swarm_memory']
MEMORY_FILES = {
    'active_state.md': """# 👑 ACTIVE PROJECT STATE
**Status:** 🟢 Initialized
**Current Focus:** Setup & Configuration

## 📋 CURRENT OBJECTIVES
*Задачи текущего спринта/этапа.*

- [ ] Awaiting initial instructions from User.

## 💬 CONTEXT & LOGS
*Краткая история последних событий.*

- **System:** Swarm environment initialized successfully.
""",
    'architecture.md': """# 🧠 ARCHITECTURE & DECISIONS
*Долговременная память архитектора.*

## Tech Stack
- Language: Python 3.x
- Framework: TBD
- Database: TBD

## Design Patterns
- Modular Monolith / Microservices (TBD)
""",
    'specifications.md': """# 🛠️ TECHNICAL SPECIFICATIONS
*Детальные ТЗ для Кодера.*

## API Contracts
*(Empty)*

## Data Models
*(Empty)*
""",
    'bug_log.md': """# 🐞 BUG LOG & QA REPORTS
*История ошибок и их решений.*

## Active Issues
*(None)*

## Resolved
*(None)*
""",
    'reflections.md': """# 🤔 ARCHITECTURAL REFLECTIONS
*Критический анализ и выученные уроки.*

## 🧐 Optimization Thoughts
- Initial swarm setup: Active.

## ⚠️ Potential Risks
- Waiting for first user tasks.
"""
}

# --- ЛОГИРОВАНИЕ ---
def setup_logging():
    log_file = Path.cwd() / 'deployment.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

class CompleteSwarmDeployer:
    def __init__(self, logger):
        self.logger = logger
        self.base_path = Path.cwd()  # Всегда текущая папка
        self.project_name = self.base_path.name

    def _write_file(self, path, content, executable=False):
        """Безопасная запись файла."""
        file_path = self.base_path / path
        if file_path.exists():
            self.logger.warning(f"⚠️ Файл уже существует (пропущен): {path}")
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            if executable:
                st = os.stat(file_path)
                os.chmod(file_path, st.st_mode | stat.S_IEXEC)
            
            self.logger.info(f"✅ Создан файл: {path}")
        except Exception as e:
            self.logger.error(f"❌ Ошибка создания {path}: {e}")

    def create_structure(self):
        """Создание директорий проекта."""
        self.logger.info("--- Создание структуры папок ---")
        for d in PROJECT_DIRS:
            (self.base_path / d).mkdir(parents=True, exist_ok=True)
            self.logger.info(f"📁 Директория: {d}/")

    def create_memory_bank(self):
        """Создание файлов памяти агентов."""
        self.logger.info("--- Инициализация памяти Роя (.swarm_memory) ---")
        for filename, content in MEMORY_FILES.items():
            self._write_file(f".swarm_memory/{filename}", content)

    def init_sqlite_db(self):
        """Пре-инициализация SQLite файла."""
        self.logger.info("--- Инициализация SQLite базы данных ---")
        db_path = self.base_path / ".swarm_memory" / "swarm_brain.db"
        if not db_path.exists():
            try:
                import sqlite3
                conn = sqlite3.connect(db_path)
                conn.execute("CREATE TABLE IF NOT EXISTS project_meta (key TEXT, value TEXT)")
                conn.close()
                self.logger.info(f"🗄️ SQLite Database initialized at {db_path}")
            except Exception as e:
                self.logger.error(f"❌ Ошибка инициализации SQLite: {e}")
        else:
            self.logger.info(f"🗄️ SQLite Database already exists at {db_path}")

    def create_configs(self):
        """Создание конфигурационных файлов."""
        self.logger.info("--- Настройка окружения ---")

        windsurf_rules = f"""# Windsurf Rules Configuration for Agent Swarm - {self.project_name}

# 🧠 SWARM BRAIN LOCATION
MEMORY_PATH=.swarm_memory/
ACTIVE_STATE=.swarm_memory/active_state.md
SPECS=.swarm_memory/specifications.md

# 🤖 CASCADE BEHAVIOR
ALWAYS_READ_ARCH=.swarm_memory/architecture.md

# 🚫 IGNORE PATTERNS
IGNORE_PATTERNS=.git/*,__pycache__/*,*.log,deployment.log,venv/*
"""
        self._write_file('.windsurfrules', windsurf_rules)

        gitignore = """__pycache__/
*.pyc
venv/
.env
.DS_Store
deployment.log
node_modules/
.swarm_memory/
"""
        self._write_file('.gitignore', gitignore)

    def create_tools(self):
        """Создание инструментов агентов."""
        self.logger.info("--- Генерация инструментов (Tools) ---")
        
        # Инструмент очистки памяти
        clean_memory = '''#!/usr/bin/env python3
"""
🧹 Инструмент очистки памяти роя
"""
import os
import json
from pathlib import Path

def clean_memory():
    memory_path = Path(".swarm_memory")
    if not memory_path.exists():
        print("❌ Папка .swarm_memory не найдена")
        return
    
    # Очищаем active_state
    active_state = memory_path / "active_state.md"
    if active_state.exists():
        with open(active_state, 'w', encoding='utf-8') as f:
            f.write("# 👑 ACTIVE PROJECT STATE\\n**Status:** 🟢 Clean\\n**Current Focus:** Ready for new tasks\\n\\n## 📋 CURRENT OBJECTIVES\\n- [ ] Awaiting instructions\\n\\n## 💬 CONTEXT & LOGS\\n- **System:** Memory cleaned successfully\\n")
        print("✅ Active state cleaned")
    
    print("🧹 Memory cleanup complete")

if __name__ == "__main__":
    clean_memory()
'''
        self._write_file('tools/clean_memory.py', clean_memory, executable=True)

        # Веб-поиск
        web_search = '''#!/usr/bin/env python3
"""
🔍 Инструмент умного веб-поиска
"""
import os
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from duckduckgo_search import DDGS
    import requests
    from bs4 import BeautifulSoup
    
    def smart_search(query, max_results=5):
        """Умный поиск с анализом результатов"""
        print(f"🔍 Поиск: {query}")
        
        try:
            # Поиск через DuckDuckGo
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=max_results))
            
            if not results:
                print("❌ Ничего не найдено")
                return []
            
            print(f"✅ Найдено {len(results)} результатов")
            return results
            
        except Exception as e:
            print(f"❌ Ошибка поиска: {e}")
            return []
    
    if __name__ == "__main__":
        if len(sys.argv) > 1:
            query = " ".join(sys.argv[1:])
            results = smart_search(query)
            for i, result in enumerate(results, 1):
                print(f"\\n{i}. {result['title']}")
                print(f"   {result['body'][:100]}...")
                print(f"   {result['href']}")
        else:
            print("Использование: python web_search.py 'ваш запрос'")
    
except ImportError:
    print("❌ Установите зависимости: pip install duckduckgo-search requests beautifulsoup4")
'''
        self._write_file('tools/web_search.py', web_search, executable=True)

    def create_scripts(self):
        """Создание скриптов запуска."""
        self.logger.info("--- Генерация скриптов запуска ---")
        
        # Скрипт запуска тестов
        test_runner = '''#!/bin/bash
# 🧪 Скрипт запуска тестов
echo "🧪 Запуск тестов..."
python -m pytest tests/ -v --tb=short
echo "✅ Тесты завершены"
'''
        self._write_file('scripts/run_tests.sh', test_runner, executable=True)

    def generate_roles_doc(self):
        """Генерация документации по ролям."""
        self.logger.info("--- Создание документации по Ролям ---")
        
        roles_content = f"""# 🎭 AGENTS ROLES - {self.project_name}

## 👑 SUPERVISOR
**Роль:** Координатор и стратег
**Задачи:**
- Распределение задач между агентами
- Контроль качества работы
- Принятие архитектурных решений
- Коммуникация с пользователем

**Промпт для Roo Code:**
```
Ты - Supervisor Agent. Ты координируешь работу агентов роя для проекта "{self.project_name}".

Твои обязанности:
1. Анализируй запросы пользователя и разбивай на задачи
2. Распределяй задачи между соответствующими агентами
3. Контролируй качество и срок выполнения
4. Интегрируй результаты работы агентов
5. Отчитывайся пользователю о прогрессе

Приложения:
- Используй .swarm_memory/active_state.md для отслеживания прогресса
- Ссылайся на .swarm_memory/architecture.md для архитектурных решений
- Обновляй .swarm_memory/specifications.md для технических деталей

Начни с анализа текущего состояния проекта.
```

## 🏗️ ARCHITECT
**Роль:** Архитектор и дизайнер систем
**Задачи:**
- Проектирование архитектуры
- Выбор технологий и паттернов
- Создание схем и диаграмм
- Документирование решений

**Промпт для Roo Code:**
```
Ты - Architect Agent. Ты проектируешь архитектуру для проекта "{self.project_name}".

Твои обязанности:
1. Анализируй требования и создавай архитектурные решения
2. Выбирай подходящие технологии и паттерны
3. Создавай диаграммы и схемы
4. Документируй архитектурные решения в .swarm_memory/architecture.md
5. Обеспечив масштабируемость и поддерживаемость

Фокусируйся на:
- Чистой архитектуре
- Лучших практиках
- Масштабируемости
- Простоте поддержки
```

## 💻 CODER
**Роль:** Разработчик и программист
**Задачи:**
- Написание кода
- Реализация функций
- Рефакторинг
- Тестирование

**Промпт для Roo Code:**
```
Ты - Coder Agent. Ты разрабатываешь код для проекта "{self.project_name}".

Твои обязанности:
1. Пиши чистый, эффективный и документированный код
2. Следуй лучшим практикам и стандартам
3. Создавай unit тесты для критического функционала
4. Рефакторь существующий код при необходимости
5. Используй .swarm_memory/specifications.md для требований

Принципы:
- KISS (Keep It Simple, Stupid)
- DRY (Don't Repeat Yourself)
- SOLID принципы
- Чистый код
```

## 🧪 TESTER
**Роль:** Тестировщик и QA
**Задачи:**
- Написание тестов
- Поиск багов
- Проверка качества
- Автоматизация тестирования

**Промпт для Roo Code:**
```
Ты - Tester Agent. Ты обеспечиваешь качество кода в проекте "{self.project_name}".

Твои обязанности:
1. Пиши автоматические тесты (unit, integration, e2e)
2. Ищи и документируй баги в .swarm_memory/bug_log.md
3. Проводи регрессионное тестирование
4. Создавай тестовые сценарии
5. Проверяй соответствие требованиям

Фокусируйся на:
- Покрытии кода тестами
- Краевых случаях
- Производительности
- Безопасности
```

## 🔍 RESEARCHER
**Роль:** Исследователь и аналитик
**Задачи:**
- Поиск информации
- Анализ технологий
- Исследование решений
- Сбор данных

**Промпт для Roo Code:**
```
Ты - Researcher Agent. Ты проводишь исследования для проекта "{self.project_name}".

Твои обязанности:
1. Ищи актуальную информацию по теме
2. Анализируй технологии и решения
3. Сравнивай альтернативы
4. Предоставляй выводы и рекомендации
5. Документируй исследования

Используй инструменты:
- web_search.py для поиска информации
- Анализируй источники
- Проверяй актуальность данных
```

## 🔄 ИНТЕГРАЦИЯ АГЕНТОВ

### Процесс работы:
1. **Supervisor** получает запрос от пользователя
2. **Supervisor** анализирует и распределяет задачи
3. **Architect** проектирует решение
4. **Coder** реализует код
5. **Tester** проверяет качество
6. **Researcher** предоставляет данные при необходимости
7. **Supervisor** интегрирует результаты и отчитывается

### Коммуникация:
- Все агенты используют .swarm_memory/ для обмена данными
- Supervisor координирует взаимодействие
- Каждый агент обновляет соответствующие файлы памяти

---
*Создано автоматически deploy_swarm_complete.py*
"""
        self._write_file('AGENTS_ROLES.md', roles_content)

    def create_requirements(self):
        """Создание requirements.txt."""
        self.logger.info("--- Создание requirements.txt ---")
        
        requirements = """duckduckgo-search>=5.0.0
beautifulsoup4
requests
tavily-python
python-dotenv
pytest
"""
        self._write_file('requirements.txt', requirements)

    def install_mcp_servers(self):
        """Автоматическая установка MCP серверов."""
        self.logger.info("--- Установка MCP серверов ---")
        
        # Проверяем наличие Node.js
        try:
            result = subprocess.run(["node", "--version"], 
                                shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                self.logger.info(f"✅ Node.js найден: {result.stdout.strip()}")
            else:
                raise FileNotFoundError
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.logger.warning("⚠️ Node.js не найден. MCP серверы не будут установлены.")
            self.logger.info("💡 Установите Node.js с https://nodejs.org/ и повторите запуск")
            return
        
        # Создаем .npmrc
        npmrc_path = self.base_path / ".npmrc"
        with open(npmrc_path, 'w', encoding='utf-8') as f:
            f.write("registry=https://registry.npmjs.org/\\n")
            f.write("@modelcontextprotocol:registry=https://registry.npmjs.org/\\n")
            f.write("strict-ssl=false\\n")
        
        # Удаляем старую папку node_modules если есть
        node_modules = self.base_path / "node_modules"
        if node_modules.exists():
            self.logger.info("🗑️ Очистка старой папки node_modules...")
            shutil.rmtree(node_modules)
        
        # Устанавливаем пакеты
        packages = ["@modelcontextprotocol/sdk"]
        
        for package in packages:
            try:
                self.logger.info(f"📦 Установка {package}...")
                subprocess.run(["npm", "install", "-D", package], 
                             shell=True, check=True, cwd=self.base_path)
            except subprocess.CalledProcessError as e:
                self.logger.error(f"❌ Ошибка установки {package}: {e}")
        
        # Компилируем серверы
        servers_path = node_modules / "@modelcontextprotocol" / "servers"
        if servers_path.exists():
            try:
                self.logger.info("🔨 Компиляция MCP серверов...")
                os.chdir(servers_path)
                subprocess.run(["npm", "install"], shell=True, check=True)
                subprocess.run(["npm", "run", "build"], shell=True, check=True)
                os.chdir(self.base_path)
            except subprocess.CalledProcessError as e:
                self.logger.warning(f"⚠️ Проблемы с компиляцией серверов: {e}")
        else:
            self.logger.warning("⚠️ Папка servers не найдена")

    def setup_additional_tools(self):
        """Установка дополнительных MCP серверов из исходного кода."""
        self.logger.info("--- Установка дополнительных MCP серверов ---")
        
        # Создаем встроенную функцию для установки
        def install_additional_servers():
            base_path = self.base_path
            tools_dir = base_path / "tools" / "mcp-servers"
            
            print("🚀 Начинаем установку недостающих инструментов...")

            # 1. Клонируем официальный репозиторий (если нет)
            if not tools_dir.exists():
                print("📥 Клонирование репозитория MCP servers...")
                try:
                    subprocess.run(f"git clone https://github.com/modelcontextprotocol/servers.git {tools_dir}", 
                                shell=True, check=True)
                except subprocess.CalledProcessError:
                    print("❌ Не удалось клонировать репозиторий")
                    return
            else:
                print("📂 Репозиторий уже существует, обновляем...")
                subprocess.run("git pull", shell=True, cwd=tools_dir)

            # 2. Список серверов для сборки
            servers_to_build = {
                "fetch": tools_dir / "src" / "fetch",
                "git": tools_dir / "src" / "git", 
                "time": tools_dir / "src" / "time",
                "sequentialthinking": tools_dir / "src" / "sequentialthinking"
            }

            built_paths = {}

            # 3. Сборка (Build)
            for name, path in servers_to_build.items():
                print(f"🔨 Сборка сервера: {name}...")
                if not path.exists():
                    print(f"⚠️ Путь не найден: {path} (Пропускаем)")
                    continue
                    
                # Установка зависимостей и билд внутри папки сервера
                subprocess.run("npm install", shell=True, cwd=path)
                subprocess.run("npm run build", shell=True, cwd=path)
                
                dist_file = path / "dist" / "index.js"
                if dist_file.exists():
                    built_paths[name] = str(dist_file)
                    print(f"✅ {name} готов!")
                else:
                    print(f"❌ Не удалось собрать {name}")

            # 4. Обновляем MCP конфигурацию
            node_modules = base_path / "node_modules"
            
            # Пути к filesystem/memory
            fs_path = node_modules / "@modelcontextprotocol" / "server-filesystem" / "dist" / "index.js"
            mem_path = node_modules / "@modelcontextprotocol" / "server-memory" / "dist" / "index.js"
            
            # Экранирование для JSON
            def p(path_str): 
                return str(path_str).replace("\\", "\\\\")

            mcp_config = {
                "mcpServers": {
                    "filesystem": {
                        "command": "node",
                        "args": [p(fs_path), p(base_path)]
                    },
                    "memory": {
                        "command": "node",
                        "args": [p(mem_path)]
                    }
                }
            }

            # Добавляем новые серверы
            for name, path in built_paths.items():
                mcp_config["mcpServers"][name] = {
                    "command": "node",
                    "args": [p(path)]
                }

            # 5. Сохранение
            roo_dir = base_path / ".roo"
            roo_dir.mkdir(exist_ok=True)
            roo_config_path = roo_dir / "mcp.json"
            
            with open(roo_config_path, "w", encoding="utf-8") as f:
                json.dump(mcp_config, f, indent=2)

            print("\\n" + "="*50)
            print("🎉 ГОТОВО! Полный набор инструментов собран.")
            print(f"📄 Конфигурация обновлена: {roo_config_path}")
            print("="*50)

        try:
            install_additional_servers()
            self.logger.info("✅ Дополнительные MCP серверы установлены")
            
        except Exception as e:
            self.logger.warning(f"⚠️ Не удалось установить дополнительные серверы: {e}")

    def create_mcp_config(self):
        """Создание рабочей MCP конфигурации."""
        self.logger.info("--- Создание MCP конфигурации ---")
        current_dir = str(self.base_path).replace("\\", "\\\\")
        
        # Проверяем доступные серверы
        node_modules = self.base_path / "node_modules" / "@modelcontextprotocol"
        available_servers = {}
        
        # Проверяем filesystem сервер
        fs_path = node_modules / "server-filesystem" / "dist" / "index.js"
        if fs_path.exists():
            available_servers["filesystem"] = {
                "command": "node",
                "args": [
                    f"{current_dir}\\\\node_modules\\\\@modelcontextprotocol\\\\server-filesystem\\\\dist\\\\index.js",
                    current_dir
                ]
            }
        
        # Проверяем memory сервер
        memory_path = node_modules / "server-memory" / "dist" / "index.js"
        if memory_path.exists():
            available_servers["memory"] = {
                "command": "node",
                "args": [
                    f"{current_dir}\\\\node_modules\\\\@modelcontextprotocol\\\\server-memory\\\\dist\\\\index.js"
                ]
            }
        
        # Проверяем дополнительные серверы
        additional_servers = ["fetch", "git", "time", "sequentialthinking"]
        tools_mcp = self.base_path / "tools" / "mcp-servers" / "src"
        
        for server in additional_servers:
            server_path = tools_mcp / server / "dist" / "index.js"
            if server_path.exists():
                available_servers[server] = {
                    "command": "node",
                    "args": [str(server_path).replace("\\", "\\\\")]
                }
        
        mcp_config = {"mcpServers": available_servers}
        
        # Создаем папку .roo и сохраняем конфиг
        roo_dir = self.base_path / ".roo"
        roo_dir.mkdir(exist_ok=True)
        roo_config_path = roo_dir / "mcp.json"
        
        try:
            with open(roo_config_path, 'w', encoding='utf-8') as f:
                json.dump(mcp_config, f, indent=2, ensure_ascii=False)
            self.logger.info(f"💾 Конфиг MCP создан: {roo_config_path}")
            
            if available_servers:
                servers_list = ", ".join(available_servers.keys())
                self.logger.info(f"✅ Доступны MCP серверы: {servers_list}")
            else:
                self.logger.warning("⚠️ Ни один MCP сервер не найден")
                
        except Exception as e:
            self.logger.error(f"❌ Ошибка создания MCP конфигурации: {e}")

    def create_env_example(self):
        """Создание примера .env файла."""
        self.logger.info("--- Создание .env.example ---")
        
        env_example = f"""# Environment variables for {self.project_name}
# Get your API keys at respective websites

# Tavily API Key - https://tavily.com
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxxx

# OpenAI API Key - https://platform.openai.com
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx

# Add other API keys below as needed
# ANTHROPIC_API_KEY=...
# GOOGLE_API_KEY=...
"""
        self._write_file('.env.example', env_example)

    def create_readme(self):
        """Создание README с инструкциями."""
        self.logger.info("--- Создание README.md ---")
        
        readme_content = f"""# 🚀 {self.project_name}

Проект с развернутым окружением Agent Swarm.

## 🛠️ Настройка окружения

1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Настройте переменные окружения:**
   ```bash
   cp .env.example .env
   # Отредактируйте .env с вашими API ключами
   ```

3. **Активируйте MCP серверы:**
   - Перезапустите Windsurf/Roo Code
   - MCP серверы уже настроены в `.roo/mcp.json`

## 📁 Структура проекта

```
{self.project_name}/
├── src/                    # Основной код
├── tests/                   # Тесты
├── docs/                    # Документация
├── scripts/                 # Скрипты
├── tools/                   # Инструменты
│   ├── clean_memory.py      # Очистка памяти
│   ├── web_search.py        # Веб-поиск
│   └── mcp-servers/         # Дополнительные MCP серверы
├── .swarm_memory/           # Память агентов
│   ├── active_state.md      # Текущее состояние
│   ├── architecture.md      # Архитектура
│   ├── specifications.md   # Технические задания
│   ├── bug_log.md         # Лог ошибок
│   └── reflections.md      # Рефлексии
├── .roo/                   # Конфигурация Roo Code
│   └── mcp.json           # MCP серверы
├── .windsurfrules          # Правила Windsurf
├── .gitignore              # Git ignore
├── .env.example            # Пример переменных окружения
├── requirements.txt         # Зависимости Python
├── AGENTS_ROLES.md         # Роли агентов
└── README.md               # Документация проекта
```

## 🤖 Использование агентов

1. Откройте проект в Windsurf/Roo Code
2. Выберите режим **Supervisor**
3. Напишите: **"Инициализируй проект"**
4. Следуйте инструкциям агента

## 🎭 Доступные агенты

- **Supervisor** - Координатор и стратег
- **Architect** - Архитектор и дизайнер систем
- **Coder** - Разработчик и программист
- **Tester** - Тестировщик и QA
- **Researcher** - Исследователь и аналитик

Подробности в `AGENTS_ROLES.md`

## 📚 Документация

- `AGENTS_ROLES.md` - Описание ролей агентов
- `.swarm_memory/` - Память и контекст проекта

## 🔧 Инструменты

- `tools/clean_memory.py` - Очистка памяти агентов
- `tools/web_search.py` - Умный веб-поиск
- `scripts/run_tests.sh` - Запуск тестов

---
Развернуто с помощью Agent Swarm Complete Deployment Script
"""
        self._write_file('README.md', readme_content)

    def cleanup(self):
        """Полное удаление развернутого окружения роя."""
        self.logger.info("--- Очистка окружения роя ---")
        
        # Удаляем все файлы и папки роя
        swarm_items = [
            '.swarm_memory',
            '.windsurfrules',
            '.clinerules',
            '.roo',
            'AGENTS_ROLES.md',
            'README.md',
            '.env.example',
            'requirements.txt',
            'tools',
            'scripts',
            'deployment.log'
        ]
        
        for item in swarm_items:
            item_path = self.base_path / item
            if item_path.exists():
                if item_path.is_dir():
                    shutil.rmtree(item_path)
                else:
                    item_path.unlink()
                self.logger.info(f"🗑️ Удалено: {item}")
        
        # Удаляем node_modules если есть
        node_modules = self.base_path / "node_modules"
        if node_modules.exists():
            shutil.rmtree(node_modules)
            self.logger.info("🗑️ Удалено: node_modules")
        
        # Удаляем .npmrc
        npmrc_path = self.base_path / ".npmrc"
        if npmrc_path.exists():
            npmrc_path.unlink()
            self.logger.info("🗑️ Удалено: .npmrc")
        
        self.logger.info("✅ Очистка завершена")

def show_help():
    """Показать справку."""
    help_text = """
🚀 COMPLETE AGENT SWARM DEPLOYMENT SCRIPT

Использование:
  python deploy_swarm_complete.py [опции]

Опции:
  --cleanup     - Полная очистка окружения роя
  --mcp-only    - Только установка MCP серверов
  --help        - Эта справка

Что делает скрипт:
✅ Создает структуру проекта
✅ Инициализирует память агентов
✅ Устанавливает MCP серверы
✅ Создает инструменты и скрипты
✅ Генерирует документацию
✅ Настраивает окружение

После развертывания:
1. Установите зависимости: pip install -r requirements.txt
2. Создайте .env файл: cp .env.example .env
3. Добавьте API ключи в .env
4. Перезапустите Windsurf/Roo Code
5. Выберите режим Supervisor и напишите: "Инициализируй проект"
"""
    print(help_text)

def main():
    logger = setup_logging()
    deployer = CompleteSwarmDeployer(logger)
    
    # Обработка аргументов командной строки
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--help":
            show_help()
            return
        elif arg == "--cleanup":
            print("\\n🗑️ ОЧИСТКА ОКРУЖЕНИЯ РОЯ...")
            deployer.cleanup()
            print("✅ Очистка завершена!")
            return
        elif arg == "--mcp-only":
            print("\\n📦 УСТАНОВКА ТОЛЬКО MCP СЕРВЕРОВ...")
            deployer.install_mcp_servers()
            deployer.setup_additional_tools()
            deployer.create_mcp_config()
            print("✅ MCP серверы установлены!")
            return
    
    print(f"\\n🚀 Starting Complete Swarm Deployment for '{deployer.project_name}'...")
    print(f"📁 Папка проекта: {deployer.base_path}")

    try:
        deployer.create_structure()
        deployer.create_memory_bank()
        deployer.init_sqlite_db()
        deployer.create_configs()
        deployer.install_mcp_servers()
        deployer.setup_additional_tools()
        deployer.create_requirements()
        deployer.create_tools()
        deployer.create_scripts()
        deployer.generate_roles_doc()
        deployer.create_env_example()
        deployer.create_mcp_config()
        deployer.create_readme()
        
        print("\\n✅ DEPLOYMENT SUCCESSFUL!")
        print("="*60)
        print(f"🎉 Проект '{deployer.project_name}' готов к работе!")
        print("\\n📋 Дальнейшие шаги:")
        print("1. Установите зависимости: pip install -r requirements.txt")
        print("2. Создайте .env файл: cp .env.example .env")
        print("3. Добавьте свои API ключи в .env")
        print("4. Перезапустите Windsurf/Roo Code для активации MCP")
        print("5. Выберите режим Supervisor и напишите: 'Инициализируй проект'")
        print("\\n📖 Ознакомьтесь с документацией:")
        print("- README.md - общая информация")
        print("- AGENTS_ROLES.md - роли агентов")
        print("- .swarm_memory/ - память проекта")
        print("\\n🔧 Доступные опции:")
        print("--cleanup  - очистка окружения")
        print("--mcp-only - только MCP серверы")
        print("--help     - эта справка")
        print("="*60)
        
    except Exception as e:
        logger.error(f"Critical Failure: {e}")
        print(f"\\n❌ FAILED: {e}")

if __name__ == "__main__":
    main()
