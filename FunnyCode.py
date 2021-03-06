def simuLat(dd,cc,Beta,Delta):
    """
    input:
        dd is the lattice dimension,
        cc is the lattice constant,
        Beta is the lattice rotation angle in radians
        Delta is the initial phase;
    output: simulated 2D topo
    can test: simuLat(500,1,0.1,0.2)
    """
    lattice=[[math.cos(cc/(2*3.1415)*(x*math.cos(Beta)-y*math.sin(Beta))+Delta*3.14)+math.cos(cc/(2*3.14)*(y*math.cos(Beta)+x*math.sin(Beta))) for x in range(dd)] for y in range(dd)]
    HH=np.array(lattice)
    plt.imshow(HH)
    plt.show()
    return
