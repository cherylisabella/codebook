# Microeconomics - Part 3 Homework 3

## 1. Name the Game

With the utility function $(u_i = a + be_i + ce_j + de_ie_j)$ where $(i, j \in {N, S})$ represent North and South, and $(e_i, e_j \in \{0, 1\})$ represent Restrict (0) or Emit (1), the payoff matrix is:

| North \ South     | Restrict $(e_S=0)$       | Emit $(e_S=1)$       |
|-------------------|-----------------------------|--------------------------|
| Restrict $(e_N=0)$ | $(a, a)$                  | $(a+c, a+b+d)$           |
| Emit $(e_N=1)$    | $(a+b, a+c)$              | $(a+b+c+d, a+b+c+d)$     |

### Prisoner's Dilemma:
When emitting is the dominant strategy for both, but both would be better off restricting. This requires:
- `a + b > a` ⟹ **b > 0**
- `a + b + c + d > a + c` ⟹ **b + d > 0**
- And the Pareto-inferior outcome (Emit, Emit) must be the Nash Equilibrium, with the Pareto-superior outcome (Restrict, Restrict) preferred: `a > a + b + c + d` ⟹ **b + c + d < 0**

### Assurance Game:
When both (Restrict, Restrict) and (Emit, Emit) are Nash equilibria.
- For (Restrict, Restrict) to be a Nash Equilibrium:
  - `a > a + b` ⟹ **b < 0**
  - `a > a + c` ⟹ **c < 0**
- For (Emit, Emit) to be a Nash Equilibrium:
  - `a + b + c + d > a + c` ⟹ **b + d > 0**
  - `a + b + c + d > a + b` ⟹ **c + d > 0**

Typically, for environmental policy, `a > a + b + c + d` would also hold, making (Restrict, Restrict) Pareto superior.

### Chicken (Hawk-Dove) Game:
When each prefers to emit if the other restricts, but both emitting is the worst outcome.
- North's preferences: Emit (if South Restricts) > Restrict (if South Restricts) ⟹ **b > 0**. Restrict (if South Emits) > Emit (if South Emits) ⟹ **b + c + d < 0**.
- South's preferences: Emit (if North Restricts) > Restrict (if North Restricts) ⟹ **c > 0**. Restrict (if North Emits) > Emit (if North Emits) ⟹ **b + c + d < 0**.
- Also, we need `a + c > a` and `a + b > a + b + c + d`, implying **c > 0** and **c + d < 0**.

## 2. Bad Chemistry

Consider the utility functions:
<p align="center">$u = \alpha + \beta a + \gamma A + \delta aA + \lambda a^2$</p>
<p align="center">$U = \alpha + \beta A + \gamma a + \delta aA + \lambda A^2$</p>

### 2.1 Nash Equilibrium and External Effects:
- To find the Nash equilibrium, we take the first-order conditions with respect to each player's strategy, assuming the other's is fixed:
<p align="center">
$\frac{\partial u}{\partial a} = \beta + \delta A + 2\lambda a = 0 \implies a^*(A) = -\frac{\beta + \delta A}{2\lambda}$
</p>
<p align="center">
$\frac{\partial U}{\partial A} = \beta + \delta a + 2\lambda A = 0 \implies A^*(a) = -\frac{\beta + \delta a}{2\lambda}$
</p>

- Solving these simultaneously for a symmetric Nash equilibrium ($a^* = A^* = e^*$):
<p align="center">
$e^* = -\frac{\beta + \delta e^*}{2\lambda} \implies 2\lambda e^* = -\beta - \delta e^* \implies (2\lambda + \delta) e^* = -\beta$
</p>
<p align="center">
$\mathbf{e^* = -\frac{\beta}{2\lambda + \delta}}$
</p>

- External Effect:
The external effect of $a$ on $U$ is $\frac{\partial U}{\partial a} = \gamma + \delta A$, and the external effect of $A$ on $u$ is $\frac{\partial u}{\partial A} = \gamma + \delta a$. At the Nash equilibrium, the external effect is 
 $\gamma + \delta e^* = \mathbf{\gamma - \frac{\beta \delta}{2\lambda + \delta} = \frac{\gamma(2\lambda + \delta) - \beta \delta}{2\lambda + \delta}}$

   - Positive external effect if $\gamma(2\lambda + \delta) - \beta \delta > 0$.
   - Negative external effect if $\gamma(2\lambda + \delta) - \beta \delta < 0$.

