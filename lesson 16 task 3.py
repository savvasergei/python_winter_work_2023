def title_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.title()
        return modified_result
    return wrapper()
@title_decorator
def h():
    return input()
print(h)