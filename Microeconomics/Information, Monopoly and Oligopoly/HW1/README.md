# Microeconomics - Part 2 Homework 1

---

## Part 1: Collusion and multi-market contact

### 1.1 Monopoly

V is the willingness to pay of consumers. Let c be the common marginal costs, n the number of firms in the economy, here c = 0.

If a single firm were active in market A or B, it would set a price `p_m = V`.  
The sum of the monopolist’s future discounted profits would be:

$$
\sum_{n=0}^{\infty} \delta^t \pi_{it} = \sum_{n=0}^{\infty} \delta^t \cdot \frac{V - c}{n} = V \sum_{n=0}^{\infty} \delta^t = \frac{V}{1 - \delta} = \frac{\Pi^m}{1 - \delta}
$$

---

### 1.2 Nash equilibrium

**Market A.** Two firms active: Firm 1 and Firm 2  
Nash equilibrium of the one-period simultaneous price-setting game?

Market A is a duopoly.  
The game:

- Stage 1: Firms 1 and 2 simultaneously set prices  
- Stage 2: Consumers simultaneously decide how much to purchase, and from which firm

Costs of production: 0

Profit functions: 

$$
\Pi_1 = (p - c_1) D(p) = p D(p)
$$  

$$
\Pi_2 = (p - c_2) D(p) = p D(p)
$$

In Bertrand competition, each firm undercuts the other until price = marginal cost = 0.

**Equilibrium:**
p₁* = p₂* = pₐ = c = 0



Firms earn zero profits.

<br>

**Market B.** Three firms: Firm 1, 2, and 3  
Same Bertrand logic:  

$$
p_B = 0
$$  

Firms earn zero profits.

---

### 1.3 Market A

#### (a) Collusive equilibrium (Tit-for-Tat)

Firms collude at `p = V` .  
Each has an incentive to cut price. Collusion can be enforced with Tit-for-Tat.

**No deviation:**

$$
\Pi_C = \sum \delta^t \pi_t = \sum \delta^t \cdot \frac{V}{2} = \frac{V}{1 - \delta} \cdot \frac{1}{2}
$$

**Deviation:**

$$
\Pi_D = (V - \epsilon) + \sum \delta^t \cdot 0 \approx V
$$

Sustainable if:

$$
\Pi_D \leq \Pi_C \Rightarrow \delta \geq \frac{1}{2}
$$

---

#### (b) Condition on $$\delta$$

$$
\delta \geq \frac{1}{2}
$$  

⇒ Firms value future collusive profits enough

---

### 1.4 Market B

#### (a) Collusive equilibrium (Tit-for-Tat)

Firms set `p = V`

**No deviation:**

$$
\Pi_C = \sum \delta^t \cdot \frac{V}{3} = \frac{V}{1 - \delta} \cdot \frac{1}{3}
$$

**Deviation:**

$$
\Pi_D = (V - \epsilon) + \sum \delta^t \cdot 0 \approx V
$$

---

#### (b) Condition on $$\delta$$

$$
\Pi_D \leq \Pi_C \Rightarrow \delta \geq \frac{2}{3}
$$

---

### 1.5 “Collusive linkage”

#### (a) Firm 3 only in Market B with share `s < 1`

**No deviation:**

$$
\Pi_{3,C} = \sum \delta^t \cdot V \cdot s = \frac{V \cdot s}{1 - \delta}
$$

**Deviation:**

$$
\Pi_{3,D} = V
$$

Incentive constraint:

$$
V \leq \frac{V \cdot s}{1 - \delta} \Rightarrow \delta \geq 1 - s
$$

---

#### (b) Firm 1 in both A and B

**No deviation:**

$$
\Pi_{1,C} = \frac{V}{2(1 - \delta)} + \frac{V(1 - s)}{2(1 - \delta)}
$$

**Deviations:**

- Market A only:
  
$$
\Pi_{1,D,A} = V + \frac{V(1 - s)}{2}
$$

- Market B only:
  
$$
\Pi_{1,D,B} = \frac{V}{2} + V
$$

- Both:
  
$$
\Pi_{1,D,AB} \approx 2V
$$

Order:

$$
\Pi_{1,D,A} < \Pi_{1,D,B} < \Pi_{1,D,AB}
$$

---

#### (c) Incentive constraint:

$$
\frac{V}{2(1 - \delta)} + \frac{V(1 - s)}{2(1 - \delta)} \leq 2V  
\Rightarrow V(1 + 1 - s) \leq 4V(1 - \delta)  
\Rightarrow 2 + s \leq 4\delta  
\Rightarrow \delta \geq \frac{2 + s}{4}
$$

