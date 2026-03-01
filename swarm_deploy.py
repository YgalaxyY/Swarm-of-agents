#!/usr/bin/env python3
"""
🚀 COMPLETE AGENT SWARM DEPLOYMENT SCRIPT v2.0
Усовершенствованная версия с жесткой логикой кооперации.

Особенности v2.0:
✅ Strict Context Protocol - защита от потери контекста
✅ Handoff Mechanism - логированная передача задач
✅ Enhanced Memory - структурированные Markdown файлы
✅ Role-Specific SOPs - четкие алгоритмы для каждого агента

Использование:
  python deploy_swarm_v2.py [опции]

Опции:
  --cleanup     - очистка окружения
  --mcp-only    - только установка MCP серверов
  --help        - справка
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

# --- КОНФИГУРАЦИЯ СТРУКТУРЫ ---
PROJECT_DIRS = [
    'src', 'tests', 'docs', 'scripts', 'tools', 
    '.swarm_memory', '.swarm_memory/logs', '.swarm_memory/archive'
]
# --- УЛУЧШЕННАЯ ПАМЯТЬ ---
MEMORY_FILES = {
    'active_state.md': """# 👑 ACTIVE PROJECT STATE
> **CRITICAL:** This file is the Single Source of Truth. Read it before ANY action.

## 🚦 Status
**Phase:** 🟢 Initialization
**Current Sprint:** Setup & Config
**Last Updated By:** System Setup

## 🎯 Current Objectives (High Priority)
- [ ] Awaiting initial User Instruction
- [ ] Supervisor to break down the first task

## 🏗️ Active Context
*Краткое описание того, над чем прямо сейчас идет работа.*
System initialized. Waiting for Supervisor assignment.

## 🔗 Active File References
*Список файлов, которые сейчас изменяются или важны.*
- `AGENTS_ROLES.md` 
""",

    'architecture.md': """# 🧠 ARCHITECTURE & DECISIONS
*Долговременная память архитектора.*

## 🏗️ System Design
- **Language:** Python 3.x
- **Architecture Style:** Modular Monolith (Default)
- **Data Storage:** SQLite (via MCP) / File System

## 📜 Decision Log (ADR)
| ID | Date | Decision | Rationale | Status |
|----|------|----------|-----------|--------|
| 001| Today| Init Swarm | Project kickoff | Accepted |
""",

    'specifications.md': """# 🛠️ TECHNICAL SPECIFICATIONS
*Детальные ТЗ для Кодера.*

## 📦 API Contracts
*(Define interfaces here)*

## 🗃️ Data Models
*(Define schemas here)*
""",

    'handoff_log.md': """# 🤝 HANDOFF LOG (Communication Channel)
*История передачи задач между агентами. Пишите сюда сообщения для коллеги.*

## 📨 Latest Messages
**[System] -> [Supervisor]:** Project environment created. Ready for instructions.
""",

    'qa_checklist.md': """# � QA & TESTING CHECKLIST
*Критерии готовности задач.*

## ✅ Definition of Done (DoD)
- [ ] Code compiles/runs without errors
- [ ] Unit tests written and passed
- [ ] Documentation updated
- [ ] `active_state.md` updated
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

