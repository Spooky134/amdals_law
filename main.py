from amdal import *
import matplotlib.pyplot as plt


def main():
    amdl_list = (AmdalN(1, 100, 1, 0.1),
                 AmdalA(0.1, 0.9, 0.1, 5),
                 AmdalNetworkN(1, 80, 1, 0.1, 0.1, 0.1),
                 AmdalNetworkA(1, 80, 1, 5, 0.1, 0.1),
                 AmdalNetworkCa(0.1, 0.9, 0.1, 5, 0.1, 0.1),
                 AmdalNetworkCt(0.1, 0.9, 0.1, 5, 0.1, 0.1))
    
    labels = ({'x_label': 'n', 'y_label': 'R'},
              {'x_label': 'a', 'y_label': 'R'},
              {'x_label': 'n', 'y_label': 'R'},
              {'x_label': 'a', 'y_label': 'R'},
              {'x_label': 'ca', 'y_label': 'R'},
              {'x_label': 'ct', 'y_label': 'R'})
    
    for i, amdl, label in zip(range(1, len(labels)+1), amdl_list, labels):
        res = amdl.evalute()

        plt.figure(i, figsize=(8, 4))
        plt.plot([point.x for point in res], [point.y for point in res], label=amdl.FORMULA)
        plt.title(f'Graph {amdl.NAME}')
        plt.xlabel(label["x_label"])
        plt.ylabel(label["y_label"]) 
        plt.grid(True)
        plt.legend()

    plt.show()


if __name__ == "__main__":
    main()