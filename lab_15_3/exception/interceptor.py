def exception_interceptor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 200
        except Exception as e:
            return str(e), 400 if isinstance(e, ValueError) else 500

    return wrapper
