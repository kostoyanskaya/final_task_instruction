# Номер успешной посылки: 112983428.
def decipher_instruction(instruction: str) -> str:
    """Расшифровывает сжатые сообщения."""
    storage: list[tuple[str, str]] = []
    result = ''
    line = ''

    for detail in instruction:

        if detail.isdigit():
            line += detail
        elif detail == '[':
            storage.append((result, line))
            result, line = '', ''
        elif detail == ']':
            saved_result, saved_line = storage.pop()
            result *= int(saved_line)
            result = saved_result + result
            line = ''
        else:
            result += detail

    return result


if __name__ == '__main__':
    print(decipher_instruction(instruction=input()))
