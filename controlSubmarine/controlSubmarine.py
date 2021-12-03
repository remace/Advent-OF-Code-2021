""" day 2: driving the submarine """

from Mixins.mixins import read_file

class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return(f"({self.x} ; {self.y})")

    def go_up(self, x: int):
        self.y-=x
    
    def go_down(self, x: int):
        self.y+=x

    def go_forward(self, x: int):
        self.x += x


def main():
    dataset = read_file("./controlSubmarine/dataset1.csv")
    sub = Submarine()
    with open("./controlSubmarine/answer1.csv","w") as f:
        for line in dataset:
            line = line.split(' ')
            if line[0] == 'forward':
                sub.go_forward(int(line[1]))
            elif line[0] == 'down':
                sub.go_down(int(line[1]))
            elif line[0] == 'up':
                sub.go_up(int(line[1]))
            else:
                print('ERROR')
            f.write(f'actualisation: {line[0]} -> {line[1]}\tnouvelle position: {sub}\n')
        f.write(f'dernière position: {sub} réponse au problème: {sub.x * sub.y}')
    return sub.x * sub.y


class SubmarineAim(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def __str__(self):
        return(f"({self.x} ; {self.y}; {self.aim})")

    def go_up(self, x: int):
        self.aim-=x
    
    def go_down(self, x: int):
        self.aim+=x

    def go_forward(self, x: int):
        self.x += x
        self.y += x * self.aim

def main2():
    dataset = read_file("./controlSubmarine/dataset1.csv")
    sub = SubmarineAim()

    with open("./controlSubmarine/answer2.csv","w") as f:
        for line in dataset:
            line = line.split(' ')
            if line[0] == 'forward':
                sub.go_forward(int(line[1]))
            elif line[0] == 'down':
                sub.go_down(int(line[1]))
            elif line[0] == 'up':
                sub.go_up(int(line[1]))
            else:
                print('ERROR')
            f.write(f'actualisation: {line[0]} -> {line[1]} {sub.aim}\tnouvelle position: {sub}\n')
        f.write(f'\ndernière position: {sub} réponse au problème: {sub.x * sub.y}')
    return sub.x * sub.y
