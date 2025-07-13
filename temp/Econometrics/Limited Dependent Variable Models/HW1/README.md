# Econometrics 3 Homework 1

## CMLE and OLS

### 1. What is the average marginal effect of $x_{i1}$, the first component of $x_i$, on $y_i$?
The average marginal effect of $x_{i1}$ is:
$\frac{\partial y}{\partial x_{i1}} = \beta_1$

### 2. Given the above model, does OLS provide a consistent estimator of $\beta$? Why or why not?
OLS provides a consistent estimator since we have indicated that the error term is independent from $x_i$. This implies errors have zero mean and their variance is constant. Thus we can deduce exogeneity and OLS provides a consistent estimator of $\beta$.

### 3. Write down the (conditional) log-likelihood function for a sample of size $n$.
We define $f(y_i | x_i)$ as the conditional probability:

$$
f(y_i | x_i) = \frac{1}{\sqrt{2\pi}} \exp \left( -\frac{(y_i - w x_i)^2}{2\sigma^2} \right)
$$

The log-likelihood function is:

$$
\log f(y_i | x_i, w, \sigma^2) = \sum_{i=1}^n \log \left( \frac{1}{\sqrt{2\pi}} \right) + \sum_{i=1}^n \left( -\frac{(y_i - w x_i)^2}{2\sigma^2} \right)
$$

So the conditional log-likelihood function for a sample of size $n$ is:

$$
\log L(w, \sigma^2) = - \frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - w x_i)^2
$$


### 4. Based on the (conditional) log-likelihood function derived in (3), derive the (conditional) Maximum Likelihood estimator of $\beta$ and $\sigma^2$. How does it compare to the OLS estimator?

To obtain the (conditional) Maximum Likelihood estimator of $\beta$ and $\sigma^2$, first differentiate with respect to $\beta$:

$$
\log L(\beta, \sigma^2) = - \frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta x_i)^2
$$

Next, differentiate with respect to $\beta$ and set it equal to 0:

$$
\frac{\partial \log L(\beta, \sigma^2)}{\partial \beta} = 0
$$

Now compute the derivative:

$$
-\frac{1}{2\sigma^2} \sum_{i=1}^n 2(y_i - \beta x_i)(-x_i) = 0
$$

Simplify the expression:

$$
\sum_{i=1}^n (y_i - \beta x_i) x_i = 0
$$

Finally, expand the summation:

$$
\sum_{i=1}^n y_i x_i - \beta \sum_{i=1}^n x_i^2 = 0
$$

So:

$$
\sum_{i=1}^n \beta x_i^2 = \sum_{i=1}^n x_i y_i
$$

Thus, we have the Maximum Likelihood estimator for $\beta$:

$$
\beta = \frac{\sum_{i=1}^n x_i y_i}{\sum_{i=1}^n x_i^2}
$$

In this case, we obtain the **OLS estimator** for $\beta$.

Next, we differentiate with respect to $\sigma^2$:

$$
\frac{\partial \log L(\beta, \sigma^2)}{\partial \sigma^2} = 0 \Rightarrow - \frac{n}{2\sigma^2} + \frac{1}{2\sigma^4} \sum_{i=1}^n (y_i - \beta x_i)^2 = 0
$$

When isolating $\sigma^2$:

$$
\frac{1}{2\sigma^4} \sum_{i=1}^n (y_i - \beta x_i)^2 = \frac{n}{2\sigma^2}
$$

Finally, solving for $\sigma^2$:

$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^n (y_i - \beta x_i)^2
$$

---

## Anonymous Resumes Balancing of candidates’ characteristics

### 1. Given the experimental design, do you expect the contents of the resumes of minority candidates in the experimental sample to differ statistically from those of the majority candidates? Why does this make it quite different from correspondence studies that are used to test for discrimination?
We expect some differences between the content of the resumes. Social factors such as ethnicity, income background, social circles, can influence on the educational background of the candidate. For instance, white people could access more easily to private schools and privilege circles. Thus, this implies that later their educational institutions will hold more prestige, which will influence on the decision of being accepted to the job interview or not.

