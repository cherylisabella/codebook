# Microeconomics - Part 3 Homework 2

## Coasian Bargaining

## 1.1 Eldery vs. Youth
A major difference between the elderly and the young with respect to COVID-19 is the risk of severe illness or mortality due to contracting the virus. This difference can be incorporated into a model, where the utility loss of contracting the virus is higher for the elderly than for the young, given that the elderly are generally at a higher risk of severe outcomes.

### 1.2 Maximizing Utility Functions
To obtain the preferred curfew time for each group, we need to maximize their individual utility functions with respect to $x$. 

Given the utility functions for the elderly (Equation 1) and the young (Equation 2), we take the derivative with respect to $x$ and set them equal to 0:

- **Elderly:** $\frac{du_E}{dx} = -2x = 0$ ⇒ $x_E = 0$ ⇒ 3pm curfew  

- **Young:** $\frac{du_Y}{dx} = 2 - 2x = 0$ ⇒ $x_Y = 1$ ⇒ 3am curfew  

### 1.3 Socially Optimal Curfew
The socially optimal curfew time can be found by maximizing the sum of the two groups’ utilities: $W = u_E + u_Y = 1 + x^2 + 2x - x^2$  
Taking the derivative of $W$ with respect to $x$:  
<p align="center">$\frac{dW}{dx} = 2 - 4x = 0$ ⇒ $x^* = \frac{1}{2}$</p>
<p align="center">⇒ 9pm curfew (since 0 is 3pm and 1 is 3am)</p>

### 1.4 Utility at Different Curfews
At $x = 0.75$, the respective utilities are:  
- $u_E = y + 1 - (0.75)^2 = y + 0.4375$  
- $u_Y = -y + 2(0.75) - (0.75)^2 = -y + 0.9375$

At $x = 0.5$, the respective utilities are:  
- $u_E = y + 1 - (0.5)^2 = y + 0.75$  
- $u_Y = -y + 2(0.5) - (0.5)^2 = -y + 0.75$

To make E indifferent, Y needs to offer a payment such that:  $y + 0.75 - (-y) = y + 0.4375$  

Solving for $y$, we get:  $2y = 0.4375 - 0.75 = -0.3125$  

Thus, $y = -0.15625$.  

In the context of the Coase theorem, the voluntary curfew ($x = 0.5$) is identical to the social optimum, as under efficient bargaining, the proposer can guide the outcome to the point that maximizes total utility.

### 1.5 Inducing the Social Optimum
According to Coase, if bargaining is possible, transaction costs are low, and outcomes are predictable, then regardless of the initial curfew time, the young and elderly can bargain to reach the socially optimal curfew time through mutually beneficial transfers. The initial setting only affects the distribution of gains, not the efficient outcome itself, provided rights are clear and bargaining is effective.

### 1.6 When Y Makes the Offer:
When Y makes the offer, for E to accept the social optimum, the payment must ensure that E is at least as well off as with the initial curfew ($x = 0.75$) and does not exceed $y_{\text{max}}$.  
- $u_E = y + 0.75$ when $x = 0.5$  
- $u_E = y + 0.4375$ when $x = 0.75$  

For E to accept, $y + 0.75 \geq y + 0.4375 - y$.  
Thus, $y \geq -0.3125$, meaning that E can pay at most 0.3125 to Y.

### 1.7 When E Makes the Offer:
When E makes the offer, for Y to accept, the payment needs to ensure that Y is at least as well off as with the initial curfew ($x = 0.75$) and does not exceed E's limit $y_{\text{max}}$.  
- $u_Y = -y + 0.75$ when $x = 0.5$  
- $u_Y = -y + 0.9375$ when $x = 0.75$  

For Y to accept, $-y + 0.75 \geq -y + 0.9375 + y$.  
Solving for $y$, we get $y \leq -0.09375$, meaning E would need to receive at least 0.09375 from Y.

### 1.8 Finding the Latest Initial Curfew
We can find the latest initial curfew time by considering the total utility $W(x)$. The total utility at a curfew $x$ is:  $W(x) = 1 + 2x - 2x^2$.  
The socially optimal total utility is $W(0.5) = 1.5$.

For bargaining with a maximum side payment of 0.1 to be effective in reaching the social optimum, the change in total utility should be no more than $2 \times 0.1 = 0.2$. This leads to two inequalities:  
- $-0.5 + 2x_0 - 2x_0^2 \leq 0.2$  
- $-0.5 + 2x_0 - 2x_0^2 \geq -0.2$

Solving these inequalities, we find that the latest time $x_0$ that allows for the social optimum to be reached with a maximum side payment of 0.1 is approximately $x_0 = 0.72$.

### 1.9 Impact of Initial Curfew
The social planner's initial imposition of a curfew can affect the utility levels of both parties. If bargaining is constrained by a limited ability to make transfers, the initial curfew setting creates a new baseline from which Pareto-improving trades can occur. This baseline impacts the bargaining process by shifting the bargaining power.

---

## 2. The Tragedy of the Fishers

### 2.1 Nash equilibrium
To determine the maximum A would pay B for private ownership, we need to find the Nash equilibrium under common access. Given the profit functions for both A and B:

- **A:** $\pi_A = \frac{1}{2}(1 - \frac{1}{2} e_B)e_A - e_A^2$  
- **B:** $\pi_B = \frac{1}{2}(1 - \frac{1}{2} e_A)e_B - e_B^2$

