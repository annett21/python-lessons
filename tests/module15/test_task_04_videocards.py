import unittest
from task_04_videocards.main import select_video_cards


class Test04SelectVideoCards(unittest.TestCase):
    def test_select_video_cards(self):
        """
        Проверяем обычный кейс. [3070, 2060, 3090, 3070, 3090]  должны получить [3070, 2060, 3070]
        """
        video_cards_list = [3070, 2060, 3090, 3070, 3090]
        new_video_cards_list = select_video_cards(video_cards_list)

        self.assertEqual(new_video_cards_list, [3070, 2060, 3070])

    def test_select_video_cards_no_result(self):
        """
        Проверяем обычный кейс. [3070, 3070]  должны получить []
        """
        video_cards_list = [3070, 3070]
        new_video_cards_list = select_video_cards(video_cards_list)

        self.assertEqual(new_video_cards_list, [])


if __name__ == '__main__':
    unittest.main()
