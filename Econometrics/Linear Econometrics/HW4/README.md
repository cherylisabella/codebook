# Econometrics Homework 4

## Exercise A
High fertility rates are often a concern for policy makers in developing countries. Many
studies have found a negative correlation between mother’s education and fertility. This then is
one of the reasons why promoting girl’s education has been advocated as one possible
mechanism to reduce fertility. Yet before drawing policy conclusions regarding the relationship
between fertility and mother’s education, one would want to know whether the relationship is
causal.

### 1. Endogeneity of Education
One reason for endogeneity could be `simultaneity bias`. Education may influence fertility (e.g., educated women may choose to have fewer children), but fertility may also influence education (e.g., women with children might be less likely to pursue higher education). This creates a feedback loop where the direction of causality is unclear.

Another reason could be `omitted variable bias`. Omitted variables, like personal values or socioeconomic conditions, can also play a crucial role in shaping both educational attainment and fertility decisions. For example, individuals from wealthier families often have better access to high-quality education due to financial resources, social networks, and educational expectations set by their parents. These families might also emphasize career advancement or personal development (or e.g. girls not even pushed to higher education at all), have better access to birth control, etc, leading to delayed or mitigated fertility. On the other hand, women from lower-income families may face constraints, such as the need to enter the workforce earlier, which can limit educational opportunities and lead to higher fertility rates. In any case, there are likely unobserved factors here which may be both affecting educational attainment and fertility, resulting in education potentially being endogenous.

Lastly, `measurement error` in education could also lead to simultaneity bias. Self-reported education levels could introduce additional endogeneity concerns and possibly bias estimates downward due to attenuation bias. 

### 2. Critique of Literature
The paper by Sander (1992) analyzes this issue for the US. Read the paper and critically discuss the approach used in this paper (and in particular the choice of instruments). Limit your critique to one page. Reference: W. Sander, “The Effect of Women’s Schooling on Fertility,” Economics Letters 40, 229-233.