In a Nash equilibrium, each fisherman chooses their effort to maximize profit, given the other's effort. The equilibrium is found by solving the system of equations for $e_A$ and $e_B$:

- For A:  $e_A = 6 - \frac{e_B}{2}$  
- For B:  $e_B = 6 - \frac{e_A}{2}$

Substituting $e_B$ into $e_A$, we find the Nash equilibrium at $e_A = 4$ and $e_B = 4$, with profits for both A and B being 16.

### 2.2 Pareto Ranking

#### Nash Equilibrium
- Nash equilibrium: $e_A = 4$ and $e_B = 4$ with profits $A = 16$ and $B = 16$.

#### Most Egalitarian Social Welfare Optimum
To maximize the combined profit of A and B, subject to the condition that $A = B$:
- Total profit: $A + B = 12e_A - e_A e_B - e_A^2 + 12e_B - e_A e_B - e_B^2$
- Simplifying and assuming $e_A = e_B$, we get: $A + B = 24e - 4e^2$.
- To maximize, we differentiate with respect to $e$:
  $\frac{d}{de}(24e - 4e^2) = 24 - 8e = 0$
- Solving for $e$: $e = 3$ ⇒ $e_A = 3$, $e_B = 3$.
- Thus, $A = 12(3) - 3(3) - 3^2 = 36 - 9 - 9 = 18$, and similarly for $B = 18$.

#### A is the First Mover, B Decides After
- A will choose $e_A$ to maximize their profit, anticipating B’s reaction. From B’s reaction function: $e_B = 6 - 0.5e_A$
- A’s profit function becomes:  $A = 12e_A$
- To maximize, we differentiate with respect to $e_A$:
  $\frac{dA}{de_A} = 6 - e_A = 0$
- Solving for $e_A$: $e_A = 6$, $e_B = 6 - 0.5(6) = 3$.
- Profit for A: $A = 6(6) - 0.5(6^2) = 36 - 18 = 18$.
- Profit for B: $B = 12(3) - 6(3) - 3^2 = 36 - 18 - 9 = 9$.
- Thus, $u_A = 18$ and $u_B = 9$.

#### A Makes a Take-It-Or-Leave-It Offer to B
- A offers a transfer $T$ to ensure that B is no worse off than in the Nash equilibrium ($u_B = 16$).
- In this case, A chooses $e_A = 3$, $e_B = 3$ ⇒ total profit of 36.
- A can transfer 2 to B to make B indifferent:
  $\pi_A = 18 - (-2) = 20, \pi_B = 18 + (-2) = 16$
- Alternatively, A can exclude B and choose $e_A = 6$, resulting in a profit of 36. To make B indifferent, A needs to pay 20 to B:
  $\pi_A = 36 - 20 = 16, \pi_B = 0 + 20 = 20$
- Thus, $u_A = 20$ and $u_B = 16$.

### Pareto Dominance
- (b) Pareto dominates (a):
  In case (b), both fishermen are better off ($u_A = 18$ and $u_B = 18$) than in case (a) ($u_A = 16$, $u_B = 16$). So, (b) is strictly better than (a) for both A and B, and hence (b) Pareto dominates (a).
  
- (d) Pareto dominates (a):
  In case (d), $u_A = 20$ and $u_B = 16$, which is strictly better for A than (a), where both are at 16. So, (d) also Pareto dominates (a).

- (d) Might Pareto dominate (b):
  In case (d), $u_A = 20$ and $u_B = 16$, while in case (b), both $u_A = 18$ and $u_B = 18$. It depends on how we view the total utility, but generally, (d) would be considered better overall, since the total utility ($u_A + u_B = 20 + 16 = 36$) is higher than (b)'s total utility ($u_A + u_B = 18 + 18 = 36$), so (d) can be seen as Pareto dominant or at least as good as (b).

- (c) Cannot be Pareto ranked with (a) or (b):
  In case (c), $u_A = 18$ but $u_B = 9$, which makes it incomparable with (a) and (b). Improving one fisherman’s utility here necessarily reduces the other's, so it cannot be Pareto ranked against the others.

### 2.3 Strategic Advantage of Being a Second Mover
Being a second mover can be advantageous when the first mover’s action creates a positive externality for the second mover, or when the second mover can strategically react to the first mover's actions to benefit from them. For instance, if fishing were a group activity (and the lake is so big that they cannot cover the whole lake by themselves), and one’s catch increases with the effort of others, a second mover could benefit from the first mover's higher effort. This suggests that modifying the production function, where one fisherman's effort impacts others positively, would make it advantageous for the second fisherman to adjust their effort accordingly.

### 2.4 The "Race to the Bottom" in Fishing
Assuming access to the lake is now open to everyone, the number of fishermen $N$ will increase until profits are driven to zero. Given the profit function for fisherman $i$, under symmetry, the total effort is $(N-1)e$, and the profit for each fisherman becomes:
$i = \frac{1}{2}e - (N-1)e^2 - e^2 = \frac{1}{2}e - Ne^2$

For profit to be zero, we set:
$\frac{1}{2}e - Ne^2 = 0 \quad \Rightarrow \quad e = \frac{1}{2N}$

As $N$ increases, effort decreases. The lake can sustain fishermen as long as profits remain non-negative. More fishermen will enter as long as the profit is positive, but each individual effort decreases as more fishermen join. This leads to a "race to the bottom" scenario, where overfishing can occur due to the externality from the increased number of fishermen.
