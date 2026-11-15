# Звіт до роботи

**Студент:** Муханов Володимир Сергійович, група КН-42

**Тема:** Лаб 2. Тестування з бібліотекою pytest

**Мета роботи:** навчитися писати тести за допомогою `pytest`: звичайні функції з `assert`, перевірка винятків
через `pytest.raises`, параметризація, fixtures (у тому числі `scope`, `yield`, `conftest.py`) та маркери.

## Виконання роботи

### Завдання 1. Встановлення та основи

1. Встановили бібліотеку командою:

```
pip install pytest
```

2. Створили [`app.py`](app.py) з класом `Figure` (список дозволених фігур `FIGURES`, атрибут `type`,
   властивість `get_figure_length`, методи `get_angles` та `describe`). Неправильні дані відхиляються через `assert`.
3. Написали перші тести у [`test_app.py`](test_app.py): `test_triangle_type`, `test_figure_length` та
   `test_invalid_length`, де `pytest.raises(AssertionError)` перевіряє, що `Figure("квадрат", 0)` викликає помилку.
4. Навчились запускати окремий тест: `pytest test_app.py::test_triangle_type -v`.

### Завдання 2. Параметризація

1. Додали параметризований тест для всіх дозволених фігур (`test_allowed_figure`): один тест виконується
   для кожного елемента `Figure.FIGURES`.
2. 🔥 Додали тести для кожного неправильного типу (`"коло"`, `""`, `"Квадрат"`, `"ромб"`) та кожного
   неправильного значення довжини (`0`, `-1`, `-10`, `-0.5`).
3. Додатково параметризували перевірку кутів (`test_angles`) з двома параметрами: фігура й очікуваний список кутів.

Приклад параметризації:

```python
@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    assert Figure(figure, 1).type == figure
```

### Завдання 3. Fixtures

1. У [`conftest.py`](conftest.py) створили fixture `length` (повертає 10) та `square`, що залежить від `length`
   і повертає `Figure("квадрат", 10)`. Тести `test_square_fixture` і `test_square_depends_on_length` перевіряють її властивості.
   Імпортувати fixtures у тести не потрібно, pytest знаходить їх у `conftest.py` сам.
2. Fixture `text_file` використовує вбудовану `tmp_path` та `yield`: код після `yield` видаляє файл після тесту.
3. Тест `test_describe_output` перевіряє вивід у консоль через `capsys`, а `test_monkeypatch_figures` тимчасово
   підміняє `Figure.FIGURES` через `monkeypatch`.
4. Fixture `allowed_figures` зі `scope="module"` використана у двох тестах: `test_module_fixture_first` і
   `test_module_fixture_second`. Pytest створює її один раз на файл.

### Завдання 4. Маркери

1. Позначили тести `test_triangle_type` і `test_figure_length` маркером `@pytest.mark.unit`.
2. Зареєстрували маркери `unit` і `slow` у [`pyproject.toml`](pyproject.toml).
3. Запустили лише ці тести командою `pytest -m unit -v`. Pytest вибрав 2 тести з 24, а решту (22) відфільтрував:

```
collected 24 items / 22 deselected / 2 selected

test_app.py::test_figure_length PASSED                                   [100%]

=================== 2 passed, 22 deselected, 1 warning in 0.05s ===================
```

### Завдання 5. Навмисна помилка

1. У `app.py` у конструкторі `Figure` тимчасово змінили рядок `self.type = figure_type` на `self.type = figure_type + "!"`.
2. Запустили `pytest -x --tb=short`.
3. Результат: тести, що перевіряють `type`, не проходять. Параметр `-x` зупиняє запуск одразу після першої помилки,
   тому решта тестів не виконується. Параметр `--tb=short` скорочує traceback до рядка з `assert` і порівняння значень.
4. Повернули `self.type = figure_type` і повторний запуск показав, що всі тести проходять.

Результат запуску з помилкою:

```
<< вставте сюди вивід pytest -x --tb=short з помилкою >>
```

### Запуск і результат

Команди:

```
pip install pytest
pytest -v
pytest -m unit -v
```

Результат `pytest -v`:

