# 📝 プロジェクト3: ToDoマネージャー

タスクを効率的に管理するToDoマネージャーアプリケーションです。メモリベースから永続化対応まで段階的に学習できます。

## 📚 概要

このプロジェクトでは、データ構造の活用からファイルI/O、JSON操作まで、実用的なタスク管理アプリケーションを通じて学習します。CRUD操作、検索機能、バックアップシステムなど、実際のアプリケーション開発で必要な技術を体験できます。

## 🎯 学習目標

- **データ構造の活用** - リスト、辞書を使った効率的なデータ管理
- **CRUD操作** - 作成、読み取り、更新、削除の実装
- **ファイルI/O** - データの永続化と安全な読み書き
- **JSON操作** - 構造化データの保存・読み込み
- **エラーハンドリング** - 堅牢なアプリケーション設計
- **バックアップシステム** - データの安全性確保

## 📁 ファイル構成

```
03_todo_manager/
├── README.md              # このファイル
├── simple_todo.py         # シンプル版（メモリベース）
└── todo_with_files.py     # 高度版（ファイル永続化）
```

## 🚀 使い方

### シンプルToDoマネージャー

```bash
python3 projects/03_todo_manager/simple_todo.py
```

**機能:**
- メモリ上でのToDo管理
- CRUD操作（作成・表示・更新・削除）
- 優先度設定（高・中・低）
- 検索とフィルタリング
- 統計情報表示

**推奨学習レベル:** basics/06_data_structures.py 完了後

### ファイル対応ToDoマネージャー

```bash
python3 projects/03_todo_manager/todo_with_files.py
```

**機能:**
- JSON形式でのデータ永続化
- 自動バックアップシステム
- CSVインポート/エクスポート
- 設定のカスタマイズ
- バックアップからのリストア

**推奨学習レベル:** basics/08_input_output.py 完了後

## ⚙️ 機能詳細

### ToDoの基本構造

```python
todo = {
    "id": 1,
    "title": "買い物に行く",
    "description": "牛乳、パン、卵を買う",
    "priority": "medium",  # high, medium, low
    "completed": False,
    "created_at": datetime.now(),
    "completed_at": None
}
```

### 基本操作

#### 1. ToDoの追加
```python
todo_id = manager.add_todo(
    title="重要なタスク",
    description="詳細な説明",
    priority="high"
)
```

#### 2. ToDoの検索
```python
# キーワード検索
results = manager.search_todos("買い物")

# フィルタリング
pending_todos = manager.get_all_todos(filter_completed=False)
high_priority = manager.get_all_todos(filter_priority="high")
```

#### 3. 統計情報の取得
```python
stats = manager.get_statistics()
# {'total': 10, 'completed': 7, 'pending': 3, ...}
```

## 🎮 実際の使用例

### シンプル版の実行例

```
📝 シンプルToDoマネージャー
==================================================
📊 現在の状況: 総数2 | 完了0 | 未完了2

1. ToDoを追加
2. ToDoリストを表示
3. ToDoを完了/未完了にする

選択: 1

➕ 新しいToDoを追加
タイトル: プロジェクトの企画書作成
説明（省略可）: 来週のプレゼン用資料
優先度を選択:
1. 高 (🔴)
2. 中 (🟡)
3. 低 (🟢)
選択: 1

✅ ToDoを追加しました (ID: 3)
```

### ファイル版の実行例

```
📁 ファイル対応ToDoマネージャー
====================================================
✨ データ永続化機能付きのToDoマネージャーです
📂 データ保存場所: /path/to/todo_data

💾 ファイル: 2.4KB | 最終更新: 12/08 14:30

8. バックアップ管理
9. インポート/エクスポート
10. 設定

選択: 8

💾 バックアップ管理
1. バックアップ一覧表示
2. 手動バックアップ作成
3. バックアップからリストア

選択: 1

💾 利用可能なバックアップ (3件)
============================================================
 1. todos_backup_20240108_143022.json
    📅 作成: 2024/01/08 14:30:22 | 💾 サイズ: 2.3KB
 2. todos_backup_20240107_092015.json
    📅 作成: 2024/01/07 09:20:15 | 💾 サイズ: 1.8KB
```

## 💾 データファイル

ファイル版では以下のファイルが自動生成されます：

### todos.json（メインデータ）
```json
{
  "todos": [
    {
      "id": 1,
      "title": "プロジェクト企画書作成",
      "description": "来週のプレゼン用資料",
      "priority": "high",
      "completed": false,
      "created_at": "2024-01-08T14:30:22",
      "completed_at": null
    }
  ],
  "next_id": 2,
  "last_saved": "2024-01-08T14:30:22"
}
```

### config.json（設定ファイル）
```json
{
  "auto_backup": true,
  "backup_interval_days": 7,
  "max_backups": 10,
  "default_priority": "medium",
  "date_format": "%Y-%m-%d %H:%M:%S"
}
```

### backups/（バックアップディレクトリ）
```
backups/
├── todos_backup_20240108_143022.json
├── todos_backup_20240107_092015.json
└── todos_backup_20240106_185530.json
```

## 🔧 カスタマイズ方法

### 新しい優先度レベルの追加

```python
# 優先度の拡張
PRIORITY_LEVELS = {
    "urgent": {"color": "🚨", "value": 4},
    "high": {"color": "🔴", "value": 3},
    "medium": {"color": "🟡", "value": 2},
    "low": {"color": "🟢", "value": 1}
}
```

### カスタムフィルターの実装

