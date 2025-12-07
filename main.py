import random
def simulate_single_game(skill_a, skill_b):
    """模拟单局乒乓球比赛，返回该局胜者（'A'/'B'）
    :param skill_a: 选手A的得分概率（0-1）
    :param skill_b: 选手B的得分概率（0-1）
    """
    score_a, score_b = 0, 0
    while True:
        # 随机判定得分方
        if random.random() < skill_a / (skill_a + skill_b):
            score_a += 1
        else:
            score_b += 1

        # 判定该局胜负（需满足11分且领先2分，或10平后领先2分）
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 'A' if score_a > score_b else 'B'
def simulate_match(skill_a, skill_b, best_of):
    """模拟多局制比赛（三局两胜/五局三胜），返回比赛胜者
    :param best_of: 比赛局数规则（3=三局两胜，5=五局三胜）
    """
    win_a, win_b = 0, 0
    need_win = (best_of // 2) + 1  # 需获胜的局数
    while win_a < need_win and win_b < need_win:
        game_winner = simulate_single_game(skill_a, skill_b)
        if game_winner == 'A':
            win_a += 1
        else:
            win_b += 1
    return 'A' if win_a > win_b else 'B'

def analyze_competition(skill_a, skill_b, match_times, best_of=3):
    """批量模拟比赛，统计胜率并分析
    :param match_times: 模拟比赛的总场次
    :param best_of: 每轮比赛的局数规则
    """
    win_a_total = 0
    win_b_total = 0
    for _ in range(match_times):
        match_winner = simulate_match(skill_a, skill_b, best_of)
        if match_winner == 'A':
            win_a_total += 1
        else:
            win_b_total += 1

    # 输出分析结果
    print(f"模拟{match_times}场{best_of}局{best_of//2 + 1}胜制比赛：")
    print(f"选手A胜率：{win_a_total/match_times:.2%}")
    print(f"选手B胜率：{win_b_total/match_times:.2%}")
    return win_a_total/match_times, win_b_total/match_times

# 主程序：调整参数可分析不同能力值下的竞技规律
if __name__ == "__main__":
    # 示例：选手A得分概率0.55，选手B0.45，模拟1000场三局两胜制比赛
    analyze_competition(skill_a=0.55, skill_b=0.45, match_times=1000, best_of=3)
    
    # 可扩展：对比不同规则/能力值的结果
    # analyze_competition(skill_a=0.5, skill_b=0.5, match_times=1000, best_of=5)

