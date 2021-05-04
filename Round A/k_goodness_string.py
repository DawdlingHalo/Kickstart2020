num_case = int(input("Number of test cases:"))

#empty list
l = [] 

for i in range(num_case):
  # adding required inputs for each test case
  s_len = int(input("Enter string length:"))
  exp_k = int(input("Enter expected k:"))
  s = input("Enter string:")
  
  obs_k = 0 # initalized observed k as 0

  # for loop below is implemented for every string 
  for j in range(int(s_len/2)):
    if s[j] is not s[s_len-(j+1)]:
      obs_k+=1
  if obs_k < exp_k:
    l.append(exp_k-obs_k)
  elif exp_k < obs_k:
    l.append(exp_k-obs_k)
  else :
    l.append(0)  

for i in range(len(l)):
  print(f"Case #{i}: {l[i]}\n")