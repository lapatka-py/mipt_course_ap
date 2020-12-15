class NoNameClass():
    def __init__(self, name, surname, is_hired):
        self.name = name
        self.surname = surname
        self.is_hired = is_hired


def obj_to_json(my_class_instance):
    '''
    Получает на вход объект класса NoNameClass,
    выдает на выходе JSON-представление.
    >>> a = NoNameClass('me', 'my_surname', True)
    >>> obj_to_json(a)
    {'name': 'me', 'surname': 'my_surname', 'is_hired': True'}
    '''
    pass


def json_to_obj(my_class_instance):
    '''
    Получает на вход JSON-представление,
    выдает на выходе объект класса NoNameClass.
    >>> a = NoNameClass('me', 'my_surname', True)
    >>> json_dict = get_json(a)
    >>> b = json_to_obj(json_dict)
    <__main__.MyClass object at 0x7fd8e9634510>
    '''
    pass

