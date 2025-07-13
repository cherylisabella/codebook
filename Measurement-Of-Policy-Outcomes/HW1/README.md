# Measurement Homework 1

---

## Design Effect

### 1. Comment on formula

Design effect formula:  

$$deff = 1 + (m − 1) * ρ$$

The design effect measures the impact of clustering schools on the precision of estimates:

- ρ = within-school correlation  
- m = number of students within each school  
- (m − 1) * ρ = correlation between students in each PSU  
- Higher m → higher design effect  
- Higher ρ → higher design effect  
- deff ≥ 1 (two-stage sampling decreases precision)

---

### 2. Integer value for m

Given:  
- ρ ≈ 0.22  
- c₁/c₂ ≈ 41

$$
m^* = \sqrt{\frac{1 - \rho}{\rho} \cdot \frac{c_1}{c_2}} = \sqrt{\frac{1 - 0.22}{0.22} \cdot 41} ≈ 12.1
$$

---

### 3. m in relation to c₁/c₂

m increases as c₁/c₂ increases.

- Higher cost ratio → more expensive to visit schools → more students per school makes sense
- m is directly proportional to c₁/c₂

$$
\frac{∂m^*}{∂(c₁/c₂)} > 0
$$

- If ρ > 0 and c₁/c₂ > 0, then δm*/δ(c₁/c₂) > 0  
- If ρ < 0 and c₁/c₂ < 0, then δm*/δ(c₁/c₂) < 0  
- If ρ and c₁/c₂ have opposite signs, no real solution exists.

Since costs and correlation are positive in this context:  

$$ δm*/δ(c₁/c₂) > 0 $$

---

### 4. m in relation to ρ

m decreases as ρ increases.

- More correlation within schools → fewer students needed per school  
- m is inversely proportional to ρ

$$
\frac{∂m^*}{∂ρ} < 0
$$

This is due to the derivative of:

$$
\left(\frac{1 - \rho}{\rho}\right)
$$

which is negative for all ρ > 0.

---

## Missing Values

### 1. Number of Missing Values

<div align="center">

| Variable        | Missing Count |
|----------------|----------------|
| CHILDID        | 0              |
| S1_ID          | 0              |
| S4_ID          | 0              |
| X1RSCALK1      | 0              |
| X2RSCALK1      | 401            |
| X3RSCALK1      | 10060          |
| X4RSCALK1      | 2088           |
| X1MSCALK1      | 0              |
| X2MSCALK1      | 401            |
| X3MSCALK1      | 10060          |
| X4MSCALK1      | 2088           |
| X2SSCALK1      | 401            |
| X3SSCALK1      | 10060          |
| X4SSCALK1      | 2088           |
| X4AGE          | 2088           |
| X4HEIGHT       | 2088           |
| X_CHSEX_R      | 0              |
| X4LANGST       | 3427           |
| X4LOCALE       | 1720           |
| X4HTOTAL       | 3427           |
| X1PUBPRI       | 0              |
| X4PUBPRI       | 1720           |
| XPARHIGHED_1   | 0              |
| XPARHIGHED_2   | 0              |

</div>

---

### 2. Average Scores in Reading and Mathematics

<div align="center">

| Subject     | Mean | Standard Error |
|-------------|------|----------------|
| Reading     | 70.0 | 0.120          |
| Maths | 63.4 | 0.121          |

</div>

---

### 2a. Effect of Missing Values

#### Test 1: Missingness vs Child’s Sex

<div align="center">

| Test                  | Chi² | df | p-value |
|-----------------------|------|----|---------|
| Reading vs Sex        | 0.089 | 1 | 0.7649  |
| Maths vs Sex    | 0.089 | 1 | 0.7649  |

</div>

→ Accept H₀: Missingness is independent of sex.

#### Test 2: Missingness vs Initial Scores

<div align="center">

| Test              | Group 0 Mean (SE) | Group 1 Mean (SE) | p-value     |
|-------------------|------------------|-------------------|-------------|
| Reading           | 37.9 (0.09)      | 36.6 (0.21)       | 4.71e-08    |
| Maths       | 31.1 (0.10)      | 29.1 (0.23)       | 6.22e-15    |

</div>

→ Reject H₀: Missingness depends on initial scores.

#### Test 3: Missingness vs Parental Education

<div align="center">

| Test                     | Chi²  | df | p-value |
|--------------------------|-------|----|---------|
| Reading vs Parent 1      | 0.365 | 1  | 0.546   |
| Maths vs Parent 1         | 0.365 | 1  | 0.546   |
| Reading vs Parent 2      | 18.306| 1  | 0.000   |
| Maths vs Parent 2         | 18.306| 1  | 0.000   |

</div>

→ Reject H₀ for Parent 2: Missingness depends on education level.

---

### 2b. Bias in Sample Averages

Yes. Missingness is not completely random — it’s related to prior performance and parent education.  
Thus, averages based only on complete data are likely biased.

---

### 3. Imputation Method

**Extreme Imputation Range**

<div align="center">

| Subject  | Lower Bound | Upper Bound |
|----------|-------------|-------------|
| Reading  | 63.4        | 73.8        |
| Maths     | 56.3        | 67.9        |

</div>

---

### 4. Score Comparison by Parent Education

<div align="center">

