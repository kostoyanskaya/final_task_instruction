# Номер успешной посылки: 112863724.
def decipher_instruction(instruction: str) -> str:
    """Расшифровывает сжатые сообщения."""
    storage = []
    result = ''
    line = ''

    for detail in instruction:

        if detail.isdigit():
            line += detail
        elif detail == '[':
            storage.append((result, line))
            result, line = '', ''
        elif detail == ']':
            detail, line = storage.pop()
            result *= int(line)
            result = detail + result
            line = ''
        else:
            result += detail

    return result


if __name__ == '__main__':
    print(decipher_instruction(instruction=input()))
