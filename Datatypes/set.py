"""set1 = {"sunday","monday","wednesday","thursday","friday","saturday",}
print("Set of days: ",set1)
set1.add("wedney")
print("Set of days: ",set1)
set2 = {1,2,3,4,5,6,7,8,}
print("Set of days: ",set2)
set2.add(9)
print("Set of days: ",set2)

set1.update(["Saturday"])
print("Set of days: ",set1)
set1.remove("saturday")
print("Set of days: ",set1)

set1.remove("wedney")
print("Set of days: ",set1)

set1.discard("monday")
print("Set of days: ",set1)
"""

set3 = {"alwin","alwi","alw","al"}
set4 = {"bala","mala","alw","al"}
print(set3)
print(set4)
#union

x = set4|set3
print("Union operation using pipe operator: ",x)
print("Union operation using union operator: ",set3.union(set4))
#Intersection
print("Intersection operation using intersection operator: ",set3.intersection(set4))
print("Intersection operation using intersection operator: ",set3&set4)
#Difference
print("Difference operation using difference operator: ",set3.difference(set4))
print("Difference operation using difference operator: ",set3-set4)

#symmetric Difference
print("Symmetric difference using symmetric operator: ",set3.symmetric_difference(set4))
print("Symmetric difference using symmetric operator: ",set3^set4)