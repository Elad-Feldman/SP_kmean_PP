import mykmeanssp
import numpy as np
import time
# To use this run in the terminal: python setup.py build_ext --inplace
# And on Nova: python3.8.5 setup.py build_ext --inplace
# os.system("python setup.py build_ext --inplace")

def test_3_caes():

    data=[0]*3
    data[0] = (15,"input_3.txt")
    data[1] = (3,"input_1.txt")
    data[2] = (7,"input_2.txt")
    for row in data:
        t0 = time.process_time()
        print(row)
        test_hw1_data(row)
        t1 = time.process_time() - t0
        print("Time elapsed: ", t1)

def test_hw1_data( test_data):
    k =test_data[0]
    filename = test_data[1]

    np.set_printoptions(suppress=True, linewidth=15*k)
    observations = []
    clusters = []
    indexs = []

    with open(filename, "r") as txt_file:
      txt =  txt_file.readlines()

    txt_file.close()
    for line in txt:
        line = line[:-1].split(",")
        line = [float(i) for i in line]
        observations.append(line)

    for j,dot in enumerate(observations):
        clusters.append(dot)
        indexs.append(j)
        if j+1==k:
            break

    max_iter= 200
    #print(dots)

    clusters = np.array(mykmeanssp.fit(max_iter, observations, clusters, indexs))
    clusters = np.round(clusters,4)
    print(clusters)



test_3_caes()