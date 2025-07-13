# Econometrics 3 Homework 4

## The Modernization Theory

### 1. Statistical Model

The regression line in Figure 1 is generated from a simple cross-sectional model:

$$ d_i = \beta_0 + \beta_1 s_i + \varepsilon_i, $$

where $d_i$ is the Freedom House Political Rights Index for country $i$, $s_i$ is the average level of schooling, and $\varepsilon_i$ is the error term.

### 2. Observed Relationship

The relationship is not necessarily causal because it may suffer from omitted variable bias, reverse causality, or confounding factors. Unobserved influences such as historical institutions or cultural factors might affect both education and democracy, making the estimated association merely descriptive.

### 3. Statistical Model (panel-data)

Figure 2 is based on a panel-data approach that exploits time variation. A typical model is:

$$ d_{it} = \beta_0 + \beta_1 s_{it} + u_{it}, $$

or a specification that incorporates country or time fixed effects to control for unobserved heterogeneity.

### 4. Causality in Panel-Data

The relationship in Figure 2 is more likely to be causal than Figure 1 because panel-data techniques (e.g., fixed effects or first differences) control for time-invariant unobserved heterogeneity and common shocks, reducing the risk of omitted variable bias. However, time variant factors may still be relevant so this does not establish causality.

### 5. Unbalanced Panel

An unbalanced panel is one in which not every country (or observational unit) is present in every time period; some observations are missing for certain periods.


### 6. Model Assumptions

For the model

$$ d_{it} = \alpha\, d_{it-1} + \gamma\, s_{it-1} + \mu_t + v_{it}, $$

consistency of pooled OLS requires that:

$$ E(v_{it} \mid d_{it-1}, s_{it-1}, \mu_t) = 0, $$

and that the error terms are not serially correlated. The presence of $d_{it-1}$ implies that past errors might affect current outcomes; hence, no serial correlation is crucial to avoid dynamic panel bias.

### 7. Lagged Dependent Variable

Including the lagged dependent variable $d_{it-1}$ as a regressor accounts for the persistence (inertia) in democracy. It reflects the idea that past levels of political freedom influence current levels, thus capturing the dynamic nature of the process.

### 8. Statistical Significance of $\gamma$

If column (i) shows that the coefficient $\gamma$ on $s_{it-1}$ is positive and statistically significant, then the evidence supports the modernization theory. According to column i, the independent variables democracy and education are both positive and statistically significant where democracy has a value of 0.709 and a standard error of 0.035, and education has a value of 0.027 and a standard error of 0.004.

### 9. First Differences Model

Starting with

$$ d_{it} = \alpha\, d_{it-1} + \gamma\, s_{it-1} + \delta_i + \mu_t + v_{it}, $$

taking first differences gives:

$$ \Delta d_{it} = \alpha\, \Delta d_{it-1} + \gamma\, \Delta s_{it-1} + (\mu_t - \mu_{t-1}) + (v_{it} - v_{it-1}). $$

Note that the individual fixed effects $\delta_i$ cancel out.

### 10. Inconsistency in (pooled) OLS - Nickell Bias

In the first-differenced model, the regressor $\Delta d_{it-1}$ is mechanically correlated with the error term $(v_{it} - v_{it-1})$ because $v_{it-1}$ is present in both. This correlation violates the exogeneity assumption and results in Nickell bias, rendering pooled OLS inconsistent.

### 11. Instrumental Variable Strategy - Instrumenting $\Delta d_{it-1}$

Under the assumption that the original error terms $v_{it}$ are uncorrelated over time, one can use deeper lags (e.g., $d_{it-2}$) as instruments for $\Delta d_{it-1}$. This strategy is the basis for the Arellano--Bond estimator in dynamic panel data models.

### 12. Result of Instrumenting on modernisation theory

If, after instrumenting $\Delta d_{it-1}$, the coefficient on $s_{it-1}$ remains positive and statistically significant (as shown in column (iii)), then the results support the modernization theory. Education is now no longer positive or significant.

