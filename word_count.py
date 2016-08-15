import io

with io.open("data.txt", encoding="utf-8") as file:
    line_num = 1

    while True:
        num_words = 0
        word_length = []
        avg_word_length = 0.0
        temp = 0

        line = file.readline()

        if not line:
            break

        for each_word in line.split():

            num_words += 1
            word_length.append(len(each_word))

        for each in word_length:
            temp += float(each)

        avg_word_length = temp / num_words

        print "Line {} - No.of words: {}, avg word length: {:.2f}".format(line_num, num_words, avg_word_length)

        line_num += 1
