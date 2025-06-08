#!/usr/bin/env python3
"""
プロジェクト5: 学生成績データ可視化

CSVファイルから学生の成績データを読み込み、統計分析と可視化を行うアプリです。
標準ライブラリのみを使用してデータ処理と簡易グラフ表示を実装します。

学習ポイント:
- CSVファイルの読み書き
- データの集計と統計計算
- ASCII文字による簡易可視化
- データ分析の基本概念

対応章: basics/08_input_output.py完了後
"""

import csv
import json
import math
import statistics
from datetime import datetime
from pathlib import Path

class StudentGradeAnalyzer:
    """学生成績分析クラス"""
    
    def __init__(self):
        """アナライザーを初期化"""
        self.students = []
        self.subjects = []
        self.grades = {}  # {student_id: {subject: grade}}
        self.stats = {}
    
    def load_sample_data(self):
        """サンプルデータを生成"""
        import random
        random.seed(42)  # 再現可能な結果のため
        
        subjects = ['数学', '英語', '理科', '社会', '国語']
        students = [
            f'学生{i:03d}' for i in range(1, 51)  # 50人の学生
        ]
        
        self.subjects = subjects
        self.students = students
        self.grades = {}
        
        for student in students:
            self.grades[student] = {}
            for subject in subjects:
                # 50-100点の範囲でランダムな成績
                base_score = random.randint(50, 100)
                # 各学生に特性を付与（得意・不得意科目）
                student_num = int(student.replace('学生', ''))
                if student_num % 5 == 0:  # 5人に1人は優秀
                    score = min(100, base_score + random.randint(10, 20))
                elif student_num % 7 == 0:  # 7人に1人は苦手
                    score = max(50, base_score - random.randint(10, 15))
                else:
                    score = base_score + random.randint(-5, 5)
                
                self.grades[student][subject] = score
        
        print(f"✅ サンプルデータを生成しました: {len(students)}人、{len(subjects)}科目")
    
    def load_from_csv(self, filename):
        """CSVファイルからデータを読み込み"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                headers = next(reader)  # ヘッダー行
                
                # ヘッダーから学生名と科目を抽出
                if headers[0].lower() in ['student', '学生', '氏名', 'name']:
                    self.subjects = headers[1:]
                else:
                    print("❌ CSVの最初の列は学生名である必要があります")
                    return False
                
                self.students = []
                self.grades = {}
                
                for row in reader:
                    if len(row) < len(headers):
                        continue  # 不完全な行をスキップ
                    
                    student = row[0]
                    self.students.append(student)
                    self.grades[student] = {}
                    
                    for i, subject in enumerate(self.subjects):
                        try:
                            score = float(row[i + 1])
                            self.grades[student][subject] = score
                        except (ValueError, IndexError):
                            self.grades[student][subject] = 0  # デフォルト値
                
                print(f"✅ CSVを読み込みました: {len(self.students)}人、{len(self.subjects)}科目")
                return True
                
        except FileNotFoundError:
            print(f"❌ ファイルが見つかりません: {filename}")
            return False
        except Exception as e:
            print(f"❌ CSV読み込みエラー: {e}")
            return False
    
    def export_to_csv(self, filename="grades_export.csv"):
        """CSVファイルにエクスポート"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # ヘッダー
                headers = ['学生'] + self.subjects
                writer.writerow(headers)
                
                # データ
                for student in self.students:
                    row = [student]
                    for subject in self.subjects:
                        row.append(self.grades[student].get(subject, 0))
                    writer.writerow(row)
            
            print(f"✅ CSVに出力しました: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ CSV出力エラー: {e}")
            return False
    
    def calculate_statistics(self):
        """統計情報を計算"""
        if not self.students or not self.subjects:
            print("❌ データが読み込まれていません")
            return False
        
        # 学生別統計
        student_stats = {}
        for student in self.students:
            scores = list(self.grades[student].values())
            if scores:
                student_stats[student] = {
                    'total': sum(scores),
                    'average': statistics.mean(scores),
                    'max': max(scores),
                    'min': min(scores),
                    'stdev': statistics.stdev(scores) if len(scores) > 1 else 0
                }
        
        # 科目別統計
        subject_stats = {}
        for subject in self.subjects:
            scores = [self.grades[student][subject] for student in self.students]
            if scores:
                subject_stats[subject] = {
                    'average': statistics.mean(scores),
                    'median': statistics.median(scores),
                    'max': max(scores),
                    'min': min(scores),
                    'stdev': statistics.stdev(scores) if len(scores) > 1 else 0,
                    'pass_rate': len([s for s in scores if s >= 60]) / len(scores) * 100
                }
        
        # 全体統計
        all_scores = []
        for student in self.students:
            all_scores.extend(self.grades[student].values())
        
        overall_stats = {
            'total_students': len(self.students),
            'total_subjects': len(self.subjects),
            'overall_average': statistics.mean(all_scores),
            'overall_median': statistics.median(all_scores),
            'overall_stdev': statistics.stdev(all_scores) if len(all_scores) > 1 else 0
        }
        
        self.stats = {
            'students': student_stats,
            'subjects': subject_stats,
            'overall': overall_stats
        }
        
        print("✅ 統計計算完了")
        return True
    
    def get_top_students(self, n=10, by='average'):
        """成績上位の学生を取得"""
        if 'students' not in self.stats:
            return []
        
        students_with_scores = []
        for student, stats in self.stats['students'].items():
            students_with_scores.append((student, stats[by]))
        
        # 降順でソート
        students_with_scores.sort(key=lambda x: x[1], reverse=True)
        return students_with_scores[:n]
    
    def get_grade_distribution(self, subject=None):
        """成績分布を取得"""
        if subject:
            scores = [self.grades[student][subject] for student in self.students]
        else:
            scores = []
            for student in self.students:
                scores.extend(self.grades[student].values())
        
        # 10点刻みで分布を計算
        distribution = {}
        for i in range(0, 101, 10):
            range_key = f"{i}-{i+9}"
            count = len([s for s in scores if i <= s < i+10])
            distribution[range_key] = count
        
        # 100点の場合の特別処理
        distribution["100"] = len([s for s in scores if s == 100])
        
        return distribution
    
    def create_ascii_chart(self, data, title="チャート", max_width=50):
        """ASCII文字でチャートを作成"""
        print(f"\n📊 {title}")
        print("=" * (max_width + 20))
        
        if not data:
            print("データがありません")
            return
        
        # 最大値を取得してスケールを決定
        max_value = max(data.values()) if data.values() else 1
        
        for label, value in data.items():
            # バーの長さを計算
            bar_length = int((value / max_value) * max_width) if max_value > 0 else 0
            bar = "█" * bar_length
            
            # 値の表示フォーマット
            if isinstance(value, float):
                value_str = f"{value:.1f}"
            else:
                value_str = str(value)
            
            print(f"{label:>12} |{bar:<{max_width}} {value_str}")
        
        print("=" * (max_width + 20))
    
    def create_scatter_plot(self, subject1, subject2, max_width=60, max_height=20):
        """2科目の散布図を作成（ASCII）"""
        print(f"\n📈 散布図: {subject1} vs {subject2}")
        print("=" * (max_width + 10))
        
        # データ取得
        x_data = [self.grades[student][subject1] for student in self.students]
        y_data = [self.grades[student][subject2] for student in self.students]
        
        if not x_data or not y_data:
            print("データが不足しています")
            return
        
        # スケール計算
        x_min, x_max = min(x_data), max(x_data)
        y_min, y_max = min(y_data), max(y_data)
        
        # プロット領域を作成
        plot = [[' ' for _ in range(max_width)] for _ in range(max_height)]
        
        # データポイントをプロット
        for x, y in zip(x_data, y_data):
            # 座標を正規化
            plot_x = int(((x - x_min) / (x_max - x_min)) * (max_width - 1))
            plot_y = int(((y - y_min) / (y_max - y_min)) * (max_height - 1))
            
            # Y軸は上下反転
            plot_y = max_height - 1 - plot_y
            
            # 既にプロットされている場合は異なる文字を使用
            if plot[plot_y][plot_x] == ' ':
                plot[plot_y][plot_x] = '●'
            elif plot[plot_y][plot_x] == '●':
                plot[plot_y][plot_x] = '◆'
            else:
                plot[plot_y][plot_x] = '★'
        
        # Y軸ラベルと共にプロット
        for i, row in enumerate(plot):
            y_value = y_max - (i / (max_height - 1)) * (y_max - y_min)
            print(f"{y_value:5.0f} |{''.join(row)}")
        
        # X軸の表示
        print(" " * 6 + "+" + "-" * max_width)
        x_labels = f"{x_min:5.0f}{' ' * (max_width - 10)}{x_max:5.0f}"
        print(" " * 6 + x_labels)
        print(f"\n{' ' * 20}{subject1} →")
        print("=" * (max_width + 10))
    
    def analyze_correlations(self):
        """科目間の相関を分析"""
        correlations = {}
        
        for i, subject1 in enumerate(self.subjects):
            for j, subject2 in enumerate(self.subjects):
                if i < j:  # 重複を避ける
                    x_data = [self.grades[student][subject1] for student in self.students]
                    y_data = [self.grades[student][subject2] for student in self.students]
                    
                    # ピアソン相関係数を計算
                    correlation = self._calculate_correlation(x_data, y_data)
                    correlations[f"{subject1}-{subject2}"] = correlation
        
        return correlations
    
    def _calculate_correlation(self, x_data, y_data):
        """ピアソン相関係数を計算"""
        if len(x_data) != len(y_data) or len(x_data) < 2:
            return 0
        
        x_mean = statistics.mean(x_data)
        y_mean = statistics.mean(y_data)
        
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data))
        
        x_variance = sum((x - x_mean) ** 2 for x in x_data)
        y_variance = sum((y - y_mean) ** 2 for y in y_data)
        
        denominator = math.sqrt(x_variance * y_variance)
        
        if denominator == 0:
            return 0
        
        return numerator / denominator

