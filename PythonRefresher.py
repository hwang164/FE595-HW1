import numpy as np
import matplotlib.pyplot as plt

def main():
    x=np.linspace(0,2*np.pi,1024)
    s=np.sin(x)
    c=np.cos(x)
    plt.plot(x,s)
    plt.plot(x,c)
    plt.legend()
    plt.show()


if __name__=="__main__":
    main()
