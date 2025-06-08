#!/usr/bin/env python3
"""
エラーハンドリングモジュール
初心者向けの分かりやすいエラーメッセージと解決方法を提供
"""

import sys
import platform
import os
from pathlib import Path


class BeginnerErrorHandler:
    """完全初心者向けエラー対応システム"""
    
    def __init__(self):
        self.platform = platform.system()
        self.python_cmd = "py" if self.platform == "Windows" else "python3"
    
    def handle_command_not_found(self):
        """コマンドが見つからないエラーの対処"""
        print("🚨 'python3' コマンドが見つかりません")
        print("\n🔧 解決方法:")
        
        if self.platform == "Windows":
            print("1. 'py' を試してください:")
            print("   py quizzes/quiz_runner.py basics 01")
            print("\n2. または 'python' を試してください:")
            print("   python quizzes/quiz_runner.py basics 01")
        else:
            print("1. 'python' を試してください:")
            print("   python quizzes/quiz_runner.py basics 01")
            print("\n2. Pythonがインストールされているか確認:")
            print("   which python3")
        
        print("\n💡 それでもダメな場合:")
        print("   setup/01_python_installation.py を実行してください")
    
    def handle_file_not_found(self, filename=None):
        """ファイルが見つからないエラーの対処"""
        print(f"🚨 ファイルが見つかりません: {filename or '指定されたファイル'}")
        print("\n🔧 解決方法:")
        print("1. 現在のフォルダを確認:")
        
        if self.platform == "Windows":
            print("   dir")
        else:
            print("   ls")
        
        print("   → 'quizzes' フォルダが見えるはずです")
        print("\n2. python-tutorial フォルダに移動:")
        print("   cd python-tutorial")
        print("\n3. もう一度実行:")
        print(f"   {self.python_cmd} quizzes/quiz_runner.py help")
    
    def handle_module_not_found(self, module_name):
        """モジュールが見つからないエラーの対処"""
        print(f"🚨 モジュール '{module_name}' が見つかりません")
        print("\n🔧 解決方法:")
        
        if module_name in ['colorama']:
            print("1. 必要なパッケージをインストール:")
            print(f"   {self.python_cmd} -m pip install -r requirements.txt")
            print("\n2. または個別にインストール:")
            print(f"   {self.python_cmd} -m pip install {module_name}")
        else:
            print("1. フォルダ構造を確認してください")
            print("2. すべてのファイルが正しく配置されているか確認")
    
    def handle_permission_error(self, path=None):
        """権限エラーの対処"""
        print(f"🚨 ファイルへのアクセス権限がありません: {path or 'ファイル'}")
        print("\n🔧 解決方法:")
        print("1. 別のフォルダで試す")
        print("2. 管理者権限で実行（通常は不要）")
        
        if self.platform != "Windows":
            print("3. ファイルの権限を確認:")
            print(f"   ls -la {path or '.'}")
    
    def run_environment_diagnosis(self):
        """自動環境診断"""
        print("🔍 環境診断を実行中...")
        print("=" * 50)
        
        checks = [
            ("Python インストール", self._check_python),
            ("作業ディレクトリ", self._check_directory),
            ("必要ファイル", self._check_files),
            ("実行権限", self._check_permissions)
        ]
        
        all_ok = True
        for name, check_func in checks:
            try:
                result, message = check_func()
                status = "✅" if result else "❌"
                print(f"{status} {name}: {message}")
                all_ok &= result
            except Exception as e:
                print(f"❌ {name}: エラー - {e}")
                all_ok = False
        
        print("=" * 50)
        
        if all_ok:
            print("✅ 環境に問題はありません！")
        else:
            print("⚠️  上記の問題を解決してください")
        
        return all_ok
    
    def _check_python(self):
        """Pythonインストールチェック"""
        version = sys.version.split()[0]
        major, minor = sys.version_info[:2]
        
        if major >= 3 and minor >= 8:
            return True, f"Python {version} (推奨バージョン)"
        elif major >= 3:
            return True, f"Python {version} (動作可能)"
        else:
            return False, "Python 3.x が必要です"
    
    def _check_directory(self):
        """作業ディレクトリチェック"""
        cwd = os.getcwd()
        if "python-tutorial" in cwd or "python_tutorial" in cwd:
            return True, "正しいディレクトリ"
        else:
            return False, f"現在: {cwd} (python-tutorialフォルダに移動してください)"
    
    def _check_files(self):
        """必要ファイルの存在チェック"""
        required_files = [
            "quizzes/quiz_runner.py",
            "quizzes/quiz_config.json",
            "basics/01_interpreter_basics.py"
        ]
        
        missing = []
        for file in required_files:
            if not Path(file).exists():
                missing.append(file)
        
        if not missing:
            return True, "すべてのファイルが存在"
        else:
            return False, f"不足: {', '.join(missing)}"
    
    def _check_permissions(self):
        """実行権限チェック"""
        test_file = "test_permission_check.tmp"
        try:
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            return True, "書き込み権限あり"
        except:
            return False, "書き込み権限なし"
    
    def show_troubleshooting_guide(self):
        """トラブルシューティングガイド"""
        print("\n🛠️ トラブルシューティングガイド")
        print("=" * 50)
        
        print("\n【よくある問題と解決方法】")
        
        print("\n1️⃣ コマンドが実行できない")
        print("   → Pythonがインストールされているか確認")
        print(f"   → {self.python_cmd} --version")
        
        print("\n2️⃣ ファイルが見つからない")
        print("   → 正しいフォルダにいるか確認")
        print("   → python-tutorial フォルダに移動")
        
        print("\n3️⃣ エラーメッセージが英語で分からない")
        print("   → エラーの最後の行を読む")
        print("   → 'FileNotFoundError' = ファイルが見つからない")
        print("   → 'SyntaxError' = コードの書き方が間違っている")
        print("   → 'NameError' = 変数名や関数名が間違っている")
        
        print("\n4️⃣ テストが実行できない")
        print("   → まず basics/01_interpreter_basics.py を実行")
        print("   → その後でテストを実行")
        
        print("\n💡 それでも解決しない場合:")
        print("   1. エラーメッセージ全体をコピー")
        print("   2. インターネットで検索")
        print("   3. 誰かに相談")
        print("\n" + "=" * 50)