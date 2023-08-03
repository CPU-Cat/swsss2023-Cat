##################################
#### assignment and unicode symbols 🔥🔥🔥
##################################
using LinearAlgebra 
# silly example 
🔥 = -112
🧯 = 23
🍉🚰 = 4
🔥+🍉🚰
λα = 5

# Golden ratio (nice vs. old)
ϕ = (1+√5)/2
# pi 
π 
# Navier stokes 

#NS = ρ * (∂u+(u ⋅ ̇∇*u))+𝒫 
5⋅5


##################################
#### Arrays/Vectors/Matrices
##################################

# defining a vector
powers_of_two_int = [1, 2, 4]
powers_of_two = [1, 2, 4.0]
some_random_stuff = ["SWSSS", 3, 1.0, +]

# appending stuff/mutating vectors: push!, append!

# defining a matrix
vandermonde = [1 2 4 8;  # first row
                 1 3 9 27] # second row

# concatenating 
# adding rows 
add_a_row = [vandermonde; 1 4 16 48]
# adding columns
add_a_column = [vandermonde [0;1]]
# indexing starts at 1!
add_a_column[1,2]
# slicing
add_a_column[:, 2]
add_a_column[1, :]
add_a_column[:, 2:4]
# last element is indexed by end keyword
add_a_row[:, end]
add_a_row[end]
##################################
#### loops + printing
##################################
for i in 1:10
    println(i)
end
for i in 1:2:10
    println(i)
end
#in particular ranges are written with : instead of range function
#range(5) in python <=> 0:4 in julia 
for i in 1:2:10 println(i) end
for power in powers_of_two
    println(power)
end
push!(powers_of_two, 8)
powers_of_two
append!(powers_of_two, 16)

#whileloops??
i = 0
while i<10
    println(i)
    i+=1 # i = i +1
end

##################################
#### if-elseif-else 
##################################
a = 5.0
if a<2.5
    println("a less 2.5")
elseif a< 3.5
    println("less 3.5")
else
    println("a not less 3.5")
end

##################################
#### functions
##################################

# functional programming style
function my_add(a, b)
    c = a+b
    return c
end
#function =/= method
#generic means needs specific type
function my_add(a::Float64, b::Int)
    return [a,b]
end 
Σ = my_add(5, 3)
s = my_add(5.0,3)
# for simple functions we may prefer the assignment form 
# to resemble standard math notation more closely
f(x) = 1/(2π)*exp(-1/2*x^2)

# evaluation 
p = f(0.5)

# vectorization/(map-reduce)
# evaluates our function at every element of the supplied 
# vector/array and returns the result in the same shape!

#can map function to every entry of array
f.([1.0, 2.0, 0.5, 0.7])
arrayf = [1.0, 2.0, 0.5, 0.7]
x = f.(arrayf)
# differences between python and julia
# Why Julia was created
# https://julialang.org/blog/2012/02/why-we-created-julia/# 
# Julia documentation: Noteworthy differences to other common languages
# https://docs.julialang.org/en/v1/manual/noteworthy-differences/
# Julia for data science
# https://www.imaginarycloud.com/blog/julia-vs-python/#future