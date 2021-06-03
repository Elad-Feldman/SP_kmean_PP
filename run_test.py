import os

def print_tests():
    c1 = "python kmeans_pp.py 3 333 input_1_db_1.txt input_1_db_2.txt"
    c2 = "python kmeans_pp.py 7 200 input_2_db_1.txt input_2_db_2.txt"
    c3 = "python kmeans_pp.py 15 750 input_3_db_1.txt input_3_db_2.txt"
    c4 = "python kmeans_pp.py 15  input_3_db_1.txt input_3_db_1.txt"
    c5 = "python kmeans_pp.py 15.2  206  input_1_db_1.txt input_1_db_2.txt"
    c6 = "python kmeans_pp.py 3 333.6 input_1_db_1.txt input_1_db_2.txt"
    c7 = "python kmeans_pp.py -3 50 input_1_db_1.txt input_1_db_2.txt"
    c8 = "python kmeans_pp.py 3 50 input_1_db_1.txt input_2_db_2.txt"
    CC = [c1,c2,c3,c4,c5,c6,c7,c8]

    for i,c in enumerate(CC):
        print(f"=================c{i+1}======================")
        os.system(c)
        print("=======================================")

print_tests()