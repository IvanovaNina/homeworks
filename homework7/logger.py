from datetime import datetime as dt

path = 'log.txt'


def info(first, second, oper, res):
    log = f'{dt.now()} | {first} {oper} {second} = {res}\n'
    print(log)
    with open(path, 'a') as data:
        data.write(log)