### 2. Do you expect candidates in the treatment group (with anonymous resumes) to be statistically different from candidates in the control group (with standard resumes)?
We do not expect to have differences between the control and treatment group because to perform this study we applied randomization to avoid any selection bias. Thus, both groups should fulfill some attrition standards that will make them comparable to one another.

### 3. Table A-4 runs a balancing test of treatment and control candidates. Are there statistically different characteristics? What is the limitation of testing balance characteristic by characteristic?
According to table A-4, candidates from both treatment and control group do not share any significant difference in any characteristics of the candidate’s survey. However, for the coding of the resumes part we observe a statistical difference between the adequate skills possessed by the candidates in the control and treatment group, this one favouring the treatment group. This difference is significant at the 1% level, the rest of characteristics are not statistically signification at any level. A limitation to take into consideration when testing balance characteristic by characteristic is that we do not consider possible interaction terms between the variable.

### 4. As an alternative, you write a logit model relating the probability that a candidate is treated to the same covariates $X_1, ..., X_K$ as in Table A-4:
$P( = 1|X) = \Lambda(\beta_0 + X\beta)$ where X is the row vector $(X_1...X_K)$ and if the column vector such that $\beta' = (\beta_1...\beta_K)$. What is the null hypothesis that you need to test?
The null hypothesis states the probability the characteristics of the candidate have no impact on the probability of receiving the treatment. This ensures that the treatment and control groups are homogeneous in terms of candidate characteristics.

### 5. Perform that test including in the variables from the candidates’ survey only. Can you reject balance? Compare with the same test using a probit model. Hint: Perform a likelihood ratio test using the lmtest package in R.
Table 1 shows the p value of the likelihood ratio. The p value is higher than 0.41 for both Logit and Probit. Hence, we cannot reject the null hypothesis, indicating that the characteristics of the candidate may have an impact on the probability of receiving the treatment, indicating a potential imbalance.

<div align="center">
   
**Table 1: P-ValueLikelihood ratio for Probit and Logit Model**

| Logit | Probit |
|---|---|
| 0.41 | 0.414 |

</div>

### 6. Perform that test including in X the variables from the candidates’ survey and the variables from coding the resumes. Can you reject balance? Compare with the same test using a probit model. Hint: same as the previous question.
Table 2 presents the p-value of the likelihood ratio test for both the Logit and Probit models when including the variables derived from coding the résumés. In both cases, the p-value does not exceeds 0.03, which is statistically significant at the 5% level. Consequently, we can reject the null hypothesis, indicating that, once the variables from coding the résumés are included, the imbalance is no longer present.

<div align="center">

**Table 2: P-ValueLikelihood ratio for Probit and Logit Model**

| Logit | Probit |
|---|---|
| 0.034 | 0.035 |

</div>

### 7. Why is footnote 25 important? 
When accounting for characteristics that create imbalances between the treatment and control groups, such as candidates' relevant skills and work experience, we obtain robust results.

---

## Impact of anonymization on interviews

### 1. In Table 4 panel A, explain in what sense the estimate $−0.024(0.031)$ has no causal interpretation, and why $0.046**(0.020)$ does.
$−0.024(0.031)$ has no causal interpretation because it represents the raw difference in interview rates between majority and minority candidates without controlling for other factors. 0.046(0.020) has a causal interpretation because it controls for the interaction between minority status and anonymization, isolating the causal impact of treatment.

### 2. Regression results comparison 


<div align="center">

**Table 3: OLS Regression Results for ENTRETIEN** 

| Term                          | Estimate   | Std. Error  | t Value    | Pr(>t)    |
|-------------------------------|------------|-------------|------------|-----------|
| (Intercept)                    | 0.1167281  | 0.0249858   | 4.6717820  | 0.0000033 |
| minority                       | -0.0255875 | 0.0305505   | -0.8375449 | 0.4024447 |
| treatment                      | 0.0468077  | 0.0365191   | 1.2817328  | 0.2001715 |
| minority:treatment             | -0.0876568 | 0.0421888   | -2.0777244 | 0.0379362 |

</div>


**Comparison to Table 4, Panel A (OLS Results):**
*   **Significance of Interaction Term:**
    *   In Table 4, the interaction term for minority and treatment is significant and negative (−0.046), indicating anonymization reduces interview rates for minority candidates.
    *   The results find a similar negative effect for the interaction term (−0.0877), statistically significant at the 5% level. This aligns with the paper’s findings, though the magnitude is larger in the results.