- **Substitutes or Complements:**
    - Strategies are substitutes if an increase in one leads to a decrease in the other's reaction function:  
      `∂a*(A)/∂A = -δ / 2λ` and `∂A*(a)/∂a = -δ / 2λ`.  
      They are substitutes if `δ > 0` and complements if `δ < 0`.


### 2.2 Symmetric Pareto-Efficient Allocation:
- A symmetric Pareto-efficient allocation maximises the sum of utilities $W = u + U = 2\alpha + (\beta + \gamma)(a + A) + 2\delta aA + \lambda(a^2 + A^2)$ subject to $a = A = e^{**}$.
  
- $W(e**) = 2\alpha + 2(\beta + \gamma)e** + 2\delta (e**)^2 + 2\lambda (e**)^2$

- The first-order condition is:

$$
\frac{dW}{de^{**}} = 2(\beta + \gamma) + 4\delta e^{**} + 4\lambda e^{**} = 0
$$

$$
\mathbf{e^{**} = -\frac{\beta + \gamma}{2(\lambda + \delta)}}
$$


- Comparing $e^*$ and $e^{**}$:
<p align="center">
$e^* - e^{**} = -\frac{\beta}{2\lambda + \delta} + \frac{\beta + \gamma}{2(\lambda + \delta)} = \frac{-\beta 2(\lambda + \delta) + (\beta + \gamma)(2\lambda + \delta)}{(2\lambda + \delta)2(\lambda + \delta)}
$
</p>
<p align="center">
$e^* - e^{**} = \frac{-2\beta\lambda - 2\beta\delta + 2\beta\lambda + \beta\delta + 2\gamma\lambda + \gamma\delta}{2(2\lambda^2 + 3\lambda\delta + \delta^2)} = \frac{-\beta\delta + 2\gamma\lambda + \gamma\delta}{2(2\lambda^2 + 3\lambda\delta + \delta^2)}
$
</p>

- Alternatively, consider the difference in first-order conditions. At $e*$, $\beta + \delta e* + 2\lambda e* = 0$. For Pareto efficiency, we want $\beta + \delta e** + 2\lambda e** + \gamma + \delta e** + 2\lambda e** = 0$, or $(\beta + \gamma) + 2(\delta + 2\lambda)e** = 0$.
- If the external effect is negative ($\gamma + \delta e < 0$), then at the Nash equilibrium, the marginal benefit to the individual is zero, but the social marginal benefit is negative. Therefore, the Pareto-efficient level should be lower: $\mathbf{e* > e** \iff \gamma + \delta e* < 0}$.


### 2.3 First and Second Mover Advantage:
- Assume player 1 moves first, choosing $a$. Player 2 then chooses $A$ to maximise $U$ given $a$, so:
  <p align="center">$A = A^*(a) = -\frac{\beta + \delta a}{2\lambda}$</p>
- Player 1 anticipates this and chooses $a$ to maximise their utility:

<p align="center">
$u(a, A^*(a)) = \alpha + \beta a + \gamma (-\frac{\beta + \delta a}{2\lambda}) + \delta a (-\frac{\beta + \delta a}{2\lambda}) + \lambda a^2$
</p>

- The first-order condition for player 1 is:
<p align="center">
$\frac{du}{da} = \beta - \frac{\gamma \delta}{2\lambda} - \frac{\delta(\beta + 2\delta a)}{2\lambda} + 2\lambda a = 0
$</p>
<p align="center">
$2\lambda \beta - \gamma \delta - \delta \beta - 2\delta^2 a + 4\lambda^2 a = 0
$</p>
<p align="center">$a_{first} = \frac{\delta(\gamma + \beta) - 2\lambda \beta}{4\lambda^2 - 2\delta^2}
$</p>

- The second mover will play $A(a_{first}) = -\frac{\beta + \delta a_{first}}{2\lambda}$.

