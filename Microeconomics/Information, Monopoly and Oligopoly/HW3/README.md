# Microeconomics - Part 2 Homework 3

## Part 1

The utility function of the individual is $u(w) = \sqrt{w}$.

We firstly determine whether the individual will take the precautionary action by evaluating the expected utility in both cases.

1. With precautionary action: $u_a(w) = \frac{1}{2}\sqrt{100-36} + \frac{1}{2}\sqrt{100} - \frac{4}{10} = 8.6$

2. Without precautionary action: $u_n(w) = \frac{3}{4}\sqrt{100-36} + \frac{1}{4}\sqrt{100} = 8.5$

The expected utility is higher in the scenario where the individual takes the precautionary action; consequently, if we assume individual rationality, the action will be taken to reduce the probability of loss at cost $-\frac{4}{10}$ and they will have a reservation utility of 8.6, meaning that for the individual to undergo insurance they must have, under insurance, an expected utility higher than 8.6 (participation constraint).

### Optimal contract (no action)
The insurer maximises:
$\underset{y,x}{\max} \frac{1}{4} x + \frac{3}{4}[x - y]$
such that the participation constraint is respected:
$\frac{1}{4} \sqrt{100-x} + \frac{3}{4} \sqrt{100-36-x+y} \geq 8.6$

### Optimal contract (action)
The insurer maximises:
$\underset{y,x}{\max} \frac{1}{2} x + \frac{1}{2}[x - y]$
such that the participation constraint is respected:
$\frac{1}{2} \sqrt{100-x} + \frac{1}{2} \sqrt{100-36-x+y} - \frac{4}{10} \geq 8.6$

Insurer profits are higher in the case of the individual undertaking the action since:
$\pi_{\text{action}} = x - \frac{1}{2} y > \pi_{\text{noaction}} = x - \frac{3}{4} y$
Consequently, the firm will incentivize the consumer to undertake the action, meaning that there will be a binding incentive constraint:
$IC: \frac{1}{2} \sqrt{100-x} + \frac{1}{2} \sqrt{100-36-x+y} - \frac{4}{10} \geq \frac{1}{4} \sqrt{100-x} + \frac{3}{4} \sqrt{100-36-x+y}$
Moreover, the participation constraint is binding and must be respected:
$PC: \frac{1}{2} \sqrt{100-x} + \frac{1}{2} \sqrt{100-36-x+y} - \frac{4}{10} \geq 8.6$

By solving the system we obtain:

- Participation constraint:
  $$\frac{1}{2} \sqrt{100 - x} + \frac{1}{2} \sqrt{64 - x + y} - \frac{2}{5} ≥ 8.6$$ ⟹ $$\sqrt{100 - x} + \sqrt{64 - x + y} ≥ 18$$

- Incentive compatibility constraint:
  $$\frac{1}{2} \sqrt{100 - x} + \frac{1}{2} \sqrt{64 - x + y} - \frac{2}{5} ≥ \frac{1}{4} \sqrt{100 - x} + \frac{3}{4} \sqrt{64 - x + y}$$ ⟹ $$\sqrt{100 - x} - \sqrt{64 - x + y} ≥ \frac{8}{5}$$
  
- Adding both equations:
$$(\sqrt{100 - x} + \sqrt{64 - x + y}) + (\sqrt{100 - x} - \sqrt{64 - x + y}) = 18 + \frac{8}{5}$$

- Simplifying: $2\sqrt{100 - x} = \frac{98}{5}$

- Solving for $x$: $\sqrt{100 - x} = \frac{49}{5}$

- Squaring both sides:
$100 - x = \frac{2401}{25}$
$x = \frac{99}{25}$

Substituting $x$:
$\sqrt{100 - \frac{99}{25}} + \sqrt{64 - \frac{99}{25} + y} = 18 ⟹ y = \frac{36}{5}$

$$
\begin{aligned}
x &= \frac{99}{25} = 3.96 \\
y &= \frac{36}{5} = 7.2
\end{aligned}
$$

The optimal contract under negotiable action will be given by an insurance premium of $x = \frac{99}{25}$ and a compensation of $y = \frac{36}{5}$.

The firm is risk neutral so it will accept any profit equal or higher than zero and:
$\frac{99}{25} - \frac{1}{2}\frac{36}{5} \geq 0$

## Part 2

- **Reservation utility**: $\bar{u} = 1$
- **Cost of effort** is given by $v(e) = e^2$
- **von Neumann-Morgenstern utility function** is:
$u(w) = \sqrt{w}$

### 2.1 Observable effort