### 13. Control for Economic Development

Introducing $\log GDP_{it-1}$ as a regressor controls for the level of economic development, which is likely to affect political freedom directly. Since GDP may also be correlated with education, including it helps mitigate omitted variable bias. This is based on the theory that higher national income on average is more likely to have more resources spent on education and more agency resulting in democracy.

### 14. Omission of Time Dummies

Omitting time dummies ($\mu_t$) can lead to biased estimates because they capture common shocks or trends (such as global political changes or economic cycles) that affect all countries simultaneously. If these time-varying factors correlate with both education and political freedom, omitting them will bias the coefficient estimates.

### 15. Time Dummies Bias

When comparing regression results with and without time dummies, a significant change in the estimated coefficient on education (for example, a reduction in magnitude or a loss of statistical significance) suggests that part of the previously estimated effect was due to common time shocks. This indicates that the model including time dummies likely provides a more reliable, unbiased estimate of the causal impact of education on democracy.

---

## Differences-in-Differences with Heterogeneous Treatment Effects

### 1. Identification of $\Delta_i(t)$

$\Delta_i(t)$ is not identified because we do not observe the potential treated and untreated states at the same time.

### 2. Average Treatment Effect on the Treated (ATT)

The Average Treatment Effect on the Treated (ATT) at time $k$ over date range $W$, $ATT_k(W)$, measures the average treatment effect for states that implemented the policy before or at the beginning of the date range $W$.

### 3. Parallel Trends Assumption

The parallel trends assumption we will need to make is that, in the absence of treatment, treated and untreated states would have evolved similarly.

### 4. Definition of Potential Outcomes

Using the definition of potential outcomes:

$$ DD_D = E[y(1) \mid t = post, state = L] - E[y(0) \mid t = pre, state = L] - (E[y(1) \mid t = post, state = K] - E[y(0) \mid t = pre, state = K]), $$

Under the parallel trends assumption:

$$ E[y(0) \mid t = post, state = L] - E[y(0) \mid t = pre, state = L] = E[y(0) \mid t = post, state = K] - E[y(0) \mid t = pre, state = K], $$

Therefore:

$$ DD_D = E[y(1) - y(0) \mid t = post, state = L] + E[y(1) - y(0) \mid t = pre, state = K] - E[y(1) - y(0) \mid t = post, state = K]. $$

### 5. Treatment Effects Over Time

If treatment effects are stable over time, the middle term, $E[y(1) - y(0) \mid t = pre, state = K] = E[y(1) - y(0) \mid t = post, state = K]$, cancels out so we obtain:

$$ DD_D = E[y(1) - y(0) \mid t = post, state = L]. $$

If treatment effects are heterogeneous, the middle term does not cancel out, leading to biased estimates of the treatment effect.

A potential problem is that the comparison relies on assumptions about the evolution of treatment effects. If treatment effects vary over time and across states, then:

- The estimate may capture differences in the timing and magnitude of treatment effects rather than the true causal impact.
- The presence of treatment effect heterogeneity can lead to differential biases, particularly if states experience different degrees of policy impact over time.

### 6. Simplified Staggered Treatment Model with 2 States and 3 Periods
To construct the table, we first created a dataset containing the variables $state$, $period$, $treatment$, and an $suicide_{rate}$. Since no real data was provided, we randomly chose the suicide rate as the outcome variable.

<div align="center">

**Table 1: Results of the TWFE regression and computation of weights `w_it`**

| state | period | treatment | suicide_rate | residuals | weights        |
|-------|--------|-----------|--------------|-----------|----------------|
| 1     | 1      | 0         | 5            | 0         | 0.000000e+00   |
| 1     | 2      | 1         | 7            | 0         | -6.004800e+15  |
| 1     | 3      | 1         | 8            | 0         | 1.715657e+15   |
| 2     | 1      | 0         | 6            | 0         | 0.000000e+00   |
| 2     | 2      | 0         | 7            | 0         | 0.000000e+00   |
| 2     | 3      | 1         | 9            | 0         | 7.064470e+14   |

