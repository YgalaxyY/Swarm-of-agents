#!/usr/bin/env python3
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
            new_lines.append(f"**Phase:** {status}\n")
        elif "**Last Updated By:**" in line:
            new_lines.append(f"**Last Updated By:** Agent ({datetime.datetime.now().strftime('%H:%M')})\n")
        elif "## 🏗️ Active Context" in line:
            new_lines.append(line)
            new_lines.append(f"{message}\n")
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
