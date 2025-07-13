# Econometrics 3 Homework 2 

## Holidays with classmates

### Question 1: What are some unobserved determinants of the choice of alternative?

As in most cases, some variables influence the decision-making process that are not observable, such as:

- **Personal preferences on privacy**: Some students may prefer to pay more and have more private restrooms instead of common bathrooms shared with the whole floor.
- **Past experiences**: Some students may have had bad past experiences in hostels or staying at a friend's house that may influence their final choice.
- **Budget constraints**: Some students may be more at ease with their financial management and may have a larger budget to spend, while others running short on money may prefer to pay as little as possible.
- **Expectations of the trip**: Students may have different visions of what they expect from this trip. For instance, some could see this opportunity as a way to enjoy partying and may prefer hostels to meet more people and party more, while others may prefer to get the group together and stay at a private house to really connect with each other.

### Question 2: Assuming IIA, write down a statistical model (conditional choice probabilities) of the student’s choice allowing for alternative specific intercepts.

In this case, assuming the IIA (Independence of Irrelevant Alternatives), meaning that we assume the relative probabilities of two alternatives are the same regardless of other alternatives and their evaluations, we can write the following statistical model of the student's choice allowing for alternative-specific intercepts:

$$P(y_i = j \mid x_i) = \frac{\exp(x_i \beta_k + \alpha_k)}{1 + \exp(x_i \beta_k + \alpha_k)}$$

Where:

- $x_i$ represents unobservable variables we listed earlier.
- $\beta_k$ captures the marginal effect of choosing the desired outcome in the individual's utility.
- $\alpha_k$ is an alternative-specific intercept, varying if the individual has an unobserved preference for a certain outcome.
- $y$ is the final outcome chosen by the student.

This verifies the IIA assumption since even if we introduce another option, the relative probabilities of choosing a certain outcome remain the same.

### Question 3: Is the IIA assumption plausible? Explain.

Even though for the previous question we assumed that introducing a fourth option would have no effect on the relative probabilities of choosing that option, we cannot really see this assumption as plausible in this case. For instance, if the students were offered a much more attractive option that would increase everyone's utility, they would likely choose this one. A precise example could be if the student's school offered a subsidy for staying in a residence at a low price. This would disrupt the relative probabilities of the previous chosen outcomes, violating the IIA assumption. However, evaluating all possible unobservable variables, each option seems to fulfill at least one of the student's preferences, so we could argue that a fourth option would only slightly change the relative probabilities of each outcome. Thus, in all cases, the IIA assumption would be disrupted.

### Question 4: Ordered Probit Model and introduction of expected weather

In the case of introducing expected weather, the first option is no longer a plausible scenario; therefore, we violate the IIA assumption since relative probabilities are going to drastically change. The ordered probit assumes that a one-unit change in an explanatory variable shifts preferences consistently, without causing a structural change. However, in this context, the tent option is off the table when expected weather is included in the decision model. Thus, we no longer have linearity in the following model:

$$U_j = \alpha_j + Y \beta_j + M_j \gamma + \epsilon_j$$

As a solution, we could consider another model more appropriate to this situation, such as the Nested Logit, where choices follow a logical order that would be more consistent with the expected weather factor. We can consider the following model:

Denoting $Y_i$ as the final outcome:

$$
Y_i =
\begin{cases}
1, & \text{good weather, then we consider all 3 options } j \in [1, 2, 3] \\
0, & \text{bad weather, then we only consider 2 options } j \in [2, 3]
\end{cases}
$$


---

## Going to the gym

For this case, we consider two possible outcomes:

$$M_t \mid G_t, S_t \sim \text{Poisson}(\lambda(S_t) G_t)$$

Where:

- $M_t$ is the number of weight machines used.
- $S_t$ is the physical shape that will determine how many machines will she use.
- $G_t$ is a binary variable that indicates whether she attended the gym or not.
- $n$ is the total number of days in the sample.

Assume $G_t$ follows a Bernoulli distribution with two possible outcomes:

$$
G_t =
\begin{cases}
1, & \text{with probability } p = \frac{2}{7} \\
0, & \text{with probability } 1 - p = \frac{5}{7}
\end{cases}
$$


Now we can plug this value into our statistical model for the number of weight machines she uses on a sample of $n$ random days:

$$
M_t \sim \text{Poisson}(\lambda_t)
$$

We define the parameter $\lambda_t$ as a function of both $G_t$ and $S_t$:

$$
\lambda_t = G_t e^{\beta_0 + \beta_1 S_t}
$$

The probability distribution function of $M_t$ is:

$$
P(M_t \mid G_t, S_t) = \frac{\lambda_t^{M_t} e^{-\lambda_t}}{M_t!}
$$

And the conditional log-likelihood function is:

