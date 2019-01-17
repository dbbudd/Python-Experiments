import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydea

inputs = pd.DataFrame([[100, 70], [120, 123], [50, 20], [67, 17], [98, 20], [76, 12]], columns=['Teaching staff', 'Research staff'])
outputs = pd.DataFrame([[1540, 154, 59], [1408, 186, 23 ], [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]], columns=['Undergraduates', 'Masters', 'Publications'])
env_vars = pd.DataFrame([[  5.15262633e+00,   5.25431862e+03],
       [  8.62019738e+00,   1.10390901e+04],
       [  3.95821220e+00,   5.88356035e+03],
       [  9.21476691e+00,   1.54834181e+03],
       [  2.96674662e-01,   1.40433297e+04],
       [  1.41538397e+01,   3.75047428e+03]], columns=['Funding', 'City_size'])

uni_prob = pydea.DEAProblem(inputs, outputs, returns="CRS")
myresults = uni_prob.solve()

print(myresults['Status'])

print(myresults['Efficiency'])

print(myresults['Weights'])

myresults['Efficiency'].hist(bins=50)
plt.ylabel('Frequency')
plt.xlabel('Efficiency score')
plt.title('Distribution of efficiency scores')

