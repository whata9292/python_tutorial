#!/usr/bin/env python3
"""
プロジェクト3: シンプルToDoマネージャー

メモリ上でToDoリストを管理するシンプルなアプリケーションです。
リスト、辞書などのデータ構造の使い方を学習します。

学習ポイント:
- リストと辞書の活用
- CRUD操作（作成、読み取り、更新、削除）
- 検索とフィルタリング
- 状態管理

対応章: basics/06_data_structures.py完了後
"""

from datetime import datetime

class SimpleTodoManager:
    """シンプルなToDoマネージャークラス"""
    
    def __init__(self):
        """ToDoマネージャーを初期化"""
        self.todos = []
        self.next_id = 1
    
    def add_todo(self, title, description="", priority="medium"):
        """
        新しいToDoを追加
        
        Args:
            title (str): ToDoのタイトル
            description (str): 詳細説明
            priority (str): 優先度 ("high", "medium", "low")
        
        Returns:
            int: 追加されたToDoのID
        """
        if not title.strip():
            raise ValueError("タイトルは必須です")
        
        if priority not in ["high", "medium", "low"]:
            priority = "medium"
        
        todo = {
            "id": self.next_id,
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority,
            "completed": False,
            "created_at": datetime.now(),
            "completed_at": None
        }
        
        self.todos.append(todo)
        todo_id = self.next_id
        self.next_id += 1
        
        return todo_id
    
    def get_todo(self, todo_id):
        """
        IDでToDoを取得
        
        Args:
            todo_id (int): ToDoのID
            
        Returns:
            dict: ToDoの辞書、見つからない場合はNone
        """
        for todo in self.todos:
            if todo["id"] == todo_id:
                return todo
        return None
    
    def update_todo(self, todo_id, title=None, description=None, priority=None):
        """
        ToDoを更新
        
        Args:
            todo_id (int): 更新するToDoのID
            title (str): 新しいタイトル
            description (str): 新しい説明
            priority (str): 新しい優先度
            
        Returns:
            bool: 更新成功時True、失敗時False
        """
        todo = self.get_todo(todo_id)
        if not todo:
            return False
        
        if title is not None:
            if not title.strip():
                raise ValueError("タイトルは空にできません")
            todo["title"] = title.strip()
        
        if description is not None:
            todo["description"] = description.strip()
        
        if priority is not None:
            if priority in ["high", "medium", "low"]:
                todo["priority"] = priority
        
        return True
    
    def complete_todo(self, todo_id):
        """
        ToDoを完了にする
        
        Args:
            todo_id (int): 完了するToDoのID
            
        Returns:
            bool: 成功時True、失敗時False
        """
        todo = self.get_todo(todo_id)
        if not todo:
            return False
        
        todo["completed"] = True
        todo["completed_at"] = datetime.now()
        return True
    
    def uncomplete_todo(self, todo_id):
        """
        ToDoを未完了にする
        
        Args:
            todo_id (int): 未完了にするToDoのID
            
        Returns:
            bool: 成功時True、失敗時False
        """
        todo = self.get_todo(todo_id)
        if not todo:
            return False
        
        todo["completed"] = False
        todo["completed_at"] = None
        return True
    
    def delete_todo(self, todo_id):
        """
        ToDoを削除
        
        Args:
            todo_id (int): 削除するToDoのID
            
        Returns:
            bool: 削除成功時True、失敗時False
        """
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                del self.todos[i]
                return True
        return False
    
    def get_all_todos(self, filter_completed=None, filter_priority=None):
        """
        ToDoリストを取得（フィルタ機能付き）
        
        Args:
            filter_completed (bool): True=完了のみ、False=未完了のみ、None=全て
            filter_priority (str): 優先度でフィルタ
            
        Returns:
            list: フィルタされたToDoリスト
        """
        filtered_todos = self.todos.copy()
        
        if filter_completed is not None:
            filtered_todos = [todo for todo in filtered_todos 
                            if todo["completed"] == filter_completed]
        
        if filter_priority is not None:
            filtered_todos = [todo for todo in filtered_todos 
                            if todo["priority"] == filter_priority]
        
        return filtered_todos
    
    def search_todos(self, keyword):
        """
        キーワードでToDoを検索
        
        Args:
            keyword (str): 検索キーワード
            
        Returns:
            list: マッチしたToDoリスト
        """
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
        """
        統計情報を取得
        
        Returns:
            dict: 統計情報の辞書
        """
        total = len(self.todos)
        completed = len([todo for todo in self.todos if todo["completed"]])
        pending = total - completed
        
        priority_count = {"high": 0, "medium": 0, "low": 0}
        for todo in self.todos:
            if not todo["completed"]:
                priority_count[todo["priority"]] += 1
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "high_priority": priority_count["high"],
            "medium_priority": priority_count["medium"],
            "low_priority": priority_count["low"]
        }