class GradeAnalyzerUI:
    """成績分析アプリのUI"""
    
    def __init__(self):
        """UIを初期化"""
        self.analyzer = StudentGradeAnalyzer()
    
    def show_welcome(self):
        """ウェルカムメッセージ"""
        print("=" * 60)
        print("📊 学生成績データ可視化アプリ")
        print("=" * 60)
        print("学生の成績を分析し、統計情報とグラフを表示します")
        print("=" * 60)
    
    def show_main_menu(self):
        """メインメニュー"""
        print("\n📋 メニュー")
        print("-" * 40)
        print("1. サンプルデータを生成")
        print("2. CSVファイルから読み込み")
        print("3. 基本統計を表示")
        print("4. 成績上位者を表示")
        print("5. 科目別統計を表示")
        print("6. 成績分布を表示")
        print("7. 散布図を表示")
        print("8. 相関分析")
        print("9. データをCSVに出力")
        print("10. 詳細レポート生成")
        print("0. 終了")
        print("-" * 40)
    
    def run(self):
        """メインループ"""
        self.show_welcome()
        
        while True:
            try:
                self.show_main_menu()
                choice = input("選択: ").strip()
                
                if choice == "1":
                    self.analyzer.load_sample_data()
                    self.analyzer.calculate_statistics()
                elif choice == "2":
                    filename = input("CSVファイル名: ").strip()
                    if self.analyzer.load_from_csv(filename):
                        self.analyzer.calculate_statistics()
                elif choice == "3":
                    self.show_basic_statistics()
                elif choice == "4":
                    self.show_top_students()
                elif choice == "5":
                    self.show_subject_statistics()
                elif choice == "6":
                    self.show_grade_distribution()
                elif choice == "7":
                    self.show_scatter_plot()
                elif choice == "8":
                    self.show_correlations()
                elif choice == "9":
                    filename = input("出力ファイル名 (デフォルト:grades_export.csv): ").strip()
                    if not filename:
                        filename = "grades_export.csv"
                    self.analyzer.export_to_csv(filename)
                elif choice == "10":
                    self.generate_detailed_report()
                elif choice == "0":
                    print("\n👋 成績分析アプリを終了します")
                    break
                else:
                    print("❌ 無効な選択です")
                
                input("\nEnterキーで続行...")
                
            except KeyboardInterrupt:
                print("\n\n👋 成績分析アプリを終了します")
                break
            except Exception as e:
                print(f"❌ エラー: {e}")
                input("Enterキーで続行...")
    
    def show_basic_statistics(self):
        """基本統計を表示"""
        if not self.analyzer.stats:
            print("❌ まずデータを読み込んでください")
            return
        
        overall = self.analyzer.stats['overall']
        
        print("\n📊 全体統計")
        print("=" * 40)
        print(f"👥 学生数:       {overall['total_students']:3d}人")
        print(f"📚 科目数:       {overall['total_subjects']:3d}科目")
        print(f"📈 全体平均:     {overall['overall_average']:6.2f}点")
        print(f"📊 中央値:       {overall['overall_median']:6.2f}点")
        print(f"📉 標準偏差:     {overall['overall_stdev']:6.2f}")
        print("=" * 40)
    
    def show_top_students(self):
        """成績上位者を表示"""
        if not self.analyzer.stats:
            print("❌ まずデータを読み込んでください")
            return
        
        try:
            n = int(input("表示する人数 (デフォルト:10): ") or "10")
        except ValueError:
            n = 10
        
        top_students = self.analyzer.get_top_students(n, 'average')
        
        print(f"\n🏆 成績上位 {n}人（平均点順）")
        print("=" * 50)
        print("順位  学生名       平均点    総合点")
        print("-" * 50)
        
        for i, (student, avg_score) in enumerate(top_students, 1):
            total_score = self.analyzer.stats['students'][student]['total']
            print(f"{i:2d}.  {student:<12} {avg_score:6.2f}点  {total_score:6.1f}点")
        
        print("=" * 50)
    
    def show_subject_statistics(self):
        """科目別統計を表示"""
        if not self.analyzer.stats:
            print("❌ まずデータを読み込んでください")
            return
        
        subject_stats = self.analyzer.stats['subjects']
        
        print("\n📚 科目別統計")
        print("=" * 80)
        print("科目名     平均点  中央値  最高点  最低点  標準偏差  合格率")
        print("-" * 80)
        
        for subject, stats in subject_stats.items():
            print(f"{subject:<8} {stats['average']:6.1f}  {stats['median']:6.1f}  "
                  f"{stats['max']:6.1f}  {stats['min']:6.1f}  {stats['stdev']:6.2f}  "
                  f"{stats['pass_rate']:5.1f}%")
        
        print("=" * 80)
        
        # 平均点のバーチャート
        avg_data = {subject: stats['average'] for subject, stats in subject_stats.items()}
        self.analyzer.create_ascii_chart(avg_data, "科目別平均点")
    
    def show_grade_distribution(self):
        """成績分布を表示"""
        if not self.analyzer.stats:
            print("❌ まずデータを読み込んでください")
            return
        
        print("1. 全科目合計")
        for i, subject in enumerate(self.analyzer.subjects, 2):
            print(f"{i}. {subject}")
        
        try:
            choice = int(input("選択: "))
            if choice == 1:
                distribution = self.analyzer.get_grade_distribution()
                title = "全科目 成績分布"
            elif 2 <= choice <= len(self.analyzer.subjects) + 1:
                subject = self.analyzer.subjects[choice - 2]
                distribution = self.analyzer.get_grade_distribution(subject)
                title = f"{subject} 成績分布"
            else:
                print("❌ 無効な選択です")
                return
            
            self.analyzer.create_ascii_chart(distribution, title)
            
        except ValueError:
            print("❌ 有効な数値を入力してください")
    
    def show_scatter_plot(self):
        """散布図を表示"""
        if not self.analyzer.subjects or len(self.analyzer.subjects) < 2:
            print("❌ 2科目以上のデータが必要です")
            return
        
        print("散布図に表示する科目を選択してください:")
        for i, subject in enumerate(self.analyzer.subjects, 1):
            print(f"{i}. {subject}")
        
        try:
            x_choice = int(input("X軸の科目番号: ")) - 1
            y_choice = int(input("Y軸の科目番号: ")) - 1
            
            if 0 <= x_choice < len(self.analyzer.subjects) and 0 <= y_choice < len(self.analyzer.subjects):
                subject1 = self.analyzer.subjects[x_choice]
                subject2 = self.analyzer.subjects[y_choice]
                self.analyzer.create_scatter_plot(subject1, subject2)
            else:
                print("❌ 無効な選択です")
                
        except ValueError:
            print("❌ 有効な数値を入力してください")
    
    def show_correlations(self):
        """相関分析を表示"""
        if not self.analyzer.stats:
            print("❌ まずデータを読み込んでください")
            return
        
        correlations = self.analyzer.analyze_correlations()
        
        print("\n🔗 科目間相関分析")
        print("=" * 50)
        print("科目ペア                相関係数  判定")
        print("-" * 50)
        
        for pair, correlation in sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True):
            if abs(correlation) >= 0.7:
                strength = "強い"
            elif abs(correlation) >= 0.4:
                strength = "中程度"
            elif abs(correlation) >= 0.2:
                strength = "弱い"
            else:
                strength = "ほぼなし"
            
            direction = "正" if correlation > 0 else "負"
            
            print(f"{pair:<20} {correlation:8.3f}  {direction}の{strength}相関")
        
        print("=" * 50)
        print("📍 相関係数の目安:")
        print("  0.7以上: 強い相関")
        print("  0.4-0.7: 中程度の相関") 
        print("  0.2-0.4: 弱い相関")
        print("  0.2未満: ほぼ相関なし")
    
    def generate_detailed_report(self):
        """詳細レポートを生成"""
        if not self.analyzer.stats:
            print("❌ まずデータを読み込んでください")
            return
        
        filename = input("レポートファイル名 (デフォルト:grade_report.txt): ").strip()
        if not filename:
            filename = "grade_report.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("学生成績分析レポート\n")
                f.write(f"生成日時: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
                
                # 全体統計
                overall = self.analyzer.stats['overall']
                f.write("■ 全体統計\n")
                f.write(f"学生数: {overall['total_students']}人\n")
                f.write(f"科目数: {overall['total_subjects']}科目\n")
                f.write(f"全体平均: {overall['overall_average']:.2f}点\n")
                f.write(f"中央値: {overall['overall_median']:.2f}点\n")
                f.write(f"標準偏差: {overall['overall_stdev']:.2f}\n\n")
                
                # 科目別統計
                f.write("■ 科目別統計\n")
                subject_stats = self.analyzer.stats['subjects']
                for subject, stats in subject_stats.items():
                    f.write(f"\n【{subject}】\n")
                    f.write(f"  平均点: {stats['average']:.1f}点\n")
                    f.write(f"  中央値: {stats['median']:.1f}点\n")
                    f.write(f"  最高点: {stats['max']:.1f}点\n")
                    f.write(f"  最低点: {stats['min']:.1f}点\n")
                    f.write(f"  標準偏差: {stats['stdev']:.2f}\n")
                    f.write(f"  合格率: {stats['pass_rate']:.1f}%\n")
                
                # 成績上位者
                f.write("\n■ 成績上位者（TOP 10）\n")
                top_students = self.analyzer.get_top_students(10, 'average')
                for i, (student, avg_score) in enumerate(top_students, 1):
                    f.write(f"{i:2d}. {student}: {avg_score:.2f}点\n")
                
                # 相関分析
                f.write("\n■ 科目間相関分析\n")
                correlations = self.analyzer.analyze_correlations()
                for pair, correlation in sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True):
                    f.write(f"{pair}: {correlation:.3f}\n")
            
            print(f"✅ 詳細レポートを生成しました: {filename}")
            
        except Exception as e:
            print(f"❌ レポート生成エラー: {e}")

def main():
    """メイン関数"""
    app = GradeAnalyzerUI()
    app.run()

if __name__ == "__main__":
    main()

"""
🎯 学習のポイント:

1. データ処理
   - CSVファイルの読み書き
   - データの集計と統計計算
   - 欠損データの処理

2. 統計分析
   - 平均値、中央値、標準偏差
   - 相関係数の計算
   - 成績分布の分析

3. データ可視化
   - ASCII文字による棒グラフ
   - 散布図の簡易実装
   - チャートの作成

4. ファイルI/O
   - CSV形式での入出力
   - レポートファイルの生成
   - エンコーディングの考慮

🔧 改良案:
- matplotlibを使った本格的なグラフ
- より高度な統計分析
- データベース連携
- Web UIの実装

⚡ 実行方法:
python3 projects/05_data_visualizer/student_grades.py

📊 サンプルデータ機能付きなので、すぐに試すことができます！
"""