- Consider substitutes ($\delta > 0$): The first mover internalises some of the negative externality (if it exists), potentially reducing their action compared to the simultaneous Nash. The second mover reacts to this lower action by playing a lower level as well. However, the first mover has strategically influenced the outcome to their benefit, generally leading to a first-mover advantage. The second mover will generally do worse because they are reacting to a choice that has already incorporated strategic considerations by the first mover.

- Consider complements ($\delta < 0$): The first mover's increase in action will be met by an increase from the second mover. The strategic commitment to a higher level can benefit the first mover. The second mover will generally do better as they can leverage the first mover's commitment to a higher level of the complementary strategy.

### 2.4 Chemical Intensive vs IPM:
- Let $a$ be the level of chemical use by Lower and $A$ be the level of chemical use by Upper.

- The second mover will play $A(a_{first}) = -\frac{\beta + \delta a_{first}}{2\lambda}$.

- Chemicals generate negative externalities (kill predators), so $\gamma < 0$. Increased use of chemicals by one raises the output of the user ($\beta > 0$) and lowers the output and raises the marginal productivity of chemical use in the other farm for any given level of other inputs. This implies that if Lower uses more chemicals, Upper's output decreases (captured by the $\gamma a$ term) and the effectiveness of Upper's chemical use might increase at the margin (captured by the $\delta aA$ term, with $\delta > 0$, meaning they are substitutes). The term $\lambda a^2$ captures diminishing returns to chemical use ($\lambda < 0$).

- IPM generates positive externalities, but the model is in terms of chemical use. So, a lower level of chemical use corresponds to a higher level of IPM.

- To map this, let $a$ and $A$ represent the intensity of chemical use. Increased chemical use by one lowers the other's output for a given chemical level ($\gamma < 0$). Increased chemical use by one might make the other's chemical use slightly more effective at the margin (due to fewer natural predators), so $\delta > 0$ (substitutes).

