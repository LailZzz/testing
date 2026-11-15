# Лаб 2: Тестування з бібліотекою pytest

Тема: `notes/07_testing/02_pytest`. Мова: Python 3.10+.

## Структура

| Файл | Призначення |
|------|-------------|
| `app.py` | клас `Figure` (`FIGURES`, `type`, `get_figure_length`, `get_angles`, `describe`) |
| `conftest.py` | спільні fixtures: `length`, `square`, `text_file` (з `yield`) |
| `test_app.py` | 24 тести: `parametrize`, fixtures, `scope="module"`, маркер `unit`, `tmp_path`, `capsys`, `monkeypatch` |
| `pyproject.toml` | реєстрація маркерів `unit` і `slow` |
| `requirements.txt` | залежність `pytest` |
| `REPORT.md` | звіт до роботи |

## Встановлення

```
pip install pytest
```

## Запуск

Команди виконуються з цієї папки:

```
python app.py
pytest -v
pytest test_app.py::test_triangle_type -v
pytest -m unit -v
pytest --collect-only
pytest -x --tb=short
```

Якщо команда `pytest` не знайдена, використовуйте `python -m pytest`.
