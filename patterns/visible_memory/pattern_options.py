
def set_default_options(self=None):
    """
        Опции по умолчанию
        n_figures - количество комбинаций фигур (кнопок ответов - макс 39)
        n_colours - количество цветов фигур в одной кнопке (оптимально 2)
        rand_fig - случайное количество фигур в одной кнопке одного цвета
        difficult_fig_max - случайная максимальная сложность фигур (1 линии, 2 треугольки, 3 четырехугольники)
        difficult_fig_min - минимальная сложность фигуг
        difficult_detals - детализация построения фигур в кнопке (минимум 2, оптимально 12)
        memory_figs - количество фигур для запоминания (оптимально 5, максимум 12)
    """

    self.options = {'name_options': 'default', 'n_figures': 13, 'n_colours': 2, 'rand_fig': 2, 'difficult_fig_min': 3, 'difficult_fig_max': 6,
                    'difficult_detals': 3, 'memory_figs': 12}

def set_pattern_options(self=None, pattern=None):
    """
        функция установки проверки пользовательских опций
    """
    if len(self.options.keys()) == len(pattern):

        for n_key, n_value in zip(self.options.keys(), pattern):
            self.options[n_key] = n_value

        """
            проверяем корректность данных
        """
        if self.options['n_figures'] < 2: self.options['n_figures'] = 2
        if self.options['n_figures'] > 39: self.options['n_figures'] = 39

        if self.options['n_colours'] < 1: self.options['n_colours'] = 1
        if self.options['n_colours'] > 7: self.options['n_colours'] = 7

        if self.options['rand_fig'] < 1: self.options['rand_fig'] = 1

        if self.options['difficult_fig_max'] < 1: self.options['difficult_fig_max'] = 1
        if self.options['difficult_fig_max'] < self.options['difficult_fig_min']: self.options['difficult_fig_min'] = self.options['difficult_fig_max']

        if self.options['difficult_detals'] < 2: self.options['difficult_detals'] = 2

        if self.options['memory_figs'] < 1: self.options['memory_figs'] = 1
        if self.options['memory_figs'] > 12: self.options['memory_figs'] = 12