</div>

Next, we estimated a Two-Way Fixed Effects (TWFE) regression using the feols() function in R, controlling for both state and period fixed effects. After running the regression, I extracted the residuals $e_{it}$ and computed the weights using the formula:

$w_{it} = \frac{D_{it} e_{it}}{e_{it}^2}$


We aim to show that the coefficient $\beta$ in model 4 corresponds to the simple mean of  $DID_1$ and $DID_2$.

The two DiD estimators are constructed as follows:
$DID_1 = (y_{12} - y_{11}) - (y_{22} - y_{21}),$
$DID_2 = (y_{23} - y_{22}) - (y_{13} - y_{12}).$

We know from theory that the Two-Way Fixed Effects (TWFE) estimator of $\beta$ captures the average treatment effect across all periods and treatment groups. When treatment timing varies across groups, the TWFE estimator aggregates treatment effects, typically weighting different periods differently.

In this case, since there are only two DiD estimates ($DID_1$ and $DID_2$), and they are constructed symmetrically, the TWFE estimator takes their simple average: $\beta = \frac{DID_1 + DID_2}{2}.$

As discussed previously, the Two-Way Fixed Effects (TWFE) estimator aggregates different treatment effects over time. However, this aggregation may be biased if treatment effects are heterogeneous across groups and periods. 

We know that the TWFE estimate can be expressed as a weighted average of individual treatment effects, where some weights may be negative or disproportionately large for certain groups. This leads to an  inconsistency in identifying a single causal effect because the weights depend on the variation in treatment timing, rather than on a well-defined causal mechanism. If treatment effects change over time, the estimate $\beta$ may capture a mix of positive and negative effects. 

In addition, Difference-in-Differences provides a valid causal interpretation only if the parallel trends assumption is verfied in the absence of treatment. However, in a staggered treatment setting the comparisons made by TWFE may violate this assumption.

In a staggered treatment model with multiple states and periods, the Two-Way Fixed Effects estimator does not always provide a straightforward causal interpretation. One major issue is that it implicitly compares newly treated units to already treated units, rather than using a proper never-treated control group. As a result, states that receive treatment earlier are more likely to be assigned negative weights. This happens because, when later-treated groups are used as a comparison, early-treated groups may effectively serve as control units, even though they have already been exposed to the treatment.

Negative weights are also likely to appear in periods that are immediately before or after treatment adoption. Since TWFE averages treatment effects across all groups, it sometimes compares a newly treated unit in period $t$ to another unit that was treated in period $t-1$, rather than to an entirely untreated unit. 

An alternative would be the estimator developed by Callaway and Sant’Anna (2021). This method compares each treated group only to units that have never been treated, ensuring that treatment effects are not biased by previously treated units. By avoiding comparisons between groups that received treatment at different times, this estimator corrects the weighting issues in TWFE.

Another approach is the event-study specification with flexible leads and lags. This method avoids implicit comparisons between groups that received treatment at different times and helps assess whether treatment effects remain stable, increase, or decrease after implementation.


### 7. Goodman-Bacon (2021) - comments on results and treatment effect heterogeneity
Figure 6 from Goodman-Bacon (2021) shows that the different comparisons yield both positive and negative DiD estimates with varying weights. For example, the treatment effect estimate for states that adopted unilateral divorce reform before 1964 is strongly negative (-7.04) and has the highest weight (0.38), whereas the effect estimated using later-treated states as controls is much smaller and carries a lower weight (0.11). This suggests that the timing of treatment influences the estimated effect. 

Furthermore, the treatment effect when comparing reform states to non-reform states is also negative (-5.33). This shows that the overall DiD estimate of -3.08 is an average of heterogeneous effects across different comparisons. These results confirm that the TWFE estimate does not reflect a single well-defined treatment effect but captures a mix of treatment effects that vary across groups and periods.

