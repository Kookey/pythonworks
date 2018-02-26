def show_magicans(magicans):
    '''打印魔术师的姓名'''
    for magican in magicans:
        print(magican)


magicans = ['Tom', 'Dav', "Jack"]
update_magicans = []
show_magicans(magicans)


def make_great(magicans, update_magicans):
    '''修改魔术师列表'''
    while magicans:
        current_magican = magicans.pop() + " the Great"
        update_magicans.append(current_magican)


#make_great(magicans, update_magicans)
#show_magicans(update_magicans)

make_great(magicans[:], update_magicans)
show_magicans(update_magicans)
show_magicans(magicans)
