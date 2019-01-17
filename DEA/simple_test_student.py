import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydea

inputs = pd.DataFrame([
    [1, 94, 1],
    [2, 95, 20],
    [2, 94, 5],
    [3, 80, 3],
    [1, 93, 5],
    [2, 88, 3]
    ], columns=['Aptitude', 'Attendance Avg.', 'Pastoral Count'])

outputs = pd.DataFrame([
    [4.0, 94, 1540],
    [3.0, 90, 1408],
    [1.0, 20.0, 690],
    [1.4, -10.0, 674],
    [2.0, 70.0, 674],
    [2.9, -5.0, 1686]], columns=['GPA', 'NAPLAN', 'Work Practices'])

env_vars = pd.DataFrame([
    [  5.15262633e+00,   5.25431862e+03],
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

'''
myresults['Efficiency'].hist(bins=50)
plt.ylabel('Frequency')
plt.xlabel('Efficiency score')
plt.title('Distribution of efficiency scores')

'''
