+++
title = "Induction on Recurrence Relations"
date = 2019-12-12
+++


Created: Oct 31, 2019 10:58 AM
Deadline: Dec 03, 2019
Name: Jon Kelley
Required?: No
Status: Not Started
Topic: Mathematical Reasoning

1. Suppose you are lining up Legos, and each yellow Lego takes up one inch, each pink Lego takes up two inches, and each purple Lego takes up two inches. We have an infinite number of each type of piece, and all of the pieces within a color can be considered identical.

1. (a) Find a recurrence relations to count an = the number of ways to fill in an n inch line
using an unlimited supply of the provided Legos for n ≥ 1. Please include the first 8
terms, using computational power to iterate through your RR if you wish.

    first 8 terms:

    An n-inch line can be made by an combination of 1-inch yellow pieces, 2 inch pink pieces, and 2 inch purple pieces. We will consider these ME and E cases. If line of Legos is 1 inch long, then there will only be one way to create it: 1 yellow piece. If the line of Legos is 2 inches long, then there will be three ways to create it: 2 yellow, 1 pink, or 1 purple. These pieces will serve as our initial conditions for the recurrence relation. 

    If we add 1 more inch to this sequence, we can insert in between any of the existing lego pieces. If we add 2 more inches to the sequence, we can insert either 2 yellow pieces or 1 pink piece or 1 purple piece into the sequence. Similarly, if we had to remove these pieces from an existing line of Legos n long, we would do it piece by piece until the line had no more Legos left, counting as we went. The number of ways we can arrange the sequence by removing 1 pink piece is the same as the number of ways we can arrange the sequence by removing 1 purple piece, as is the number of ways we can arrange the sequence by removing 1 yellow piece, however the yellow piece removes 1 fewer inches from the line. This pattern  can be written as a simple recursive function:

        def solve_from_n(n):
        	if n == 0:
        		# We have solved this
        			return 1
        	if n < 0:
        		# Not a valid pattern
            return 0
        	if n >= 1:
            # Solve for both pink and purple
        		return solve_from_n(n - 2) + solve_from_n(n-2) + solve_from_n(n-1)

    From this recursive function, we see that a_n is simply:

    $$a_n = 2a_{n-2} + a_{n-1}$$

    Our first 8 numbers sequence 

    1, 3, 5, 11, 21, 43, 85, 171

    With initial conditions 

    $$a_1 = 1, a_2 = 3 	ag{1}$$

    $$a_n = a_{n-1} + 2a_{n-2} 	ag{2}$$

2. (b) Using your above RR (which you may now take as fact), prove by induction that the number of ways to fill an n inch Lego line with the given Legos is also given by the 1n+1 1 n 1n+1 1 n
closed-form solution 3 2 + 3 (−1) . In other words, prove that an = 3 2 + 3 (−1) ,

    Let 

    $$P(n) = " a_n = rac{1}{3}2^{n+1} + rac{1}{3}(-1)^n" 	ext{ for all } n \ge 3$$

    Base case: n = 3, because the RR theorem requires n-1 and n-2. The RR says that 

    $$a_3 = 3 + 2*1 = 5$$

    and the P(3) proposition says that this should be equal to 

    $$rac{1}{3} 2^4 + rac{1}{3}(-1)^3 = 5$$

    Suppose P(3) ... P(k) hold for some k≥2. (This is allowed because we showed it works for k = 2). Consider P (k + 1); we wish to show 

    $$a_{n + 1} = rac{1}{3}2^{n+2} + rac{1}{3}(-1)^{n+1}$$

    If a_n is 1, and a_n + 1 is 3, so:
