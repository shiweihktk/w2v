def search_word(word):
    total_number = 54000  # 总的训练词数
index_number = creathash(word)%total_number
    while index_table[index_number][0]!= word:
        index_number = index_number +_1
        return index_table[index_number][1]
