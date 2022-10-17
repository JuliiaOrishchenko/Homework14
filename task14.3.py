def arg_rules(type_: type, max_length: int, contains: list):
    def outer_wrapper(func):
        func
        def inner_wrapper(name):
            if not isinstance(name, str):
                return False, f"Name type should be {type_}"
            if len(name) > max_length:
                return False, f"Max len cannot be greater than {max_length}"
            for item in contains:
                if item not in name:
                    return False, "Invalid name"
            return func(name)
        return inner_wrapper
    return outer_wrapper


@arg_rules(str, 15, ['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('S@SH05'))
