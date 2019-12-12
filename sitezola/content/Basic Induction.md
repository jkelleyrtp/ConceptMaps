+++
title = "Basic Induction"
date = 2019-12-12
+++


Created: Oct 28, 2019 12:05 PM
Deadline: Nov 07, 2019
Name: Richard Gao
Related to Discrete Problem Database (Tags): ../Discrete%20Problem%20Database/Basic%20Induction%20IQC.md
Required?: No
Status: Completed
Topic: Mathematical Reasoning

# Question:

Prove by induction that the following equation is true for all n ≥ 1:

$$\sum_{r=1}^{n}r(n+1) = rac{1}{3}n(n+1)(n+2)$$

# Answer:

The above equation is the proposition P(n) for all n ≥ 1. We perform a proof by induction as so.

### Basis Step: P(1)

$$\sum_{r=1}^{1}r(r+1) = rac{1}{3}(1)(1+1)(1+2)$$

$$1(2)=rac{1}{3}(2)(3)$$

$$2=2$$

### Inductive Step: Assume P(k) is true

$$\sum_{r=1}^{k}r(r+1) = rac{1}{3}(k)(k+1)(k+2)$$

$$1(1+1)+2(2+1)+...+k(k+1)=rac{1}{3}(k)(k+1)(k+2)$$

### Show: P(k+1) is true

$$\sum_{r=1}^{k+1}r(r+1) = rac{1}{3}(k+1)(k+1+1)(k+1+2)$$

$$1(1+1)+2(2+1)+...+k(k+1)+(k+1)(k+1+1)=rac{1}{3}(k+1)(k+2)(k+3)$$

Substitute in definition of P(k)

$$rac{1}{3}(k)(k+1)(k+2)+(k+1)(k+2)=rac{1}{3}(k+1)(k+2)(k+3)$$

Factor out

$$(rac{1}{3}(k+1)(k+2))(k+3)=rac{1}{3}(k+1)(k+2)(k+3)$$

By associative property of multiplication

$$rac{1}{3}(k+1)(k+2)(k+3)=rac{1}{3}(k+1)(k+2)(k+3)$$

Since P(1) is true and the implication P(k)→P(k+1) is true for all integers k ≥ 1, the principle of mathematical induction shows that P(n) is true for all positive integers greater than 1.❏
