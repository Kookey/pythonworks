#-*- coding:utf-8 -*-
def make_album(singer, album):
    '''制作专辑'''
    result = {"singer": singer, "album": album}
    return result

album = make_album('周杰伦', "摩羯座")
print(album)


def make_album2(singer, album, number=''):
    '''制作专辑'''
    result = {"singer": singer, "album": album}
    if number:
        result["number"] = number
    return result
album = make_album2('Lily', 'Hello World')
print(album)

album = make_album2('Lily', 'Go!!!!', 30)
print(album)

while True:
    print("/nPlease enter your favorite singer and album.")
    print("Enter 'q' to quit!")
    f_singer = input("Singer name:")
    if f_singer == 'q':
        break
    f_album = input("Album:")
    if f_album == 'q':
        break
    result = make_album(f_singer, f_album)
    print(result)
