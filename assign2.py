#main function
# n is the number of vertices
# weights is a list of their weights, v_1, ..., v_n
def mwis (n, weights):
    #
    #FILL IN CODE HERE
    #
   # print weights
    opt = [0, weights[0]];
    
    vert = [set(), set([0])] 

   
    for i in range (2, n):
		vert.append(set())
		#print "comparing " + str(opt[i- 1]) + " and " + str(opt[i-2]) + " + " + str(weights[i-1])
		if (opt[i - 1] > (opt[i -2] + weights[i-1])): #don't include vi
			opt.append(opt[i-1])
			vert[i] = vert[i -1]
		else:#include vi
			#print "chose " + str(weights[i-1])
			opt.append(opt[i-2]+ weights[i-1])
			vert[i] = vert[i-2].union(set([i-1]))
    #check last element
    last = weights[len(weights) - 1] + opt[n - 2];
    if (last > opt[len(opt) -1]):
    	opt.append(last)
        vert[len(weights) - 1] = vert[len(weights) -2].union(set([len(weights) -1]))#included
    else:#not included, vertices don't update
    	opt.append(opt[len(opt) - 1])
        vert[len(weights) -1] = vert[len(weights) -2]
    sol_items = [1]
    return (opt[1:], max(opt), sorted(vert[len(weights) -1]))

#TODO to get indices
  
  
#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE    

#Read input
f = open("input.txt", "r")
weights = [int(x) for x in f.readline().split()] 
n = len (weights)

#call mwis
(opt, sol_tot_weight, sol_items) = mwis(n, weights)

#output solution
print ' '.join(map(str, opt))
print sol_tot_weight
print ' '.join(map(str, sol_items))