$$
\log \mathcal{L}(\lambda_t) = \sum_{t=1}^{n} \left[ M_t \log \lambda_t - \lambda_t - \log(M_t!) \right]
$$

Substituting $\lambda_t$, we get:

$$
\log \mathcal{L}(\beta_0, \beta_1) = \sum_{t=1}^{n} \left[ M_t \log (G_t e^{\beta_0 + \beta_1 S_t}) -  G_t e^{\beta_0 + \beta_1 S_t} - \log(M_t!) \right]
$$

---

## Nested Logit
### Question 1: Non-parametric Assumptions when $\lambda = 1$

We require the following assumptions:

1. The error terms are independent from one another.
2. The error terms are identically distributed.
3. The error term follows a type-I extreme value distribution, such that the CDF for the error term is:

$$
P(\epsilon_{ijt} \leq \epsilon) = \exp(- \exp(-\epsilon))
$$

The first assumption pertains to IIA (Independence of Irrelevant Alternatives). This assumption is questioned if the introduction of a third option changes the utility ratio between the first two options. For example, introducing a train as a third choice might impact the utility ratio between two flights. Specifically, a person might prefer the train over a short flight, potentially reducing the likelihood of choosing the short flight in comparison to the long one. 

The Hausman and McFadden (1984) test can be used to assess this assumption: if the parameters for a subset of alternatives are the same as those for the full set, we can conclude that the assumption holds.

We can test the second and third assumptions by plotting the residuals $\epsilon_{ijt}$ from the model. If their distribution matches the Type I extreme value CDF, we can infer that these assumptions are satisfied.

### Question 2: Non-parametric Assumptions when $\lambda = 0$

The parameter $\lambda$ determines the degree of independence in the unobserved utility across different choices within each group. A higher $\lambda$ means less correlation between these utilities.

When $\lambda = 0$, the errors within a group are perfectly correlated, implying that the error term follows the structure:

$$
v_{it}(\lambda) + \lambda \epsilon_{ijt} = v_{it}(0)
$$

which makes the error term constant within the group. In this case, the model assumes that consumers in the same group face identical unobserved factors influencing their decisions.

As a result, no additional non-parametric assumptions about the error term are required. The decision-making process becomes simpler: everyone within the group makes the same choice. They either all select a particular flight or all choose the outside option (such as not flying at all). Therefore, if $k$ represents the chosen option, the probability of selecting option $j$ is:

$$
P(k = j) = 1
$$

while the probability of choosing any other option is:

$$
P(k \neq j) = 0
$$

## Question 3: Log Likelihood Function

#### Probability

The probability is:

$$
P(\text{outside}) = \frac{1}{1 + D_t^\lambda}
$$

where $D_t$ is the overall attractiveness of all airline alternatives, and $\lambda$ is the nesting parameter (adjusted for correlation).

#### Unconditional Probability

To obtain the unconditional probability of choosing airline product $j$, we need the probability of choosing to fly and the probability of choosing $j$ given that they are flying.

First, the probability of choosing to fly is:

$$
P(\text{flying}) = 1 - P(\text{outside}) = \frac{D_t^\lambda}{1 + D_t^\lambda}
$$

Secondly, the probability of selecting $j$ given that an individual chooses to fly is:

$$
P(j | \text{flying}) = \frac{\exp(x_j \beta - \alpha p_j)}{D_t}
$$

Thus, the unconditional probability of choosing airline product $j$ is:

$$
P(j) = P(j | \text{flying}) \times P(\text{flying})
$$

Substituting the above expressions:

$$
P(j) = \left( \frac{\exp\left( \frac{x_j \beta - \alpha p_j}{\lambda} \right)}{D_t} \right) \times \left( \frac{D_t^\lambda}{1 + D_t^\lambda} \right)
$$

Simplifying:

$$
P(j) = \frac{D_t^{\lambda-1}}{1 + D_t^\lambda} \times \exp\left( \frac{x_j \beta - \alpha p_j}{\lambda} \right)
$$

#### Expression

Since option $i$ can either be an airline product or the outside option, we write:

$$
P(j | x_i, p_i) =
\begin{cases}
\frac{D_t^{\lambda-1}}{1 + D_t^\lambda} \times \exp\left( \frac{x_j \beta - \alpha p_j}{\lambda} \right), & \text{if } j \text{ is an airline product} \\
\frac{1}{1 + D_t^\lambda}, & \text{if } j \text{ is the outside option}
\end{cases}
$$

#### Log-Likelihood Function

The log-likelihood function for the nested logit model is the sum of the logarithm of probabilities of the observed choices across all individuals and alternatives. Using the conditional probability of choosing option $j$ from above, the log-likelihood function across all individuals $i$ and all possible options $j$ is:

