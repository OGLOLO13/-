grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2 = list(students)
students2.sort(reverse=False)
A,B,J,K,S = grades
A1=sum(A)/len(A)
B1=sum(B)/len(B)
J1=sum(J)/len(J)
K1=sum(K)/len(K)
S1=sum(S)/len(S)
AVG=[A1,B1,J1,K1,S1]
gradeavg = {k: v for k, v in zip(students2,AVG)}
print(gradeavg)
print(gradeavg['Steve'])


