The instruments used by Sander (parents' education) should fulfil two main conditions, namely that they are correlated with women's schooling and only have effects on fertility through the effects on women's education. On a surface level, parental education is a logical choice for an instrument because it is likely to be strongly correlated with the woman’s educational attainment. Typically, parents with higher education levels tend to provide more opportunities and support for their children's schooling (i.e. they encourage or simply can afford education), thus satisfying the relevance criterion for a good instrument. This link between parental and child education is well-established in the literature, as family background plays a significant role in shaping educational outcomes.

However, a more critical issue is whether parental education is a valid instrument in terms of homogeneity. As mentioned before, as an instrument, parental education should not have a direct effect on the daughter's fertility except through its impact on education. If unobserved factors (e.g. socioeconomic status or family planning preferences) influence both the parent's and the daughter's education and fertility, then the parental education instruments could lead to biased estimates. For example, more educated parents might instil specific family values or attitudes towards childbearing that could independently influence a woman’s fertility decisions, even after accounting for her education. So if parental education affects women's fertility other than through the effect of the women's education, then the exclusion restriction would be violated and it would not be a valid instrument. The study could perhaps benefit from more robustness checks to validate the results of the study (i.e. testing the instruments in different contexts to be more certain of their reliability).

The sample is focused on American women who have largely completed their fertility, which strengthens the validity of the results, as the sample includes women in their 30s and 40s whose childbearing is nearly finished. However, there may be some limitations to the sample selection. The study primarily relies on cross-sectional data, which may fail to capture dynamic decision-making processes regarding education and fertility over time. In other words, using cross-sectional data in this way hinders the ability to study the long-term (dynamic) effects of education on fertility; women's decisions for education and fertility are likely to change over time, and economic conditions, social norms, cultural shifts, etc, can have differing effects on different demographics over different periods. Longer-term longitudinal data could be used instead if this dimension is something that is desired to be studied (could be useful for analyzing causality here). Furthermore, although it is justified why younger women are not selected for the study (e.g. incomplete fertility), the fact that they are not included on some level discounts the fact that the relationship between education and fertility decisions may be changing concerning time due to social acceptance, general ability to secure contraceptives, and so on. In this way, the mindset and decision-making of younger women about education and fertility may be very different from relatively older women, not making the results as widely valid/generalizable for all women (more so just their older cohorts).

Sander compares the results from ordinary least squares (OLS) estimation with those from two-stage least squares (TSLS) to highlight the potential bias in OLS estimates. Interestingly, his findings show that education has a significant negative effect on fertility, regardless of whether it is treated as endogenous or exogenous. This suggests that the endogeneity of education may not be a major concern in this particular context, at least according to the Hausman test conducted in the study. However, it is important to note that the Hausman test could potentially be sensitive to the particular instrument used (not an issue here if we accept that parents' and women's education are strongly correlated) and the specific sample under study.

Overall, it is important to address endogeneity in studies of education and fertility. This is because the results hinge heavily on the validity of the instruments. The IV validity is questionable through a violation of the exclusion restriction; dynamic effects failed to be captured and there are sampling (selection) issues and advantages. The exogeneity of these instruments is difficult to prove conclusively, and the study could benefit from a more detailed discussion of alternative pathways through which parental education might influence fertility beyond their impact on the woman's schooling.


## Exercise B
We now want to understand the determinants of fertility, using a dataset on women in Botswana
in 1988. The dataset includes information on the number of children, years of education, age and
television ownership (among other variables). We also have a birth date of the women, and a
number of characteristics about the communities in which the individuals live (access to roads,
electricity,…). We want to analyze the effect of education on fertility.

### 1. Econometric Assumptions 
We can construct a dummy variable frsthalf equaling one if the woman was born during the first six months of the year. Which assumptions do you need in order to use frsthalf as an instrument for education? Are these assumptions reasonable in this case? Explain.

To be able to use `frsthalf` as an instrumental variable in the relation between education and fertility, we need to make sure that:

- `frsthalf` is relevant: it should be correlated, positively or negatively, to education. This assumption is likely reasonable because in countries like Botswana where the school year starts in January ((https://eduatlas.co.bw/botswana-2024-school-calendar/), being born in the first half of the year allows children to start school earlier. This could lead to higher levels of education on average.

- Exclusion-restriction holds: `frsthalf` should only explain fertility through its effect on education and not through other channels (not correlated with error term). However, this is a more delicate assumption. If there are cultural, seasonal, or health factors associated with being born in certain months that also affect fertility decisions, the exclusion restriction could be violated. For example, traditions or social norms around birth timing could directly affect fertility, weakening the instrument's validity (cf. Audrey M. Dorélien, 2016 for example). 

While the relevance assumption seems plausible, the exclusion restriction may be harder to justify, which makes the instrument potentially weak.

### 2. OLS and IV model estimations 
Estimate the following model with OLS and with IV (using frsthalf as an instrument for educ). Compare the estimations and interpret the results (and the differences between them) – estimations are reported below. 

Given: 
<p align="center">
  $children = \beta_0 + \beta_1educ + \beta_2age + \beta_3age^2 + u$
</p>

<div align="center">

|                         | **educ**        | **children (2)** | **children (3)** |
|-------------------------|-----------------|------------------|------------------|
| **frsthalf**             | -0.852*** (0.113) |                  |                  |
| **frsthalf.IV**          |                 | -0.171*** (0.053) |                  |
| **educ**                 |                 |                  | -0.091*** (0.006) |
| **age**                  | -0.108** (0.042) | 0.324*** (0.018) | 0.332*** (0.017) |
| **agesq**                | -0.001 (0.001)   | -0.003*** (0.0003) | -0.003*** (0.0003) |
| **Constant**             | 9.693*** (0.598) | -3.388*** (0.550) | -4.138*** (0.241) |
| **Observations**         | 4,361           | 4,361            | 4,361            |
| **R²**                   | 0.108           | 0.547            | 0.569            |
| **Adjusted R²**          | 0.107           | 0.546            | 0.568            |
| **Residual Std. Error**  | 3.711           | 1.497            | 1.460            |
| **F Statistic**          | 175.207***      | 1,751.100***     | 1,915.196***     |
| **Note:**                | *p*<0.1; **p**<0.05; ***p**<0.01 | | |

</div>
  
In the first stage of OLS, we first see that `frsthalf` is significantly and negatively associated with education, as expected (being born in the first half of the year is associated with -0.85 years of education, everything else equal). We note that $frsthalf$ only explains 10% of the variation of education, which is little.

For the effect of education on fertility, the following methods were used: an OLS estimation and an IV model using `frsthalf` as an instrument for education. As far as age is concerned, the estimates are significant and identical in both models: the positive coefficient on age and the negative coefficient on age squared indicate that fertility initially increases with age, but that the desire for additional children diminishes as women get older.

- `OLS`: A year increase in education is associated with lower fertility (- 0.09 children), all else equal. This result is significant at the 1% level.
- `IV`: The 2SLS estimates show a stronger negative effect of education on fertility compared to OLS: a year increase in education is associated with fewer children (- 0.17), all else equal. This difference suggests that OLS might be underestimating the causal effect of education on fertility, potentially due to omitted variables or reversed causality, as the OLS estimation is endogenous (cf Sander 1992). 


### 3. IV - first stage
What does the first stage of the IV tell you about the choice of frsthalf as an instrument?

`frsthalf` seems to be a good instrument in the sens that it has a significant negative effect on education : being born in first half of the year is associated with a 0.852 years decrease in education compared to being born in the last six months of the year. This was expected (cf. Question 1). The first stage has a small p-value that implies that `firsthalf` is a relevant instrument. Nevertheless, we note that this variable explains only 10% of the variation of education, which does raise concerns about the strength of the instrument.


### 4. Inclusion of age and the square of age
Do you think it was a good idea to include age and the square of age? Why or why not?

Including both $age$ and $age^2$ is useful because it captures the non-linear relationship between age and fertility. We assume that fertility often follows a non-linear pattern, potentially a quadratic pattern, where it is higher at certain ages and lower at others (such as younger age versus close to menopause). Without the quadratic term, the model may not adequately account for these changes across a woman's life cycle. The estimates on $age$ and $age^2$ are also statistically significant. Lastly, $age$ responds to omitted-variable bias, while including $age^2$ helps to avoid model misspecification.  


### 5. Policy application 
Can you conclude from these estimates that a policy increasing education for women is likely to reduce fertility? Explain

The results suggest a significant negative relationship between education and fertility. If the assumptions for the IV estimation hold, then increasing women's education is likely to reduce fertility.

The results suggest that education has a negative effect on fertility in both the OLS and IV regressions. However, education is only one of many factors influencing fertility, and it’s important to recognize that increasing education alone may not definitively reduce fertility across the entire population. Fertility decisions are influenced by other unobserved factors such as lifestyle, health, religious beliefs, and socio-economic conditions.

In the IV estimation, the instrument `firsthalf` affects fertility outcomes only for the group of women whose education was influenced by being born in the first half of the year. This means that the IV results provide a Local Average Treatment Effect (LATE). The IV estimate reflects the causal effect of education on fertility only among those influenced by their birth month, which limits broader generalisation. This subgroup thus may not be representative of the general population, and the effect of increasing education in other contexts or groups could differ.


### 6. Preferences
Some research suggests that exposure to soap operas in TV can be an effective mechanism in developing countries to reduce fertility.1 How would you test whether fertility preferences are different between people who own a television versus those that don’t have a television?

To test whether fertility preferences differ depending on television exposure (potentially to content like soap operas), we used OLS regression models. We use the variable "owning a TV" as a proxy for television exposure and, "ideal number of children" for fertility preferences, and add various controls to ensure the robustness of the relation. 

|                         | **(1)**           | **(2)**           | **(3)**           | **(4)**           |
|-------------------------|-------------------|-------------------|-------------------|-------------------|
| **tv**                  | -1.029*** (0.116)  | -0.348*** (0.117)  | -0.672*** (0.114)  | -0.740*** (0.114)  |
| **educ**                |                   | -0.166*** (0.009)  | -0.113*** (0.009)  | -0.108*** (0.009)  |
| **age**                 |                   |                   | 0.134*** (0.024)   | 0.079*** (0.025)   |
| **agesq**               |                   |                   | -0.001*** (0.0004) | -0.0004 (0.0004)   |
| **evermarr**            |                   |                   |                   | 0.539*** (0.075)   |
| **Constant**            | 4.713*** (0.035)   | 5.634*** (0.059)   | 2.603*** (0.342)   | 3.273*** (0.353)   |
| **Observations**        | 4,240             | 4,240             | 4,240             | 4,240             |
| **R²**                  | 0.018             | 0.096             | 0.159             | 0.169             |
| **Adjusted R²**         | 0.018             | 0.095             | 0.159             | 0.169             |
| **Residual Std. Error** | 2.199 (df = 4238)  | 2.111 (df = 4237)  | 2.036 (df = 4235)  | 2.024 (df = 4234)  |
| **F Statistic**         | 79.061*** (df = 1; 4238) | 224.686*** (df = 2; 4237) | 200.751*** (df = 4; 4235) | 172.826*** (df = 5; 4234) |
| **Note:**               | ^[p < 0.1; p < 0.05; p < 0.01] | | |

In all models, the coefficient for $tv$ is negative and statistically significant at the 1% level, which suggests that owning a television is associated with desiring fewer children. We note that the effect size diminishes slightly as more control variables are added, but it remains the most important coefficient observed in our models. For example, the effect of owning a TV on fertility preferences is 7 times more substantial than the effect of an additional year of education.

As expected, an increase in education is associated with desiring fewer children, consistent with what we found in the questions above. Note that here, we did not use IV to estimate education, as the actual level of education and the number of children desired is more likely to be endogenous than the actual number of children. The positive coefficient on age and the negative coefficient on age squared indicate that fertility preferences initially increase with age, but are slower and slower (while older women may desire more children, the desire for additional children diminishes as they get older). Finally, as expected, being ever married is associated with desiring more children. All these relations (except $agesq$ in model 4) are statistically significant at the 1% level.



### 7. Alternative experimental design
How would you proceed if you want to test whether television ownership has an effect on fertility?

The available data are not sufficient to allow us to identify a causal relationship between fertility and TV ownership, as we don't know the preference in fertility/actual fertility before having a TV, or the preference change/actual fertility after owning it. Therefore, to test whether television ownership affects fertility, we could construct an RCT. It helps establish causality by randomly assigning participants to treatment and control groups, thus eliminating confounding factors and providing unbiased estimates. Unlike observational studies, which are vulnerable to endogeneity concerns due to omitted variable bias, simultaneity, and measurement error, RCTs inherently control for these issues through random assignment.

In this case, endogeneity may arise because education and fertility are influenced by shared factors, such as socioeconomic status, cultural norms, or family planning preferences. Randomly assigning participants to receive educational interventions addresses these confounding factors, isolating the effect of education on fertility.

Design of the RCT:

1. Population: The RCT would target a sample of adolescent women in a developing country setting where high fertility rates are common, and educational attainment varies.
2. Random Assignment: Participants would be randomly assigned to two groups:
3. Treatment Group: Receives additional years of formal schooling or targeted educational support programs.
4. Control Group: Follows the existing education system without additional intervention.
5. Intervention: The educational intervention could include scholarships, conditional cash transfers, or additional tutoring to ensure the treatment group completes a higher level of schooling than the control group.
6. Data Collection: Data will be collected on both groups over several years, focusing on educational attainment and fertility outcomes.
7. Additional variables such as socioeconomic background, access to healthcare, and family planning information would also be recorded to understand potential moderating factors.

Outcome Measures:
- The primary outcome of interest is the number of children per woman (fertility rate). Secondary outcomes include changes in fertility preferences, marriage age, and contraceptive use.

Expected Challenges and Solutions:

- Ethical Considerations: Providing additional education to some participants but not others may raise ethical concerns. These can be mitigated by ensuring the control group also receives some benefits (e.g., information on family planning) and by obtaining informed consent.
- Attrition: Longitudinal studies may suffer from participant dropout. Mitigating this requires regular follow-ups, small incentives, and engaging local stakeholders to keep participants involved.
- Generalisability: While the RCT offers high internal validity, results may be context-specific. Replicating the study in different regions could enhance external validity.

Overall, using an RCT allows for a rigorous examination of the causal effect of education on fertility by addressing endogeneity through random assignment. This study could yield valuable insights into education’s role in shaping fertility behaviours, helping policymakers develop more effective interventions to promote lower fertility rates through educational policies.