class EnhancedSwarmDeployer:
    def __init__(self, logger):
        self.logger = logger
        self.base_path = Path.cwd()
        self.project_name = self.base_path.name

    def _write_file(self, path, content, executable=False):
        file_path = self.base_path / path
        if file_path.exists():
            self.logger.warning(f"⚠️ Файл существует (пропуск): {path}")
            return
        
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            if executable:
                st = os.stat(file_path)
                os.chmod(file_path, st.st_mode | stat.S_IEXEC)
            
            self.logger.info(f"✅ Создан: {path}")
        except Exception as e:
            self.logger.error(f"❌ Ошибка {path}: {e}")

    def create_structure(self):
        self.logger.info("--- 1. Создание структуры папок ---")
        for d in PROJECT_DIRS:
            (self.base_path / d).mkdir(parents=True, exist_ok=True)

    def create_memory_bank(self):
        self.logger.info("--- 2. Инициализация памяти (.swarm_memory) ---")
        for filename, content in MEMORY_FILES.items():
            self._write_file(f".swarm_memory/{filename}", content)

    def create_configs(self):
        self.logger.info("--- 3. Настройка конфигураций ---")
        
        # Windsurf Rules - Оптимизированы для контекста
        windsurf_rules = f"""# Windsurf Rules - {self.project_name}

# 🧠 MEMORY ACCESS PROTOCOL
1. BEFORE answering: ALWAYS read `.swarm_memory/active_state.md` 
2. AFTER finishing: UPDATE `.swarm_memory/active_state.md` and `.swarm_memory/handoff_log.md` 
3. NEVER delete content from memory without backing it up to `.swarm_memory/archive/` 

# � PROJECT CONTEXT
MEMORY_DIR=.swarm_memory/
DOCS_DIR=docs/
"""
        self._write_file('.windsurfrules', windsurf_rules)
        
        # Gitignore
        gitignore = """__pycache__/
*.pyc
venv/
.env
.DS_Store
node_modules/
.swarm_memory/logs/
.roo/
"""
        self._write_file('.gitignore', gitignore)

    def create_tools(self):
        self.logger.info("--- 4. Генерация инструментов ---")
        
        # Инструмент обновления статуса (Важный для координации!)
        update_state = '''#!/usr/bin/env python3
"""
📝 Инструмент для быстрого обновления статуса проекта
"""
import sys
from pathlib import Path
import datetime

def update_status(status, message):
    path = Path(".swarm_memory/active_state.md")
    if not path.exists():
        return
        
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        if "**Phase:**" in line:
            new_lines.append(f"**Phase:** {status}\\n")
        elif "**Last Updated By:**" in line:
            new_lines.append(f"**Last Updated By:** Agent ({datetime.datetime.now().strftime('%H:%M')})\\n")
        elif "## 🏗️ Active Context" in line:
            new_lines.append(line)
            new_lines.append(f"{message}\\n")
        else:
            new_lines.append(line)
            
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"✅ Status updated: {status}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        update_status(sys.argv[1], " ".join(sys.argv[2:]))
    else:
        print("Usage: update_state.py [STATUS] [MESSAGE]")
'''
        self._write_file('tools/update_state.py', update_state, executable=True)

        # Веб-поиск (стандартный)
        web_search = '''#!/usr/bin/env python3
"""
🔍 Simple Web Search
"""
import sys
try:
    from duckduckgo_search import DDGS
    
    def search(query):
        print(f"🔍 Searching: {query}...")
        results = list(DDGS().text(query, max_results=5))
        if not results:
            print("❌ No results found.")
            return
        for i, r in enumerate(results, 1):
            print(f"\\n{i}. {r['title']}\\n   {r['href']}\\n   {r['body'][:150]}...")

    if __name__ == "__main__":
        if len(sys.argv) > 1:
            search(" ".join(sys.argv[1:]))
        else:
            print("Usage: python web_search.py 'query'")
except ImportError:
    print("❌ Run: pip install duckduckgo-search")
'''
        self._write_file('tools/web_search.py', web_search, executable=True)

    def generate_enhanced_roles(self):
        self.logger.info("--- 5. Создание Smart Roles (AGENTS_ROLES.md) ---")
        
        roles_content = f"""# 🎭 SWARM INTELLIGENCE ROLES - {self.project_name}

> **⚠️ UNIVERSAL RULE:** Every agent MUST read `.swarm_memory/active_state.md` FIRST to understand the current context.

## 👑 SUPERVISOR (Manager)
**Цель:** Управление состоянием и распределение задач.
**System Prompt:**
Ты - Supervisor. Ты — мозг операции. Ты НЕ пишешь код, ты управляешь процессом.

ТВОЙ АЛГОРИТМ:

📥 READ: Прочитай .swarm_memory/active_state.md и handoff_log.md.

🧠 THINK: Проанализируй запрос пользователя. Разбей его на атомарные шаги.

📝 PLAN: Обнови active_state.md, добавив задачи в чек-лист.

👉 DELEGATE: Вызови нужного агента (Coder, Architect, Researcher), дав ему четкую задачу.

🔄 REVIEW: Когда агент вернет результат, проверь его и обнови статус в active_state.md.

ФОРМАТ ОБЩЕНИЯ: Всегда начинай ответ с: [Supervisor Status]: (Planning / Delegating / Reviewing) [Next Agent]: (Name of agent)


## 🏗️ ARCHITECT (System Designer)
**Цель:** Создание структуры и принятие технических решений.
**System Prompt:**
Ты - Architect. Ты отвечаешь за структуру, безопасность и масштабируемость.

ТВОЙ АЛГОРИТМ:

📥 READ: Прочитай architecture.md и требования от Supervisor.

🧠 DESIGN: Продумай решение. Используй sequentialthinking сервер, если нужно.

📝 DOCUMENT: Запиши решение в .swarm_memory/architecture.md.

🤝 HANDOFF: Сообщи Supervisor'у или Coder'у, что архитектура готова.

ВАЖНО:

Не пиши реализацию, пиши интерфейсы.

Обновляй specifications.md для Кодера.


## 💻 CODER (Implementer)
**Цель:** Написание качественного кода по спецификации.
**System Prompt:**
Ты - Coder. Ты пишешь код, который работает.

ТВОЙ АЛГОРИТМ:

📥 READ: Прочитай specifications.md и задачу от Supervisor.

🛠️ CODE: Реализуй функционал. Следуй стандартам PEP8/ESLint.

🧪 SELF-TEST: Запусти базовую проверку (syntax check).

📝 LOG: Обнови handoff_log.md, сообщив: "Функция X реализована в файле Y".

🛑 STOP: Не тестируй глубоко, передай задачу Tester'у.


## 🧪 TESTER (QA & Security)
**Цель:** Поиск багов и проверка соответствия требованиям.
**System Prompt:**
Ты - Tester. Ты — последний рубеж обороны.

ТВОЙ АЛГОРИТМ:

📥 READ: Прочитай specifications.md и код.

💣 ATTACK: Попробуй сломать код. Пиши тесты (pytest/jest).

🐞 REPORT: Если нашел баг — запиши в handoff_log.md и верни Кодеру.

✅ VERIFY: Если все чисто — обнови qa_checklist.md и active_state.md.


## � WORKFLOW PROTOCOL (HANDOFF)
Как передавать задачи, чтобы не потерять контекст:

1. **Перед завершением хода:**
   - Агент обновляет `handoff_log.md`:
     > "Completed task X. Changed files: A, B. Next step: Need Testing."
   - Агент вызывает инструмент `update_state.py` (если доступен) или правит `active_state.md`.

2. **При начале хода:**
   - Агент читает `handoff_log.md` (последние 5 строк) и `active_state.md`.
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
        self.logger.info("--- 6. Установка MCP серверов ---")
        
        # Проверка Node.js
        try:
            subprocess.run(["node", "-v"], check=True, capture_output=True)
        except:
            self.logger.error("❌ Node.js не найден! MCP серверы не будут установлены.")
            return

        # .npmrc
        with open(self.base_path / ".npmrc", 'w') as f:
            f.write("registry=https://registry.npmjs.org/\nstrict-ssl=false\n")

        # Очистка и установка
        if (self.base_path / "node_modules").exists():
            shutil.rmtree(self.base_path / "node_modules")

        packages = ["@modelcontextprotocol/sdk"]
        subprocess.run(["npm", "install", "-D"] + packages, shell=True, cwd=self.base_path)

        # Скачивание и сборка доп. серверов (Time, SequentialThinking - критичны для логики)
        tools_dir = self.base_path / "tools" / "mcp-servers"
        if not tools_dir.exists():
            subprocess.run(f"git clone https://github.com/modelcontextprotocol/servers.git {tools_dir}", shell=True)
        
        # Билд только критически важных серверов
        critical_servers = ["time", "sequentialthinking", "filesystem"]
        built_servers = {}
        
        # Filesystem и Memory берутся из пакетов, SequentialThinking билдим
        seq_path = tools_dir / "src" / "sequentialthinking"
        if seq_path.exists():
            self.logger.info("🧠 Building Sequential Thinking Server...")
            subprocess.run("npm install && npm run build", shell=True, cwd=seq_path)
            built_servers["sequentialthinking"] = str(seq_path / "dist" / "index.js")

        # Формирование конфига
        mcp_config = {
            "mcpServers": {
                "filesystem": {
                    "command": "npx",
                    "args": ["-y", "@modelcontextprotocol/server-filesystem", str(self.base_path)]
                },
                "memory": {
                    "command": "npx",
                    "args": ["-y", "@modelcontextprotocol/server-memory"]
                }
            }
        }
        
        # Добавляем собранные серверы
        for name, path in built_servers.items():
            mcp_config["mcpServers"][name] = {
                "command": "node",
                "args": [path]
            }

        # Сохранение конфига
        roo_dir = self.base_path / ".roo"
        roo_dir.mkdir(exist_ok=True)
        with open(roo_dir / "mcp.json", "w") as f:
            json.dump(mcp_config, f, indent=2)
            
        self.logger.info("✅ MCP Config created with SequentialThinking!")

    def create_readme(self):
        readme = f"""# 🚀 {self.project_name} (Swarm Enhanced)

