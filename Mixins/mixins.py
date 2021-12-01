

def read_file(path):
    dataset = []
    with open(path, "r") as f :
        next_line = f.readline()
        while not next_line == '':
            dataset.append(next_line.rstrip("\n"))
            next_line = f.readline()
    return(dataset)