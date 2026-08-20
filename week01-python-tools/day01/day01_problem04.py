#the problem:
# Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy
# (measured in Joules), 𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, 
# the formula means that mass and energy are equivalent.
# implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
# Assume that the user will input an integer.

#the solution:

mass=int(input())
c=300000000
energy=mass*c*c
print(energy)