---

#### (d) Combined condition

- Firm 1 & 2: $\delta \geq \frac{2 + s}{4}$
- Firm 3: $\delta \geq 1 - s$

Let’s find $s$ where:

$$
1 - s = \frac{2 + s}{4}
$$

which implies:

$$
4(1 - s) = 2 + s \quad \Rightarrow \quad s = \frac{2}{5}
$$

So:
- If $s < \frac{2}{5}$: $\delta \geq 1 - s$
- If $s > \frac{2}{5}$: $\delta \geq \frac{2 + s}{4}$
- If $s = \frac{2}{5}$: both equal


---

#### (e) Collusion most likely when:

$$
\delta \geq \max(1 - s, \frac{2 + s}{4})
\Rightarrow \text{minimum when } s = \frac{2}{5}
$$

---

## Part 2: Price competition and investment in cost reduction

### 2.1 Unobservable costs

#### (a) In hypothetical equilibrium

- **Demand:** $Dᵢ(pᵢ, pⱼ) = \frac{1}{2} + \frac{pⱼ - pᵢ}{(2t)}$

- **Profit:** $πᵢ = (pᵢ - c + δ*) · Dᵢ = (pᵢ - c + δ*) · (\frac{1}{2} + \frac{pⱼ - pᵢ}{2t})$


FOC:

$$
\frac{\partial \pi_i}{\partial p_i} = \frac{1}{2} + \frac{p_j - p_i}{2t} - \frac{p_i - c + \delta^*}{2t} = 0
$$

Solving:

$$
p_i = \frac{p_j + c - \delta^* + t}{2}
\Rightarrow p_i^* = t + c - \delta^*
\Rightarrow D_i = \frac{1}{2}
$$

---

#### (b) Corresponding investment cost and increase in profit

Investment cost:  

$$
\gamma(\delta) = \alpha \delta^2
$$

Marginal cost:

$$
\Delta \gamma = 2\alpha \delta^* \epsilon
$$

Profit gain:

$$
\Delta \pi = \frac{1}{2} \cdot \epsilon
$$

---

#### (c) Equilibrium value of the cost reduction  

Set marginal cost = gain: 

$$
2\alpha \delta^* = \frac{1}{2} \Rightarrow \delta^* = \frac{1}{4\alpha}
$$

---

### 2.2 Observable costs

#### (a) Each firm’s price, margin, and sales volume in the hypothetical equilibrium

Price:  

$$
p_i^* = t + c - \delta^{**}
$$  

Sales: $D_i = \frac{1}{2}$  
Margin: $p_i - (c - \delta^{**}) = t$


---
#### (b) Impact on the price set by Firm 2 in Period 2

Firm 1 reduces cost by ε: 

$$ p_1 = t + c - \delta^* - \epsilon $$

Firm 2 response:

$$
p_2 = \frac{p_1 + c - \delta^* + t}{2} = t + c - \delta^* - \frac{\epsilon}{2}
$$

---

#### (c) Impact of Firm 2’s price increase on the demand for Firm 1’s product

Change in demand:

$$
\Delta D_1 = \frac{1}{2t} \cdot \frac{\epsilon}{2} = \frac{\epsilon}{4t}
$$

---

#### (d) Impact of Firm 2’s price increase on Firm 1’s profit

Profit:

$$
\pi_1 = (p_1 - c + \delta^*) D_1
\Rightarrow \Delta \pi_1 = (t - \epsilon) \cdot \frac{\epsilon}{4t}
= \frac{t\epsilon - \epsilon^2}{4t}
$$

---
#### (e) Equilibrium value of the cost reduction

**Effects of ε:**

1. Investment cost:  `Δγ = 2α δ** ε`

2. Direct profit:   `Δπ_cost = ε / 2`

3. Strategic profit: `Δπ_strategic = (tε - ε²) / 4t`

4. Equilibrium:  
   `2α δ** ε = ε / 2 + (tε - ε²) / 4t`  
   `⇒ 2α δ** = 3 / 4`  
   `⇒ δ** = 3 / (8α)`

---

### Part 3: Economic intuition

$$
\delta^* = \frac{1}{4\alpha}, \quad \delta^{**} = \frac{3}{8\alpha}
\Rightarrow \delta^{**} > \delta^*
$$

**Reason:**  
When costs are observable, cost reduction influences rivals’ prices, boosting demand and incentivizing higher investment.

---
