games=["StarCraft2",[
    "Blizzard Entertainment" ,"RTS"
],"Dota 2","OverWatch"]
print(games)
print(len(games))
print(games[0])#列表是从0开始的
#Head First Python Page13
games.insert(1, "2010")

games.insert(3,"2013")
print(games)
games.append(2016)
newgame=input("a new game")
#创建一个临时变量用于插入
games.append(newgame)

print(games)

#HPF P14:在小列表中可以从头创建列表，避免计算
#HPF P15:
for each_flick in games:#有关each_flick（目标标识符）更多 HPF P16参考
    print(each_flick)
    
#HPF P18:
print(games[2][0])#嵌套列表显示

