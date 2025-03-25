# Pandas_05

# 184. Department Highest Salary_Solution_Q1

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    salaryDict={}
    for i in range(len(employee)):
        salary = employee['salary'][i]
        d_id = employee['departmentId'][i]
        if d_id in salaryDict:
            if salary > salaryDict[d_id]:
                salaryDict[d_id]= salary
        else:
            salaryDict[d_id] = salary

    deptDict = {}
    for i in range(len(department)):
        name = department['name'][i]
        d_id = department['id'][i]
        deptDict[d_id]= name

    result =[]
    for i in range(len(employee)):
        salary = employee['salary'][i]
        d_id = employee['departmentId'][i]
        name = employee['name'][i]
        if salary == salaryDict[d_id]:
            result.append([d_id, name, salary])
    
    for element in result:
        d_id = element[0]
        element[0] = deptDict[d_id]

    return pd.DataFrame(result, columns = ['Department', 'Employee', 'Salary'])

#Alternative1

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df= employee.merge(department, left_on= 'departmentId', right_on ='id', how='inner')
    max_salary = df.groupby('departmentId')['salary'].transform('max')
    df= df[df['salary'] == max_salary]
    return df[['name_y', 'name_x', 'salary']].rename(columns = {'name_y': 'Department', 'name_x': 'Employee'})

______________________________________________________________________________________________________________________________________

# 178. Rank Scores_Solution_Q2

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values('score', ascending=False)

#Alternative1

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    allScore=[]

    for i in range(len(scores)):
        s= scores['score'][i]
        allScore.append(s)
    allScore.sort(reverse= True)
    if(len(allScore)) ==0:
        return pd.DataFrame([], columns= ['score', 'rank'])
    result=[]
    rnk=1
    result.append([allScore[0],1])
    for i in range(1, len(allScore)):
        if allScore[i] != allScore[i-1]:
            rnk= rnk+1
        result.append([allScore[i], rnk])
    return pd.DataFrame(result, columns= ['score', 'rank'])

______________________________________________________________________________________________________________________________________


    