def type_converter(type_of_output):

    def deco(func):

        def wrapper(*args, **kwargs):

            try:
                if (type_of_output == "str"):
                    return str(args)
                if (type_of_output == "int"):      
                    return int(args)
                if (type_of_output == "float"):
                    return float(args)
                
            except Exception:
                return f"Could not convert into {args}"
            
            return
        
        return wrapper
    return deco


@type_converter("str")
def return_int():
    return 5

@type_converter("int")
def return_string():
    return "Not a number"

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen