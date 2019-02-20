
def callable_func(obj):
    method_list = [method for method in dir(obj)
                    if callable(getattr(obj, method))]
    return method_list


def func_doc(obj):
    method_list = callable_func(obj)
    method_document = [{method: str(getattr(obj, method).__doc__)}
                        for method in method_list]
    return method_document


for info in func_doc(object):
    print(info)
