import operator

"""Count words."""



def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    words = str.split(s)

    word_dict = {}
    for w in words :
        if w in word_dict :
            word_dict[w] += 1
        else :
            word_dict[w] = 1

    words = [ (w,c) for w,c in word_dict.iteritems()]
    words = sorted(words,key=operator.itemgetter(0))
    words = sorted(words,key=operator.itemgetter(1), reverse=True)
    return words[:n]


    # TODO: Count the number of occurences of each word in s

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    #return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
