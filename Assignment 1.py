#Papa Yaw Appiah-Kwakye
#6929121
#Github Username -  spykwakye

#Question a
W = 10   
Load_intensity = W

L = 12   
Beam_length = L

x = 0    
Distance_on_the_beam = x

M = (W * (-6*x**2 + 6*L*x - L**2))/12
Bending_moment = M

V = W * ((L/2) - x)
Shear_force = V

print(f'a) Moment when x = 0 is {M}KN/m') 
print() 
print(f'V when x = 0 is V = {V}KN')
#For Shear Force and Bending Moment when x = 0

x = L = 12
M = (W * (-6*x**2 + 6*L*x - L**2))/12
print()
print(f'Moment when x = 12 is {M}KN/m')
#For the Bending moment at the end of the beam

V = W * ((L/2) - x) 
print()
print(f'V when x = 12 is {V}KN')
#For Shear Force at the end of the beam


#Question b
a = -6
b = 72
c = -144

com_square = b/(2*a)
#This is for the coefficient of x in the quadratic of the form ax^2 + bx + c = 0 

constant = -c/a + com_square**2
#Squaring the term b/2a and adding it to the constant -c/a  in order to represent the quadratic -6x^2 + 72x - 144 in the form x^2 + bx/a = -c/a 

contraflexure_a = (constant**0.5 - com_square)
contraflexure_b = (-constant**0.5 - com_square)
#point_of_contraflexure_1 and point_of_contraflexure_2 are roots of the quadratic equation.

print()
print(f'b)The distances at which the bending moment will be zero are x1 = {contraflexure_a} and x2= {contraflexure_b}') 

#Question c
V = 0 
x = V + (L/2) 
point_of_zero_shear_force = x 
print()
print('c) ' + str(point_of_zero_shear_force) + ' is the point at which the Shear Force is = 0')


#Question d
import numpy as np
beam_length = 12  
steps = 0.01 
w = 10
span_of_beam = np.arange (0, beam_length + steps, steps) # list to discretize the beam length
x = span_of_beam 
M = W * (-6*x**2 + 6*L*x - L**2)/12 
print()
print('e) The Moment for each step along the span is {0}'.format(M))
#The Bending Moment for each value of x within the beam_span


#Question e
start = 0 
step = 0.01 
k = L + step 
x = np.arange(start,k,step)
V = w*(L/2 - x) 
print()
print('(e) The shear force for each step along the span is {}'.format(V))
#The shear force(V) for each value of x within the beam_span


#Question f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(span_of_beam) 
m_AM = min(AM)
"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""

#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/W
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print(f'f)The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))     


#Question g
"""
Let the relative errors be r_error
"""
r_error_1 = ((9.464101615137753-9.46)/9.464101615137753*100)
r_error_2 = (( 2.539999999999999-2.5358983848622456)/2.539999999999999*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_error_1,r_error_2))


#Question h
import numpy as np
def calculate_M(W, L, x):
    return(W * (-6*x**2 + 6*L*x - L**2)/12)

beam_length = 12
steps = 10
BMoment_values = []

for x in span_of_beam:
    M = calculate_M(W, L, x)
    BMoment_values.append(M) 
    
max_Y = max(BMoment_values) #Maximum Bending Moment in the list of moment values
min_Y = min(BMoment_values) #Minimum Bending Moment in the list of moment values
print()
print("h) Maximum bending moment:", max_Y) #Maximum Bending Moment

print()
print("Minimum bending moment:", min_Y) #Minimum Bending Moment










