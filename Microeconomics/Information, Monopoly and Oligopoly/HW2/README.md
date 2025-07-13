# Microeconomics - Part 2 Homework 2

---

## Part 1: Exclusivity clauses, incentives and bargaining

### 1.1 Socially efficient level of effort

The total social welfare function is: $$W(v) = (v_{min} + v) + \left(v_{min} + \frac{v}{2} \right) - C(v)$$  

since we maximize total welfare to determine the socially efficient level of effort and the consumer’s utility depends on effort $$v$$.

Differentiating with respect to $$v$$, the first-order condition (FOC) for maximization is:

$$
1 + \frac{1}{2} - C'(v_{opt}) = 0 \Rightarrow C'(v_{opt}) = \frac{3}{2}
$$

Thus, in the socially optimal case, effort should be chosen such that the marginal benefit of effort equals the marginal cost of effort.

---

### 1.2 Joint surplus, price paid by the consumer to the incumbent as the result of such bargaining

If the incumbent incurs effort cost $C(v)$, bargaining determines the price and joint surplus.

- The consumer gets utility $$v_{min} + v$$ from the incumbent’s good.
- If buying from an entrant, utility is $$v_{min} + \frac{v}{2}$$.
- The difference in value is: $\Delta v = (v_{min} + v) - (v_{min} + \frac{v}{2}) = \frac{v}{2}$

- The incumbent’s cost is $C(v)$, and its marginal cost is $$c_I$$.

The joint surplus is therefore:  

$$
S = \frac{v}{2} - (c_I - c_E)
$$

Since bargaining leads to a 50/50 split of the joint surplus, the consumer pays:

$$
p = c_I + \frac{1}{2} \left( \frac{v}{2} - (c_I - c_E) \right)
$$

---

### 1.3 Level of effort chosen by the incumbent

If exclusivity clauses are not allowed, the incumbent must compete with entrants. The incumbent will choose its effort level based on profit maximization.

The incumbent maximizes its profit:

$$
\pi = p - c_I - C(v)
$$

Substituting $$p$$:

$$
\pi = c_I + \frac{1}{2} \left( \frac{v}{2} - (c_I - c_E) \right) - c_I - C(v)
$$

Maximizing with respect to $$v$$, we get the first-order condition:

$$
\frac{1}{4} - C'(v_{no\ exclusivity}) = 0 \Rightarrow C'(v_{no\ exclusivity}) = \frac{1}{4}
$$

---

### 1.4 Level of effort chosen by the incumbent under modified assumption

If exclusivity clauses are allowed, the incumbent has monopoly power and captures full consumer surplus:  

$$
p = v_{min} + v
$$

Profit:

$$
\pi = (v_{min} + v) - c_I - C(v)
$$

First-order condition:

$$
1 - C'(v_{exclusivity}) = 0 \Rightarrow C'(v_{exclusivity}) = 1
$$

---

### 1.5 Minimum transfer, social surplus

The consumer would only accept exclusivity if offered at least the surplus it gets in the competitive case.

The transfer needed is:

$$
T \geq \frac{v}{2} - (c_I - c_E)
$$

If exclusivity is prohibited, the social surplus may increase if the exclusivity contract prevents optimal competition.  
Overall, banning exclusivity could either increase or decrease social surplus, depending on how much effort is lost due to lack of incentives.

---

## Part 2: Competition with exclusive and non-exclusive contracts

### 2.1 Continuum of equilibria 

In that problem, the consumer faces four options:

- To buy only A:  
  <div align="center">
    $$U_A - \min(p^e_A, p^n_A)$$, assume $$= U_A - p^e_A$$
  </div>

- To buy only B:  
  <div align="center">
    $$U_B - \min(p^e_B, p^n_B)$$, assume $$= U_B - p^e_B$$
  </div>

- To buy both:  
  <div align="center">
    $$U_N - (p^n_A + p^n_B)$$
  </div>

