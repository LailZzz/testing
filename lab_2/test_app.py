import pytest

from app import Figure


@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


@pytest.mark.unit
def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"


@pytest.mark.unit
def test_figure_length():
    assert Figure("прямокутник", 7).get_figure_length == 7


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    assert Figure(figure, 1).type == figure


def test_square_fixture(square):
    assert square.type == "квадрат"
    assert square.get_figure_length == 10


def test_square_depends_on_length(square, length):
    assert square.get_figure_length == length


@pytest.mark.parametrize("figure_type", ["коло", "", "Квадрат", "ромб"])
def test_invalid_figure_type(figure_type):
    with pytest.raises(AssertionError):
        Figure(figure_type, 5)


@pytest.mark.parametrize("bad_length", [0, -1, -10, -0.5])
def test_invalid_length_values(bad_length):
    with pytest.raises(AssertionError):
        Figure("квадрат", bad_length)


@pytest.mark.parametrize(
    "figure, angles",
    [
        ("квадрат", [90, 90, 90, 90]),
        ("прямокутник", [90, 90, 90, 90]),
        ("трикутник", [60, 60, 60]),
    ],
)
def test_angles(figure, angles):
    assert Figure(figure, 3).get_angles() == angles


def test_module_fixture_first(allowed_figures):
    assert "квадрат" in allowed_figures


def test_module_fixture_second(allowed_figures):
    assert len(allowed_figures) == 3


def test_text_file(text_file):
    assert text_file.read_text(encoding="utf-8") == "готово"


def test_describe_output(capsys):
    Figure("квадрат", 5).describe()
    captured = capsys.readouterr()
    assert captured.out == "квадрат, довжина 5\n"


def test_monkeypatch_figures(monkeypatch):
    monkeypatch.setattr(Figure, "FIGURES", ["квадрат"])
    with pytest.raises(AssertionError):
        Figure("трикутник", 2)
