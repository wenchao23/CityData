from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

def cuboid_data2(o, size=(1,1,1), step = .5):
    X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],         
         [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
         [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
         [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
         [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
         [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
    X = np.array(X).astype(float)
    for i in range(3):
        X[:,:,i] *= size[i]
    X += np.array(o)

    point_ob =  np.array([[0, 0, 0],
            [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
                [0, 0.2, 0],
                [0, 0.4, 0],
                [0, 0.6, 0],
                [0, 0.8, 0],
                [0, 0.1, 0],
                [0, 0.3, 0],
                [0, 0.5, 0],
                [0, 0.7, 0],
                [1, 0.2, 0],
                [1, 0.4, 0],
                [1, 0.6, 0],
                [1, 0.8, 0],
                [1, 0.1, 0],
                [1, 0.3, 0],
                [1, 0.5, 0],
                [1, 0.6, 0],
                [0.2, 1, 1],
                [0.4, 1, 1],
                [0.6, 1, 1],
                [0.8, 1, 1],
                [0.1, 1, 1],
                [0.3, 1, 1],
                [0.5, 1, 1],
                [0.7, 1, 1],
                [0.2, 0, 1],
                [0.4, 0, 1],
                [0.6, 0, 1],
                [0.8, 0, 1],
                [0.1, 0, 1],
                [0.3, 0, 1],
                [0.5, 0, 1],
                [0.7, 0, 1]])* np.array([size[0],size[1],0]) + np.array(o)
    point_ob_top =  np.array([[0.2, 0.2, 1],
                [0.4, 0.4, 1],
                [0.6, 0.6, 1],
                [0.8, 0.8, 1],
                [0.2, 0.8, 1],
                [0.6, 0.4, 1],
                [0.4, 0.6, 1],
                [0.8, 0.2, 1],
                ])* np.array([size[0],size[1],size[2]]) + np.array(o)   
    obstacle = point_ob 
    start = 110
    stop = size[2]
    for i in np.arange(start = start, stop = stop, step = step):
        b = point_ob + np.array([0,0,i])
        obstacle = np.concatenate((obstacle,b), axis = 0)
    return X, obstacle

def plotCubeAt2(ax, positions,sizes=None,colors=None, **kwargs):
    if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
    if not isinstance(sizes,(list,np.ndarray)): sizes=[(1,1,1)]*len(positions)
    g = []
    for p,s,c in zip(positions,sizes,colors):
        X, obstacle = cuboid_data2(p, size=s)
    g.append( X )
    li = Line3DCollection(np.concatenate(g), colors='k', linewidths=0.4, linestyles=':')
    ax.add_collection3d(li)
    pc = 1
    return pc, obstacle 
    