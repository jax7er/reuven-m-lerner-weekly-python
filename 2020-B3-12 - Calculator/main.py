from cmd import Cmd
from operator import sub, mul, truediv
from functools import reduce

class Calculator(Cmd):
    prompt = "(calc) "

    def _parse(self, arg: str):
        return (int(s) for s in arg.split() if s.isnumeric())

    def precmd(self, line: str) -> str:
        args = line.split()

        args[0] = {"+": "add", "-": "sub", "*": "mul", "/": "div"}.get(args[0], args[0])

        return " ".join(args)

    def do_add(self, arg: str):
        print(sum(self._parse(arg)))

    def do_sub(self, arg: str):
        print(reduce(sub, self._parse(arg)))

    def do_mul(self, arg: str):
        print(reduce(mul, self._parse(arg)))

    def do_div(self, arg: str):
        print(reduce(truediv, self._parse(arg)))

Calculator().cmdloop()