import unittest
from statsClass import Stats
from statsClass import addUser


class MyTestCase(unittest.TestCase):
    def test_stats_creatation_object(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4}})
        self.assertEqual(stats.stats["user1"]["total_number_of_try"], 7)  # add assertion here

    def test_stats_get_mean(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4}})
        self.assertEqual(stats.getMean(stats.stats, "user1"), 1.75)

    def test_stats_get_time(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4}})
        self.assertEqual(stats.getTime(stats.stats, "user1", 4), 194858898.25)

    def test_stats_add_user(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4}})
        user2 = \
            {
                "user2": {
                    "total_number_of_try": 17,
                    "total_time": 7794793,
                    "tl_number_of_game_played": 4
                }
            }
        addUser(user2)


if __name__ == '__main__':
    unittest.main()
