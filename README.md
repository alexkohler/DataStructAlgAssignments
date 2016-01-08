#Assignment 1 - Binary Search
Implement Binary Search

Input: The input is given in a file called input.txt. It contains a list of white-space delimited integers. The first integer is the target, while the rest is a list of values, sorted in non-descending order.

Output: The location of the target in the values list (using a 0-based offset). If the target is not in the list, return -1

Additional Requirements: The program should specifically implement binary search, as opposed to another algorithm. You can assume that the input is given according to specifications (e.g. sorted), so you do not need to implement error checking of the input. 

Example 1:
Input: 3 -10 -7 3 5 10 11 13
Output: 2
Explanation: The target is 3. The values list is 10 -7 3 5 10 11 13. The target is present in the third number. The 0-based offset is 2.

Example 2:
Input: -3 -10 -7 3 5 10 11
Output: -1
Explanation: The target is -3 .The values list is -10 -7 3 5 10 11. The target is not present in the values list, so the output is -1.


-----

#Assignment 2 - Dynamic Programming
Implement Dynamic Programming Algorithm for Independent Set (IS) on a Line Graph

This problem is exactly the one discussed in lecture on 09/25. You are given a graph on n vertices, where the vertices are connected together in a line. Each vertex has a weight. These weights are specified by v_1,v_2, ..., v_n. An independent set (IS) is a subset of the vertices such that no two vertices in the set have an edge between them. The weight of an IS is the sum of the weights of the vertices in the set. The problem is to find a maximum weight IS in the graph.

Recall from the recitation that the dynamic programming recurrence for the problem is given as follows:
OPT(i) = max( v_i + OPT(i - 2), OPT(i - 1) ) 

In this problem, your goal is to implement a bottom-up dynamic programming algorithm, based on the above recurrence. Starter code is provided.

Input: The input is given in a file called input.txt. It contains a list of white-space delimited integers. This list corresponds to the weights of the problem: v_1, ..., v_n. 

Output: Your output must contain three lines. The first line should contain a list of white-space delimited integers. These integers should correspond to the values OPT(1), OPT(2), ..., OPT(n), in that order. The second line should contain a single integer, which is the the maximum weight of an IS. The third line should contain a list of white-space delimited integers, sorted in increasing order. This line corresponds to the indices of a maximum weight IS, using a 0-based offset. In the case there is more than one maximum weight IS, you can output an arbitrary one.


Example :
Input: 8 3 7 10 4
Output: 
8 8 15 18 19
19
0 2 4


-----

#Assignment 3 - Min-Gap data structure
Many of the data structures we have seen in class support "dynamic set" operations. In these structures, you maintain a set of numbers Q and support efficient INSERT, DELETE, and SEARCH operations. In this assignment, you need to create a data structure to support the dynamic set operations and, in addition, the MIN-GAP operation. The MIN-GAP of the set Q returns the difference of the two closest numbers in Q. For example, if Q = {1, 5, 9, 15, 18, 22}, then MIN-GAP(Q) returns 3, since 15 and 18 are two closest numbers in Q and their difference is 3. 

To create the data structure, you need augment a regular binary search tree (BST). Note that in the real world, you would want to augment a Red Black tree, but for the ease of the assignment, we will use a BST instead. Your data structure must support the INSERT, DELETE, and SEARCH operations in the same time as for a regular BST. The MIN-GAP operation should be supported in O(1) time.

You can support the MIN-GAP operation in constant time by adding attributes "mingap", "minval", and "maxval" to every node. For a node x, x.mingap should be the minimum gap in the subtree rooted at x, x.minval should be the minimum value in the subtree rooted at x, and x.maxval should be the maximum value in the subtree rooted at x. An implementation of a BST will be provided as starter code. You will need figure out how to modify the code to maintain the above attributes without affecting the running times of INSERT or DELETE.

Input: The input is given in a file called input.txt. The first line contains instructions for the creation of the tree. For example, "I15 I1 I5 I9 I18 I22 D15" specifies a tree that is created by inserting 15, inserting 1, inserting 5, inserting 9, inserting 18, inserting 22, and deleting 15. Only positive integers are used as keys. You can assume that if an element is to be deleted, it occurs in the tree. Code for parsing the input and creating the tree is provided in the starter code, so there is no need for you to modify it.

Output: Your output must contain a single line with white-space delimited integers. The line should contain the value of MIN-GAP of the root of the tree after EACH operation in the first line of the input, except for the very first operation. You can assume that the size of the tree will always be at least two. The code for the output is also provided in the starter code, so there is no need for you to modify it.

Example :
Input:
I15 I1 I5 I9 I18 I22 D15

Output: 
14 4 4 3 3 4
