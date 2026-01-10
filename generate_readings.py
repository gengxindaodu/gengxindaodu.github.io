#!/usr/bin/env python3
"""
生成730天读经计划的文件模板
"""

import os
from datetime import datetime, timedelta

# 读经计划 - 这是一个简化的示例，您需要根据实际情况调整
# 格式: (起始天数, 书卷简称, 起始章, 结束章)
reading_plan = [
    # 创世记 50章
    (1, "创世记", 1, 2),
    (2, "创世记", 3, 5),
    (3, "创世记", 6, 9),
    (4, "创世记", 10, 14),
    (5, "创世记", 15, 18),
    (6, "创世记", 19, 21),
    (7, "创世记", 22, 24),
    (8, "创世记", 25, 26),
    (9, "创世记", 27, 29),
    (10, "创世记", 30, 31),
    (11, "创世记", 32, 34),
    (12, "创世记", 35, 37),
    (13, "创世记", 38, 40),
    (14, "创世记", 41, 42),
    (15, "创世记", 43, 45),
    (16, "创世记", 46, 47),
    (17, "创世记", 48, 50),
    
    # 出埃及记 40章
    (18, "出埃及记", 1, 3),
    (19, "出埃及记", 4, 6),
    (20, "出埃及记", 7, 9),
    # ... 继续添加更多书卷和章节
    
    # 注意: 这只是示例，您需要完整规划730天的读经计划
]

def generate_daily_reading_files(output_dir="_daily_readings", start_date="2024-01-01"):
    """生成每日读经文件"""
    os.makedirs(output_dir, exist_ok=True)
    
    start = datetime.strptime(start_date, "%Y-%m-%d")
    
    for day in range(1, 731):  # 1到730天
        day_str = f"{day:03d}"  # 格式化为001, 002, ...
        current_date = start + timedelta(days=day-1)
        
        # 这里需要根据实际的读经计划确定每天的经文
        # 示例：简单分配
        passage = f"待定经文 - 第{day}天"
        
        filename = os.path.join(output_dir, f"day-{day_str}.md")
        
        content = f"""---
day: {day}
passage: "{passage}"
date: {current_date.strftime("%Y-%m-%d")}
reflections: []
---

## {passage}

[这里添加经文内容]

---

**注意**: 请填写实际的圣经经文内容
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if day % 100 == 0:
            print(f"已生成 {day} 天的文件...")
    
    print(f"完成！已生成730天的读经文件到 {output_dir} 目录")

def generate_reading_plan_template():
    """生成读经计划模板，帮助规划730天的内容"""
    
    # 圣经书卷和章节数
    books = [
        ("创世记", 50), ("出埃及记", 40), ("利未记", 27), ("民数记", 36), 
        ("申命记", 34), ("约书亚记", 24), ("士师记", 21), ("路得记", 4),
        ("撒母耳记上", 31), ("撒母耳记下", 24), ("列王纪上", 22), ("列王纪下", 25),
        ("历代志上", 29), ("历代志下", 36), ("以斯拉记", 10), ("尼希米记", 13),
        ("以斯帖记", 10), ("约伯记", 42), ("诗篇", 150), ("箴言", 31),
        ("传道书", 12), ("雅歌", 8), ("以赛亚书", 66), ("耶利米书", 52),
        ("耶利米哀歌", 5), ("以西结书", 48), ("但以理书", 12), ("何西阿书", 14),
        ("约珥书", 3), ("阿摩司书", 9), ("俄巴底亚书", 1), ("约拿书", 4),
        ("弥迦书", 7), ("那鸿书", 3), ("哈巴谷书", 3), ("西番雅书", 3),
        ("哈该书", 2), ("撒迦利亚书", 14), ("玛拉基书", 4),
        ("马太福音", 28), ("马可福音", 16), ("路加福音", 24), ("约翰福音", 21),
        ("使徒行传", 28), ("罗马书", 16), ("哥林多前书", 16), ("哥林多后书", 13),
        ("加拉太书", 6), ("以弗所书", 6), ("腓立比书", 4), ("歌罗西书", 4),
        ("帖撒罗尼迦前书", 5), ("帖撒罗尼迦后书", 3), ("提摩太前书", 6), 
        ("提摩太后书", 4), ("提多书", 3), ("腓利门书", 1), ("希伯来书", 13),
        ("雅各书", 5), ("彼得前书", 5), ("彼得后书", 3), ("约翰一书", 5),
        ("约翰二书", 1), ("约翰三书", 1), ("犹大书", 1), ("启示录", 22)
    ]
    
    total_chapters = sum(chapters for _, chapters in books)
    print(f"圣经总章节数: {total_chapters}")
    print(f"730天读经计划，平均每天: {total_chapters/730:.2f} 章\n")
    
    print("建议的读经计划分配：")
    print("=" * 60)
    
    day = 1
    for book_name, chapters in books:
        # 简单策略：每天读2-3章
        days_needed = max(1, (chapters + 2) // 3)  # 向上取整
        chapters_per_day = chapters / days_needed
        
        print(f"{book_name} ({chapters}章) - 分配 {days_needed} 天")
        
        current_chapter = 1
        for i in range(days_needed):
            if i == days_needed - 1:
                # 最后一天读完剩余章节
                end_chapter = chapters
            else:
                end_chapter = min(current_chapter + int(chapters_per_day) - 1, chapters)
            
            print(f"  第{day}天: {book_name} {current_chapter}-{end_chapter}章")
            current_chapter = end_chapter + 1
            day += 1
        
        print()
    
    print(f"总计: {day-1} 天")
    print(f"剩余天数: {730 - (day-1)} 天（可用于复习或灵修）")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "plan":
        # 生成读经计划模板
        generate_reading_plan_template()
    else:
        # 生成文件
        print("开始生成730天读经文件模板...")
        generate_daily_reading_files()
        print("\n提示: 运行 'python generate_readings.py plan' 可查看建议的读经计划")