- The parameters would be:
  - $\mathbf{\beta > 0}$ (Direct benefit of own chemical use)
  - $\mathbf{\gamma < 0}$ (Negative externality of other's chemical use on output)
  - $\mathbf{\delta > 0}$ (Chemical use are substitutes; one's increased use raises the marginal product of the other's)
  - $\mathbf{\lambda < 0}$ (Diminishing returns to own chemical use)
  - $\mathbf{\alpha}$ (Baseline output)


## 3. Contracts

Let $u(y, e)$ be the utility function, increasing and concave in income $y$ and decreasing and convex in effort $e$. Production is $Q(E)$ with $Q' > 0, Q'' < 0$, where $E$ is total effort.

### 3.1 Agent owns the production function:
Effort is chosen to maximise utility: 
- Effort is chosen to maximise utility: $\max_{e} u(Q(e), e)$. The first-order condition is $u_y Q'(e) + u_e = 0$, or $-\frac{u_e}{u_y} = Q'(e)$ (marginal rate of substitution equals marginal product).
- Not applicable as there are no other parameters to determine.
- This is Pareto optimal because the agent internalises all costs and benefits of their effort.

### 3.2 Agent works under a contract with share $s$ for the owner:
- Effort is chosen to maximise utility: $\max_{e} u((1-s)Q(e), e)$. The first-order condition is $u_y (1-s)Q'(e) + u_e = 0$, or $-\frac{u_e}{u_y} = (1-s)Q'(e)$. The agent equates their MRS to a fraction of the marginal product.

- The owner chooses $s$ to maximise their profit $sQ(e*)$, where $e*$ is the agent's optimal effort given $s$. This will depend on the outside option of the agent (zero utility). The owner will choose $s$ such that the agent participates and owner profit is maximised.

- This is generally not Pareto optimal unless $s = 0$. The agent only receives a fraction of the output, so they will exert less effort than the socially optimal level (where they receive the full marginal product).

### 3.3 Agent pays a fixed sum $k$ to the owner:
- Effort is chosen to maximise utility: $\max_{e} u(Q(e) - k, e)$. The first-order condition is $u_y Q'(e) + u_e = 0$, or $-\frac{u_e}{u_y} = Q'(e)$. The agent equates their MRS to the marginal product.

- The owner chooses $k$ to maximise their profit $k$, subject to the agent achieving at least zero utility: $u(Q(e*) - k, e*) \ge u(0, 0)$, where $e*$ satisfies the FOC in step 1. The owner will extract all surplus above the agent's outside option.

- The level of effort is Pareto optimal because the agent receives the full marginal product of their effort at the margin. However, the distribution of surplus might not be considered socially optimal.

### 3.4 Owner offers a contingent renewal contract with wage $w$ to a team of $n$ identical agents:
- Each agent chooses effort to maximise utility: $\max_{e_i} u(w, e_i)$. The first-order condition is $u_e(w, e_i) = 0$. Since $u$ is decreasing in $e$, this implies a fixed effort level $e^*$ independent of the production.

- The owner chooses $w$ to maximise profit $Q(n e*) - n w$, subject to the agents achieving at least zero utility $u(w, e^*) \ge u(0, 0)$. The owner will choose the lowest $w$ that ensures participation.

- This is generally not Pareto optimal. The fixed wage does not link individual effort to the marginal product of team effort. Agents have no incentive to exert the optimal level of effort from a social perspective, leading to potential free-riding in the team.

### 3.5 Team of $n$ identical agents share equally in the product:
- Each agent $i$ chooses effort $e_i$ to maximise utility: $\max_{e_i} u\left(\frac{Q(E)}{n}, e_i\right)$, where $E = \sum_{j=1}^n e_j$.
    - The first-order condition for agent $i$ is $u_y\left(\frac{Q(E)}{n}, e_i\right) \frac{Q'(E)}{n} + u_e\left(\frac{Q(E)}{n}, e_i\right) = 0$.
    - In a symmetric equilibrium where $e_i = e$ for all $i$, the FOC becomes $u_y\left(\frac{Q(ne)}{n}, e\right) \frac{Q'(ne)}{n} + u_e\left(\frac{Q(ne)}{n}, e\right) = 0$, or $-\frac{u_e}{u_y} = \frac{Q'(ne)}{n}$.

- Not applicable as there is no owner setting parameters.

- This is not Pareto optimal (tragedy of the commons in effort). Each agent only receives $\frac{1}{n}$ of the marginal product of their effort, leading to under-provision of effort compared to the social optimum where they would internalise the full marginal product $Q'(ne)$.

### 3.6 Owner pays each worker $Q - x$:
- Each agent's income is $y = Q(E) - x$, where $E$ is the total effort of all workers. The individual worker's effort $e_i$ affects $Q(E)$. The agent chooses effort to maximise $u(Q(E), e_i) - x$. The first-order condition for agent $i$ is $u_y(Q(E) - x, e_i) Q'(E) + u_e(Q(E) - x, e_i) = 0$.

- The owner chooses $x$ to maximise profit $nx$, subject to the agents participating: $u(Q(E*) - x, e*) \ge u(0, 0)$, where $E* = n e*$ is the total effort under this scheme. The owner will set $x$ to extract all surplus.

- This is generally not Pareto optimal. While each worker's effort increases total output, they do not fully internalise the benefit of their marginal effort because $Q$ depends on the effort of all workers. There is a positive externality of one worker's effort on others' income, leading to under-provision of effort in the non-cooperative equilibrium.

### 3.7 Owner offers contingent renewal with fee $B$ and wage $w$:

- Once the agent pays $B$ and starts working, their effort decision is the same as in (d): $\max_{e} u(w, e)$, leading to a fixed effort level $e^*$.

- The owner chooses $w$ and $B$ to maximise profit, considering the agents' participation constraint. The present value of the profit stream per worker is:
  <p align="center">
  $-B + \sum_{t=0}^\infty \frac{Q(ne^*) - nw}{(1+r)^t}$
  </p>

  where $r$ is the discount rate. The agent will participate if the utility from the contract, considering $B$, is at least their outside option. The owner will set $w$ and $B$ to extract the maximum surplus while ensuring participation.

- Similar to (d), the effort level is generally not Pareto optimal because it is fixed and does not respond to the marginal product of effort. The upfront fee $B$ affects participation but not the marginal effort decision.

