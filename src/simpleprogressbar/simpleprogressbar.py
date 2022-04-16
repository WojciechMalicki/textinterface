class progressBar():
    def __init__(self, width:int = 20, char:str = '#', spc:str = '-') -> None:
        self.PERCENT_LENGTH = 5
        self.width = int(width) - self.PERCENT_LENGTH
        self.char = char[0]
        self.spc = spc[0]

    def next(self, progress:float = 0) -> str:
        percent = str(int(progress*100)) + '%'
        percent = (self.PERCENT_LENGTH - 2 - len(percent)) * ' ' + percent
        bar = f'{{{percent}}}'\
              f'[{int(progress * self.width) * self.char}'\
              f'{(self.width - int(progress * self.width)) * self.spc}]'
        print(bar, end = '\r')

    def end(self):
        self.next(1)

