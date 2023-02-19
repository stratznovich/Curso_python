import datetime
def convert(s):
    return str(datetime.timedelta(hours = s ))
s = int(input('insira o valor em segundos: '))
print(convert(s))

