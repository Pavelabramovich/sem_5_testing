import inspect


def main(function):
    locale = inspect.stack()[1][0].f_locals
    module = locale.get('__name__', None)

    if module == "__main__":
        locale[function.__name__] = function
        function()

    return function