In a setting with a risk-neutral principal, a risk-averse agent, and full information, under the optimal contract, the principal will pay the agent a wage contingent upon the level of effort $\bar{w}(e)$ that satisfies the participation constraint (i.e., the agent's reservation utility net of cost of effort):

<p align="center">$u[\bar{w}(e)] = \bar{u} + v(e)$</p>

Given that the utility function of the agent is: $u(w) = \sqrt{w}$
and the reservation utility $\bar{u} = 1$:

<p align="center">$⟹ \sqrt{\bar{w}(e)} = 1 + e^2$</p>
with e ∈ [0, 1]

#### 2.1.1 Agent's wage
- Low observable effort: with $e = 0$, the wage under optimal contract is $\bar{w}(0) = 1$
- High observable effort: with $e = 1$, the wage under optimal contract is $\bar{w}(1) = 4$

#### 2.1.2 Firm's profit
The firm's profit under the contract is given by: $\Pi(e) = E[x - \bar{w}(e)]$

- Low observable effort: with $e = 0$, the profit under the optimal contract is given by:
$\Pi(0) = E[x] - \bar{w}(0) = \frac{4}{10} \cdot 0 + \frac{4}{10} \cdot 10 + \frac{2}{10} \cdot 25 - 1 = 8$

- High observable effort: with $e = 1$, the profit under the optimal contract is given by: $\Pi(1) = E[x] - \bar{w}(1) = \frac{4}{10} \cdot 10 + \frac{4}{10} \cdot 25 + \frac{2}{10} \cdot 0 - 4 = 10$

Firm's profit is higher under high effort and $\bar{w}(1) = 4$, therefore the firm will offer the contract $c = \{e = 1; \bar{w}(e) = 4\}$. Since the contract satisfies the participation constraint, the agent receives utility $u[w(c)] = 2 > \bar{u}$ and will accept the contract.

### 2.2 Non-observable effort

When effort is not observable, the offered wage $\bar{w}$ must satisfy not only the participation constraint, but it also must incentivize the agent to put in the desired level of effort.

- If the desired level of effort is $e = 0$, then the wage $\bar{w} = 1$ will satisfy the participation constraint, as proven in the previous question, and incentivize effort $e = 0$.
- If the desired level of effort is $e = 1$, then the optimal wage must satisfy the participation and incentive constraints:
  - The participation constraint is satisfied if:
  $$\frac{2}{10} \sqrt{\bar{w}_1} + \frac{4}{10} \sqrt{\bar{w}_2} + \frac{4}{10} \sqrt{\bar{w}_3} ≥ \bar{u} + e^2$$
  $$\Longrightarrow \frac{2}{10} \sqrt{\bar{w}_1} + \frac{4}{10} \sqrt{\bar{w}_2} + \frac{4}{10} \sqrt{\bar{w}_3} - 2 ≥ 0$$

  - The incentive constraint is satisfied if the expected wage is higher than under $e = 0$, which is:

$$\frac{4}{10} \sqrt{\bar{w}_1} + \frac{4}{10} \sqrt{\bar{w}_2} + \frac{2}{10} \sqrt{\bar{w}_3} - 1$$

$$\Longrightarrow \frac{2}{10} \sqrt{\bar{w}_1} + \frac{4}{10} \sqrt{\bar{w}_2} + \frac{4}{10} \sqrt{\bar{w}_3} - 2 ≥ \frac{4}{10} \sqrt{\bar{w}_1} + \frac{4}{10} \sqrt{\bar{w}_2} + \frac{2}{10} \sqrt{\bar{w}_3} - 1$$
  
We know that when $x_1 = 0$, the firm will offer $w_1 = 0$ to maximise profits. We can therefore simplify the expression:
$$\frac{2}{10} \sqrt{\bar{w}_3} - 1 \geq 0$$

$$\Longrightarrow \bar{w}_3 = 25$$

Substituting this into the participation constraint we obtain:

$$\bar{w}_2 = 0$$


#### 2.2.1 Firm's profit

The firm's profit under the contract is given by:

$$\Pi(e) = E[x - \bar{w}(e)]$$

- Low observable effort: with $e = 0$, the profit under the optimal contract is given by:

$$\Pi(0) = E[x] - \bar{w}(0) = \frac{4}{10} \cdot 0 + \frac{4}{10} \cdot 10 + \frac{2}{10} \cdot 25 - 1 = 8$$

- High observable effort: with $e = 1$, the profit under the optimal contract is given by:

$$\Pi(1) = E[x] - \bar{w}(1) = \frac{4}{10} \cdot 10 + \frac{4}{10} \cdot 25 + \frac{2}{10} \cdot 0 - E(\bar{w})$$

Since $\bar{w}_1 = \bar{w}_2 = 0$:

$$E(\bar{w}) = \frac{4}{10} \bar{w}_3 = 10$$

The expected profit is:

$$\Pi(1) = 14 - 10 = 4$$

Firm's profit is higher under low effort and $\bar{w}(0) = 1$, therefore the firm will offer the contract $c = \{ e = 0; \bar{w} = 1 \}$. Since the contract satisfies the participation constraint, the agent receives utility $u[w(c)] = 1 = \bar{u}$ and will accept the contract or not accept it indifferently, inputting level of effort $e = 0$.

## Part 3

### 3.1 The contract(s) offered by $P$ if she can distinguish the type of agent

Firstly, the principal maximizes profit under $\pi = \sqrt{e} - w$ for each type A and B. She is also subject to the participation constraints for each type:

$$IR_A: w^A - e^A \geq 0$$

$$IR_B: w^B - 2e^B \geq 0$$

Or, more generally:

$$w^i - t_i \cdot e_i \geq 0, \quad \text{with} \quad i = A, B \quad \text{and} \quad t_A = 1 \quad \text{and} \quad t_B = 2$$

Maximizing profit under:

$$\underset{e_i}{\max} \quad \pi_i = \sqrt{e_i} - e_i t_i$$

and deriving the first order condition by taking the derivative with respect to $e$ yields:

$$\frac{\partial \pi_i}{\partial e_i} = 0$$

$$e_i^* = \frac{1}{4t_i^2}$$

Substituting the values for A and B of $t_i$, we obtain the contracts offered by the principal to each type:

- Type A: $(e_A, w_A, \pi_A) = \left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right)$
- Type B: $(e_B, w_B, \pi_B) = \left(\frac{1}{16}, \frac{1}{8}, \frac{1}{8}\right)$

