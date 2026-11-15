ANGLES = {
    "квадрат": [90, 90, 90, 90],
    "прямокутник": [90, 90, 90, 90],
    "трикутник": [60, 60, 60],
}


class Figure:
    def __init__(self, figure_type: str, length: float):
        if figure_type not in ANGLES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль")
        self._type = figure_type
        self._length = length

    @property
    def get_figure_type(self):
        return self._type

    @property
    def get_figure_length(self):
        return self._length

    def get_angles(self):
        return list(ANGLES[self._type])


if __name__ == "__main__":
    for t, l in [("квадрат", 4), ("прямокутник", 6), ("трикутник", 3)]:
        f = Figure(t, l)
        print(f.get_figure_type, f.get_figure_length, f.get_angles())
