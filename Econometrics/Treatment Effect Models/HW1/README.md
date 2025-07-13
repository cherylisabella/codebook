# Homework 1 – Rubin Model and Roy Model (and Conditional Expectation Manipulation)

We consider a labor market training program that is offered to workers. This training may increase a given individual’s wage from $w_0$ to $w_1$. Attending the program has a cost $c$. Each agent knows their wage outcome, with and without training, with certainty. Both counterfactual wages in the population are heterogeneous, but the cost $c$ is common to everyone. 

<p align="center">$w_1 = w_0 + \delta$</p>

where $\delta$ and $w_0$ are heterogeneous in the population. We impose $\delta > 0$ and, at the beginning of this exercise, assume that $\delta$ and $w_0$ are mean-independent $E(w_0 | \delta) = E(w_0)$. This assumption will be relaxed later.

---

## Exercise Questions

1. What is the treatment impact of a given individual $i$? What is the average treatment impact in the population?

If worker *i* takes part in the training, their wage is:

<p align="center">$w_{1i} = w_{0i} + \delta_i$</p>

If they do not participate, their wage remains $w_{0i}$. The wage post-measurement is:

<p align="center">$w_{\text{After}, i} = w_{0i} + \delta_i \cdot T_i$</p>

where $T_i = 1$ if individual *i* participates in training, and 0 otherwise.

The treatment impact on individual *i* is simply:

<p align="center">$\delta_i$</p>

The average treatment impact in the population is the expected value of $\delta$:

<p align="center">$ATE = E(\delta)$</p>

---

2. Write the decision model of attending the training or not (Roy model).
   
Individuals decide to participate if the training effect exceeds the cost. Formally:

<p align="center">$T = 1 \text{ if and only if } \delta_i > c$</p>

Therefore, the expected initial wages are:

<p align="center">$E(w_0 | T = 1) = E(w_0 | \delta > c)$</p>
<p align="center">$E(w_0 | T = 0) = E(w_0 | \delta \leq c)$</p>

However, due to the mean independence assumption, these conditional expectations equal the unconditional expectation:

<p align="center">$E(w_0 | T = 1) = E(w_0 | T = 0) = E(w_0)$</p>


---

3. Based on that decision rule, people sort themselves into the training program. We observe average wages of treated and untreated. What does each of those averages measure?

The average wage of the treated group is:

<p align="center">$\bar{w}_{\text{trained}} = E(w_1 | T = 1) = E(w_0 + \delta | \delta > c)$</p>

The average wage of the untreated group is:

<p align="center">$\bar{w}_{\text{untrained}} = E(w_0 | T = 0)$</p>

The untreated group's average reflects selection effects since only those with $\delta \leq c$ remain untreated.

---

4. If you compare average wages of the treated and untreated, what parameter do you estimate? Interpret that parameter.

Comparing average wages of treated and untreated estimates the Average Treatment Effect on the Treated (ATT):

<p align="center">$ATT = E(w_1 | T = 1) - E(w_0 | T = 1)$</p>

Since $E(w_0 | T = 1) = E(w_0 | T = 0)$ under our assumptions, we estimate ATT unbiasedly by:

<p align="center">$\hat{ATT} = E(w_1 | T = 1) - E(w_0 | T = 0)$</p>

---

5. Compute the value of the average wage in each of these populations:
   
For group $Z = 0$ (standard program):

<p align="center">$E(w | Z = 0) = E[w_1 | \delta > c] \alpha + E[w_0 | \delta \leq c] (1 - \alpha)$</p>

where $\alpha = P(\delta > c)$.

For group $Z = 1$ (no training):

<p align="center">$E(w | Z = 1) = E(w_0)$</p>

For group $Z = 2$ (subsidized training, cost reduced by $s$):

<p align="center">$E(w | Z = 2) = E[w_1 | \delta > c - s] \beta + E[w_0 | \delta \leq c - s] (1 - \beta)$</p>

where $\beta = P(\delta > c - s)$.


---

6. Show that comparing group $Z = 1$ with group $Z = 0$ identifies the same parameter as in the absence of an experiment.

The difference in average wages is:

<p align="center">$E(w | Z = 0) - E(w | Z = 1) = \alpha (E[w_1 | \delta > c] - E[w_0 | \delta \leq c])$</p>

Given mean independence, this recovers the same ATT plus selection bias as the non-experimental comparison.

---

7. Explain why the mean-independence between $\delta$ and $w_0$ ensures that the naive wage comparison can estimate a treatment parameter without the experiment. Why can’t we obtain ATE, though?

Mean independence $E(w_0 | \delta) = E(w_0)$ ensures:

<p align="center">$E(w_0 | Z = 1) = E(w_0 | \delta \leq c, Z = 0)$</p>

Hence, the naive comparison estimates ATT without bias. However, ATE is not identified because we only observe treated outcomes for $\delta > c$.

---

8. Show that it is possible to identify the impact of the training on the population induced to participate by the subsidy $s$ using groups $Z = 2$ and $Z = 0$.

The subsidy acts as an instrument affecting only participation, not wages directly. LATE is defined as:

<p align="center">$LATE = \frac{E(w | Z = 2) - E(w | Z = 0)}{\beta - \alpha}$</p>

This captures the average treatment effect for those induced to train by the subsidy, i.e., $c > \delta > c - s$.

---

9. What can you estimate if $s = c$?

If the subsidy fully covers the cost $(s = c)$:

<p align="center">$LATE = E(w_1 | \delta > 0) - E(w_0 | \delta > 0)$</p>

Since $\delta > 0$ by assumption, everyone participates, allowing the true ATE to be calculated without selection bias:

<p align="center">$ATE = E(w_1 | Z = 2) - E(w_0 | Z = 1)$</p>

---

10. Assume that $w_0 = a + \rho \delta + \epsilon$ where $\epsilon$ is uncorrelated with $\delta$ and has mean zero. Show that the naive comparison of wages of treated and untreated absent an experiment would no longer identify a treatment parameter. Discuss the bias.

Assuming:

<p align="center">$w_0 = a + \rho \delta + \epsilon$</p>

Naive comparison yields:

<p align="center">$E(w_1 | \delta > c) - E(w_0 | \delta \leq c) = E(\delta | \delta > c) + \rho (E(\delta | \delta > c) - E(\delta | \delta \leq c))$</p>

Bias depends on the sign of $\rho$:
- $\rho > 0$: Overestimates the effect.
- $\rho < 0$: Underestimates the effect.
- $\rho = 0$: No bias.
  

---

11. Show that comparing group $Z = 1$ with group $Z = 0$ identifies the same treatment parameter as before.

The wage difference is:

<p align="center">$E(w | Z = 0) - E(w | Z = 1) = \alpha E(w_1 | \delta > c) + (1 - \alpha) E(w_0 | \delta \leq c) - E(w_0)$</p>

Since $w_1 = w_0 + \delta$, we expand the first term:

<p align="center">$\alpha E(w_0 + \delta | \delta > c) + (1 - \alpha) E(w_0 | \delta \leq c) - E(w_0)$</p>

Substitute $w_0 = a + \rho \delta + \epsilon$:

<p align="center">$\alpha E(a + \rho \delta + \epsilon + \delta | \delta > c) + (1 - \alpha) E(a + \rho \delta + \epsilon | \delta \leq c) - E(a + \rho \delta + \epsilon)$</p>

Now, break the expectations down:

<p align="center">$\alpha a + \alpha \rho E(\delta | \delta > c) + \alpha E(\epsilon | \delta > c) + \alpha E(\delta | \delta > c) + (1 - \alpha) a + (1 - \alpha) \rho E(\delta | \delta \leq c) + (1 - \alpha) E(\epsilon | \delta \leq c) - a - \rho E(\delta) - E(\epsilon)$</p>


By assumption, $E(\epsilon) = E(\epsilon | \delta) = 0$, so all $\epsilon$ terms drop. Now simplify the constants:

<p align="center">$a (\alpha + 1 - \alpha) - a + \alpha \rho E(\delta | \delta > c) + (1 - \alpha) \rho E(\delta | \delta \leq c) - \rho E(\delta) + \alpha E(\delta | \delta > c)$</p>

The constants cancel, leaving:

<p align="center">$\alpha \rho E(\delta | \delta > c) + (1 - \alpha) \rho E(\delta | \delta \leq c) - \rho E(\delta) + \alpha E(\delta | \delta > c)$</p>

Now, expand $E(\delta)$:

<p align="center">$E(\delta) = \alpha E(\delta | \delta > c) + (1 - \alpha) E(\delta | \delta \leq c)$</p>

Plugging this back, the $\rho$ terms collapse:

<p align="center">$\alpha \rho E(\delta | \delta > c) + (1 - \alpha) \rho E(\delta | \delta \leq c) - \rho [\alpha E(\delta | \delta > c) + (1 - \alpha) E(\delta | \delta \leq c)] + \alpha E(\delta | \delta > c)$</p>

Finally, the $\rho$ terms cancel completely, leaving:

<p align="center">$\alpha E(\delta | \delta > c)$</p>

