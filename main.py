from amdal import *
import matplotlib.pyplot as plt


def main():
    amdl_list = ((AmdalN(1, 100, 1, 0.1), {'x_label': 'n', 'y_label': 'R'}),
                 (AmdalA(0.1, 0.9, 0.1, 5), {'x_label': 'a', 'y_label': 'R'}),
                 (AmdalNetworkN(1, 80, 1, 0.1, 0.1, 0.1), {'x_label': 'n', 'y_label': 'R'}),
                 (AmdalNetworkA(1, 80, 1, 5, 0.1, 0.1), {'x_label': 'a', 'y_label': 'R'}),
                 (AmdalNetworkCa(0.1, 0.9, 0.1, 5, 0.1, 0.1), {'x_label': 'ca', 'y_label': 'R'}),
                 (AmdalNetworkCt(0.1, 0.9, 0.1, 5, 0.1, 0.1), {'x_label': 'ct', 'y_label': 'R'}),)
    
    for i, amdl in enumerate(amdl_list):
        res = amdl[0].evalute()

        plt.figure(i, figsize=(8, 4))
        plt.plot([el.x for el in res], [el.y for el in res], label=amdl[0].FORMULA)
        plt.title(f'Graph {amdl[0].NAME}')
        plt.xlabel(amdl[1]["x_label"])
        plt.ylabel(amdl[1]["y_label"]) 
        plt.grid(True)
        plt.legend()

    plt.show()


if __name__ == "__main__":
    main()