| Test               | Group 0 Mean (SE) | Group 1 Mean (SE) | t-stat | p-value |
|--------------------|------------------|-------------------|--------|---------|
| Parent 1 Reading   | 65.2 (0.19)      | 73.3 (0.14)       | -34.50 | 0       |
| Parent 1 Maths     | 58.5 (0.19)      | 66.7 (0.15)       | -34.73 | 0       |
| Parent 2 Reading   | 66.5 (0.16)      | 74.7 (0.16)       | -36.33 | 0       |
| Parent 2 Maths     | 59.7 (0.16)      | 68.3 (0.16)       | -37.92 | 0       |

</div>

→ All differences are statistically significant.

---

### 5. Equal Sampling Probability

Let:  
- Nᵢ = number of students in school i  
- m = number of schools  
- Total students = ∑Nⱼ

Then:  

$$
P(\text{student}) = \frac{N_i}{\sum_j N_j} \cdot \frac{20}{N_i} = \frac{20}{\sum_j N_j}
$$

→ All students have equal probability of being selected.

---

### 6. Clustered SEs

<div align="center">

| Subject    | Mean | SE (Clustered) |
|------------|------|----------------|
| Reading    | 70.0 | 0.21           |
| Maths      | 63.4 | 0.22           |

</div>

---

### 7. Clustering vs Non-Clustering

<div align="center">

| Subject | SE (No Cluster) | SE (Clustered) |
|---------|------------------|----------------|
| Reading | 0.12             | 0.21           |
| Maths    | 0.12             | 0.22           |

</div>

→ Clustering increases SE due to within-school correlation.

#### Why Clustering is Still Used:
- Clustering underestimates SEs if ignored → false precision.
- Schools are natural clusters — logistically and contextually easier.
- More cost-effective than simple random sampling across entire population.

---

### 8. Regression With Clustering (Parental Education)

<div align="center">

| Model          | Intercept | Effect | SE (Int.) | SE (Eff.) | p-value |
|----------------|-----------|--------|-----------|-----------|---------|
| Reading (P1)   | 65.15     | 8.19   | 0.25      | 0.28      | 0.000   |
| Maths (P1)      | 58.53     | 8.20   | 0.23      | 0.28      | 0.000   |
| Reading (P2)   | 66.47     | 8.21   | 0.22      | 0.27      | 0.000   |
| Maths (P2)      | 59.68     | 8.61   | 0.22      | 0.28      | 0.000   |

</div>

---

### 9. Regression Without Initial Score Controls

- Parent education strongly predicts outcomes.
- Children of more educated parents score ~8 points higher.
- Results are statistically significant.

---

### 10. Regression With Initial Score Controls

<div align="center">

| Variable      | Reading Est. | SE   | p     | Maths Est. | SE   | p     |
|---------------|--------------|------|-------|-----------|------|-------|
| Intercept     | 41.02        | 1.93 | 0.00  | 42.48     | 1.71 | 0.00  |
| X_CHSEX_R     | -1.99        | 0.19 | 0.00  | 0.70      | 0.17 | 0.00  |
| XPARHIGHED_1  | 2.39         | 0.24 | 0.00  | 1.11      | 0.21 | 0.00  |
| XPARHIGHED_2  | 1.83         | 0.23 | 0.00  | 1.32      | 0.20 | 0.00  |
| X4AGE         | -0.02        | 0.02 | 0.33  | -0.08     | 0.02 | 0.00  |
| X4PUBPRI      | 1.13         | 0.30 | 0.00  | -0.26     | 0.26 | 0.32  |
| X4LANGST      | -1.68        | 0.28 | 0.00  | -0.47     | 0.25 | 0.06  |
| X1RSCALK1     | 0.76         | 0.01 | 0.00  | 0.85      | 0.01 | 0.00  |

</div>

Model Fit:  
- R² (Reading): 44.36%  
- R² (Maths): 57.27%

---

### Reading Scores (`X4RSCALK1`) Model:

**Significant predictors:**
- Being male decreases Reading scores by approximately 1.99 points (p < 0.001).
- Parent 1’s education increases scores by 2.39 points.
- Parent 2’s education increases scores by 1.83 points.
- Initial Reading score (`X1RSCALK1`) has a coefficient of 0.76 — each point adds 0.76 to the final score.

**Model fit:**  
Explains about 44.4% of the variance (R² ≈ 0.44).

---

### Maths Scores (`X4MSCALK1`) Model:

**Significant predictors:**
- Being male increases Maths scores by 0.70 points (p < 4.41e-05).
- Parent 1’s higher education increases scores by 1.11 points (p = 1.12e-07).
- Parent 2’s higher education increases scores by 1.32 points (p = 5.62e-11).
- Initial Maths score (`X1MSCALK1`) has a strong positive effect: 0.85 per point (p < 2e-16).

**Model fit:**  
Explains about 57.3% of the variance (R² ≈ 0.57).

---

### Importance of Controlling for Initial Scores

Controlling for initial scores is important for several reasons:

1. **Initial scores are strong predictors of final scores:**
   - In the Reading model, `X1RSCALK1` has a coefficient of 0.76.
   - In the Maths model, `X1MSCALK1` has an even stronger coefficient of 0.85.

2. **Controls for confounding and reduces bias:**
   - Some variation in final scores is already explained by initial ability.
   - Without controlling, we would overestimate the effect of variables like parental education or sex.

3. **Improves model fit and precision:**
   - R² increases substantially when initial scores are included.
     - Reading: from a lower baseline to 44.36%
     - Maths: up to 57.27%
   - This leads to a more accurate and better-fitting model with more reliable coefficient estimates.
