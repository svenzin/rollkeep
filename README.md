# rollkeep

Experimentation and implementations of the Roll and Keep dice rules.

## Roll and Keep rules

Roll and Keep is a system where the player throws a number of dice and keep a subset of the results,
usually the best ones. The way dice faces are counted and evaluated depends on the game system.

A straight forward example: The player throws 4 6-sided dice, keep the best 3 and uses the sum of values.
In this example, a throw containing [ 3, 4, 1, 2 ] would mean the player keep 4, 3 and 2 for a final
result of 4 + 3 + 2 = 9.

## Values of interest and format
A JSON serialization of the described data structure. 

### Throw
A simple random throw of N dice with D faces. The result is an array of the dice faces.
Example: Throw N=4 D=6 ->
    "[ 4, 2, 6, 5 ]"

### Probability
The probability of every possible result for a throw of N dice with D faces, keep K dice.
The result is an array of tuples with the value and the probability of getting this value.
Example: N=3, D=3, K=2 ->
    "[ [ 2, 1/27 ],
       [ 3, 3/27 ],
	   [ 4, 7/27 ],
	   [ 5, 9/27 ],
	   [ 6, 7/27 ] ]"

### Cumulative Probability
Same format as Probability but the tuples contain the value, and the probability of getting 
a result lower or equal to this value.
If P(x) is the probability of getting x, and C(x) the cumulative probability of getting x,
then C(x) = sum for i <= x of P(x)
Example: N=3, D=3, K=3 ->
    "[ [ 2,  1/27 ],
       [ 3,  4/27 ],
	   [ 4, 11/27 ],
	   [ 5, 20/27 ],
	   [ 6, 27/27 ] ]"

## Uses
### PUMPP system
TODO

## Current state
### Python