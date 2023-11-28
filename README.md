[![CI/CD GitHub Actions](https://github.com/Samvel228/p-test/actions/workflows/test-action.yml/badge.svg)](https://github.com/Samvel228/p-test/actions/workflows/test-action.yml)
[![Coverage Status](https://coveralls.io/repos/Samvel228/p-test/badge.svg?branch=main)](https://coveralls.io/github/Samvel228/p-test?branch=main)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Samvel228_p-test&metric=alert_status)](https://sonarcloud.io/dashboard?id=Samvel228_p-test)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Samvel228_p-test&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Samvel228_p-test)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=Samvel228_p-test&metric=code_smells)](https://sonarcloud.io/dashboard?id=Samvel228_p-test)

# План тестирования

## Атестационное тестирование:  
Тест А1  
Действие: Выбран пункт меню "Добавить карточку". Вводится термин "Python" и определение "A high-level programming language."  
Ожидаемый результат: Карточка с термином "Python" и определением "A high-level programming language." добавлена в self.deck.flashcards

Тест А2  
Действие: Вызывается метод display_menu. 
Ожидаемый результат: Выводится меню с шестью пунктами

Тест А3  
Действие: Выбран пункт меню "Учить карты". Подставлены моки для input и print.  
Ожидаемый результат: Вызывается метод study_flashcards у объекта self.deck, и выводится сообщение "Правильно" или "Ошибка! правильное определение: ...".

Тест А4  
Действие: Выбран пункт меню "Учить карты". Подставлены моки для input и print.  
Ожидаемый результат: Вызывается метод study_flashcards у объекта self.deck, и выводится сообщение "Правильно" или "Ошибка! правильное определение: ...".

Тест А5  
Действие:Выбран пункт меню "Загрузить карточки". Вводится имя файла "test_deck.pkl". Подставлен мок для input.  
Ожидаемый результат: Вызывается метод load_flashcard_deck у объекта self.deck с аргументом "test_deck.pkl".

Тест А6  
Действие:Выбран пункт меню "Изменить карточку". Вводится термин "Python" и новое определение "An interpreted, high-level and general-purpose programming language."  
Ожидаемый результат: У карточки с термином "Python" в self.deck.flashcards изменено определение на "An interpreted, high-level and general-purpose programming language."

Тест А7  
Действие:Воспроизведен весь поток действий для добавления карточки: выбор пункта меню "Добавить карточку", ввод термина "JavaScript" и определения "A lightweight, interpreted, or just-in-time compiled programming language with first-class functions."  
Ожидаемый результат: Карточка с термином "JavaScript" и определением "A lightweight, interpreted, or just-in-time compiled programming language with first-class functions." добавлена в self.deck.flashcards. 

Тест А8  
Действие:Воспроизведен весь поток действий для обучения карт: выбор пункта меню "Учить карты", ввод ответа на вопрос об определении карточки. Подставлены моки для input и print.  
Ожидаемый результат: Выводится сообщение "Правильно" или "Ошибка! правильное определение: ...". 


## Блочное тестирование:

### Класс `Flashcard`
#### Тест Б1.1:  
Входные данные: Создается объект Flashcard с термином "Python" и определением "A high-level programming language."  
Ожидаемый результат: Метод display возвращает строку "Python: A high-level programming language."
Тест F2: test_edit_flashcard

#### Тест Б1.2:  
Входные данные: Создается объект Flashcard с термином "Term" и определением "Old definition."  
Ожидаемый результат: После вызова метода edit_flashcard с новым определением "New definition.", значение definition в объекте изменяется на "New definition."
Тест F3: test_flashcard_similarity

#### Тест Б1.3:  
Входные данные: Создается объект Flashcard с термином "Programming" и определением "Programming is an art of thinking."  
Ожидаемый результат: Метод check_similarity возвращает True при сравнении с ответом пользователя "Programming is a form of creative thinking."

#### Тест Б1.1:  
Входные данные: a=1, b=-3, c=2 (дискриминант > 0)  
Ожидаемый результат: Два корня, вернуть указатель на массив [2, 1].

#### Тест Б1.2:  
Входные данные: a=1, b=-2, c=1 (дискриминант = 0)  
Ожидаемый результат: Один корень, вернуть указатель на массив [1].

#### Тест Б1.3:  
Входные данные: a=2, b=2, c=2 (дискриминант < 0)   
Ожидаемый результат: Нет действительных корней, вернуть NULL.

### Класс `FlashcardDeck`
#### Тест Б2.1: test_add_flashcard

Входные данные: Создается объект FlashcardDeck и объект Flashcard с термином "Term" и определением "Deff".  
Ожидаемый результат: Метод add_flashcard добавляет созданный объект Flashcard в атрибут flashcards объекта FlashcardDeck.

#### Тест Б2.2: test_study_flashcards_correct_answer

Входные данные: Создается объект FlashcardDeck и объект Flashcard с термином "Term1" и определением "Definition1".  
Ожидаемый результат: При вводе "Definition1" пользователем в процессе обучения (study_flashcards), выводится "Правильно".

#### Тест Б2.3: test_study_flashcards_incorrect_answer

Входные данные: Создается объект FlashcardDeck и объект Flashcard с термином "Term1" и определением "Definition1".  
Ожидаемый результат: При вводе "IncorrectAnswer" пользователем в процессе обучения (study_flashcards), выводится "Ошибка! правильное определение: Definition1".

#### Тест Б2.4: test_save_flashcard_deck

Входные данные: Создается объект FlashcardDeck и добавляется фиктивная карточка.  
Ожидаемый результат: При вызове метода save_flashcard_deck с аргументом "test_deck.pkl", функция open вызывается с ожидаемыми аргументами, и функция pickle.dump вызывается с ожидаемыми аргументами.

#### Тест Б2.5: test_load_flashcard_deck

Входные данные: Создается объект FlashcardDeck и подготавливаются фиктивные данные для загрузки.  
Ожидаемый результат: При вызове метода load_flashcard_deck с аргументом "test_deck.pkl", функция open вызывается с ожидаемыми аргументами, и функция pickle.load вызывается с ожидаемыми аргументами. После этого атрибут flashcards в объекте FlashcardDeck обновляется с ожидаемыми данными.

## Интеграционное тестирование:

#### Тест И1:
Методы: `int fibonachi(int num)`, `double* square(double a, double b, double c)`  
Описание: Проверка использования результата функции `fibonachi` в функции `square`  
Входные данные: a= fibonachi(5) b= fibonachi(5) c= fibonachi(5)  
Ожидаемый результат: Результат `fibonachi(5)` будет использован в `square` для расчета корней.  
