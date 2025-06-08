#!/usr/bin/env python3
"""
=================================
数当てゲーム - 基本版
=================================

コンピュータがランダムに選んだ数字を当てるゲームです。
これは Python プログラミングの基本要素を組み合わせた
初心者向けのプロジェクトです。

実装する機能:
- ランダムな数字の生成（1〜100）
- ユーザーからの推測入力
- ヒント表示（大きい/小さい）
- 試行回数のカウント
- エラーハンドリング
"""

import random


def print_welcome_message():
    """ゲーム開始時のメッセージを表示"""
    print("=" * 50)
    print("🎯 数当てゲームへようこそ！")
    print("=" * 50)
    print()
    print("ルール:")
    print("• コンピュータが1〜100の数字を選びました")
    print("• あなたの推測を入力してください")
    print("• ヒントを参考に正解を目指しましょう")
    print("• 何回で当てられるでしょうか？")
    print()
    print("ゲームを開始します！")
    print("-" * 30)


def get_user_guess():
    """ユーザーから推測を入力してもらう"""
    while True:
        try:
            guess = input("\nあなたの推測（1〜100）: ")
            
            # 特別なコマンドをチェック
            if guess.lower() in ['quit', 'exit', 'やめる']:
                return None
            
            # 数値に変換
            guess_number = int(guess)
            
            # 範囲をチェック
            if 1 <= guess_number <= 100:
                return guess_number
            else:
                print("⚠️  1〜100の範囲で入力してください")
                
        except ValueError:
            print("⚠️  有効な数字を入力してください")
            print("   例: 50")


def give_hint(guess, target):
    """推測に対するヒントを表示"""
    if guess < target:
        print("📈 もっと大きい数字です")
    else:
        print("📉 もっと小さい数字です")


def play_game():
    """メインゲームロジック"""
    # ランダムな数字を生成
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("\n🎲 数字を選びました！さあ、当ててみてください。")
    print("💡 ヒント: 'quit' と入力するとゲームを終了できます")
    
    while True:
        # ユーザーから推測を取得
        guess = get_user_guess()
        
        # ゲーム終了が選択された場合
        if guess is None:
            print(f"\n👋 ゲームを終了します。正解は {target_number} でした！")
            return
        
        attempts += 1
        
        # 推測の結果をチェック
        if guess == target_number:
            # 正解！
            print("\n" + "🎉" * 20)
            print("　　正解おめでとうございます！　　")
            print("🎉" * 20)
            print()
            print(f"正解: {target_number}")
            print(f"試行回数: {attempts}回")
            
            # 成績に応じたコメント
            if attempts == 1:
                print("💫 奇跡的な一発正解！素晴らしい運です！")
            elif attempts <= 5:
                print("🏆 優秀な成績です！効率的な推測でした！")
            elif attempts <= 10:
                print("👍 良い成績です！戦略的に攻めましたね！")
            else:
                print("🎯 粘り強く頑張りました！")
            
            break
        
        else:
            # ヒントを表示
            print(f"\n❌ 残念！推測: {guess}")
            give_hint(guess, target_number)
            print(f"試行回数: {attempts}回目")


def ask_play_again():
    """もう一度プレイするか確認"""
    while True:
        response = input("\nもう一度プレイしますか？ (yes/no): ").lower()
        if response in ['yes', 'y', 'はい', 'やる']:
            return True
        elif response in ['no', 'n', 'いいえ', 'やめる']:
            return False
        else:
            print("'yes' または 'no' で答えてください")


def main():
    """メイン関数"""
    print_welcome_message()
    
    # ゲームループ
    while True:
        play_game()
        
        # 継続確認
        if not ask_play_again():
            break
    
    # 終了メッセージ
    print("\n" + "=" * 50)
    print("🙏 数当てゲームをプレイしていただき、")
    print("    ありがとうございました！")
    print("=" * 50)
    print()
    print("💡 次のステップ:")
    print("• game_logic.py で機能分割版を試す")
    print("• 自分なりの機能を追加してみる")
    print("• 他のプロジェクトにも挑戦する")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  ゲームが中断されました")
        print("また遊んでくださいね！")
    except Exception as e:
        print(f"\n❌ 予期しないエラーが発生しました: {e}")
        print("プログラムを確認してください")