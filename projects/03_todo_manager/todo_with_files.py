#!/usr/bin/env python3
"""
プロジェクト3: ファイル対応ToDoマネージャー

ToDoリストをJSONファイルに保存し、永続化機能を持つToDoマネージャーです。
ファイルI/O、JSON操作、バックアップ機能などを学習します。

学習ポイント:
- ファイルI/O操作
- JSON形式でのデータ保存・読み込み
- データの永続化
- バックアップとリストア機能
- 設定ファイルの管理

対応章: basics/08_input_output.py完了後
"""

import json
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

class FileBasedTodoManager:
    """ファイルベースのToDoマネージャークラス"""
    
    def __init__(self, data_dir="todo_data"):
        """
        ToDoマネージャーを初期化
        
        Args:
            data_dir (str): データ保存ディレクトリ
        """
        self.data_dir = Path(data_dir)
        self.todos_file = self.data_dir / "todos.json"
        self.config_file = self.data_dir / "config.json"
        self.backup_dir = self.data_dir / "backups"
        
        self.todos = []
        self.next_id = 1
        self.config = {
            "auto_backup": True,
            "backup_interval_days": 7,
            "max_backups": 10,
            "default_priority": "medium",
            "date_format": "%Y-%m-%d %H:%M:%S"
        }
        
        self._ensure_directories()
        self.load_config()
        self.load_todos()
    
    def _ensure_directories(self):
        """必要なディレクトリを作成"""
        self.data_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
    
    def save_config(self):
        """設定をファイルに保存"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ 設定の保存に失敗: {e}")
    
    def load_config(self):
        """設定をファイルから読み込み"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
        except Exception as e:
            print(f"⚠️ 設定の読み込みに失敗: {e}")
            print("デフォルト設定を使用します")
    
    def save_todos(self):
        """ToDoリストをファイルに保存"""
        try:
            # datetime オブジェクトを文字列に変換
            todos_to_save = []
            for todo in self.todos:
                todo_copy = todo.copy()
                todo_copy['created_at'] = todo['created_at'].isoformat()
                if todo_copy['completed_at']:
                    todo_copy['completed_at'] = todo['completed_at'].isoformat()
                todos_to_save.append(todo_copy)
            
            data = {
                'todos': todos_to_save,
                'next_id': self.next_id,
                'last_saved': datetime.now().isoformat()
            }
            
            with open(self.todos_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # 自動バックアップ
            if self.config["auto_backup"]:
                self._create_backup()
                
        except Exception as e:
            print(f"❌ ToDoリストの保存に失敗: {e}")
    
    def load_todos(self):
        """ToDoリストをファイルから読み込み"""
        try:
            if self.todos_file.exists():
                with open(self.todos_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                self.next_id = data.get('next_id', 1)
                
                # 文字列をdatetimeオブジェクトに変換
                loaded_todos = []
                for todo in data.get('todos', []):
                    todo['created_at'] = datetime.fromisoformat(todo['created_at'])
                    if todo['completed_at']:
                        todo['completed_at'] = datetime.fromisoformat(todo['completed_at'])
                    else:
                        todo['completed_at'] = None
                    loaded_todos.append(todo)
                
                self.todos = loaded_todos
                print(f"✅ {len(self.todos)}件のToDoを読み込みました")
                
        except Exception as e:
            print(f"⚠️ ToDoリストの読み込みに失敗: {e}")
            print("新しいToDoリストを開始します")
            self.todos = []
            self.next_id = 1
    
    def _create_backup(self):
        """バックアップを作成"""
        try:
            if not self.todos_file.exists():
                return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.backup_dir / f"todos_backup_{timestamp}.json"
            
            shutil.copy2(self.todos_file, backup_file)
            
            # 古いバックアップの削除
            self._cleanup_old_backups()
            
        except Exception as e:
            print(f"⚠️ バックアップの作成に失敗: {e}")
    
    def _cleanup_old_backups(self):
        """古いバックアップファイルを削除"""
        try:
            backup_files = list(self.backup_dir.glob("todos_backup_*.json"))
            backup_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            
            max_backups = self.config["max_backups"]
            if len(backup_files) > max_backups:
                for old_backup in backup_files[max_backups:]:
                    old_backup.unlink()
                    
        except Exception as e:
            print(f"⚠️ 古いバックアップの削除に失敗: {e}")
    
    def list_backups(self):
        """利用可能なバックアップリストを取得"""
        try:
            backup_files = list(self.backup_dir.glob("todos_backup_*.json"))
            backup_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            
            backups = []
            for backup_file in backup_files:
                stat = backup_file.stat()
                backups.append({
                    'filename': backup_file.name,
                    'path': backup_file,
                    'created': datetime.fromtimestamp(stat.st_mtime),
                    'size': stat.st_size
                })
            
            return backups
            
        except Exception as e:
            print(f"❌ バックアップリストの取得に失敗: {e}")
            return []
    
    def restore_from_backup(self, backup_path):
        """バックアップからリストア"""
        try:
            # 現在のファイルをバックアップ
            if self.todos_file.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                emergency_backup = self.backup_dir / f"todos_before_restore_{timestamp}.json"
                shutil.copy2(self.todos_file, emergency_backup)
            
            # バックアップからリストア
            shutil.copy2(backup_path, self.todos_file)
            
            # データを再読み込み
            self.load_todos()
            
            return True
            
        except Exception as e:
            print(f"❌ リストアに失敗: {e}")
            return False
    
    def export_to_csv(self, filename=None):
        """ToDoリストをCSVファイルにエクスポート"""
        try:
            import csv
            
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = self.data_dir / f"todos_export_{timestamp}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # ヘッダー
                writer.writerow(['ID', 'タイトル', '説明', '優先度', '完了状態', '作成日時', '完了日時'])
                
                # データ
                for todo in self.todos:
                    completed_at = todo['completed_at'].strftime(self.config['date_format']) if todo['completed_at'] else ""
                    writer.writerow([
                        todo['id'],
                        todo['title'],
                        todo['description'],
                        todo['priority'],
                        '完了' if todo['completed'] else '未完了',
                        todo['created_at'].strftime(self.config['date_format']),
                        completed_at
                    ])
            
            print(f"✅ CSVファイルにエクスポートしました: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ CSVエクスポートに失敗: {e}")
            return False
    
    def import_from_csv(self, filename):
        """CSVファイルからToDoリストをインポート"""
        try:
            import csv
            
            if not Path(filename).exists():
                print(f"❌ ファイルが見つかりません: {filename}")
                return False
            
            imported_count = 0
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    try:
                        self.add_todo(
                            title=row['タイトル'],
                            description=row.get('説明', ''),
                            priority=row.get('優先度', 'medium')
                        )
                        imported_count += 1
                    except Exception as e:
                        print(f"⚠️ 行のインポートに失敗: {e}")
            
            print(f"✅ {imported_count}件のToDoをインポートしました")
            return True
            
        except Exception as e:
            print(f"❌ CSVインポートに失敗: {e}")
            return False
    
    def add_todo(self, title, description="", priority=None, due_date=None):
        """ToDoを追加（ファイル保存付き）"""
        if not title.strip():
            raise ValueError("タイトルは必須です")
        
        if priority is None:
            priority = self.config["default_priority"]
        
        if priority not in ["high", "medium", "low"]:
            priority = "medium"
        
        todo = {
            "id": self.next_id,
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority,
            "completed": False,
            "created_at": datetime.now(),
            "completed_at": None,
            "due_date": due_date
        }
        
        self.todos.append(todo)
        todo_id = self.next_id
        self.next_id += 1
        
        self.save_todos()
        return todo_id
    
    def update_todo(self, todo_id, **kwargs):
        """ToDoを更新（ファイル保存付き）"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                for key, value in kwargs.items():
                    if key in todo and value is not None:
                        if key == "title" and not value.strip():
                            raise ValueError("タイトルは空にできません")
                        todo[key] = value.strip() if isinstance(value, str) else value
                
                self.save_todos()
                return True
        return False
    
    def complete_todo(self, todo_id):
        """ToDoを完了にする（ファイル保存付き）"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                todo["completed_at"] = datetime.now()
                self.save_todos()
                return True
        return False
    
    def delete_todo(self, todo_id):
        """ToDoを削除（ファイル保存付き）"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                del self.todos[i]
                self.save_todos()
                return True
        return False
    
    def search_todos(self, keyword):
        """ToDoを検索"""
        if not keyword.strip():
            return []
        
        keyword = keyword.lower().strip()
        results = []
        
        for todo in self.todos:
            if (keyword in todo["title"].lower() or 
                keyword in todo["description"].lower()):
                results.append(todo)
        
        return results
    
    def get_statistics(self):
        """統計情報を取得"""
        total = len(self.todos)
        completed = len([todo for todo in self.todos if todo["completed"]])
        pending = total - completed
        
        priority_count = {"high": 0, "medium": 0, "low": 0}
        for todo in self.todos:
            if not todo["completed"]:
                priority_count[todo["priority"]] += 1
        
        # ファイル情報
        file_info = {}
        if self.todos_file.exists():
            stat = self.todos_file.stat()
            file_info = {
                "file_size": stat.st_size,
                "last_modified": datetime.fromtimestamp(stat.st_mtime)
            }
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "high_priority": priority_count["high"],
            "medium_priority": priority_count["medium"],
            "low_priority": priority_count["low"],
            "file_info": file_info
        }

class AdvancedTodoManagerUI:
    """高度なToDoマネージャーのUI"""
    
    def __init__(self):
        """UIを初期化"""
        self.manager = FileBasedTodoManager()
        self.priority_colors = {
            "high": "🔴",
            "medium": "🟡", 
            "low": "🟢"
        }
    
    def show_welcome(self):
        """ウェルカムメッセージを表示"""
        print("=" * 70)
        print("📁 ファイル対応ToDoマネージャー")
        print("=" * 70)
        print("✨ データ永続化機能付きのToDoマネージャーです")
        print(f"📂 データ保存場所: {self.manager.data_dir.absolute()}")
        print("=" * 70)
    
    def show_main_menu(self):
        """メインメニューを表示"""
        stats = self.manager.get_statistics()
        
        print(f"\n📊 現在の状況: 総数{stats['total']} | 完了{stats['completed']} | 未完了{stats['pending']}")
        
        if stats['file_info']:
            size_kb = stats['file_info']['file_size'] / 1024
            modified = stats['file_info']['last_modified'].strftime("%m/%d %H:%M")
            print(f"💾 ファイル: {size_kb:.1f}KB | 最終更新: {modified}")
        
        print("=" * 70)
        print("1. ToDoを追加")
        print("2. ToDoリストを表示")
        print("3. ToDoを完了/未完了にする")
        print("4. ToDoを編集")
        print("5. ToDoを削除")
        print("6. ToDoを検索")
        print("7. 統計情報を表示")
        print("8. バックアップ管理")
        print("9. インポート/エクスポート")
        print("10. 設定")
        print("0. 終了")
        print("=" * 70)
    
    def backup_menu(self):
        """バックアップ管理メニュー"""
        print("\n💾 バックアップ管理")
        print("-" * 40)
        print("1. バックアップ一覧表示")
        print("2. 手動バックアップ作成")
        print("3. バックアップからリストア")
        print("0. 戻る")
        
        choice = input("選択: ").strip()
        
        if choice == "1":
            self.show_backups()
        elif choice == "2":
            self.manager._create_backup()
            print("✅ バックアップを作成しました")
        elif choice == "3":
            self.restore_from_backup()
        elif choice == "0":
            return
        else:
            print("❌ 無効な選択です")
    
    def show_backups(self):
        """バックアップ一覧を表示"""
        backups = self.manager.list_backups()
        
        if not backups:
            print("📝 利用可能なバックアップがありません")
            return
        
        print(f"\n💾 利用可能なバックアップ ({len(backups)}件)")
        print("=" * 60)
        
        for i, backup in enumerate(backups, 1):
            created = backup['created'].strftime("%Y/%m/%d %H:%M:%S")
            size_kb = backup['size'] / 1024
            print(f"{i:2d}. {backup['filename']}")
            print(f"    📅 作成: {created} | 💾 サイズ: {size_kb:.1f}KB")
            print("-" * 60)
    
    def restore_from_backup(self):
        """バックアップからリストア"""
        backups = self.manager.list_backups()
        
        if not backups:
            print("📝 利用可能なバックアップがありません")
            return
        
        self.show_backups()
        
        try:
            choice = int(input("リストアするバックアップ番号: ")) - 1
            if 0 <= choice < len(backups):
                backup = backups[choice]
                print(f"\n⚠️ 現在のデータは自動的にバックアップされます")
                confirm = input(f"'{backup['filename']}' からリストアしますか？ (y/N): ").strip().lower()
                
                if confirm == 'y':
                    if self.manager.restore_from_backup(backup['path']):
                        print("✅ リストアが完了しました")
                    else:
                        print("❌ リストアに失敗しました")
                else:
                    print("❌ リストアをキャンセルしました")
            else:
                print("❌ 無効な番号です")
        except ValueError:
            print("❌ 有効な番号を入力してください")
    
    def import_export_menu(self):
        """インポート/エクスポートメニュー"""
        print("\n📤 インポート/エクスポート")
        print("-" * 40)
        print("1. CSVファイルにエクスポート")
        print("2. CSVファイルからインポート")
        print("0. 戻る")
        
        choice = input("選択: ").strip()
        
        if choice == "1":
            filename = input("保存ファイル名（省略可）: ").strip()
            if filename:
                self.manager.export_to_csv(filename)
            else:
                self.manager.export_to_csv()
        elif choice == "2":
            filename = input("インポートファイル名: ").strip()
            if filename:
                self.manager.import_from_csv(filename)
            else:
                print("❌ ファイル名を入力してください")
        elif choice == "0":
            return
        else:
            print("❌ 無効な選択です")
    
    def settings_menu(self):
        """設定メニュー"""
        print("\n⚙️ 設定")
        print("-" * 40)
        print(f"1. 自動バックアップ: {'有効' if self.manager.config['auto_backup'] else '無効'}")
        print(f"2. バックアップ間隔: {self.manager.config['backup_interval_days']}日")
        print(f"3. 最大バックアップ数: {self.manager.config['max_backups']}個")
        print(f"4. デフォルト優先度: {self.manager.config['default_priority']}")
        print("0. 戻る")
        
        choice = input("変更する項目: ").strip()
        
        try:
            if choice == "1":
                self.manager.config['auto_backup'] = not self.manager.config['auto_backup']
                status = '有効' if self.manager.config['auto_backup'] else '無効'
                print(f"✅ 自動バックアップを{status}にしました")
            elif choice == "2":
                days = int(input("バックアップ間隔（日数）: "))
                if days > 0:
                    self.manager.config['backup_interval_days'] = days
                    print(f"✅ バックアップ間隔を{days}日に設定しました")
                else:
                    print("❌ 1以上の数値を入力してください")
            elif choice == "3":
                max_backups = int(input("最大バックアップ数: "))
                if max_backups > 0:
                    self.manager.config['max_backups'] = max_backups
                    print(f"✅ 最大バックアップ数を{max_backups}個に設定しました")
                else:
                    print("❌ 1以上の数値を入力してください")
            elif choice == "4":
                print("デフォルト優先度:")
                print("1. 高 (🔴)")
                print("2. 中 (🟡)")
                print("3. 低 (🟢)")
                priority_choice = input("選択 (1-3): ").strip()
                priority_map = {"1": "high", "2": "medium", "3": "low"}
                if priority_choice in priority_map:
                    self.manager.config['default_priority'] = priority_map[priority_choice]
                    print(f"✅ デフォルト優先度を{priority_map[priority_choice]}に設定しました")
                else:
                    print("❌ 無効な選択です")
            elif choice == "0":
                return
            else:
                print("❌ 無効な選択です")
                return
            
            self.manager.save_config()
            
        except ValueError:
            print("❌ 無効な入力です")
    
    def run(self):
        """アプリケーションのメインループ"""
        self.show_welcome()
        
        while True:
            try:
                self.show_main_menu()
                choice = input("選択: ").strip()
                
                if choice == "1":
                    self.add_todo_interactive()
                elif choice == "2":
                    self.show_todos_interactive()
                elif choice == "3":
                    self.toggle_completion_interactive()
                elif choice == "4":
                    self.edit_todo_interactive()
                elif choice == "5":
                    self.delete_todo_interactive()
                elif choice == "6":
                    self.search_todos_interactive()
                elif choice == "7":
                    self.show_statistics_interactive()
                elif choice == "8":
                    self.backup_menu()
                elif choice == "9":
                    self.import_export_menu()
                elif choice == "10":
                    self.settings_menu()
                elif choice == "0":
                    print("\n👋 ToDoマネージャーを終了します")
                    print("💾 データは自動保存されました")
                    break
                else:
                    print("❌ 無効な選択です")
                
                input("\nEnterキーで続行...")
                
            except KeyboardInterrupt:
                print("\n\n👋 ToDoマネージャーを終了します")
                print("💾 データは自動保存されました")
                break
            except Exception as e:
                print(f"❌ 予期しないエラー: {e}")
                input("Enterキーで続行...")
    
    # 基本的なUI メソッドは simple_todo.py と同じなので省略
    # 実際には継承を使ってコードの重複を避ける方が良い
    
    def add_todo_interactive(self):
        """対話式でToDoを追加"""
        print("\n➕ 新しいToDoを追加")
        print("-" * 30)
        
        title = input("タイトル: ").strip()
        if not title:
            print("❌ タイトルは必須です")
            return
        
        description = input("説明（省略可）: ").strip()
        
        print("優先度を選択:")
        print("1. 高 (🔴)")
        print("2. 中 (🟡)") 
        print("3. 低 (🟢)")
        
        priority_choice = input(f"選択 (1-3、デフォルト:{self.manager.config['default_priority']}): ").strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        priority = priority_map.get(priority_choice, self.manager.config['default_priority'])
        
        try:
            todo_id = self.manager.add_todo(title, description, priority)
            print(f"✅ ToDoを追加しました (ID: {todo_id})")
            print("💾 ファイルに自動保存されました")
        except ValueError as e:
            print(f"❌ エラー: {e}")
    
    def show_todos_interactive(self):
        """対話式でToDoリストを表示"""
        print("\n📋 ToDoリスト表示")
        print("-" * 30)
        
        if not self.manager.todos:
            print("📝 ToDoがありません")
            return
        
        for todo in self.manager.todos:
            priority_icon = self.priority_colors[todo["priority"]]
            status_icon = "✅" if todo["completed"] else "⏳"
            
            created = todo["created_at"].strftime("%m/%d %H:%M")
            
            print(f"{status_icon} [{todo['id']:3d}] {priority_icon} {todo['title']}")
            
            if todo["description"]:
                print(f"    📄 {todo['description']}")
            
            print(f"    📅 作成: {created}")
            
            if todo["completed"] and todo["completed_at"]:
                completed = todo["completed_at"].strftime("%m/%d %H:%M")
                print(f"    ✅ 完了: {completed}")
            
            print("-" * 60)
    
    def toggle_completion_interactive(self):
        """対話式でToDoの完了状態を切り替え"""
        print("\n🔄 ToDoの完了状態を変更")
        print("-" * 30)
        
        try:
            todo_id = int(input("ToDoのID: "))
            
            if self.manager.complete_todo(todo_id):
                print("🎉 ToDoを完了しました！")
                print("💾 ファイルに自動保存されました")
            else:
                print("❌ 指定されたIDのToDoが見つかりません")
                
        except ValueError:
            print("❌ 有効なIDを入力してください")
    
    def edit_todo_interactive(self):
        """対話式でToDoを編集"""
        print("\n✏️ ToDoを編集")
        print("-" * 30)
        
        try:
            todo_id = int(input("編集するToDoのID: "))
            
            new_title = input("新しいタイトル（変更しない場合は空白）: ").strip()
            new_description = input("新しい説明（変更しない場合は空白）: ").strip()
            
            updates = {}
            if new_title:
                updates['title'] = new_title
            if new_description:
                updates['description'] = new_description
            
            if updates and self.manager.update_todo(todo_id, **updates):
                print("✅ ToDoを更新しました")
                print("💾 ファイルに自動保存されました")
            else:
                print("❌ 更新に失敗しました")
                
        except ValueError:
            print("❌ 有効なIDを入力してください")
    
    def delete_todo_interactive(self):
        """対話式でToDoを削除"""
        print("\n🗑️ ToDoを削除")
        print("-" * 30)
        
        try:
            todo_id = int(input("削除するToDoのID: "))
            
            confirm = input("本当に削除しますか？ (y/N): ").strip().lower()
            
            if confirm == 'y' and self.manager.delete_todo(todo_id):
                print("✅ ToDoを削除しました")
                print("💾 ファイルに自動保存されました")
            else:
                print("❌ 削除をキャンセルしました")
                
        except ValueError:
            print("❌ 有効なIDを入力してください")
    
    def search_todos_interactive(self):
        """対話式でToDoを検索"""
        print("\n🔍 ToDoを検索")
        print("-" * 30)
        
        keyword = input("検索キーワード: ").strip()
        
        if not keyword:
            print("❌ キーワードを入力してください")
            return
        
        results = self.manager.search_todos(keyword)
        
        if not results:
            print(f"📝 '{keyword}' にマッチするToDoが見つかりませんでした")
            return
        
        print(f"\n🔍 検索結果: '{keyword}' ({len(results)}件)")
        print("=" * 60)
        for todo in results:
            priority_icon = self.priority_colors[todo["priority"]]
            status_icon = "✅" if todo["completed"] else "⏳"
            print(f"{status_icon} [{todo['id']:3d}] {priority_icon} {todo['title']}")
            if todo["description"]:
                print(f"    📄 {todo['description']}")
            print("-" * 60)
    
    def show_statistics_interactive(self):
        """統計情報を表示"""
        stats = self.manager.get_statistics()
        
        print("\n📊 統計情報")
        print("=" * 50)
        print(f"📝 総ToDo数:        {stats['total']:3d}")
        print(f"✅ 完了:            {stats['completed']:3d}")
        print(f"⏳ 未完了:          {stats['pending']:3d}")
        print("-" * 50)
        print("📈 未完了の優先度別:")
        print(f"🔴 高優先度:        {stats['high_priority']:3d}")
        print(f"🟡 中優先度:        {stats['medium_priority']:3d}")
        print(f"🟢 低優先度:        {stats['low_priority']:3d}")
        
        if stats['file_info']:
            print("-" * 50)
            print("💾 ファイル情報:")
            size_kb = stats['file_info']['file_size'] / 1024
            modified = stats['file_info']['last_modified'].strftime("%Y/%m/%d %H:%M:%S")
            print(f"📁 サイズ:          {size_kb:.1f}KB")
            print(f"📅 最終更新:        {modified}")
        
        print("=" * 50)
        
        if stats['total'] > 0:
            completion_rate = (stats['completed'] / stats['total']) * 100
            print(f"🎯 完了率: {completion_rate:.1f}%")

def main():
    """メイン関数"""
    app = AdvancedTodoManagerUI()
    app.run()

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. ファイルI/O操作
   - JSON形式でのデータ保存・読み込み
   - ファイルの存在確認と安全な操作
   - エラーハンドリング

2. データの永続化
   - アプリケーション終了後もデータが保持される
   - 自動保存機能の実装

3. バックアップとリストア
   - データの安全性確保
   - 履歴管理と復旧機能

4. 設定管理
   - ユーザー設定の永続化
   - 設定ファイルの管理

5. インポート/エクスポート
   - CSV形式での外部連携
   - データの移行機能

🔧 改良案:
- 期限設定機能
- カテゴリ機能
- 共有機能
- クラウド同期
- 通知機能

⚡ 実行方法:
python3 projects/03_todo_manager/todo_with_files.py
"""