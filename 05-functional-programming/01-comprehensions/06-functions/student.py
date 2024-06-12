def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director]) 

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return any(genre in movie.genres and movie.director == director for movie in movies)

def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2

def is_increasing(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))

"""ns[1:] is a slice of the list ns starting from the second element (index 1) to the end. This effectively shifts the list one position to the left.

zip(ns, ns[1:]) pairs each element in ns with the next element in ns. The zip function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences.

(x <= y for x, y in zip(ns, ns[1:])) is a generator expression that checks for each pair (x, y) if x is less than or equal to y. This is true if the list is in non-decreasing order.

all() is a built-in Python function that returns True if all elements of the iterable (in this case, the generator expression) are true. If at least one comparison x <= y is False, all() will return False.

So, the entire line return all(x <= y for x, y in zip(ns, ns[1:])) will return True if the list ns is in non-decreasing order (i.e., each element is less than or equal to the next one), and False otherwise.

"""
def count_matching(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x == y)

def weighted_sum(ns, weights):
    return sum(n * w for n, w in zip(ns, weights))

def alternating_caps(string):
    chars = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(string)]
    return "".join(chars)

def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}