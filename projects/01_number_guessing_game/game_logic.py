#!/usr/bin/env python3
"""
=================================
数当てゲーム - 機能分割版
=================================

main.py の機能をより構造化し、拡張機能を追加した版です。
関数やクラスを使ってコードを整理し、再利用性を高めています。

追加機能:
- 難易度設定
- 最高記録の保存
- 詳細な統計表示
- より良いユーザーインターフェース
"""

import random
import json
import os
from datetime import datetime


class NumberGuessingGame:
    """数当てゲームのメインクラス"""
    
    def __init__(self):
        """ゲームの初期化"""
        self.stats_file = "game_stats.json"
        self.load_statistics()
        
        # 難易度設定
        self.difficulty_levels = {
            1: {"range": (1, 50), "name": "簡単", "max_attempts": 8},
            2: {"range": (1, 100), "name": "普通", "max_attempts": 10},
            3: {"range": (1, 200), "name": "難しい", "max_attempts": 12}
        }
    
    def load_statistics(self):
        """統計データを読み込む"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    self.stats = json.load(f)
            except:
                self.stats = self._initialize_stats()
        else:
            self.stats = self._initialize_stats()
    
    def _initialize_stats(self):
        """統計データの初期化"""
        return {
            "total_games": 0,
            "total_wins": 0,
            "best_attempts": {},  # 難易度別の最小試行回数
            "average_attempts": {},  # 難易度別の平均試行回数
            "game_history": []
        }
    
    def save_statistics(self):
        """統計データを保存"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  統計データの保存に失敗: {e}")
    
    def print_welcome_message(self):
        """ゲーム開始時のメッセージを表示"""
        print("=" * 60)
        print("🎯 数当てゲーム - 拡張版")
        print("=" * 60)
        print()
        print("機能:")
        print("• 難易度選択（簡単・普通・難しい）")
        print("• 最高記録の保存")
        print("• 詳細な統計表示")
        print("• より詳しいヒント")
        print()
    
    def select_difficulty(self):
        """難易度を選択"""
        print("難易度を選択してください:")
        print()
        
        for level, config in self.difficulty_levels.items():
            range_min, range_max = config["range"]
            print(f"{level}. {config['name']} "
                  f"(範囲: {range_min}〜{range_max}, "
                  f"推奨最大試行回数: {config['max_attempts']})")
        
        while True:
            try:
                choice = int(input("\n難易度（1-3）: "))
                if choice in self.difficulty_levels:
                    return choice
                else:
                    print("1、2、3のいずれかを選択してください")
            except ValueError:
                print("有効な数字を入力してください")
    
    def get_user_guess(self, min_val, max_val):
        """ユーザーから推測を入力してもらう"""
        while True:
            try:
                guess = input(f"\nあなたの推測（{min_val}〜{max_val}）: ")
                
                # 特別なコマンドをチェック
                if guess.lower() in ['quit', 'exit', 'やめる', 'stats']:
                    return guess.lower()
                
                # 数値に変換
                guess_number = int(guess)
                
                # 範囲をチェック
                if min_val <= guess_number <= max_val:
                    return guess_number
                else:
                    print(f"⚠️  {min_val}〜{max_val}の範囲で入力してください")
                    
            except ValueError:
                print("⚠️  有効な数字を入力してください")
    
    def give_detailed_hint(self, guess, target, attempts):
        """詳細なヒントを表示"""
        difference = abs(guess - target)
        
        # 方向のヒント
        if guess < target:
            direction = "📈 もっと大きい数字です"
        else:
            direction = "📉 もっと小さい数字です"
        
        # 距離のヒント
        if difference <= 5:
            distance = "🔥 とても近いです！"
        elif difference <= 15:
            distance = "🌡️  近いです"
        elif difference <= 30:
            distance = "🌊 まあまあです"
        else:
            distance = "❄️  遠いです"
        
        print(f"{direction} - {distance}")
        
        # 試行回数に応じた追加ヒント
        if attempts >= 5:
            print("💡 ヒント: 二分探索を試してみましょう（中央値から攻める）")
    
    def play_single_game(self, difficulty):
        """1回のゲームをプレイ"""
        config = self.difficulty_levels[difficulty]
        min_val, max_val = config["range"]
        difficulty_name = config["name"]
        max_attempts = config["max_attempts"]
        
        # ランダムな数字を生成
        target_number = random.randint(min_val, max_val)
        attempts = 0
        
        print(f"\n🎲 {difficulty_name}モードで数字を選びました！")
        print(f"範囲: {min_val}〜{max_val}")
        print(f"推奨最大試行回数: {max_attempts}回")
        print("💡 コマンド: 'quit'=終了, 'stats'=統計表示")
        
        while True:
            # ユーザーから推測を取得
            guess = self.get_user_guess(min_val, max_val)
            
            # 特別なコマンドの処理
            if guess == 'quit' or guess == 'やめる':
                print(f"\n👋 ゲームを終了します。正解は {target_number} でした！")
                return False
            elif guess == 'stats':
                self.show_statistics()
                continue
            
            attempts += 1
            
            # 推測の結果をチェック
            if guess == target_number:
                # 正解！
                self._handle_win(target_number, attempts, difficulty, max_attempts)
                return True
            else:
                # ヒントを表示
                print(f"\n❌ 残念！推測: {guess}")
                self.give_detailed_hint(guess, target_number, attempts)
                print(f"試行回数: {attempts}回目")
                
                # 最大試行回数に近づいた場合の警告
                if attempts >= max_attempts:
                    print("⚠️  推奨試行回数を超えました。頑張って！")
    
    def _handle_win(self, target, attempts, difficulty, max_attempts):
        """勝利時の処理"""
        print("\n" + "🎉" * 25)
        print("　　　正解おめでとうございます！　　　")
        print("🎉" * 25)
        print()
        print(f"正解: {target}")
        print(f"試行回数: {attempts}回")
        print(f"難易度: {self.difficulty_levels[difficulty]['name']}")
        
        # 成績評価
        if attempts == 1:
            print("💫 奇跡的な一発正解！宝くじを買いに行きましょう！")
        elif attempts <= max_attempts // 2:
            print("🏆 素晴らしい！戦略的な推測でした！")
        elif attempts <= max_attempts:
            print("👍 良い成績です！推奨回数内で達成しました！")
        else:
            print("🎯 粘り強く頑張りました！諦めない心が大切です！")
        
        # 統計を更新
        self._update_statistics(difficulty, attempts, True)
        
        # 新記録かチェック
        self._check_new_record(difficulty, attempts)
    
    def _update_statistics(self, difficulty, attempts, won):
        """統計データを更新"""
        self.stats["total_games"] += 1
        if won:
            self.stats["total_wins"] += 1
        
        # 難易度別統計
        diff_key = str(difficulty)
        if diff_key not in self.stats["best_attempts"]:
            self.stats["best_attempts"][diff_key] = attempts
            self.stats["average_attempts"][diff_key] = [attempts]
        else:
            if won and attempts < self.stats["best_attempts"][diff_key]:
                self.stats["best_attempts"][diff_key] = attempts
            if won:
                self.stats["average_attempts"][diff_key].append(attempts)
        
        # ゲーム履歴
        game_record = {
            "date": datetime.now().isoformat(),
            "difficulty": difficulty,
            "attempts": attempts,
            "won": won
        }
        self.stats["game_history"].append(game_record)
        
        # 履歴が長すぎる場合は古いものを削除
        if len(self.stats["game_history"]) > 50:
            self.stats["game_history"] = self.stats["game_history"][-50:]
        
        self.save_statistics()
    
    def _check_new_record(self, difficulty, attempts):
        """新記録かどうかチェック"""
        diff_key = str(difficulty)
        if diff_key in self.stats["best_attempts"]:
            if attempts == self.stats["best_attempts"][diff_key]:
                print("🏅 新記録達成！または記録タイ！")
    
    def show_statistics(self):
        """統計情報を表示"""
        print("\n" + "📊" * 15)
        print("　　　ゲーム統計　　　")
        print("📊" * 15)
        
        print(f"\n総ゲーム数: {self.stats['total_games']}")
        print(f"勝利数: {self.stats['total_wins']}")
        
        if self.stats['total_games'] > 0:
            win_rate = (self.stats['total_wins'] / self.stats['total_games']) * 100
            print(f"勝率: {win_rate:.1f}%")
        
        print("\n【難易度別記録】")
        for level, config in self.difficulty_levels.items():
            level_key = str(level)
            if level_key in self.stats["best_attempts"]:
                best = self.stats["best_attempts"][level_key]
                avg_list = self.stats["average_attempts"][level_key]
                avg = sum(avg_list) / len(avg_list)
                print(f"{config['name']}: 最高 {best}回, 平均 {avg:.1f}回")
            else:
                print(f"{config['name']}: 未プレイ")
        
        print("\n" + "=" * 30)
    
    def ask_play_again(self):
        """もう一度プレイするか確認"""
        while True:
            response = input("\nもう一度プレイしますか？ (yes/no): ").lower()
            if response in ['yes', 'y', 'はい', 'やる']:
                return True
            elif response in ['no', 'n', 'いいえ', 'やめる']:
                return False
            else:
                print("'yes' または 'no' で答えてください")
    
    def run(self):
        """メインゲームループ"""
        self.print_welcome_message()
        
        # 最初に統計を表示（ゲーム履歴がある場合）
        if self.stats["total_games"] > 0:
            print("前回までの記録:")
            self.show_statistics()
        
        while True:
            # 難易度選択
            difficulty = self.select_difficulty()
            
            # ゲームプレイ
            game_completed = self.play_single_game(difficulty)
            
            # 継続確認
            if not self.ask_play_again():
                break
        
        # 終了時の統計表示
        if self.stats["total_games"] > 0:
            print("\n最終統計:")
            self.show_statistics()
        
        # 終了メッセージ
        print("\n" + "=" * 60)
        print("🙏 数当てゲーム拡張版をプレイしていただき、")
        print("    ありがとうございました！")
        print("=" * 60)
        print()
        print("💡 さらなるチャレンジ:")
        print("• より効率的な戦略を考える（二分探索など）")
        print("• GUI版の作成（tkinter）")
        print("• ネットワーク対戦版の作成")
        print("• 他のプロジェクトに挑戦")


def main():
    """メイン関数"""
    game = NumberGuessingGame()
    game.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  ゲームが中断されました")
        print("また遊んでくださいね！")
    except Exception as e:
        print(f"\n❌ 予期しないエラーが発生しました: {e}")
        print("プログラムを確認してください")