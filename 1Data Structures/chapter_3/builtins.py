Errors = []
Warnings = []
Exceptions = []
built_in_functions = []

for key, value in __builtins__.__dict__.items():
    if 'error' in key.lower():
        Errors.append([key, value])
    elif 'warn' in key.lower():
        Warnings.append([key, value])
    elif 'exception' in key.lower():
        Exceptions.append([key, value])
    elif 'built' in str(value).lower():
        built_in_functions.append([key, value])
    else:
        print(key, value)

print(len(Errors), Errors)
print(len(Warnings), Warnings)
print(len(Exceptions), Exceptions)
print(len(built_in_functions), built_in_functions)
