from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tasks
from django.views.generic import ListView, DetailView, CreateView


class HomeTasks(ListView):
    model = Tasks
    template_name = 'task_manager/home_tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeTasks, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['list_themes'] = list_themes
        context['difficulty'] = difficulty
        context['classes'] = classes
        return context

    def get_queryset(self):
        return Tasks.objects.all()  # .select_related('category')


class SearchTasks(ListView):
    model = Tasks
    template_name = 'task_manager/home_tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchTasks, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['list_themes'] = list_themes
        context['difficulty'] = difficulty
        context['classes'] = classes
        return context

    def get_queryset(self):
        query = self.request.GET.get('search_text')
        res = []
        for qur in query.split():
            res.extend(Tasks.objects.filter(content__icontains=qur))
            res.extend(Tasks.objects.filter(title__icontains=qur))
        return res


class FilterTasks(ListView):
    model = Tasks
    template_name = 'task_manager/home_tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FilterTasks, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['list_themes'] = list_themes
        context['difficulty'] = difficulty
        context['classes'] = classes
        return context

    def get_queryset(self):
        difficulty = self.request.GET.get('difficulty')
        classes = self.request.GET.get('classes')
        themes = self.request.GET.get('themes')
        res = Tasks.objects.all()
        if difficulty != 'Сложность':
            res = res.filter(difficulty__icontains=difficulty)
        if classes != 'Класс':
            res = res.filter(classes__icontains=classes)
        if themes is not None:
            final_res = []
            for them in themes.split():
                final_res.extend(res.filter(themes__icontains=them))
            res = final_res
        return res


class ViewTasks(DetailView):
    model = Tasks
    template_name = 'task_manager/view_task.html'
    context_object_name = 'task_item'


difficulty = range(1, 11)
classes = range(5, 12)

list_themes_clasificator = {
    "Логика и теория множеств": [
        "Математическая логика",
        "Теория множеств",
        "Отношение порядка",
        "Отношение эквивалентности. Классы эквивалентности",
        "Лингвистика",
        "Задачи - шутки",
        "Теория алгоритмов",
        "Логика и теория множеств",
    ],

    "Алгебра и арифметика": [
        "Арифметика. Устный счет и т.п.",
        "Арифметические действия. Числовые тождества",
        "Средние величины",
        "Текстовые задачи",
        "Дроби",
        "Системы счисления",
        "Модуль числа",
        "Многочлены",
        "Формальные степенные ряды",
        "Алгебраическая геометрия",
        "Рациональные функции",
        "Корни. Степень с рациональным показателем",
        "Линейная и полилинейная алгебра",
        "Теория групп",
        "Теория чисел. Делимость",
        "Последовательности",
        "Алгебраические неравенства и системы неравенств",
        "Алгебраические уравнения и системы уравнений",
        "Тригонометрия",
        "Показательные функции и логарифмы",
        "Комплексные числа",
        "Графики и ГМТ на координатной плоскости",
        "Алгебра и арифметика (прочее)",
    ],

    "Геометрия": [
        "Планиметрия",
        "Стереометрия",
        "Проективная геометрия",
        "Аффинная геометрия",
        "Комбинаторная геометрия",
        "Топология",
        "Выпуклый анализ и линейное программирование",
        "Геометрия (прочее)",
    ],

    "Комбинаторика": [
        "Классическая комбинаторика",
        "Треугольник Паскаля и бином Ньютона",
        "Производящие функции",
        "Числа Каталана",
        "Теория графов",
        "Комбинаторика (прочее)",
    ],

    "Вероятность и статистика": [
        "Теория вероятностей",
        "Математическая статистика",
    ],

    "Математический анализ": [
        "Действительные числа",
        "Числовые последовательности",
        "Функции одной переменной. Непрерывность",
        "Производная",
        "Интеграл",
        "Ряды",
        "Последовательности и ряды функций",
        "Функции нескольких переменных",
        "Математический анализ (прочее)",
    ],

    "Методы": [
        "Индукция",
        "Принцип Дирихле",
        "Принцип крайнего",
        "Инварианты и полуинварианты",
        "Вспомогательная раскраска",
        "Алгебраические методы",
        "Геометрические методы",
        "Методы математического анализа",
        "Доказательство от противного",
        "Примеры и контрпримеры. Конструкции",
        "Методы решения задач с параметром",
    ],
}

list_themes = [
    "Математическая логика",
    "Теория множеств",
    "Отношение порядка",
    "Отношение эквивалентности. Классы эквивалентности",
    "Лингвистика",
    "Задачи - шутки",
    "Теория алгоритмов",
    "Логика и теория множеств",
    "Арифметика. Устный счет и т.п.",
    "Арифметические действия. Числовые тождества",
    "Средние величины",
    "Текстовые задачи",
    "Дроби",
    "Системы счисления",
    "Модуль числа",
    "Многочлены",
    "Формальные степенные ряды",
    "Алгебраическая геометрия",
    "Рациональные функции",
    "Корни. Степень с рациональным показателем",
    "Линейная и полилинейная алгебра",
    "Теория групп",
    "Теория чисел. Делимость",
    "Последовательности",
    "Алгебраические неравенства и системы неравенств",
    "Алгебраические уравнения и системы уравнений",
    "Тригонометрия",
    "Показательные функции и логарифмы",
    "Комплексные числа",
    "Графики и ГМТ на координатной плоскости",
    "Алгебра и арифметика (прочее)",
    "Планиметрия",
    "Стереометрия",
    "Проективная геометрия",
    "Аффинная геометрия",
    "Комбинаторная геометрия",
    "Топология",
    "Выпуклый анализ и линейное программирование",
    "Геометрия (прочее)",
    "Классическая комбинаторика",
    "Треугольник Паскаля и бином Ньютона",
    "Производящие функции",
    "Числа Каталана",
    "Теория графов",
    "Комбинаторика (прочее)",
    "Теория вероятностей",
    "Математическая статистика",
    "Действительные числа",
    "Числовые последовательности",
    "Функции одной переменной. Непрерывность",
    "Производная",
    "Интеграл",
    "Ряды",
    "Последовательности и ряды функций",
    "Последовательности и ряды функций",
    "Функции нескольких переменных",
    "Математический анализ (прочее)",
    "Индукция",
    "Принцип Дирихле",
    "Принцип крайнего",
    "Инварианты и полуинварианты",
    "Вспомогательная раскраска",
    "Алгебраические методы",
    "Геометрические методы",
    "Методы математического анализа",
    "Доказательство от противного",
    "Примеры и контрпримеры. Конструкции",
    "Методы решения задач с параметром",
]
