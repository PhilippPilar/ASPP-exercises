Day2 - Exercises

Answers:

1) -> solutions in folder 1_animals

2) -> code in 2_buggy is corrected and gives correct results

3)a) lines 22-27 -> avoiding double loop would be a good start


     lines 9,14,19 create the most memory usage; makes sense as size of array is increased


3)b) line 52 -> improve factorize
	--> line 26 -> can while loop or if statement be improved?
			-> possible to calculate both n%p, n/p in one statement?
			-> maybe keeping track of index in p and creating factors in one 			   step would be faster than appending at each step?
      
	memory usage appears to be almost constant throughout program


3)c)
	-> matmult_improved contains improved version using numpy;
		-speedup: ~140-150 times faster
