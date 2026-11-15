# Лабораторна: Загальне тестування та unittest

Тема: `notes/07_testing/01_general_and_unittest`. Мова: Python 3.10+, сторонні залежності не потрібні.

## Структура

| Файл | Призначення |
|------|-------------|
| `validation.py` | перевірка даних: `assert`, `raise ValueError`, `create_name` |
| `text_utils.py` | `count_symbols`, `count_vowels`, `divide` |
| `app.py` | клас `Figure` (`get_figure_type`, `get_figure_length`, `get_angles`) |
| `input_app.py` | функція з `input()` для тесту з `mock.patch` |
| `test.py` | 23 юніт-тести (`unittest`, `setUp`, `subTest`, `mock.patch`) |
| `REPORT.md` | звіт до роботи |

## Запуск

Команди виконуються з цієї папки:

```
python app.py                 # ручна перевірка Figure
python test.py                # запуск тестів
python -m unittest -v         # докладний вивід
python -m unittest test.TestFigure -v   # лише тести Figure
```

Очікуваний результат:

```
Ran 23 tests in 0.002s

OK
```

## Що покриває робота

- ⭐ власна перевірка числа (`check_positive`) і опис результатів у звіті;
- ⭐ `count_vowels` та 🔥 тести для порожнього рядка, цифр і українських літер;
- ⭐ `get_angles` і тести для квадрата, прямокутника й трикутника;
- 🔥 тести для нульової, від'ємної довжини та невідомого типу фігури;
- ⭐ `subTest` для всіх типів `Figure`;
- ⭐ функція з `input()` і тест через `patch`;
- тест, що спочатку не проходив, і результат після виправлення (див. `REPORT.md`).
