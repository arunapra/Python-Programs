def outer_decorator(args):
    def inner_decorator(func):
        def wrapped(ag):
            return func(ag)+args
        return wrapped
    return inner_decorator

args = ["Hello", "Good Morning", "Bye,Bye"]

for diff in args:
    @outer_decorator(diff)
    def my_greeting(ag):
        return "John Says "+ag

    print(my_greeting(","))
    
