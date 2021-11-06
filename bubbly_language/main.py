import re
from collections import deque
import logging


def add(stack: deque[int or float]) -> int or float:
    assert len(stack) > 1
    sum = stack.pop() + stack.pop()
    stack.appendleft(sum)
    return sum


def sub(stack: deque[int or float]) -> int or float:
    assert len(stack) > 1
    diff = stack.pop() - stack.pop()
    stack.appendleft(diff)
    return diff


def mul(stack: deque[int or float]) -> int or float:
    assert len(stack) > 1
    prod = stack.pop() * stack.pop()
    stack.appendleft(prod)
    return prod


def div(stack: deque[int or float]) -> float:
    assert len(stack) > 1
    dividend, divisor = stack.pop(), stack.pop()
    assert divisor != 0
    quot = dividend / divisor
    stack.appendleft(quot)
    return quot


def _is_num_else_str(s: str) -> str or int or float:
    ''' unsafe for outside of module use '''
    if s.isdigit():
        return int(s)
    elif str(s).replace('.', '', 1).isdigit():
        return float(s)
    else:
        return s


def scanner(pattern: re.Pattern, input_text: str) -> list[str or int or float]:
    dirty_tokens: list[str] = [next(filter(bool, local))
                               for local in pattern.findall(input_text)]
    scrubbed_tokens = [tok.strip('()') for tok in dirty_tokens]
    clean_tokens = [_is_num_else_str(tok) for tok in scrubbed_tokens]

    # simple way to check if tokens are valid
    assert ''.join(dirty_tokens) == input_text
    assert (clean_tokens[0], clean_tokens[-1]) == ('start', 'end')
    return clean_tokens


def execute(tokens: list[str or int or float]) -> int or float:
    value_stack = deque()
    operation_queue = deque()
    ops_swither = {'add': add, 'sub': sub, 'mul': mul, 'div': div}

    # parsing
    i = 0
    while i < len(tokens):
        match tokens[i]:
            case "push":
                value_stack.appendleft(tokens[i+1])
                i += 1
            case 'pop':
                value_stack.pop(tokens[i+1])
                i += 1
            case 'start':
                pass
            case 'end':
                break
            case 'add' | 'sub' | 'mul' | 'div':
                operation_queue.appendleft(ops_swither[tokens[i]])
        i += 1

    # execution
    for op in operation_queue:
        op(value_stack)
    return value_stack.pop()


def main():
    logging.basicConfig(
        format='%(levelname)s - %(asctime)s - %(message)s',
        datefmt="%H:%M:%S",
        level=logging.DEBUG)

    pattern = re.compile(
        r"(\(start\))|"
        r"(\(push\))|"
        r"(\(add\))|"
        r"(\(sub\))|"
        r"(\(mul\))|"
        r"(\(div\))|"
        r"(\([0-9]+(.)??[0-9]*\))|"
        r"(\(pop\))|"
        r"(\(end\))")

    input_text = "(start)(push)(5)(push)(8)(push)(1)(add)(add)(end)"
    # being lexing
    logging.debug("Lexing...")
    tokens = scanner(pattern, input_text)
    print(tokens)

    # being parse-execution
    logging.debug("executing...")
    print(execute(tokens))


if __name__ == "__main__":
    main()