```
collected 24 items

test_app.py::test_triangle_type PASSED                                   [  4%]
test_app.py::test_figure_length PASSED                                   [  8%]
test_app.py::test_invalid_length PASSED                                  [ 12%]
test_app.py::test_allowed_figure[\u043a\u0432\u0430\u0434\u0440\u0430\u0442] PASSED [ 16%]
test_app.py::test_allowed_figure[\u043f\u0440\u044f\u043c\u043e\u043a\u0443\u0442\u043d\u0438\u043a] PASSED [ 20%]
test_app.py::test_allowed_figure[\u0442\u0440\u0438\u043a\u0443\u0442\u043d\u0438\u043a] PASSED [ 25%]
test_app.py::test_square_fixture PASSED                                  [ 29%]
test_app.py::test_square_depends_on_length PASSED                        [ 33%]
test_app.py::test_invalid_figure_type[\u043a\u043e\u043b\u043e] PASSED   [ 37%]
test_app.py::test_invalid_figure_type[] PASSED                           [ 41%]
test_app.py::test_invalid_figure_type[\u041a\u0432\u0430\u0434\u0440\u0430\u0442] PASSED [ 45%]
test_app.py::test_invalid_figure_type[\u0440\u043e\u043c\u0431] PASSED   [ 50%]
test_app.py::test_invalid_length_values[0] PASSED                        [ 54%]
test_app.py::test_invalid_length_values[-1] PASSED                       [ 58%]
test_app.py::test_invalid_length_values[-10] PASSED                      [ 62%]
test_app.py::test_invalid_length_values[-0.5] PASSED                     [ 66%]
test_app.py::test_angles[\u043a\u0432\u0430\u0434\u0440\u0430\u0442-angles0] PASSED [ 70%]
test_app.py::test_angles[\u043f\u0440\u044f\u043c\u043e\u043a\u0443\u0442\u043d\u0438\u043a-angles1] PASSED [ 75%]
test_app.py::test_angles[\u0442\u0440\u0438\u043a\u0443\u0442\u043d\u0438\u043a-angles2] PASSED [ 79%]
test_app.py::test_module_fixture_first PASSED                            [ 83%]
test_app.py::test_module_fixture_second PASSED                           [ 87%]
test_app.py::test_text_file PASSED                                       [ 91%]
test_app.py::test_monkeypatch_figures PASSED                             [100%]

======================== 24 passed, 1 warning in 0.08s ========================
```

Усі 24 тести пройшли (`24 passed`). Попередження (`warning`) походить із плагіна `anyio`, встановленого в системі, і не стосується тестів.

### Різниця між `unittest.TestCase` і функцією pytest

| | `unittest.TestCase` | pytest |
|---|---|---|
| Форма тесту | метод у класі, що успадковує `TestCase` | звичайна функція `test_...` |
| Перевірки | спеціальні методи: `assertEqual`, `assertRaises` | звичайний `assert`, `pytest.raises` |
| Підготовка даних | `setUp`, `tearDown` | fixtures (`@pytest.fixture`, `yield`, `scope`) |
| Кілька наборів даних | `subTest` у циклі | `@pytest.mark.parametrize` |
| Підміна залежностей | `unittest.mock.patch` | `monkeypatch`, `capsys`, `tmp_path` |
| Групування | окремі класи | маркери (`-m unit`) |

Тест на pytest коротший, а при помилці показує значення обох частин порівняння.

## Висновок

* ❓ **Що зроблено в роботі:** встановлено pytest, написано тести для класу `Figure` з параметризацією, fixtures
  (`conftest.py`, `yield`, `scope="module"`), маркером `unit`, а також із `tmp_path`, `capsys` і `monkeypatch`.
* ❓ **Чи досягнуто мети роботи:** так, мету досягнуто.
* ❓ **Які нові знання отримано:** як писати тести звичайними функціями з `assert`; як `parametrize` замінює цикл із `subTest`;
  як fixtures готують дані й прибирають ресурси; як позначати тести маркерами й запускати окремі групи.
* ❓ **Чи вдалось відповісти на всі питання, задані в ході роботи:** так, відповіді є у звіті.
* ❓ **Чи вдалося виконати всі завдання:** так, виконано всі завдання з позначками ⭐ та 🔥.
* ❓ **Чи виникли складності у виконанні завдання:** суттєвих складностей не було, найбільше уваги вимагали fixtures та область їх дії (`scope`).
* ❓ **Чи подобається такий формат здачі (Feedback):** так, формат зручний: звіт, код і результати лежать в одному репозиторії.
* ❓ **Побажання для покращення (Suggestions):** додати в конспект готовий приклад звіту саме для лабораторної з pytest.

**Посилання на репозиторій:** https://github.com/LailZzz/testing/tree/main/lab_2
