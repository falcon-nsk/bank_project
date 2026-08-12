from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as error:
                message = f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

                raise

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")
            else:
                print(message)
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
