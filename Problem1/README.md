# How to Run

Have the latest python3 version
python3 Problem1.py

# Proof of correctness

I tried to go for a lock-free synchronization method for this concurrent linked list. By using a shared set a servant can check whether the present has been already added or thanked. In addition, I split the presents evenly between the 4 servants and each servant will alternative between adding or thanking the guest, and the minotaur will randomely give a search order to a servant as well. As long as the servants lean more toward adding and thanking, rather than searching, there will be no presents remaining unthanked.

# Efficiency

I believe this solution to be efficient as I am avoiding using locks for a better approach for the most part. I am only using a lock for searching which can be replaced for a lock-free approach as well to further optimize this program.

# Experimental Evaluation 
I have tested this program on small and large amount of presents as well as servants. I have found results to be consistent with what should be expected in terms of runtime and correctness. 
 