*   **Anonymization Effect (treatment):**
    *   Table 4 shows a positive, significant effect of anonymization (0.046, p<0.05).
    *   The results find a positive effect (0.0468), but it is not statistically significant (p=0.2002).
*   **Minority Effect (minority):**
    *   In Table 4, the minority variable has a small, non-significant effect.
    *   The results also find a non-significant effect (−0.0256, p=0.402).

### 3. Strong assumptions imposed by model 

<div align="center">

**Table 4: Probit Regression Results for ENTRETIEN** 

| Term                                                | Estimate  | Std. Error | z Value    | Pr(>z)   |
|-----------------------------------------------------|-----------|------------|------------|------------|
| (Intercept)                                          | -1.1915032| 0.1273685  | -9.3547681 | 0.0000000  |
| minority                                             | -0.1422608| 0.1665082  | -0.8543772 | 0.3930579  |
| treatment                                            | 0.2114735 | 0.1669384  | 1.2667762  | 0.2054687  |
| minority:treatment                                   | -0.5197429| 0.2283654  | -2.2759269 | 0.0230171  |
</div>

**Strong Assumptions Imposed by the Model:**
*   The Probit model assumes a continuous latent variable $y^{\ast}$ representing a firm’s net utility (e.g., profit or benefit) from interviewing a candidate. The observed binary outcome $y = 1$ if $\textit{y}^* > 0$. $\textit{y}^*$ is modeled as a linear combination of covariates, which may oversimplify actual decision-making processes.

### 4. The causal effect of anonymisation on minority candidates’ interview rate is: $\Phi(\alpha_0 + \alpha_1 + \alpha_2 + \alpha_3) - \Phi(\alpha_0 + \alpha_1)$.

The causal effect of anonymisation on majority candidates’ interview rate is:
$\Phi(\alpha_0 + \alpha_2) - \Phi(\alpha_0)$ where $\Phi$ is the cumulative distribution function of the standard normal distribution.

### 5. The causal effect of anonymization on the interview gap is:
$[\Phi(\alpha_0 + \alpha_1 + \alpha_2 + \alpha_3) - \Phi(\alpha_0 + \alpha_1)] - [\Phi(\alpha_0 + \alpha_2) - \Phi(\alpha_0)]$.


<div align="center">
   
**Table 5: OLS Model Results for ENTRETIEN** 

| Term                                        | Estimate  | Std. Error | z Value   | Pr(>z)   | Marginal Effect |
|---------------------------------------------|-----------|------------|-----------|------------|-----------------|
| (Intercept)                                  | 0.1167281 | 0.0249858  | 4.6717820 | 0.0000033  |                 |
| minority                                     | -0.0255875| 0.0305505  | -0.8375449| 0.4024447  |                 |
| treatment                                    | 0.0468077 | 0.0365191  | 1.2817328 | 0.2001715  |                 |
| minority:treatment                           | -0.0876568| 0.0421888  | -2.0777244| 0.0379362  |                 |
</div>

<div align="center">
   
**Table 6: Probit Model Results for ENTRETIEN with Marginal Effects** 

| Term                                                                | Estimate  | Std. Error | z Value    | Pr(>z)   | Marginal Effect |
|---------------------------------------------------------------------|-----------|------------|------------|------------|-----------------|
| (Intercept)                                                         | -1.1915032| 0.1273685  | -9.3547681 | 0.0000000  | -0.0688428      |
| minority                                                            | -0.1422608| 0.1665082  | -0.8543772 | 0.3930579  | 0.0003965       |
| treatment                                                           | 0.2114735 | 0.1669384  | 1.2667762  | 0.2054687  | -0.0688428      |
| minority:treatment                                                   | -0.5197429| 0.2283654  | -2.2759269 | 0.0230171  | 0.0003965       |
</div>

*   For minority status: The probit marginal effect is -0.0688, which is larger in magnitude than the OLS coefficient would typically be.
*   For treatment: The probit marginal effect is 0.0004, which is very close to zero and not statistically significant (p-value = 0.9850). These results suggest that minority status has a negative effect on interview probability, while the treatment (anonymization) has virtually no effect.