```python
def get_todos_by_date_range(self, start_date, end_date):
    """日付範囲でToDoをフィルタ"""
    filtered_todos = []
    for todo in self.todos:
        if start_date <= todo['created_at'].date() <= end_date:
            filtered_todos.append(todo)
    return filtered_todos
```

### エクスポート形式の拡張

```python
def export_to_markdown(self, filename):
    """Markdown形式でエクスポート"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# ToDoリスト\n\n")
        
        for todo in self.todos:
            status = "✅" if todo['completed'] else "⏳"
            f.write(f"- {status} **{todo['title']}**\n")
            if todo['description']:
                f.write(f"  - {todo['description']}\n")
            f.write(f"  - 優先度: {todo['priority']}\n\n")
```

## 🧪 テスト方法

### 基本機能のテスト

```python
def test_todo_operations():
    """基本操作のテスト"""
    manager = SimpleTodoManager()
    
    # 追加テスト
    todo_id = manager.add_todo("テストタスク", "テスト用", "high")
    assert todo_id == 1
    
    # 取得テスト
    todo = manager.get_todo(todo_id)
    assert todo['title'] == "テストタスク"
    assert todo['priority'] == "high"
    
    # 完了テスト
    assert manager.complete_todo(todo_id) == True
    todo = manager.get_todo(todo_id)
    assert todo['completed'] == True
    
    # 削除テスト
    assert manager.delete_todo(todo_id) == True
    assert manager.get_todo(todo_id) == None
    
    print("✅ 全テスト合格")

test_todo_operations()
```

### ファイル操作のテスト

```python
def test_file_operations():
    """ファイル操作のテスト"""
    import tempfile
    import shutil
    
    # 一時ディレクトリでテスト
    with tempfile.TemporaryDirectory() as temp_dir:
        manager = FileBasedTodoManager(temp_dir)
        
        # データ保存テスト
        manager.add_todo("テストタスク")
        assert manager.todos_file.exists()
        
        # データ読み込みテスト
        manager2 = FileBasedTodoManager(temp_dir)
        assert len(manager2.todos) == 1
        assert manager2.todos[0]['title'] == "テストタスク"
    
    print("✅ ファイル操作テスト合格")

test_file_operations()
```

## 💡 学習のポイント

### 1. データ構造の適切な選択
- **リスト**: ToDoの順序を保持
- **辞書**: 構造化データの表現
- **ID管理**: データの一意性確保

### 2. CRUD操作の実装
- **Create**: データの追加とバリデーション
- **Read**: 検索とフィルタリング
- **Update**: 部分的な更新の処理
- **Delete**: 安全な削除操作

### 3. エラーハンドリング
- **入力検証**: 不正データの早期チェック
- **ファイル操作**: 存在しないファイルやアクセス権限
- **データ整合性**: ID重複や不正な状態の回避

### 4. ユーザビリティ
- **直感的なメニュー**: 分かりやすいナビゲーション
- **フィードバック**: 操作結果の明確な表示
- **エラーメッセージ**: 建設的で分かりやすい案内

## 🔄 改良案

### 機能拡張のアイデア
1. **期限設定** - due_date フィールドの追加
2. **カテゴリ機能** - タスクのグループ化
3. **サブタスク** - 階層構造のサポート
4. **タグ機能** - ラベルによる分類
5. **時間追跡** - 作業時間の記録
6. **リマインダー** - 期限通知機能

### アーキテクチャの改善
1. **MVCパターン** - Model, View, Controller の分離
2. **データベース対応** - SQLiteの活用
3. **API化** - REST APIとしての提供
4. **GUI版** - tkinter/PyQt を使ったデスクトップアプリ
5. **Web版** - Flask/Django を使ったWebアプリ

## 📈 パフォーマンスの最適化

### 大量データ対応
```python
def search_todos_optimized(self, keyword):
    """最適化された検索機能"""
    if not keyword.strip():
        return []
    
    keyword = keyword.lower()
    
    # インデックスを使った高速検索（実装例）
    results = []
    for todo in self.todos:
        # 早期リターンによる最適化
        if keyword in todo["title"].lower():
            results.append(todo)
        elif keyword in todo["description"].lower():
            results.append(todo)
    
    return results
```

### メモリ効率の改善
```python
def get_todos_generator(self, filter_func=None):
    """ジェネレータを使ったメモリ効率的な取得"""
    for todo in self.todos:
        if filter_func is None or filter_func(todo):
            yield todo
```

## 🎓 次のステップ

このプロジェクト完了後の推奨学習：

1. **プロジェクト4** - テキスト解析で文字列処理を深く学習
2. **データベース** - SQLiteを使ったデータ永続化
3. **Web化** - Flask/Djangoを使ったWebアプリ開発
4. **API開発** - RESTful APIの設計と実装
5. **テスト駆動開発** - unittestを使った本格的なテスト

## ❓ よくある質問

**Q: データが保存されません**
A: ファイル版を使用していて、適切な書き込み権限があるか確認してください。data_dirの場所も確認してください。

**Q: バックアップが作成されません**
A: 設定で`auto_backup`が有効になっているか確認してください。手動でバックアップを作成することも可能です。

**Q: 大量のToDoを扱うと遅くなります**
A: 現在の実装はシンプルな線形検索です。より大量のデータには、データベース（SQLite）の使用を検討してください。

**Q: 他のアプリからデータをインポートしたい**
A: CSV形式でのインポート機能があります。Excel等からCSV出力したデータを読み込めます。

**Q: チーム間でToDoリストを共有したい**
A: 現在はローカルファイルのみです。共有には、クラウドストレージへの保存やサーバー機能の追加が必要です。

---

**効率的なタスク管理をお楽しみください！** 📝✨