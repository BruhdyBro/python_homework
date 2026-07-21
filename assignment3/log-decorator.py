import logging

def logger_decorator (func):
    def wrapper(*args, **kwargs):
        
        logger = logging.getLogger(f"{func.__name__}_parameter_log")
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.FileHandler("./decorator.log","a"))

        logger.log(logging.INFO, (f"function: {func.__name__}"))
        if (args):
            logger.log(logging.INFO, (f"Positional paramaters: {args}"))
        else:
            logger.log(logging.INFO, ("positional paramaters: none"))

        if (kwargs):
            logger.log(logging.INFO, (f"keyword paramaters: {kwargs}"))
        else:
            logger.log(logging.INFO, ("keyword paramaters: none"))

        logger.log(logging.INFO, (f"return: {func(*args, **kwargs)}"))
        logger.log(logging.INFO, (f""))
        return 
    
    return wrapper


@logger_decorator
def greeting():
    print("Hello, World!")

@logger_decorator
def var_args(*args):

    i = 0
    for arg in args:
        i += 1

    return True

@logger_decorator
def var_kwargs(**kwargs):
    i = 0
    for key, arg in kwargs.items():
        i += 1

    return logger_decorator(var_kwargs)


greeting()
var_args("banana", "start", "true", "Testing")
var_kwargs(name="bruhdy", age=22, one="more" + " time")