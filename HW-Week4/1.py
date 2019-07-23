edges = [[0,1],[0,2],[1,3],[2,4],[3,5],[4,5],
         [0,6],[1,9],[2,10],[2,14],[3,13],[3,17],[4,18],[5,21],
         [6,7],[6,10],[7,8],[8,9],[9,13],
         [10,11],[11,12],[11,15],[12,13],[12,16],
         [14,15],[14,18],[15,16],[16,17],[17,21],
         [18,19],[19,20],[20,21]]

n = 22

x = np.array(np.zeros(n))
y = np.array(np.zeros(n))

alpha = 360/22

x[0] = 1
y[0] = 0

for idx in range(22):
  d = alpha * idx
  if(d < 90):
    x[idx] = 1 * np.cos(d * np.pi / 180)
    y[idx] = 1 * np.sin(d * np.pi / 180)
  elif d == 180:
    x[idx] = -1
    y[idx] = 0
  elif d <180:
    d = d - 90
    x[idx] = -1 * np.sin(d * np.pi / 180)
    y[idx] = 1 * np.cos(d * np.pi / 180)
  elif d <270:
    d = d - 180
    x[idx] = -1 * np.cos(d * np.pi / 180)
    y[idx] = -1 * np.sin(d * np.pi / 180)
  else:
    d = d - 270
    x[idx] = 1 * np.sin(d * np.pi / 180)
    y[idx] = -1 * np.cos(d * np.pi / 180)
  

# insert code here to
# compute positions
# in arrays x and y
# for vertex locations
# for a radial layout
# of the graph edges

drawgraph(x,y,edges)

