## Task 1
minutes_in_week = 60*24*7

## Task 2
remainder_without_mod = 2304811 - 2304811//47 * 47	# don't actually need the //

## Task 3
divisible_by_3 = (673+909)%3 is 0

## Task 4
x = -9
y = 1/2
statement_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## Task 5
first_five_squares = { num_five**2 for num_five in {1,2,3,4,5} }

## Task 6
first_five_pows_two = { 2**num_six for num_six in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = { 3, 4, 5 }
Y1 = { 5, 6, 7 }

## Task 8: enter in the two new sets
X2 = { 0, 1, 2 }
Y2 = { 3, 6, 12 }

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = { huns*(base**2) + tens*base + ones for huns in digits for tens in digits for ones in digits }

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { x for x in S for y in T if x is y }

## Task 11
L_average = sum([20,10,15,75])/len([20,10,15,75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(sets) for sets in LofL]) # use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [ [letter,num] for letter in {'A','B','C'} for num in {1,2,3} ] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [ (x,y,z) for x in S for y in S for z in S if x+y+z is 0 ] 

## Task 15
exclude_zero_list = [ (x,y,z) for x in S for y in S for z in S if (sum([x,y,z]) == 0) and ([x,y,z] != [0,0,0]) ]

## Task 16
first_of_tuples_list = [ (x,y,z) for x in S for y in S for z in S if (sum([x,y,z]) == 0) and ([x,y,z] != [0,0,0]) ][0]

## Task 17
L1 = [ 1,1,1 ] # <-- want len(L1) != len(list(set(L1)))
L2 = [ 1,3,2 ] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {odd for odd in range(100) if odd%2 is 1}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [ x+y for (x,y) in zip([10,25,40],[1,15,20]) ]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [ dlist[j][k] for j in range(len(dlist)) ]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [ dlist[j][k] if k in dlist[j] else "NOT PRESENT" for j in range(len(dlist)) ] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [ dlist[j][k] if k in dlist[j] else "NOT PRESENT" for j in range(len(dlist)) ] # <-- as you do here

## Task 23
square_dict = { x:x**2 for x in range(100) }

## Task 24
D = {'red','white','blue'}
identity_dict = { d:d for d in D }

## Task 25
base = 10
digits = set(range(10))
representation_dict = { hun*(base)**2+ten*base+one:[hun,ten,one] for hun in digits for ten in digits for one in digits}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { names[i]:d[i] for i in range(len(names)) if i in d }

## Task 27
def nextInts(L): return [ x+1 for x in L ]

## Task 28
def cubes(L): return [ x**3 for x in L ] 

## Task 29
def dict2list(dct, keylist): return [ dct[keylist[x]] for x in range(len(keylist)) ]

## Task 30 
def list2dict(L, keylist): return { keylist[x]:L[x] for x in range(len(L)) } 

