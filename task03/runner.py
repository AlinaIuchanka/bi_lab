# The input examples:
# runner("fizzbuzz", "generate_numbers")
# runner("fizzbuzz", "generate_numbers(8)")
# runner("fizzbuzz()", "generate_numbers(8)")
# runner("generate_numbers()")
# etc.

# Or from command line:
# python runner.py fizzbuzz generate_numbers(8)
# etc.
import pytasks
import sys


def runner(*args):
    arg_def_all = dir(pytasks)
    arg_def = []
    for func in arg_def_all:
        if func[: 2] != "__":
            arg_def.append(func)
    if not args:
        args = arg_def

    for func_name in args:
        left_bracket = func_name.find("(")
        if left_bracket != -1:
            argument = func_name[left_bracket + 1:-1]
            func_call = func_name[: left_bracket]
            if func_call in arg_def:
                if argument:
                    print(func_call, getattr(pytasks, func_call)(argument))
                else:
                    print(func_call, getattr(pytasks, func_call)())
        else:
            if func_name in arg_def:
                print(func_name, getattr(pytasks, func_name)())
    return


if __name__ == "__main__":
    func_args = sys.argv[1:]
    if not func_args:
        runner()
    else:
        runner(*func_args)
