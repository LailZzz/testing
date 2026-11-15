import pytest

from app import Figure


@pytest.fixture
def length():
    return 10


@pytest.fixture
def square(length):
    return Figure("квадрат", length)


@pytest.fixture
def text_file(tmp_path):
    path = tmp_path / "result.txt"
    path.write_text("готово", encoding="utf-8")
    yield path
    path.unlink()
