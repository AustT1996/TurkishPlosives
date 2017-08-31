# Revise dictionary again
possible_other_allowed = ['à', 'á', 'â', 'ã', 'ä', 'å', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'ÿ', 'ā', 'ă', 'ć', 'č', 'đ', 'ē', 'ĕ', 'ě', 'ğ', 'ġ', 'ħ', 'ĩ', 'ī', 'ı', 'ĸ', 'ĺ', 'ļ', 'ľ', 'ń', 'ő', 'ř', 'ś', 'ş', 'š', 'ť', 'ũ', 'ū', 'ű', 'ż', 'ž', 'ƒ', 'ơ', 'ǻ']
with codecs.open('tr_freq_list_v1.txt', 'r', 'UTF-8') as f:
    with codecs.open('tr_freq_list.txt', 'w', 'UTF-8') as f_out:
        reader = csv.reader(f)
        tr_letter_fd = defaultdict(int)
        for row in reader:
            n = int(row[1])
            if not any([letter not in possible_other_allowed and letter not in tr_alphabet
                    for letter in row[0]]):
                f_out.write("{},{}\n".format(row[0], n))