class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: float):
        assert figure_type in self.FIGURES, f"Невідомий тип фігури: {figure_type}"
        assert length > 0, "Довжина має бути більшою за нуль"
        self.type = figure_type
        self._length = length

    @property
    def get_figure_length(self):
        return self._length

    def get_angles(self):
        if self.type == "трикутник":
            return [60, 60, 60]
        return [90, 90, 90, 90]

    def describe(self):
        print(f"{self.type}, довжина {self._length}")


if __name__ == "__main__":
    for name, size in [("квадрат", 4), ("прямокутник", 6), ("трикутник", 3)]:
        figure = Figure(name, size)
        figure.describe()
