#!/usr/bin/env python3
"""
進捗管理モジュール
学習の進行状況を追跡し、視覚的に表示
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path


class ProgressTracker:
    """学習進捗の追跡と可視化"""
    
    def __init__(self):
        self.results_dir = Path("quizzes/results")
        self.progress_file = self.results_dir / "progress.json"
        self.scores_dir = self.results_dir / "scores"
        
        # ディレクトリを作成
        self.results_dir.mkdir(exist_ok=True)
        self.scores_dir.mkdir(exist_ok=True)
        
        # 進捗データを読み込み
        self.progress_data = self._load_progress()
    
    def _load_progress(self):
        """進捗データを読み込む"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self._initialize_progress()
        return self._initialize_progress()
    
    def _initialize_progress(self):
        """初期進捗データを作成"""
        return {
            "user_info": {
                "start_date": datetime.now().isoformat(),
                "last_activity": datetime.now().isoformat()
            },
            "basics": {f"{i:02d}": {"completed": False, "best_score": 0, "attempts": 0} 
                      for i in range(1, 13)},
            "projects": {f"{i:02d}": {"completed": False, "best_score": 0, "attempts": 0} 
                        for i in range(1, 6)},
            "achievements": []
        }
    
    def save_progress(self):
        """進捗データを保存"""
        self.progress_data["user_info"]["last_activity"] = datetime.now().isoformat()
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress_data, f, indent=2, ensure_ascii=False)
    
    def get_completion_status(self, section, number):
        """特定セクションの完了状況を取得"""
        key = f"{number:02d}"
        if section in self.progress_data and key in self.progress_data[section]:
            return self.progress_data[section][key]
        return {"completed": False, "best_score": 0, "attempts": 0}
    
    def update_score(self, section, number, score, passed):
        """スコアを更新"""
        key = f"{number:02d}"
        if section not in self.progress_data:
            self.progress_data[section] = {}
        
        if key not in self.progress_data[section]:
            self.progress_data[section][key] = {
                "completed": False, 
                "best_score": 0, 
                "attempts": 0
            }
        
        data = self.progress_data[section][key]
        data["attempts"] += 1
        data["last_attempt"] = datetime.now().isoformat()
        
        if score > data["best_score"]:
            data["best_score"] = score
        
        if passed:
            data["completed"] = True
            data["completed_date"] = datetime.now().isoformat()
        
        self.save_progress()
        
        # 個別スコアも保存
        self._save_individual_score(section, number, score, passed)
    
    def _save_individual_score(self, section, number, score, passed):
        """個別のスコアを保存"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{section}_{number:02d}_{timestamp}.json"
        filepath = self.scores_dir / filename
        
        score_data = {
            "section": section,
            "number": number,
            "score": score,
            "passed": passed,
            "timestamp": datetime.now().isoformat()
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(score_data, f, indent=2)
    
    def show_dashboard(self):
        """初心者向け進捗ダッシュボード"""
        print("\n📈 あなたの学習進捗")
        print("=" * 60)
        
        # 開始日と学習日数
        start_date = datetime.fromisoformat(self.progress_data["user_info"]["start_date"])
        days_learning = (datetime.now() - start_date).days + 1
        print(f"🗓️  学習開始から {days_learning} 日目")
        print()
        
        # 基礎セクション進捗
        print("🔤 基礎セクション (basics/01-12):")
        print("-" * 50)
        
        basics_names = [
            "インタープリター基礎", "数値と文字列", "リストとシーケンス",
            "制御フロー", "関数", "データ構造", "モジュール",
            "入出力", "エラーと例外", "クラス", "標準ライブラリ",
            "外部ライブラリ"
        ]
        
        completed_basics = 0
        for i in range(1, 13):
            status = self.get_completion_status("basics", i)
            icon = "✅" if status["completed"] else "⏳"
            score = f"({status['best_score']}%)" if status["best_score"] > 0 else ""
            name = basics_names[i-1] if i <= len(basics_names) else f"レッスン{i}"
            print(f"   {icon} {i:02d}: {name:<20} {score}")
            if status["completed"]:
                completed_basics += 1
        
        progress_percent = (completed_basics / 12) * 100
        print(f"\n   進捗: {completed_basics}/12 完了 ({progress_percent:.0f}%)")
        self._draw_progress_bar(progress_percent)
        
        # プロジェクト進捗
        print("\n🛠️ プロジェクトセクション:")
        print("-" * 50)
        
        project_names = [
            "数当てゲーム", "電卓アプリ", "連絡先管理",
            "天気アプリ", "Webスクレイパー"
        ]
        
        completed_projects = 0
        for i in range(1, 6):
            status = self.get_completion_status("projects", i)
            icon = "✅" if status["completed"] else "⏳"
            score = f"({status['best_score']}%)" if status["best_score"] > 0 else ""
            name = project_names[i-1] if i <= len(project_names) else f"プロジェクト{i}"
            print(f"   {icon} {i}: {name:<20} {score}")
            if status["completed"]:
                completed_projects += 1
        
        # 次のアクション提案
        next_action = self.suggest_next_action()
        print(f"\n💡 次のおすすめ: {next_action}")
        print("=" * 60)
    
    def _draw_progress_bar(self, percentage):
        """プログレスバーを描画"""
        bar_length = 40
        filled = int(bar_length * percentage / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"   [{bar}] {percentage:.0f}%")
    
    def suggest_next_action(self):
        """次のアクションを提案"""
        # 未完了の最初の基礎レッスンを探す
        for i in range(1, 13):
            status = self.get_completion_status("basics", i)
            if not status["completed"]:
                if status["attempts"] == 0:
                    return f"basics/{i:02d} の学習を開始しましょう"
                else:
                    return f"basics/{i:02d} のテストに再挑戦しましょう"
        
        # すべての基礎が完了している場合
        for i in range(1, 6):
            status = self.get_completion_status("projects", i)
            if not status["completed"]:
                return f"プロジェクト {i} に挑戦しましょう"
        
        return "おめでとうございます！すべて完了しました！"
    
    def check_retry_eligibility(self, section, number):
        """再挑戦可能かチェック"""
        status = self.get_completion_status(section, number)
        
        if status["completed"]:
            return True, "すでに合格しています！"
        
        if status["attempts"] >= 3:
            # 最後の試行時刻をチェック
            if "last_attempt" in status:
                last_attempt = datetime.fromisoformat(status["last_attempt"])
                cooling_period = timedelta(hours=1)
                
                if datetime.now() - last_attempt < cooling_period:
                    remaining = cooling_period - (datetime.now() - last_attempt)
                    minutes = int(remaining.total_seconds() / 60)
                    return False, f"あと {minutes} 分待ってください"
        
        remaining_attempts = max(0, 3 - status["attempts"])
        return True, f"あと {remaining_attempts} 回挑戦できます"
    
    def get_section_name(self, section_type, number):
        """セクション名を取得"""
        if section_type == "basics":
            names = [
                "インタープリター基礎", "数値と文字列", "リストとシーケンス",
                "制御フロー", "関数", "データ構造", "モジュール",
                "入出力", "エラーと例外", "クラス", "標準ライブラリ",
                "外部ライブラリ"
            ]
            return names[number-1] if number <= len(names) else f"レッスン{number}"
        else:
            names = [
                "数当てゲーム", "電卓アプリ", "連絡先管理",
                "天気アプリ", "Webスクレイパー"
            ]
            return names[number-1] if number <= len(names) else f"プロジェクト{number}"