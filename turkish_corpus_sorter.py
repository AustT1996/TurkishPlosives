# Quick script to sort out the single-use words from the Turkish Corpus
# The original corpus is not included
import codecs
with codecs.open('turkish_freq_list_raw.txt', 'r', 'UTF-8') as f_in:
    with codecs.open('tr_freq_list_v1.txt', 'w', 'UTF-8') as f_out:
        for line in f_in:
            l = line.strip().split('\t')
            try:
                word = l[1].lower()
                freq = int(l[2])
                if word.isalpha() and freq > 1:
                    f_out.write("{},{}\n".format(word, freq))
            except IndexError: # This came up from blank lines in file
                pass