class TodoManagerUI:
    """ToDoマネージャーのユーザーインターフェース"""
    
    def __init__(self):
        """UIを初期化"""
        self.manager = SimpleTodoManager()
        self.priority_colors = {
            "high": "🔴",
            "medium": "🟡", 
            "low": "🟢"
        }
    
    def show_welcome(self):
        """ウェルカムメッセージを表示"""
        print("=" * 60)
        print("📝 シンプルToDoマネージャー")
        print("=" * 60)
        print("タスクを効率的に管理しましょう！")
        print("=" * 60)
    
    def show_main_menu(self):
        """メインメニューを表示"""
        stats = self.manager.get_statistics()
        
        print(f"\n📊 現在の状況: 総数{stats['total']} | 完了{stats['completed']} | 未完了{stats['pending']}")
        print("=" * 60)
        print("1. ToDoを追加")
        print("2. ToDoリストを表示")
        print("3. ToDoを完了/未完了にする")
        print("4. ToDoを編集")
        print("5. ToDoを削除")
        print("6. ToDoを検索")
        print("7. 統計情報を表示")
        print("0. 終了")
        print("=" * 60)
    
    def format_todo(self, todo):
        """ToDoを見やすい形式でフォーマット"""
        priority_icon = self.priority_colors[todo["priority"]]
        status_icon = "✅" if todo["completed"] else "⏳"
        
        created = todo["created_at"].strftime("%m/%d %H:%M")
        
        result = f"{status_icon} [{todo['id']:3d}] {priority_icon} {todo['title']}"
        
        if todo["description"]:
            result += f"\n    📄 {todo['description']}"
        
        result += f"\n    📅 作成: {created}"
        
        if todo["completed"] and todo["completed_at"]:
            completed = todo["completed_at"].strftime("%m/%d %H:%M")
            result += f" | 完了: {completed}"
        
        return result
    
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
        
        priority_choice = input("選択 (1-3、デフォルト:2): ").strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        priority = priority_map.get(priority_choice, "medium")
        
        try:
            todo_id = self.manager.add_todo(title, description, priority)
            print(f"✅ ToDoを追加しました (ID: {todo_id})")
        except ValueError as e:
            print(f"❌ エラー: {e}")
    
    def show_todos_interactive(self):
        """対話式でToDoリストを表示"""
        print("\n📋 ToDoリスト表示オプション")
        print("-" * 30)
        print("1. 全て表示")
        print("2. 未完了のみ表示")
        print("3. 完了済みのみ表示")
        print("4. 優先度でフィルタ")
        
        choice = input("選択 (1-4): ").strip()
        
        filter_completed = None
        filter_priority = None
        
        if choice == "2":
            filter_completed = False
        elif choice == "3":
            filter_completed = True
        elif choice == "4":
            print("優先度を選択:")
            print("1. 高 (🔴)")
            print("2. 中 (🟡)")
            print("3. 低 (🟢)")
            priority_choice = input("選択 (1-3): ").strip()
            priority_map = {"1": "high", "2": "medium", "3": "low"}
            filter_priority = priority_map.get(priority_choice)
            if not filter_priority:
                print("❌ 無効な選択です")
                return
        
        todos = self.manager.get_all_todos(filter_completed, filter_priority)
        
        if not todos:
            print("📝 表示するToDoがありません")
            return
        
        print(f"\n📋 ToDoリスト ({len(todos)}件)")
        print("=" * 60)
        for todo in todos:
            print(self.format_todo(todo))
            print("-" * 60)
    
    def toggle_completion_interactive(self):
        """対話式でToDoの完了状態を切り替え"""
        print("\n🔄 ToDoの完了状態を変更")
        print("-" * 30)
        
        try:
            todo_id = int(input("ToDoのID: "))
            todo = self.manager.get_todo(todo_id)
            
            if not todo:
                print("❌ 指定されたIDのToDoが見つかりません")
                return
            
            print(f"\n現在のToDo:")
            print(self.format_todo(todo))
            
            if todo["completed"]:
                if self.manager.uncomplete_todo(todo_id):
                    print("✅ ToDoを未完了にしました")
                else:
                    print("❌ 更新に失敗しました")
            else:
                if self.manager.complete_todo(todo_id):
                    print("🎉 ToDoを完了しました！")
                else:
                    print("❌ 更新に失敗しました")
                    
        except ValueError:
            print("❌ 有効なIDを入力してください")
    
    def edit_todo_interactive(self):
        """対話式でToDoを編集"""
        print("\n✏️ ToDoを編集")
        print("-" * 30)
        
        try:
            todo_id = int(input("編集するToDoのID: "))
            todo = self.manager.get_todo(todo_id)
            
            if not todo:
                print("❌ 指定されたIDのToDoが見つかりません")
                return
            
            print(f"\n現在のToDo:")
            print(self.format_todo(todo))
            
            print("\n新しい情報を入力してください（変更しない場合は空白のままEnter）:")
            
            new_title = input(f"新しいタイトル [{todo['title']}]: ").strip()
            new_description = input(f"新しい説明 [{todo['description']}]: ").strip()
            
            print("新しい優先度:")
            print("1. 高 (🔴)")
            print("2. 中 (🟡)")
            print("3. 低 (🟢)")
            priority_choice = input(f"選択 [{todo['priority']}]: ").strip()
            
            priority_map = {"1": "high", "2": "medium", "3": "low"}
            new_priority = priority_map.get(priority_choice)
            
            # 空文字列の場合はNoneにして、更新をスキップ
            title_to_update = new_title if new_title else None
            desc_to_update = new_description if new_description else None
            priority_to_update = new_priority if new_priority else None
            
            try:
                if self.manager.update_todo(todo_id, title_to_update, desc_to_update, priority_to_update):
                    print("✅ ToDoを更新しました")
                else:
                    print("❌ 更新に失敗しました")
            except ValueError as e:
                print(f"❌ エラー: {e}")
                
        except ValueError:
            print("❌ 有効なIDを入力してください")
    
    def delete_todo_interactive(self):
        """対話式でToDoを削除"""
        print("\n🗑️ ToDoを削除")
        print("-" * 30)
        
        try:
            todo_id = int(input("削除するToDoのID: "))
            todo = self.manager.get_todo(todo_id)
            
            if not todo:
                print("❌ 指定されたIDのToDoが見つかりません")
                return
            
            print(f"\n削除対象のToDo:")
            print(self.format_todo(todo))
            
            confirm = input("\n本当に削除しますか？ (y/N): ").strip().lower()
            
            if confirm == 'y':
                if self.manager.delete_todo(todo_id):
                    print("✅ ToDoを削除しました")
                else:
                    print("❌ 削除に失敗しました")
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
            print(self.format_todo(todo))
            print("-" * 60)
    
    def show_statistics_interactive(self):
        """統計情報を表示"""
        stats = self.manager.get_statistics()
        
        print("\n📊 統計情報")
        print("=" * 40)
        print(f"📝 総ToDo数:        {stats['total']:3d}")
        print(f"✅ 完了:            {stats['completed']:3d}")
        print(f"⏳ 未完了:          {stats['pending']:3d}")
        print("-" * 40)
        print("📈 未完了の優先度別:")
        print(f"🔴 高優先度:        {stats['high_priority']:3d}")
        print(f"🟡 中優先度:        {stats['medium_priority']:3d}")
        print(f"🟢 低優先度:        {stats['low_priority']:3d}")
        print("=" * 40)
        
        if stats['total'] > 0:
            completion_rate = (stats['completed'] / stats['total']) * 100
            print(f"🎯 完了率: {completion_rate:.1f}%")
    
    def run(self):
        """アプリケーションのメインループ"""
        self.show_welcome()
        
        # サンプルデータを追加
        self.manager.add_todo("Welcome!", "シンプルToDoマネージャーへようこそ！", "low")
        self.manager.add_todo("このアプリを試してみる", "各機能を使ってToDoを管理してみましょう", "medium")
        
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
                elif choice == "0":
                    print("\n👋 ToDoマネージャーを終了します")
                    print("お疲れ様でした！")
                    break
                else:
                    print("❌ 無効な選択です")
                
                input("\nEnterキーで続行...")
                
            except KeyboardInterrupt:
                print("\n\n👋 ToDoマネージャーを終了します")
                break
            except Exception as e:
                print(f"❌ 予期しないエラー: {e}")
                input("Enterキーで続行...")

def main():
    """メイン関数"""
    app = TodoManagerUI()
    app.run()

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. データ構造の活用
   - リストを使ったToDoの管理
   - 辞書を使った構造化データ
   - フィルタリングと検索の実装

2. CRUD操作
   - Create: ToDoの作成
   - Read: ToDoの表示・検索
   - Update: ToDoの編集・状態変更
   - Delete: ToDoの削除

3. ユーザーインターフェース
   - メニューシステムの設計
   - エラーハンドリング
   - ユーザーフレンドリーな表示

4. オブジェクト指向設計
   - データとロジックの分離
   - クラスの設計と責任分離

🔧 改良案:
- ファイル保存機能
- カテゴリ機能
- 期限設定
- ソート機能
- エクスポート機能

⚡ 実行方法:
python3 projects/03_todo_manager/simple_todo.py
"""