#!/usr/bin/env python3
"""
🧹 SWARM CLEANUP SCRIPT
Полное удаление агентового роя из любого проекта.

Использование:
  python swarm_cleanup.py [--force]

Опции:
  --force     - Принудительное удаление без подтверждения
  --help      - Эта справка

⚠️  ВНИМАНИЕ: Этот скрипт безвозвратно удалит все следы агентового роя!
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

class SwarmCleanup:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.removed_items = []
        self.errors = []

    def log(self, message, level="INFO"):
        """Логирование сообщений"""
        prefix = {
            "INFO": "ℹ️",
            "SUCCESS": "✅", 
            "WARNING": "⚠️",
            "ERROR": "❌",
            "DELETE": "🗑️"
        }
        print(f"{prefix.get(level, 'ℹ️')} {message}")

    def confirm_cleanup(self):
        """Подтверждение удаления"""
        print("\n" + "="*60)
        print("🚨 СКРИПТ УДАЛЕНИЯ АГЕНТОВОГО РОЯ")
        print("="*60)
        print(f"📁 Папка: {self.base_path}")
        print("\n📋 Будут удалены следующие элементы:")
        
        # Показываем что будет удалено
        cleanup_items = self.get_cleanup_items()
        for item in cleanup_items:
            item_path = self.base_path / item
            if item_path.exists():
                if item_path.is_dir():
                    print(f"   📁 {item}/ (папка)")
                else:
                    print(f"   📄 {item} (файл)")
        
        print("\n" + "⚠️" * 20)
        print("ЭТО ДЕЙСТВИЕ НЕВОЗМОЖНО ОТМЕНИТЬ!")
        print("⚠️" * 20)
        
        try:
            response = input("\nВы уверены, что хотите продолжить? (yes/no): ").lower()
            return response in ['yes', 'y', 'да', 'д']
        except KeyboardInterrupt:
            print("\n\n❌ Операция отменена пользователем")
            return False

    def get_cleanup_items(self):
        """Получить список элементов для удаления"""
        return [
            # Основные файлы и папки роя
            '.swarm_memory',
            '.roo',
            '.windsurfrules',
            'AGENTS_ROLES.md',
            'swarm_deploy.py',
            
            # Временные и лог файлы
            'deployment.log',
            '.npmrc',
            'package.json',
            'package-lock.json',
            'node_modules',
            
            # Инструменты и скрипты
            'tools',
            'scripts',
            
            # Документация роя
            'README_GITHUB.md',
            'CHANGELOG.md',
            
            # Конфигурационные файлы
            '.env.example',
            'requirements.txt',
            
            # Git файлы (только если это репозиторий роя)
            '.git'
        ]

    def remove_item(self, item_path):
        """Безопасное удаление элемента"""
        try:
            if item_path.exists():
                if item_path.is_dir():
                    shutil.rmtree(item_path)
                    self.log(f"Удалена папка: {item_path.name}", "DELETE")
                else:
                    item_path.unlink()
                    self.log(f"Удален файл: {item_path.name}", "DELETE")
                self.removed_items.append(str(item_path))
                return True
        except Exception as e:
            self.errors.append(f"Ошибка удаления {item_path}: {e}")
            self.log(f"Не удалось удалить {item_path}: {e}", "ERROR")
            return False
        return False

    def cleanup(self, force=False):
        """Основная функция очистки"""
        self.log("Начинаю очистку агентового роя...", "INFO")
        
        # Подтверждение если не force
        if not force and not self.confirm_cleanup():
            self.log("Операция отменена", "WARNING")
            return False

        # Удаляем все элементы
        cleanup_items = self.get_cleanup_items()
        success_count = 0
        
        for item in cleanup_items:
            item_path = self.base_path / item
            if self.remove_item(item_path):
                success_count += 1

        # Отчет
        print("\n" + "="*50)
        print("📊 ОТЧЕТ ОБ УДАЛЕНИИ")
        print("="*50)
        
        if self.removed_items:
            print(f"✅ Успешно удалено: {len(self.removed_items)} элементов")
            for item in self.removed_items:
                print(f"   🗑️ {item}")
        
        if self.errors:
            print(f"\n❌ Ошибок: {len(self.errors)}")
            for error in self.errors:
                print(f"   ❌ {error}")
        
        if not self.removed_items:
            print("\nℹ️  Следы агентового роя не найдены")
        else:
            print(f"\n🎉 Очистка завершена! Проект очищен от агентового роя.")
        
        return len(self.errors) == 0

def main():
    parser = argparse.ArgumentParser(
        description="🧹 Полное удаление агентового роя из проекта",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""""
Примеры использования:
  python swarm_cleanup.py              # С подтверждением
  python swarm_cleanup.py --force       # Без подтверждения
  python swarm_cleanup.py --help        # Справка
        """
    )
    
    parser.add_argument(
        '--force', 
        action='store_true',
        help='Принудительное удаление без подтверждения'
    )
    
    parser.add_argument(
        '--path',
        type=str,
        help='Путь к папке проекта (по умолчанию: текущая папка)'
    )
    
    args = parser.parse_args()
    
    # Проверка прав доступа
    try:
        test_file = Path(args.path) if args.path else Path.cwd() / '.cleanup_test'
        test_file.touch()
        test_file.unlink()
    except PermissionError:
        print("❌ Недостаточно прав для записи в папку. Запустите от имени администратора.")
        sys.exit(1)
    
    # Запуск очистки
    cleanup = SwarmCleanup(args.path)
    success = cleanup.cleanup(force=args.force)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