$$
L_{\text{nested logit}} = \sum_i \sum_j y_{ij} \log(P(j | x_i, p_i))
$$

where $y_{ij}$ is an indicator variable equal to 1 if individual $i$ chooses option $j$ and 0 otherwise.

Substituting the probabilities for both the airline product and the outside option, the log-likelihood function is:

$$
L_{\text{nested logit}} = \sum_i \left[ \sum_{j \in \text{airline}} y_{ij} \log\left( \frac{D_t^{\lambda-1}}{1 + D_t^\lambda} \times \exp\left( \frac{x_j \beta - \alpha p_j}{\lambda} \right) \right) + y_{i, \text{outside}} \log\left( \frac{1}{1 + D_t^\lambda} \right) \right]
$$

Finally:

$$
L_{\text{nested logit}} = \sum_i \left[ \sum_{j \in \text{airline}} y_{ij} \left( (\lambda - 1) \log D_t - \log(1 + D_t^\lambda) + \frac{x_j \beta - \alpha p_j}{\lambda} \right) + y_{i, \text{outside}} \left( - \log(1 + D_t^\lambda) \right) \right]
$$

#### Unconditional Probability (When $\lambda = 1$)

If $\lambda = 1$, the nested logit model simplifies to a multinomial logit. In this case, choices are independent across the alternatives, and the probability of choosing alternative $j$ is:

$$
P(j) = \frac{\exp(x_j \beta - \alpha p_j)}{\sum_k \exp(x_k \beta - \alpha p_k)}
$$

Since the log-likelihood function is the same for all individuals $i$, this becomes:

$$
L_{\text{multinomial logit}} = \sum_i \sum_j y_{ij} \log(P(j))
$$

Finally:

$$
L_{\text{multinomial logit}} = \sum_i \sum_j y_{ij} \left( x_j \beta - \alpha p_j - \log \sum_k \exp(x_k \beta - \alpha p_k) \right)
$$

In the nested logit model, the probability of choosing alternative $j$ depends on both the attractiveness of the alternative and the structure of the nest:

$$
P(j) = P(j | \text{flying}) \times P(\text{flying})
$$

This then becomes:

$$
P(j) = \frac{D_t^{\lambda-1}}{1 + D_t^\lambda} \times \exp\left( \frac{x_j \beta - \alpha p_j}{\lambda} \right)
$$

Overall, the main difference is that alternatives within the nested logit are correlated, while choices in the multinomial logit are assumed to be independent.

### Question 4: Parameters

The marginal effects for the multinomial logit are the derivatives of the log-likelihood function with respect to its parameters:

$$
\frac{\partial L_{\text{multinomial logit}}}{\partial \alpha}, \quad \frac{\partial L_{\text{multinomial logit}}}{\partial \beta}
$$

where $$\alpha$$ is the marginal disutility of a price increase for consumers, and $$\beta$$ is a vector of tastes for characteristics of consumers.

The marginal effects of the nested logit are the derivatives of the nested logit log-likelihood function:

$$
\frac{\partial L_{\text{nested logit}}}{\partial \alpha}, \quad \frac{\partial L_{\text{nested logit}}}{\partial \beta}, \quad \frac{\partial L_{\text{nested logit}}}{\partial \lambda}
$$

where $$\lambda$$ is the nesting parameter. This is different from the multinomial logit, as in the multinomial logit, choices are assumed to be independent due to the Independence of Irrelevant Alternatives (IIA) assumption. In the nested logit model, the IIA assumption is relaxed as correlation is allowed between alternatives within the same nest.

### Question 5: Nested Logit vs Simple Multinomial Model

The nested logit model generally offers advantages over the basic multinomial logit when choices within groups are correlated. In the multinomial logit model, the Independence of Irrelevant Alternatives (IIA) assumption dictates that the relative probability of choosing between two alternatives remains unaffected by the presence of other alternatives. However, this assumption can be overly restrictive when choices are naturally grouped.

For example, airline products are often closer substitutes for each other than for outside options. The nested logit model addresses this by allowing for correlation within groups, or "nests," which is captured by the nesting parameter $\lambda$. If $\lambda$ is close to 1, the model behaves similarly to the multinomial logit, meaning there’s little correlation between choices within the nest. As $\lambda$ decreases, the correlation within the nest increases, making the model more flexible.

This structure allows the nested logit model to better capture substitution patterns. For instance, if a specific airline product becomes unavailable, the multinomial logit assumes consumers are equally likely to switch to any other option. In contrast, the nested logit model acknowledges that consumers are more likely to switch to another airline product within the same group rather than to an outside option.

Thus, the nested logit model provides a more realistic approach to analyzing choice behavior when alternatives within a group share common unobserved factors. By relaxing the IIA assumption within nests, it is better suited for modeling structured choices, such as airline selection.
