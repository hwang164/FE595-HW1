import numpy as np
import matplotlib.pyplot as plt

def main():
    x=np.linspace(0,2*np.pi,1024)
    s=np.sin(x)
    c=np.cos(x)
    plt.plot(x,s,label="sin")
    plt.plot(x,c,label="cos")

    tan_x = np.linspace(0, 2 * np.pi)
    tan_y = np.tan(tan_x)
    max_index = tan_y.argmax()
    min_idex = tan_y.argmin()

    tan_x[max_index] = np.nan
    tan_x[min_idex] = np.nan
    tan_y[max_index] = np.nan
    tan_y[min_idex] = np.nan
    plt.plot(tan_x, tan_y, color="red", label="tan")
    
    plt.ylim(-1, 1)
    plt.legend()
    plt.axhline(y=0.0, color='black')
    plt.show()


if __name__=="__main__":
    main()
