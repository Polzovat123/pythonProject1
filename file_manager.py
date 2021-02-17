import csv
from read_config import get_time

def write_first_data(l_1, l_2, l_3, l_4):
    with open('database/data.csv', 'a', encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerows([(l_1[i], l_2[i], l_3[i], l_4[i]) for i in range(len(l_1))])
    print('All data has been successfully written to the file')
    clear_array(l_1, l_2, l_3, l_4)
    print('working buffer cleared')

def clear_array(l_1, l_2, l_3, l_4):
    l_1.clear()
    l_2.clear()
    l_3.clear()
    l_4.clear()



