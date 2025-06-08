#!/usr/bin/env python3
"""
理解度テスト実行エンジン

Python完全初心者向けチュートリアルの理解度テストを実行する
メインプログラムです。

使用方法:
  python3 quizzes/quiz_runner.py basics 01    # 基礎01テスト
  python3 quizzes/quiz_runner.py project 01   # プロジェクト01テスト
  python3 quizzes/quiz_runner.py progress     # 進捗確認
  python3 quizzes/quiz_runner.py help         # ヘルプ
  python3 quizzes/quiz_runner.py diagnose     # 環境診断
"""

import sys
import json
import argparse
import platform
from pathlib import Path

# 自作モジュールをインポート
try:
    from error_handler import BeginnerErrorHandler
    from progress_tracker import ProgressTracker
except ImportError as e:
    print(f"❌ モジュールのインポートエラー: {e}")
    print("現在のディレクトリが quizzes/ またはプロジェクトルートか確認してください")
    sys.exit(1)


class QuizRunner:
    """理解度テスト実行エンジン"""
    
    def __init__(self):
        self.config = self._load_config()
        self.error_handler = BeginnerErrorHandler()
        self.progress_tracker = ProgressTracker()
        self.platform = platform.system()
        self.python_cmd = "py" if self.platform == "Windows" else "python3"
    
    def _load_config(self):
        """設定ファイルを読み込み"""
        config_file = Path("quizzes/quiz_config.json")
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print("⚠️  設定ファイルが見つかりません")
            return self._default_config()
    
    def _default_config(self):
        """デフォルト設定"""
        return {
            "quiz_settings": {"pass_score": 70, "max_retries": 3},
            "messages": {
                "welcome": "🧪 理解度テストを開始します",
                "pass": "✅ 合格おめでとうございます！",
                "fail": "📚 もう少し復習が必要です"
            }
        }
    
    def parse_arguments(self):
        """コマンドライン引数を解析"""
        parser = argparse.ArgumentParser(
            description="Python学習チュートリアル理解度テスト",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
使用例:
  %(prog)s basics 01      # 基礎第1章のテスト
  %(prog)s project 01     # プロジェクト1のテスト
  %(prog)s progress       # 進捗確認
  %(prog)s help           # 詳細ヘルプ
  %(prog)s diagnose       # 環境診断
            """
        )
        
        parser.add_argument('command', 
                          help='実行するコマンド (basics, project, progress, help, diagnose)')
        parser.add_argument('number', nargs='?', type=int,
                          help='章番号またはプロジェクト番号')
        parser.add_argument('--debug', action='store_true',
                          help='デバッグモードで実行')
        
        return parser.parse_args()
    
    def main(self):
        """メイン実行関数"""
        try:
            args = self.parse_arguments()
            
            if args.command == "help":
                self.show_help(args.number or 1)
            elif args.command == "progress":
                self.progress_tracker.show_dashboard()
            elif args.command == "diagnose":
                self.error_handler.run_environment_diagnosis()
            elif args.command in ["basics", "project"]:
                if args.number is None:
                    print("❌ 章番号またはプロジェクト番号を指定してください")
                    print(f"例: {self.python_cmd} quizzes/quiz_runner.py {args.command} 01")
                    return
                self.run_quiz(args.command, args.number)
            else:
                print(f"❌ 不明なコマンド: {args.command}")
                self.show_help(1)
        
        except KeyboardInterrupt:
            print("\n\n⚠️  テストを中断しました")
        except Exception as e:
            if "--debug" in sys.argv:
                raise  # デバッグモードでは例外をそのまま表示
            self.handle_error(e)
    
    def run_quiz(self, section, number):
        """クイズ実行"""
        print(self.config["messages"]["welcome"])
        print("=" * 50)
        
        # セクション名を取得
        section_name = self.progress_tracker.get_section_name(
            section + "s", number  # basics -> basics, project -> projects
        )
        print(f"📝 {section_name} の理解度テスト")
        print()
        
        # 再挑戦可能かチェック
        eligible, message = self.progress_tracker.check_retry_eligibility(
            section + "s", number
        )
        
        if not eligible:
            print(f"⏰ {message}")
            return
        
        print(f"💡 {message}")
        print()
        
        # テストの説明
        self._show_quiz_info()
        
        if not self._confirm_start():
            print("テストをキャンセルしました")
            return
        
        # 実際のテスト実行（デモ版）
        score = self._run_demo_quiz(section, number)
        
        # 結果の表示と記録
        self._show_results(score, section, number)
    
    def _show_quiz_info(self):
        """テスト情報を表示"""
        settings = self.config["quiz_settings"]
        print("📋 テストについて:")
        print(f"  • 問題数: 6-8問")
        print(f"  • 合格ライン: {settings['pass_score']}%")
        print(f"  • 再挑戦: {settings['max_retries']}回まで可能")
        print(f"  • ヒント: 利用可能（得点は少し下がります）")
        print()
    
    def _confirm_start(self):
        """開始確認"""
        while True:
            response = input("テストを開始しますか？ (yes/no): ").lower()
            if response in ['yes', 'y', 'はい']:
                return True
            elif response in ['no', 'n', 'いいえ']:
                return False
            else:
                print("'yes' または 'no' で答えてください")
    
    def _run_demo_quiz(self, section, number):
        """デモ版クイズ実行"""
        print("\n🚀 テスト開始！")
        print("=" * 50)
        
        # デモ問題（実際の実装では外部ファイルから読み込む）
        questions = self._get_demo_questions(section, number)
        
        total_score = 0
        max_score = len(questions) * 10  # 1問10点として
        
        for i, question in enumerate(questions, 1):
            print(f"\n問題 {i}: {question['question']}")
            
            if question['type'] == 'multiple_choice':
                score = self._handle_multiple_choice(question)
            elif question['type'] == 'fill_blank':
                score = self._handle_fill_blank(question)
            else:
                score = 10  # デモなので満点
            
            total_score += score
            print(f"得点: {score}/10")
        
        percentage = int((total_score / max_score) * 100)
        return percentage
    
    def _get_demo_questions(self, section, number):
        """デモ問題を生成"""
        if section == "basics" and number == 1:
            return [
                {
                    "type": "multiple_choice",
                    "question": "Pythonインタープリターを起動するコマンドは？",
                    "choices": ["python3", "python", "py", "すべて正解"],
                    "correct": 3,
                    "explanation": "環境によって異なりますが、どれも使える可能性があります"
                },
                {
                    "type": "fill_blank",
                    "question": "変数 x に 10 を代入するコードは？",
                    "template": "x ___ 10",
                    "correct": "=",
                    "explanation": "= は代入演算子です"
                },
                {
                    "type": "multiple_choice",
                    "question": "2の3乗を計算する演算子は？",
                    "choices": ["2^3", "2**3", "2*3", "pow(2,3)"],
                    "correct": 1,
                    "explanation": "** がべき乗演算子です"
                }
            ]
        else:
            return [
                {
                    "type": "multiple_choice",
                    "question": f"{section} {number} のデモ問題です",
                    "choices": ["選択肢A", "選択肢B", "選択肢C", "選択肢D"],
                    "correct": 0,
                    "explanation": "これはデモ問題です"
                }
            ]
    
    def _handle_multiple_choice(self, question):
        """選択肢問題の処理"""
        for i, choice in enumerate(question['choices']):
            print(f"  {i+1}. {choice}")
        
        while True:
            try:
                answer = input("\n答えを選んでください (1-4): ")
                answer_idx = int(answer) - 1
                
                if 0 <= answer_idx < len(question['choices']):
                    if answer_idx == question['correct']:
                        print("✅ 正解！")
                        print(f"解説: {question['explanation']}")
                        return 10
                    else:
                        print("❌ 不正解")
                        print(f"正解: {question['choices'][question['correct']]}")
                        print(f"解説: {question['explanation']}")
                        return 0
                else:
                    print("1-4の数字を入力してください")
            except ValueError:
                print("数字を入力してください")
    
    def _handle_fill_blank(self, question):
        """穴埋め問題の処理"""
        print(f"空欄を埋めてください: {question['template']}")
        
        answer = input("答え: ").strip()
        
        if answer == question['correct']:
            print("✅ 正解！")
            print(f"解説: {question['explanation']}")
            return 10
        else:
            print("❌ 不正解")
            print(f"正解: {question['correct']}")
            print(f"解説: {question['explanation']}")
            return 0
    
    def _show_results(self, score, section, number):
        """結果表示と記録"""
        print("\n" + "=" * 50)
        print("🎯 テスト結果")
        print("=" * 50)
        
        passed = score >= self.config["quiz_settings"]["pass_score"]
        
        print(f"得点: {score}% / 100%")
        print(f"合格ライン: {self.config['quiz_settings']['pass_score']}%")
        print()
        
        if passed:
            print(self.config["messages"]["pass"])
            self._show_next_steps(section, number)
        else:
            print(self.config["messages"]["fail"])
            self._show_retry_info(section, number)
        
        # 進捗を記録
        self.progress_tracker.update_score(section + "s", number, score, passed)
        
        print("\n💡 進捗を確認するには:")
        print(f"   {self.python_cmd} quizzes/quiz_runner.py progress")
    
    def _show_next_steps(self, section, number):
        """次のステップを表示"""
        print("\n📚 次のステップ:")
        
        if section == "basics":
            if number < 12:
                next_file = f"basics/{number+1:02d}_*.py"
                print(f"   {self.python_cmd} {next_file}")
            else:
                print("   基礎学習完了！setup/03_virtual_environment.py へ")
        else:
            print("   次のプロジェクトに挑戦しましょう！")
    
    def _show_retry_info(self, section, number):
        """再挑戦情報を表示"""
        status = self.progress_tracker.get_completion_status(section + "s", number)
        remaining = 3 - status["attempts"]
        
        if remaining > 0:
            print(f"\n💪 あと{remaining}回挑戦できます")
            print("復習してから再挑戦しましょう！")
        else:
            print("\n⏰ 1時間後に再挑戦できます")
    
    def show_help(self, level=1):
        """ヘルプを表示"""
        print("\n🆘 Python学習チュートリアル ヘルプ")
        print("=" * 50)
        
        print("\n【基本的な使い方】")
        print(f"{self.python_cmd} quizzes/quiz_runner.py <コマンド> [番号]")
        print()
        
        print("【利用可能なコマンド】")
        print("  basics <番号>   - 基礎学習のテスト (例: basics 01)")
        print("  project <番号>  - プロジェクトのテスト (例: project 01)")
        print("  progress        - 学習進捗を表示")
        print("  help            - このヘルプを表示")
        print("  diagnose        - 環境の問題診断")
        print()
        
        if level >= 2:
            print("【学習の流れ】")
            print("1. 学習ファイルを実行")
            print(f"   {self.python_cmd} basics/01_interpreter_basics.py")
            print()
            print("2. 理解度テストを受ける")
            print(f"   {self.python_cmd} quizzes/quiz_runner.py basics 01")
            print()
            print("3. 合格したら次の章へ")
            print()
        
        print("【困ったときは】")
        print(f"  {self.python_cmd} quizzes/quiz_runner.py diagnose")
        print("  でシステムの診断ができます")
        print()
        
        if level >= 2:
            self.error_handler.show_troubleshooting_guide()
    
    def handle_error(self, error):
        """エラーハンドリング"""
        error_name = type(error).__name__
        
        print(f"\n❌ エラーが発生しました: {error_name}")
        print(f"詳細: {error}")
        print()
        
        if "FileNotFoundError" in error_name:
            self.error_handler.handle_file_not_found(str(error))
        elif "ModuleNotFoundError" in error_name:
            module_name = str(error).split("'")[1] if "'" in str(error) else "不明"
            self.error_handler.handle_module_not_found(module_name)
        elif "PermissionError" in error_name:
            self.error_handler.handle_permission_error()
        else:
            print("💡 解決方法:")
            print("1. エラーメッセージを確認")
            print("2. 環境診断を実行:")
            print(f"   {self.python_cmd} quizzes/quiz_runner.py diagnose")
            print("3. ヘルプを確認:")
            print(f"   {self.python_cmd} quizzes/quiz_runner.py help")


def main():
    """エントリーポイント"""
    quiz_runner = QuizRunner()
    quiz_runner.main()


if __name__ == "__main__":
    main()