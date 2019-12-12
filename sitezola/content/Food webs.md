+++
title = "Food webs"
date = 2019-12-12
+++


Created: Dec 09, 2019 12:56 PM
Required?: Yes
Topic: Graphs

**Prerequisites**: basic concepts of graph theory. See, for example, Sections 7.1 and 7.2 of Discrete Mathematics and Its Applications, Second Edition, by Kenneth H. Rosen.

# Introduction

A food web is a directed graph, modeling the predator-prey relationship in an ecological community.

Looking into food webs explores the topics of:

- the minimum number of parameters needed to describe ecological competition
- how graphs can be represented as intersection graphs of families of sets

## Definition

A food web of an ecological community is a directed graph with a vertex for each species in the community and a directed edge from the vertex representing species A to the vertex representing species B if and only if A preys on B

The competition graph of a food web is a simple graph with a vertex for each species. Two vertices are joined by an (undirected) edge if and only if the species they represent have a common prey.

![Food%20webs/Untitled.png](Food%20webs/Untitled.png)

![Food%20webs/Untitled%201.png](Food%20webs/Untitled%201.png)