### 3.2 The contract(s) offered by $P$ in the case of adverse selection

In the case of adverse selection, the contracts remain the same where for type A, $(e_A, w_A) = \left(\frac{1}{4}, \frac{1}{4}\right)$ and for type B, $(e_B, w_B) = \left(\frac{1}{16}, \frac{1}{8}\right)$.

The contracts do not vary as a function of $q$. However, the expected profit of the principal does, thus:

$$E(\pi) = q\left(\frac{1}{4}\right) + (1+q)\left(\frac{1}{8}\right) = \frac{q}{4} + \frac{1-q}{8}$$

As $q$ increases, the expected profit increases.

## Part 4
### 4.1 Market supply and average quality of cars offered at each price
The market supply consists of the seller for which the price is at least equal to the cost $p \geq c$. Since the supply of cars is uniformly distributed, we can then derive market supply using the cumulative distribution function for the proportion of sellers with $c \leq p$:

$$P(c \leq p) = \frac{p - 2}{6 - 2}$$

We can then express market supply as a function of price:

$$
S(p) = 
\begin{cases}
0 & \text{if} \quad p < 2 \\
\frac{p - 2}{4} & \text{if} \quad 2 \leq p \leq 6 \\
1 & \text{if} \quad p > 6
\end{cases}
$$

### 4.2 Market Equilibrium

To find the market equilibrium, we need to determine the price $p$ where the quantity supplied equals the quantity demanded.

#### Supply Function:
Sellers are willing to sell cars at price $p \geq c$, where $c$ is the seller's cost. The supply function, given that costs are uniformly distributed between 2 and 6, is:

$$
S(p) = 
\begin{cases}
0 & \text{if} \quad p < 2 \\
\frac{p - 2}{4} & \text{if} \quad 2 \leq p \leq 6 \\
1 & \text{if} \quad p > 6
\end{cases}
$$

#### Demand Function:
Buyers value each car at $1.2 \times c$. The market equilibrium occurs when the supply equals the demand. At price $p$, the quantity demanded is equal to the number of cars buyers are willing to buy at that price.

#### Solving for Equilibrium Price:

Setting supply equal to demand,

<p align="center">$\frac{p - 2}{4} = \frac{p}{1.2}$</p>

Solving for $p$:

<p align="center">$1.2(p - 2) = 4p \quad \Rightarrow \quad 1.2p - 2.4 = 4p \quad \Rightarrow \quad p \approx 4.29$</p>

The market equilibrium price is approximately 4.29. At this price, sellers with costs between 2 and 4.29 will sell their cars, and buyers will purchase them at this price.
