import csv
Dict_teams = {}
# Статистика команды Russia #Игр: 0 #Побед:   1 #Ничьих: 2 #Поражений: 3 #Забито голов: 4 #Пропущено голов: 5 #Упущенных побед: 6


def lost_victory(home_team_goal_count, away_team_goal_count, home_team_goal_timings, away_team_goal_timings):
    home_flag, away_flag = 0, 0
    home_counter, away_counter = 0, 0
    if home_team_goal_count == 0 or away_team_goal_count == 0:
        return False
    else:
        all_timings = home_team_goal_timings + away_team_goal_timings
        all_timings.sort()
        for i in range(len(all_timings)):
            if all_timings[0] in home_team_goal_timings:
                home_counter += 1
            else:
                away_counter += 1
        if home_counter > away_counter:
            home_flag = 1
        elif away_counter > home_counter:
            away_flag = 1
    if (home_team_goal_count > away_team_goal_count or home_team_goal_count == away_team_goal_count) and away_flag == 1:
        return True
    elif (home_team_goal_count < away_team_goal_count or home_team_goal_count < away_team_goal_count) and home_flag == 1:
        return True
    else:
        return False


def datas(reader1):
    for row in reader1:
        if row['home_team_name'] not in Dict_teams:
            Dict_teams[row['home_team_name']] = [0, 0, 0, 0, 0, 0, 0]
        if int(row['home_team_goal_count']) < int(row['away_team_goal_count']):
            Dict_teams[row['home_team_name']][3] += 1
        elif int(row['home_team_goal_count']) == int(row['away_team_goal_count']):
            Dict_teams[row['home_team_name']][2] += 1
        else:
            Dict_teams[row['home_team_name']][1] += 1
        Dict_teams[row['home_team_name']][4] += int(row['home_team_goal_count'])
        Dict_teams[row['home_team_name']][5] += int(row['away_team_goal_count'])
        Dict_teams[row['home_team_name']][0] += 1

        if row['away_team_name'] not in Dict_teams:
            Dict_teams[row['away_team_name']] = [0, 0, 0, 0, 0, 0, 0]
        if int(row['away_team_goal_count']) < int(row['home_team_goal_count']):
            Dict_teams[row['away_team_name']][3] += 1
        elif int(row['home_team_goal_count']) == int(row['away_team_goal_count']):
            Dict_teams[row['away_team_name']][2] += 1
        else:
            Dict_teams[row['away_team_name']][1] += 1
        Dict_teams[row['away_team_name']][4] += int(row['away_team_goal_count'])
        Dict_teams[row['away_team_name']][5] += int(row['home_team_goal_count'])
        Dict_teams[row['away_team_name']][0] += 1
        if lost_victory(int(row['home_team_goal_count']), int(row['away_team_goal_count']),
                        row['home_team_goal_timings'].split(";"),
                        row['away_team_goal_timings'].split(";")):
            Dict_teams[row['away_team_name']][6] += 1

    return Dict_teams


try:
    with open('A.csv') as fa:
        reader = csv.DictReader(fa)
        datas(reader)
except:
    print("Something is wrong with the file A")
try:
    with open('B.csv') as fb:
        reader = csv.DictReader(fb)
        datas(reader)
except:
    print("Something is wrong with the file B")
try:
    with open('C.csv') as fc:
        reader = csv.DictReader(fc)
        datas(reader)
except:
    print("Something is wrong with the file C")
try:
    with open('D.csv') as fd:
        reader = csv.DictReader(fd)
        datas(reader)
except:
    print("Something is wrong with the file C")
try:
    with open('E.csv') as fe:
        reader = csv.DictReader(fe)
        datas(reader)
except:
    print("Something is wrong with the file C")

command_name = input("Введите название команды на английском языке с большой буквы")
while len(command_name) > 0:
    if command_name not in Dict_teams:
        print("Команда не найдена")
    else:
        print("Статистика выступления команды", command_name)
        print("Игр:", Dict_teams[command_name][0])
        print("Побед:", Dict_teams[command_name][1])
        print("Ничьих:", Dict_teams[command_name][2])
        print("Поражений:", Dict_teams[command_name][3])
        print("Забито голов:", Dict_teams[command_name][4])
        print("Пропущено голов:", Dict_teams[command_name][5])
        print("Упущенных побед:", Dict_teams[command_name][6])
        print("_______________________________________________________________________________________________________")
    command_name = input("Введите название команды на английском языке с большой буквы")