## Как работать с Роем (Protocol v2)

Этот проект настроен для работы группы AI-агентов. Чтобы они работали эффективно, следуйте правилам:

### 1. Инициализация
1. Установите зависимости: `pip install -r requirements.txt` 
2. Перезагрузите IDE (Windsurf/Roo Code).
3. В чате выберите **Supervisor** (или Custom Mode).
4. **Первый промпт:**
   > "Supervisor, инициализируй проект. Прочитай active_state.md и скажи, что делать."

### 2. Структура Памяти (.swarm_memory)
Это "мозг" проекта. Не удаляйте эти файлы.
- `active_state.md`: **Главный файл.** Текущий статус.
- `handoff_log.md`: Чат между агентами.
- `specifications.md`: ТЗ для кода.
- `architecture.md`: Решения.

### 3. Цикл работы
Агенты настроены работать циклично:
`READ Context` -> `THINK (Sequential)` -> `ACT` -> `UPDATE Log` 

---
*Deployed by Swarm Deployer v2*
"""
        self._write_file('README.md', readme)

    def final_steps(self):
        self._write_file('requirements.txt', "duckduckgo-search\npytest\n")
        self._write_file('.env.example', "OPENAI_API_KEY=sk-...\n")

def main():
    logger = setup_logging()
    
    # Аргументы
    if "--cleanup" in sys.argv:
        print("🧹 Cleaning up...")
        for p in ['.swarm_memory', 'tools', 'node_modules', '.roo', '.windsurfrules', 'AGENTS_ROLES.md']:
            path = Path(p)
            if path.exists():
                if path.is_dir(): shutil.rmtree(path)
                else: path.unlink()
        print("Done.")
        return

    deployer = EnhancedSwarmDeployer(logger)
    
    print(f"� Deploying Enhanced Swarm to {deployer.base_path}...")
    
    deployer.create_structure()
    deployer.create_memory_bank()
    deployer.create_configs()
    deployer.create_tools()
    deployer.generate_enhanced_roles()
    deployer.install_mcp_servers()
    deployer.create_readme()
    deployer.final_steps()
    
    print("\n✅ DEPLOYMENT COMPLETE!")
    print("👉 Теперь открой README.md и следуй инструкции 'Инициализация'.")

if __name__ == "__main__":
    main()
