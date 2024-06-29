unlist=[1,3,4,10,5,7,0]
print("Original list",unlist)
reverse=list(reversed(unlist))
print("Reversed list:",reverse)
ascendinglist=sorted(unlist)
print("ascending list:",ascendinglist)
descendinglist=sorted(unlist,reverse=True)
print("descending ordered list:",descendinglist)
