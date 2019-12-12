+++
title = "Induction on Graphs"
date = 2019-12-12
+++


Created: Oct 31, 2019 10:57 AM
Deadline: Nov 07, 2019
Name: Richard Gao
Required?: No
Status: Completed
Topic: Sets and Functions

# Question:

Prove by induction on the number of edges that for any simple (not necessarily connected)
graph, G, the sum of the degrees of all of G’s vertices is equal to twice the number of edges in
G.

If you prefer mathier notation, what follows is a restatement of the problem. Let G be a simple
(not necessarily connected) graph on the vertex set V and the edge set E, with |E| = n. Prove by induction on n that:

$$\sum_{v\in V}deg(v) = 2n$$

# Answer:

P(n) is the proposition that "Given a graph G with n edges, there are 2n total degrees from all of G's vertices" for all n > 1.

### Basis Step: P(1)

A graph with n=1 edges has has 2 vertices by the definition of an edge. Each vertex has a degree of 1 being the edge, summing up to 2 degrees.

### Inductive Step: Assume P(k) is true

Assume P(1) .... P(k) are true for some k ≥ 1. 

### Show: P(k+1) is true

Consider P(k+1) or a simple graph G with k+1 edges. Removing an edge from graph G, provides a graph G' with k edges. By the induction hypotheses a graph with k edges has 2k total degrees. It follows that G has 2k+2 or 2(k+1) total degrees as an edge connects two vertices adding 2 degrees to the total. This completes the induction step.

Since P(1) is true and the implication P(k)→P(k+1) is true for all integers k ≥ 1, the principle of mathematical induction shows that P(n) is true for all positive integers greater than 1.❏
