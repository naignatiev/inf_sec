# encoding: windows-1251
import codecs


def text2hex(s):
    return [codecs.encode(ch, 'windows-1251') for ch in s]


def hexs2pretty_hexs(s):
    a = []
    for ch in s:
        if ch == b'!':
            a.append('21')
        elif ch == b' ':
            a.append('20')
        elif ch == b'\x96':
            a.append('2d')
        elif ch == b',':
            a.append('2c')
        else:
            a.append(str(ch)[4:-1])
    return a


def hex2text(s):
    return ''.join([codecs.decode(ch, 'windows-1251') for ch in s])


def hex2int(ch):
    data = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    return data[ch[0]] * 16 + data[ch[1]]


def int2hex(n):
    data = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f'
    }
    return f'{data[int(n / 16)]}{data[n % 16]}'


def task1(text, code):
    code = [ch.lower() for ch in code]
    ans = []
    for k1, k2 in zip(hexs2pretty_hexs(text2hex(text)), code):
        ans.append(int2hex(hex2int(k1) ^ hex2int(k2)))
    return ans


def task2(text1, text2):
    ans = []
    for k1, k2 in zip(hexs2pretty_hexs(text2hex(text1)), hexs2pretty_hexs(text2hex(text2))):
        ans.append(int2hex(hex2int(k1) ^ hex2int(k2)))
    return ans


if __name__ == '__main__':
    print(task1('Штирлиц – Вы Герой!!',
                ['05', '0C', '17', '7F', '0E', '4E', '37', 'D2', '94', '10', '09', '2E', '22', '57', 'FF', 'C8',
                 '0B', 'B2', '70', '54']))
    print(task2('Штирлиц – Вы Герой!!', 'С Новым Годом, друзья!'))
