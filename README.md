# 🚀 Swarm_agents (Swarm Enhanced)

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
