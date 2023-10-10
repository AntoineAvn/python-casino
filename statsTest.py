import unittest
from statsClass import Stats
from statsClass import addUser, readData, updateUser, deleteUser


class MyTestCase(unittest.TestCase):
    def test_stats_creatation_object(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4, "sold": 100}})
        self.assertEqual(stats.stats["user1"]["total_number_of_try"], 7)  # add assertion here

    def test_stats_get_mean(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4, "sold": 100}})
        self.assertEqual(stats.getMean("user1"), 1.75)

    def test_stats_get_time(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4, "sold": 100}})
        self.assertEqual(stats.getTime("user1"), 194858898.25)

    def test_stats_add_user(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4, "sold": 100}})
        addUser(stats.stats)
        user2 = \
            {
                "user2": {
                    "total_number_of_try": 17,
                    "total_time": 7794793,
                    "tl_number_of_game_played": 4,
                    "sold": 100
                }
            }
        addUser(user2)
        self.assertEqual(readData("data.json").get("user2").get("total_number_of_try"), 17)
        self.assertEqual(readData("data.json").get("user1").get("total_time"), 779435593)

    def test_stats_read_data(self):
        data = readData("data.json")
        self.assertEqual(data.get("user1").get("total_number_of_try"), 7)

    def test_stats_get_number_of_game_played(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4, "sold": 100}})
        addUser(stats.stats)
        self.assertEqual(stats.getNumberOfGamePlayed("user1"), 4)
        stats2 = Stats({"user2": {"total_number_of_try": 17, "total_time": 77943435593, "tl_number_of_game_played": 48, "sold": 100}})
        addUser(stats2.stats)
        self.assertEqual(stats2.getNumberOfGamePlayed("user2"), 48)

    def test_update_user(self):
        stats = Stats({"user1": {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4, "sold": 100}})
        addUser(stats.stats)
        updateUser("user1", {"total_number_of_try": 17}, "total_number_of_try")
        self.assertFalse(readData("data.json").get("user1").get("total_number_of_try") == 7)
        self.assertTrue(readData("data.json").get("user1").get("total_number_of_try") == 17)
        updateUser("user1", {"total_number_of_try": 7, "total_time": 779435593, "tl_number_of_game_played": 4}, ["total_number_of_try", "total_time", "tl_number_of_game_played"])
        self.assertTrue(readData("data.json").get("user1").get("total_number_of_try") == 7)
        self.assertTrue(readData("data.json").get("user1").get("total_time") == 779435593)

    def test_delete_user(self):
        stats = Stats({"user17" : {"total_number_of_try": 3, "total_time": 120448, "tl_number_of_game_played": 2, "sold": 100}})
        addUser(stats.stats)
        stats = Stats({"user18" : {"total_number_of_try": 9, "total_time": 243489032, "tl_number_of_game_played": 17, "sold": 100}})
        addUser(stats.stats)
        deleteUser("user17")
        self.assertFalse(readData("data.json").get("user17"))
        self.assertTrue(readData("data.json").get("user18"))

    def test_get_sold_user(self):
        stats = Stats({"user17" : {"total_number_of_try": 3, "total_time": 120448, "tl_number_of_game_played": 2, "sold": 100}})
        addUser(stats.stats)
        self.assertEqual(stats.getSold("user17"), 100)
        self.assertEqual(readData("data.json").get("user17").get("sold"), 100)

if __name__ == '__main__':
    unittest.main()
