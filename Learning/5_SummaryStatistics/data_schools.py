import numpy as np

a = np.random.normal(1400, 200, 1000)
school_one = [x for x in a if x <= 1600]

b = np.random.normal(1000, 300, 1000)
school_two = [x for x in b if x <= 1600]

c = np.random.normal(800, 500, 1000)
school_three = [x for x in c if x <= 1600 and x >=200]