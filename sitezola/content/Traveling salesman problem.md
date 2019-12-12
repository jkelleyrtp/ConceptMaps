+++
title = "Traveling salesman problem"
date = 2019-12-12
+++


Created: Dec 09, 2019 12:57 PM
Required?: Yes
Topic: Graphs

**Prerequisites**: graphs and trees. See, for example, Chapters 7 and 8 of Discrete Mathematics and Its Applications, Second Edition, by Kenneth H. Rosen.

# Introduction

The question of concern is:

"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?"

![Traveling%20salesman%20problem/Untitled.png](Traveling%20salesman%20problem/Untitled.png)

## Formal Definition

Given a graph G in which the edges may be directed, undirected, or some of each, and in which a weight is assigned to each edge, the traveling salesman problem, denoted TSP, is the problem of finding a Hamilton circuit in G with minimum total weight, where the weight of a circuit is the sum of the weights of the edges in the circuit.
