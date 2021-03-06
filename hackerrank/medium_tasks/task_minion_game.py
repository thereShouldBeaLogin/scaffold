from pprint import pprint
import cProfile as profile


data = 'NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN'


class Player():
    points = 0
    index = []

    def build_words(self, the_string):
        from itertools import accumulate
        words = []

        for _index in self.index:
            result_string = the_string[_index:]
            _words = list(accumulate(result_string))
            words.extend(_words)

        return set(words)

    # how about worker for every word ?
    # or dynamic words map to workers based on len
    def count_points(self, list_of_words, the_string):
        # 3.8 => 1.17
        def occurances(sub):
            count = start = 0

            while True:
                start = the_string.find(sub, start) + 1
                if start > 0:
                    count += 1
                else:
                    return count

        for word in list_of_words:
            num = occurances(word)
            self.points += num

        return self.points


class Kevin(Player):
    letters_of_type = 'AEIOU'


class Stuart(Player):
    letters_of_type = 'BCDFGHJKLMNPVWXYZ'


# 48 => 20.28
class Competition():

    vovels = 'AEIOU'

    def __init__(self, the_string):
        self.the_string = the_string
        self.player1 = Kevin()
        self.player2 = Stuart()

    def _get_index(self):
        kevins = []
        stuarts = []

        for index, letter in enumerate(self.the_string):
            if letter in self.vovels:
                kevins.append(index)
            else:
                stuarts.append(index)

        self.player1.index = set(kevins)
        self.player2.index = set(stuarts)

    # 1.2
    def calculate_for_player(self, player):
        list_of_words = player.build_words(self.the_string)
        return player.count_points(list_of_words, self.the_string)

    def compare_result(self):
        self._get_index()

        # launch this in threads
        result_Kevin = self.calculate_for_player(self.player1)
        result_Stuart = self.calculate_for_player(self.player2)

        if result_Kevin > result_Stuart:
            print("Kevin %s" % result_Kevin)
        elif result_Kevin < result_Stuart:
            print("Stuart %s" % result_Stuart)
        else:
            print("This is Draw!")

dd = Competition(data)
dd.compare_result()