- To buy nothing:  
  <div align="center">
    $$0$$
  </div>


Based on net utility, the consumer will only buy A if:

$$
U_A - p^e_A \geq U_B - p^e_B \quad \text{and} \quad U_A - p^e_A \geq U_N - (p^n_A + p^n_B)
$$

To ensure the consumer does not buy both goods, set non-exclusive prices to infinity. Then we define:

$$
\begin{cases}
p^e_A = p + U_A - U_B \\
p^e_B = p
\end{cases}
\quad \text{with} \quad p \in (-(U_A - U_B), 0)
$$

Now, for consumer to choose A:

$$
U_A - p^e_A \geq U_B - p^e_B \Rightarrow U_A - (p + U_A - U_B) \geq U_B - p
\Rightarrow UB - p \geq UB - p
$$

which always holds. Thus, a continuum of equilibria exists where non-exclusive prices are infinite and consumer buys only A.

---

### 2.2 Weak preference 

Let us show that among all equilibria, the case:

$$
p^e_A = U_A - U_B \quad \text{and} \quad p^e_B = 0
$$  

is weakly preferred over others.

Profits:

$$
\pi_A = p + U_A - U_B, \quad \pi_B = p
$$

With this equilibrium:

$$
\pi_A = U_A - U_B, \quad \pi_B = 0
$$

Since $$p \in (-(U_A - U_B), 0)$$ and $$U_A > U_B$$, then $$-(U_A - U_B) < 0$$, so this choice is strongly preferred by Firm A.  
Firm B earns 0 and is indifferent.  
$\therefore$ This equilibrium is strongly preferred by Firm A, weakly by others.

---

### 2.3 Equilibrium where consumer chooses both non-exclusive offers

We show that another equilibrium exists with:

$$
\begin{cases}
p^e_A = p^n_A = U_N - U_B \\
p^e_B = p^n_B = U_N - U_A
\end{cases}
$$

Consumer chooses both non-exclusive offers if:

$$
U_N - (p^n_A + p^n_B) \geq U_A - p^e_A \quad \text{and} \quad U_N - (p^n_A + p^n_B) \geq U_B - p^e_B
$$

Given $$U_N = U_A + U_B$$ and substituting:

$$
U_A + U_B - (U_N - U_B + U_N - U_A) \geq U_A - (U_N - U_B)
$$

Simplifies to:

$$
2(U_A - U_N + U_B) > U_A - U_N + U_B
$$

which always holds. Thus, consumer prefers both goods when exclusive and non-exclusive prices are equal across firms.

---

### 2.4 Non-exclusive equilibrium

This non-exclusive equilibrium yields higher firm profits and greater total surplus than the exclusive equilibrium in Question 2.

**Exclusive:**

- $$p^e_A = U_A - U_B$$, $$p^e_B = 0$$
- Total profit = $$U_A - U_B$$

**Non-exclusive:**

- $$p^n_A = U_N - U_B$$, $$p^n_B = U_N - U_A$$
- Total profit = $$2U_N - U_A - U_B$$

Compare:

$$
U_A - U_B < 2U_N - U_A - U_B \Rightarrow U_A < 2U_N - U_A \Rightarrow 2U_A < 2U_N \Rightarrow U_N > U_A
$$

which is true since $$U_N = U_A + U_B$$

**Consumer Surplus:**

Non-exclusive:

$$
U_N - p^n_A - p^n_B = U_N - (U_N - U_B + U_N - U_A) = 2(U_A + U_B - U_N)
$$

Exclusive:

$$
U_A - p^e_A = U_A - (U_A - U_B) = U_B
$$

**Total Surplus:**

Non-exclusive:

$$
2U_N - U_A - U_B + 2(U_A + U_B - U_N) = U_A + U_B
$$

Exclusive:

$$
U_A - U_B + U_B = U_A
$$

Conclusion:

$$
U_A + U_B > U_A
$$

$\therefore$ The two-good equilibrium yields higher profit and higher total surplus.

---
