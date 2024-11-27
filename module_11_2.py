import inspect


class MyClass:
    pass


def introspection_info(obj):
    data = {'type': type(obj)}

    attrs = []
    methods = []
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):
            methods.append(attr_name)
        else:
            attrs.append(attr_name)
    data['attrs'] = attrs
    data['methods'] = methods

    # Если объект - модуль
    if inspect.ismodule(obj):
        data['module'] = obj.__name__
    else:
        # Получаем имя модуля, если доступно
        module_name = getattr(obj, '__module__', None)
        if module_name is None:  # обработка для встроенных типов
            module_name = 'builtins' if isinstance(obj, (int, str, float, list, dict, set, tuple)) else 'unknown'
        data['module'] = module_name

    return data


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)

    my_instance = MyClass()
    class_info = introspection_info(my_instance)
    print(class_info)
