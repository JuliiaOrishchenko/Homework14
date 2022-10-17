def stop_words(words: list):
    def outer_wrapper(func):
        def inner_wrapper(name):
            result = func(name)
            for word in words:
                result = result.replace(word, "*")
            return result
        return inner_wrapper
    return outer_wrapper


@stop_words(["BMW", "pepsi"])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Dan"))