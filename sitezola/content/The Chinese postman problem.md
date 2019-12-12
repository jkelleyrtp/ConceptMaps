+++
title = "The Chinese postman problem"
date = 2019-12-12
+++


Created: Dec 09, 2019 12:57 PM
Required?: Yes
Topic: Graphs

**Prerequisites**: ****Euler circuits in graphs and shortest path algorithms. See, for example, Sections 7.5 and 7.6 of Discrete Mathematics and Its Applications, Second Edition, by Kenneth H. Rosen.

# Introduction

Named after the Chinese mathematician Mei-Ko Kwan who posed the problem in 1962.

The problem is to find a shortest closed path or circuit that visits every edge of an (connected) undirected graph at least once.

## Formal definition

Given a connected weighted graph or digraph G, the Chinese Postman Problem is the problem of finding the shortest circuit that uses each edge in G at least once.

## Important Property for General Solution

Suppose G is a graph with 2k odd vertices, where k ≥ 1, and suppose C is a circuit that traces each edge of G at least once. Then the retraced edges in C can be partitioned into k paths joining pairs of the odd vertices, where each odd vertex in G is an endpoint of exactly one of the paths.
