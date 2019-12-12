+++
title = "Stirling Numbers"
date = 2019-12-12
+++


Created: Dec 09, 2019 12:52 PM
Required?: Yes
Topic: Combinatorics

**Prerequisites**: basic counting techniques and equivalence relations. See, for example, Chapters 4, 5, and 6 of Discrete Mathematics and Its Applications, Second Edition, by Kenneth H. Rosen.

- Parent Nodes: Counting & Advanced Counting

# Introduction

Stirling numbers are named after James Stirling who introduced them in the 18th century.

There are tow different sets of such numbers:

- Stirling numbers *s(n, k)* of the first kind
- Stirling numbers *S(n, k)* of the second kind

Stirling numbers are defined as the number of partitions of *n* elements into *k* non-empty subsets

- Different ways of counting orderings of each subset

Stirling numbers initially defined by Stirling as a technique in relating sequences of polynomials

## Partitioning *n* labeled objects into *k* unlabeled classes

Stirling numbers of the second kind *S(n, k)* represents the number of partitions of N into k nonempty subsets. Partitions of N are associated with sets of functions defined on N, and they correspond to equivalence relations on N.

Ex: Consider a set N = {1, 2, 3, 4}. Find *S(4, 2)*

The 2-class partitions of the 4-element set N are:

$$(\{1,2,3\},\{4\}),(\{1,2,4\},\{3\}),(\{1,3,4\},\{2\}),(\{2,3,4\},\{1\}),\(\{1,2\},\{3,4\}),(\{1,3\},\{2,4\}),(\{1,4\},\{2,3\})$$

Therefore,

$$S(4,2)=7$$

## Stirling numbers of the first kind *s(n, k)*

The Stirling numbers of the first kind s(n, k) are the numbers satisfying

$$(x)_n=\sum_{k=0}^{n}s(n,k)x^k$$
