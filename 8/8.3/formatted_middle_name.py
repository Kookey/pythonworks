def get_formatted_name(first_name, middle_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


#让实参变成可先
def get_formatted_name2(first_name, last_name, middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name
musician = get_formatted_name2('jimi', 'hendrix')
print(musician)
