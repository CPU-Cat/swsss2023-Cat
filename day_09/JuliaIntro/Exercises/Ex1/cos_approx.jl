using BenchmarkTools

function cos_approx(x, N)
    # approximation of cosine via power series expansion
    # inputs:
    #       - x : argument of cosine 
    #       - N : truncation order of the power series approximation
    # outputs:
    #       - cos_val : approximation of cos(x)

    #code option 1:
    # cos_val = 0
    # for i in 0:1:N
    #     term = (-1)^i*x^(2i)/factorial(2i)
    #     cos_val = cos_val + term
    # end
    #return cos_val 
    #code option 2:
    return sum((-1)^n*x^(2n)/factorial(2n) for n in 0:N) 
end

cos_approx(pi/3, 10)

@btime cos_approx($(π/3),$(10)) 
@btime cos($(π/3))
@btime cos(π/3)