num_case = int(input()) # number of test cases

for i in range(num_case):
  s_len ,exp_k = map(int,input().split()) # length of string and K goodness score expected
  s = input() # string
  
  obs_k = 0 # initalized observed k as 0

  # for loop below is implemented for every string 
  for j in range(int(s_len/2)):
    if s[j] is not s[s_len-(j+1)]:
      obs_k+=1
  print(f"Case #{i+1}: {abs(exp_k-obs_k)}\n")