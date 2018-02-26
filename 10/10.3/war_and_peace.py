filename = 'war_and_peace.txt'
try:
    with open(filename) as book:
        contents = book.read()
except FileNotFoundError as e:
    print("Sorry, the file" + filename + " does not exist.")
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    print(words)
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
