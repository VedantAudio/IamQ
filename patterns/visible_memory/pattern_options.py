
def set_default_options(self=None):
    """
        Опции по умолчанию
        n_figures - количество комбинаций фигур (кнопок ответов - макс 39)
        n_colours - количество цветов фигур в одной кнопке (оптимально 2)
        rand_fig - случайное количество фигур в одной кнопке одного цвета
        difficult_fig_max - случайная максимальная сложность фигур (1 линии, 2 треугольки, 3 четырехугольники)
        difficult_fig_min - минимальная сложность фигуг
        difficult_detals - детализация построения фигур в кнопке (оптимально 24)
        memory_figs - количество фигур для запоминания (оптимально 5)
    """

    self.options = {'n_figures': 12, 'n_colours': 1, 'rand_fig': 1, 'difficult_fig_min': 3, 'difficult_fig_max': 4,
                    'difficult_detals': 24, 'memory_figs': 11}