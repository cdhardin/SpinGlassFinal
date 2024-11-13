# 1. One-spin flips: Do a standard one-spin flip move for each spin in each replica.
# 2. Cluster moves: For each temperature, randomly partition the n replicas in 
# pairs and do one cluster move for each pair.
# 3. EMC: For each pair of neighbouring temperatures, do n standard EMC updates between 
# the two sets (pairing each replica from one set with one from the other).
# In a standard EMC update, two spin configurations at different temperatures are exchanged with probability
# P(1↔2) = min(1, exp[(β2−β1)*(H2−H1)] )