# Homework #2 Question 1: Summary of Shuffled Complex Evolution (SCE) optimization algorithm by Duan et al.

SCE optimization algorithm created by Duran et al. is an evolution of the CCE or Competitive Complex Evolution 
algorithm. The CCE is a global optimization algorithm that efficiently explores all possible parameters to
find a global optimum rather than just a local extrema. The SCE works by enhancing the results of the CCE. The 
major steps of the SCE can be broken down as follows:

1) We calculate the size of a sample vector. This vector is from the number of complexes p (sub-regions) and the number of points in each complex m. Each value of this vector represents an n-dimensional solution that could be feasible.
2) The SCE generates a sample of size s that is feasible within the possible set of parameters. 
3) We then rank each point in the sample in order of increasing function value (an error metric) and call this new sorted array D.
4) The SCE then partitions D into the number of complexes p with m points. This is why the sample vector needs to be of size m*p.
5) Then the SCE then evolves each complex in D individually using the CCE and store the results.
6) The SCE then merges evolved results into D and D is then resorted by increasing function value.  
7) Then we check the convergence of this evolved result, and if we are within our convergence criteria we stop. Otherwise, we repeat this process from step 4 until the convergence criteria is satisfied.

Overall this method is good at solving global optimization where using other methods would prove quite difficult. 
The types of situations that SCE excels in usually involve high dimensionality, discontinuities, 
or multiple local extrema where finding the global extrema would be taxing. However, this algorithm isn't 
fool-proof and other algorithms like some genetic algorithms can prove a better fit and converge on an answer faster.
It should be noted that the SCE does prove more robust that basic gradient descent systems as these tend to 
fall into local minima more often than the global minima. This then makes SCE better for atmospheric science 
modeling where noisy data (with many local minima) would cause gradient processes to breakdown.