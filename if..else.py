games=["StarCraft2",["Blizzard Entertainment" ,"RTS"],"Dota 2","OverWatch"]
for each_item in games:
 if isinstance(each_item,list):
    for a in each_item:
        print(a)
    else:
        print(each_item)
