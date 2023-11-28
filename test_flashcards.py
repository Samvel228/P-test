import unittest
from flashcard import Flashcard
from flashcard_deck import FlashcardDeck
from unittest.mock import patch, mock_open, MagicMock
import pickle

class TestFlashcardMethods(unittest.TestCase):

    def test_display(self):
        flashcard = Flashcard("Python", "A high-level programming language.")
        self.assertEqual(flashcard.display(), "Python: A high-level programming language.")

    def test_edit_flashcard(self):
        flashcard = Flashcard("Term", "Old definition.")
        flashcard.edit_flashcard("New definition.")
        self.assertEqual(flashcard.definition, "New definition.")

    def test_flashcard_simularity(self):
        example_flashcard = Flashcard("Programming", "Programming is an art of thinking.")
        user_answer = "Programming is a form of creative thinking."
        result = example_flashcard.check_similarity(user_answer)
        self.assertEqual(result, True)
    
class TestFlashcardDecMethods(unittest.TestCase):

    def test_add_flashcard(self):
        flashcard = Flashcard("Term", "Deff")
        deck = FlashcardDeck()
        deck.add_flashcard(flashcard)
        self.assertIn(flashcard, deck.flashcards)

    def test_study_flashcards_correct_answer(self):
        deck = FlashcardDeck()
        flashcard1 = Flashcard("Term1", "Definition1")
        deck.add_flashcard(flashcard1)

        # Подставляем "правильный" ответ при вызове input
        with patch('builtins.input', return_value="Definition1"):
            with patch('builtins.print') as mock_print:
                deck.study_flashcards()

        # Проверяем, что было выведено "Правильно"
        mock_print.assert_called_with("Правильно")

    def test_study_flashcards_incorrect_answer(self):
        deck = FlashcardDeck()
        flashcard1 = Flashcard("Term1", "Definition1")
        deck.add_flashcard(flashcard1)

        # Подставляем "неправильный" ответ, который не совпадает с Definition1
        with patch('builtins.input', return_value="IncorrectAnswer"):
            with patch('builtins.print') as mock_print:
                deck.study_flashcards()

        # Проверяем, что было выведено "Ошибка! правильное определение: Definition1"
        mock_print.assert_called_with("Ошибка! правельное определение: Definition1")
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('flashcard_deck.pickle.dump')
    def test_save_flashcard_deck(self, mock_pickle_dump, mock_open):
        # Создаем объект FlashcardDeck и добавляем в него фиктивную карточку
        deck = FlashcardDeck()
        fake_flashcard = Flashcard("Term", "Definition")
        deck.flashcards.append(fake_flashcard)

        # Вызываем функцию сохранения
        deck.save_flashcard_deck("test_deck.pkl")

        # Проверяем, что функция open вызывалась с ожидаемыми аргументами
        mock_open.assert_called_once_with("test_deck.pkl", 'wb')

        # Проверяем, что функция pickle.dump вызывалась с ожидаемыми аргументами
        mock_pickle_dump.assert_called_once_with([fake_flashcard], mock_open.return_value)
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('flashcard_deck.pickle.load')
    def test_load_flashcard_deck(self, mock_pickle_load, mock_open):
        # Подготавливаем фиктивные данные для загрузки
        fake_flashcard = Flashcard("Term", "Definition")
        fake_flashcards = [fake_flashcard]

        # Мокаем функцию open и load
        mock_open.return_value.__enter__.return_value.read.return_value = "fake_data"
        mock_pickle_load.return_value = fake_flashcards

        # Создаем объект FlashcardDeck и вызываем функцию загрузки
        deck = FlashcardDeck()
        deck.load_flashcard_deck("test_deck.pkl")

        # Проверяем, что функция open вызывалась с ожидаемыми аргументами
        mock_open.assert_called_once_with("test_deck.pkl", 'rb')

        # Проверяем, что функция pickle.load вызывалась с ожидаемыми аргументами
        mock_pickle_load.assert_called_once_with(mock_open.return_value)

        # Проверяем, что flashcards в объекте FlashcardDeck были обновлены
        self.assertEqual(deck.flashcards, fake_flashcards)

if __name__ == '__main__':
    unittest.main()