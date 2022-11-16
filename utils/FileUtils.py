import os
from utils import References


def save_grid(path: str, grid: list[list[str]]) -> None:
    file = open(path, "w")
    string = ""
    for line in grid:
        print("a")
        print(len(line))
        for i, char in enumerate(line):
            print(i)
            if i + 1 < len(line):
                string += char + " "
            else:
                string += char
        string += "\n"
    file.write(string[:-1])
    file.close()


def read_grid(path) -> list[list[str]]:
    file = open(path, 'r')
    matrice = []
    for line in file.readlines():
        matrice.append(line.replace("\n", "").split(" "))
    file.close()
    return matrice


def load_blocks() -> dict[str, list[dict[str, str | list[list[str]]]]]:
    dictionary: dict[str, list[dict[str, str | list[list[str]]]]] = {}
    for dir_ in os.listdir(References.base_path + "\\resources\\blocks"):
        blocks = []
        for file in os.listdir(References.base_path + "\\resources\\blocks\\" + dir_):
            opened_file = open(References.base_path + "\\resources\\blocks\\" + dir_ + "\\" + file, "r")
            matrice = []
            for line in opened_file.readlines():
                l_matrice = []
                for char in line:
                    if char != " " and char != "\n":
                        l_matrice.append(char)
                matrice.append(l_matrice)
            block = {"name": file[:-4], "matrice": matrice}
            blocks.append(block)
        dictionary[dir_] = blocks
    return dictionary


def file_exists(path) -> bool:
    return os.path.exists(path)
