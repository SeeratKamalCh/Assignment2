PrintStars program takes the number of stars as command line arguments from the user and then prints them in triangle shape as output.

If the user does not enter or pass number of stars line argument then the program raises an exception: Usage: Number of triangles

If the user enters the number of stars that do not form a triangle shape for example 4, then the program raises an exception: 
Usage: 4 stars do not form a triangle shape: Enter # of stars that form a triangle shape for example 1,3,6,10....

This is so because triangle is formed by sequences of numbers such as 1,3,6,10,15...... with formula n(n-1)/2=S (Number of stars) for every level
n^2-n-2S=0 is the equation formed and using quadratic formula we can solve the equation for n. n1=(-b-sqrt(b^2-4ac))/2a 
and n2=(-b+sqrt(b^2-4ac))/2a and thus find the level of triangles for number of stars given. 

If both n1 and n2 are not integers then it means these number of stars do not form a perfect triangle shape
