# Introduction

## Problem Statement
Patient experience surveys are essential for evaluating hospital quality but are currently limited by manual review and inefficiency. This project aims to develop a scalable, automated way to extract insights from hospital and departmental patient experience surveys using sentiment analysis.

#### Data Structure
Due to HIPAA constraints and the inability to take data out of the UCLA Health ULEAD Platform, this repository contains only **dummy data** to demonstrate the pipeline.  

The included code reflects the **generalized framework and workflow** used for analysis, but the **specific pipeline and proprietary data used within UCLA Health are not shared** in this repository.

## Background
Patient experience is a key indicator of clinical quality and a determinant of hospital reimbursement through the CMS HCAHPS survey. However, HCAHPS has several limitations, including low response rates, sampling bias, mode effects, and an inability to fully capture patient sentiment. Free-text responses such as complaints and comments offer richer insights but are resource-intensive to analyze manually.

## Significance
At UCLA Health, improving patient experience is a central quality initiative. To enhance efficiency and impact, we implemented a **sentiment analysis model** that automatically scores patient comments as positive, neutral, or negative. This enables:

- Real-time monitoring of sentiment trends  
- Department-level benchmarking and prioritization of improvement efforts  
- Reduced manual workload and faster decision-making  

By integrating sentiment analysis, UCLA Health can better identify areas needing attention, ensure all patient voices are represented, and improve care delivery based on actionable insights.

## Prior Approaches and Gaps
Machine learning techniques such as **BERT** and **LSTM** have been applied in sentiment analysis across domains like social media and consumer reviews. Prior healthcare studies (e.g., Doing-Harris et al.) used NLP to identify key topics and emotions in patient comments, demonstrating value in automating qualitative analysis. However, recent models predicting patient satisfaction (e.g., Liu et al.) often rely solely on numeric or binary data, excluding free-text inputs. This gap highlights an opportunity to leverage NLP to utilize underexplored textual survey data and improve the understanding of patient experiences at scale.

# Approach

## Model Selection and Rationale
Prior work by Murarka et al. (2020) demonstrated that **RoBERTa**, an optimized version of BERT, outperformed traditional models such as LSTM and BERT in detecting complex mental health conditions like depression and PTSD. Building on this success, we selected **RoBERTa** as the foundation for classifying patient survey comments into positive, neutral, and negative sentiments due to its superior contextual understanding.

RoBERTa (Robustly Optimized BERT Pretraining Approach), developed by Meta AI, improves upon BERT by removing the next-sentence prediction objective, increasing training data volume, and using dynamic masking during pretraining. These enhancements allow RoBERTa to more accurately interpret word relationships and contextual nuances — essential for analyzing healthcare survey responses.

By combining **RoBERTa** for sentiment classification with **BERTopic** for topic modeling, our approach captures both the emotional tone and thematic structure of survey data, creating a multidimensional understanding of patient and visitor feedback.

## Addressing Gaps
Fine-tuning RoBERTa on UCLA Health survey data addresses major gaps in patient experience research — specifically, the lack of NLP-based approaches to analyzing free-text data. This enables scalable, automated classification of thousands of comments, stratified by hospital, department, or service type.

### Project Workflow
Our workflow transforms qualitative survey data into actionable decision-making tools for UCLA Health through the following steps:
1. Apply pre-trained and fine-tuned RoBERTa-based models to classify survey comments by sentiment (positive, neutral, negative).  
2. Use BERTopic to identify recurring themes and filter out irrelevant responses.  
3. Aggregate and visualize sentiment trends to guide department-level decision-making.  

This framework empowers hospital administrators and clinicians to:
- Make **data-driven decisions** using quantitative sentiment metrics.  
- **Reduce burnout** by automating manual survey review.  
- **Increase efficiency** through faster, evidence-based insights.  

### Planned Next Steps
- Filter survey data to exclude irrelevant responses (e.g., comments on decor).  
- Collect and incorporate domain expert feedback (e.g., through collaboration with the Manager of Service Excellence).  
- Evaluate RoBERTa model performance using standard NLP metrics.  
- Ensure sustainability through continuous collaboration with UCLA Health operations teams.  

---

# Methods

## Data Overview

### Sources
Survey data were accessed via UCLA Health IT’s **ULEAD** platform, which supports secure, cloud-based analytics. Three survey types were considered:
1. **Staff Needs and Performance**  
2. **Patient Experience**  
3. **Family/Visitor Experience**  

For this phase, only (2) and (3) were analyzed, as these directly reflect patient satisfaction. Future work may integrate (1) to correlate staff performance and well-being with patient outcomes.

### Collection Protocols
Data were collected during **CICARE rounds** — structured interviews following UCLA Health’s service model (“Connect, Introduce, Communicate, Ask, Respond, Exit”). These rounds are conducted by trained staff and medical students who record structured and free-text feedback. Observing CICARE rounds will further inform our understanding of survey administration and ensure model outputs align with real-world workflows.

### Ethical Considerations
All data collection complies with **HIPAA**. Patients provide informed consent, and identifiers are anonymized before analysis. During modeling, additional anonymization (e.g., redacting names or organizations) is applied to minimize potential bias and preserve confidentiality.

---

## Technical Details

### Variables
- **Independent Variables:** Hospital unit, free-text comments, and whether feedback is manually reviewed or model-assisted.  
- **Dependent Variables:** Sentiment scores, classification accuracy, and improvements in efficiency and decision-making speed.  

Sentiment predictions are calculated from preprocessed and tokenized free-text data. The resulting sentiment classifications (positive, neutral, negative) are aggregated by department to identify trends and outliers.

### Modeling Framework
Our NLP pipeline integrates three complementary models:
1. **BERT (Bidirectional Encoder Representations from Transformers):** Used for Named Entity Recognition (NER) to detect references to individuals or organizations.  
2. **BERTopic:** Performs unsupervised topic modeling to group comments into coherent themes and filter irrelevant text.  
3. **RoBERTa:** Conducts fine-grained sentiment analysis of free-text survey responses.  

### Procedure
1. **Data Preprocessing:** Remove blank entries, combine prompts and responses, and tokenize text.  
2. **Sentiment Classification:** Use RoBERTa to assign sentiment scores and adjust classifications where neutral predictions mask negative context (using a ±1.5 ratio threshold).  
3. **Topic Modeling:** Apply BERTopic to cluster comments into themes for filtering and thematic analysis.  
4. **Entity Recognition:** Use BERT NER to identify references to named staff; fine-tune thresholds to minimize false positives (e.g., misclassifying “Kaiser” as a person).  

### Quantitative Evaluation

#### BERT (NER)
Initial NER results show 7.2% of survey responses reference named individuals, but false positives (e.g., tools or organizations) remain. Threshold tuning is underway to improve classification accuracy for named entities.

#### BERTopic
Unsupervised BERTopic analysis produced **14 clusters**, with key topics centered on doctors, nurses, and staff interactions. While clusters vary slightly between runs, consistent themes emerge, allowing identification of major service-related topics. Parameter tuning continues to refine cluster quality and reduce overlap.

| Cluster | Percent | Top Words / Theme |
|----------|----------|-------------------|
| 1_nurses_team_here | 12.6% | Nurses and care team experiences |
| 0_doctors_me_are | 12.6% | Doctor interactions and communication |
| 3_they_questions_answer | 9.3% | Responsiveness and answering patient questions |
| 4_great_nothing_it | 8.6% | Positive general feedback (“great experience”) |
| -1_and_is_to | 8.6% | Miscellaneous or low-coherence cluster |
| 2_the_to_wait | 8.0% | Wait times and scheduling issues |
| 6_care_kind_and | 6.3% | Compassionate and kind care |
| 5_staff_friendly_very | 5.9% | Friendly and professional staff interactions |
| 9_no_thanks_thanks | 5.1% | Expressions of gratitude and satisfaction |
| 11_always_visits_they | 5.1% | Consistency across patient visits |
| 7_surgery_the_didn | 4.8% | Surgical experience and concerns |
| 8_md_mds_ava | 4.8% | Physician availability and attentiveness |
| 10_she_nurse_her | 3.2% | Nurse-specific references and gendered mentions |
| 12_10_explanation_to | 2.7% | Clarity and thoroughness of medical explanations |
| 13_ucla_first_is | 2.3% | First impressions of UCLA Health services |

These clusters collectively capture the dominant themes within UCLA Health’s patient and visitor feedback, emphasizing staff communication, compassion, and system-level operational experiences (e.g., wait times). The insights extracted from BERTopic provide an interpretable foundation for linking sentiment trends to specific care domains.

#### RoBERTa
RoBERTa sentiment scores span:
- Positive: [-2.77, 4.01]  
- Neutral: [-0.71, 2.19]  
- Negative: [-3.34, 2.38]  

Example predictions:  
| Sentiment | Score | Comment |
|------------|--------|---------|
| Positive | 4.01 | “My first time here at UCLA Health and it was the best!” |
| Negative | 2.38 | “Only downside is the parking situation here.” |
| Neutral | 2.19 | “Ms have been calling and keeping me updated.” |

RoBERTa generally aligns well with human sentiment perception, though contextual refinement is ongoing.

Sentiment trends were analyzed across hospitals and departments. At **Ronald Reagan Hospital**, “CAFE,” “COU,” and “ICU” units showed the highest positive sentiment, while “B PHARM,” “ER,” and “MADDIE” showed higher negative sentiment proportions.

---

## Statistical Analysis
Descriptive statistics were computed for categorical survey fields (e.g., “Was Kindness Practiced?”, “Was All Information Received?”). Free-text sentiment distributions were analyzed using RoBERTa predictions.

To compare **patient** vs. **visitor** sentiment, **proportional z-tests** were applied:
\[
z = \frac{p_1 - p_2}{\sqrt{p(1 - p)(\frac{1}{n_1} + \frac{1}{n_2})}}
\]
where:
- \( p_1, p_2 \): Proportions of negative responses  
- \( p \): Pooled proportion  
- \( n_1, n_2 \): Sample sizes for each group  

Significance was tested at \( \alpha = 0.05 \). This analysis identifies statistically meaningful differences in perceived care quality between patient and visitor populations and validates whether sentiment model outputs align with survey responses.

---

**Overall**, this pipeline — integrating RoBERTa, BERT, and BERTopic — provides an efficient, scalable, and ethically grounded framework for automating sentiment analysis of UCLA Health’s patient experience surveys.

---

# Results

## BERTopic

BERTopic is an unsupervised machine learning (ML)-driven topic modeling technique that leverages transformer-based NLP models called **BERT** (Bidirectional Encoder Representations of Transformers). BERTopic processes text bidirectionally—both left-to-right and right-to-left—and supports a modular framework that can incorporate manual expert labels, enabling semi-supervised modeling.

For this project, all raw text data from **patient**, **visitor**, and **staff** surveys were consolidated into a single dataframe. Stop words (e.g., “the,” “at,” “an”) were removed. However, some contextually insignificant words (e.g., “made,” “thing”) remained due to the limitations of standard stop-word lists.

A **word cloud** visualization of the most common terms was generated after preprocessing: 

<img width="552" height="285" alt="Screenshot 2025-11-04 at 4 13 39 PM" src="https://github.com/user-attachments/assets/60a3eb57-1208-40a9-b996-0ed6fbb2159d" />

BERTopic was then applied to the cleaned dataset, successfully identifying critical aspects of patient and visitor experiences. For example:

| Raw Text Data | Keyword Extractions (Data Representation) |
|----------------|------------------------------------------|
| “It is hard to see the doctors and usually they are rushing when they talk to me.” | [doctors, talk, hard, seemed, see, thing, little, wait, everything, dr] |
| “The staff have been very helpful and provides all the information.” | [information, helpful, staff, questions, proactive, day, everyone, ask, yes] |

These examples illustrate that BERTopic can identify key contextual terms—sometimes even words not explicitly present in the text (e.g., “proactive”)—through its semantic understanding from contextual embeddings.

Cluster maps were generated to group recurring themes into distinct “topics,” such as **“talk_doctors_hard”** and **“information_helpful_staff.”** These clusters highlight common patterns in patient and visitor experiences:
<img width="619" height="451" alt="Screenshot 2025-11-04 at 4 16 46 PM" src="https://github.com/user-attachments/assets/2dc05391-e475-4540-ba58-72e895a07181" />
<img width="625" height="432" alt="Screenshot 2025-11-04 at 4 17 26 PM" src="https://github.com/user-attachments/assets/eb682364-be07-4913-81cf-0fda4ed832e0" />

### Cluster Summary

| Cluster | Percent | Theme |
|----------|----------|-------|
| 1_nurses_team_here | 12.6% | Nurses and care team experiences |
| 0_doctors_me_are | 12.6% | Doctor interactions and communication |
| 3_they_questions_answer | 9.3% | Responsiveness and answering patient questions |
| 4_great_nothing_it | 8.6% | Positive general feedback (“great experience”) |
| -1_and_is_to | 8.6% | Miscellaneous or low-coherence cluster |
| 2_the_to_wait | 8.0% | Wait times and scheduling issues |
| 6_care_kind_and | 6.3% | Compassionate and kind care |
| 5_staff_friendly_very | 5.9% | Friendly and professional staff interactions |
| 9_no_thanks_thanks | 5.1% | Expressions of gratitude and satisfaction |
| 11_always_visits_they | 5.1% | Consistency across patient visits |
| 7_surgery_the_didn | 4.8% | Surgical experiences and concerns |
| 8_md_mds_ava | 4.8% | Physician availability and attentiveness |
| 10_she_nurse_her | 3.2% | Nurse-specific mentions |
| 12_10_explanation_to | 2.7% | Clarity and thoroughness of explanations |
| 13_ucla_first_is | 2.3% | First impressions of UCLA Health services |

These clusters provide a structured overview of recurring themes across UCLA Health survey data, emphasizing communication, compassion, and operational aspects such as wait times.

### Limitations and Future Work
While BERTopic effectively reduces manual review time for large volumes of text data, its accuracy can be improved by incorporating **manual labels from clinicians and operations staff**. Integrating domain-specific vocabulary—such as CICARE-related terminology—can also enhance interpretability and contextual precision.

---

## Sentiment Analysis

Although initial analysis was planned for only **patient** and **visitor** surveys, the scope was expanded to include **staff survey data** as well.

### Staff Survey Summary

| Metric | Count / Percentage |
|---------|-------------------|
| Total Surveys | 1,166 |
| Opportunities for Improvement = True | 81.4% |
| Resources Needed for Role = True | 83.4% |
| Resources Needed Listed | 14.1% |
| CICARE Practice Rating = 4 (Always) | 78.7% |
| CICARE Practice Rating = 3 (Usually) | 17.7% |
| CICARE Practice Rating = 2 (Sometimes) | 2.9% |
| CICARE Practice Rating = 1 (Never) | 0.7% |
| Need Follow-Up = True | 71.5% |

Although 78.7% of staff rated “Always” for CICARE practice, 71.5% still indicated a need for follow-up, suggesting that high self-ratings coexist with unmet needs or improvement opportunities.

---

### Patient and Visitor Surveys

We analyzed patient (n = 195) and visitor (n = 93) survey data side-by-side, comparing closed-ended responses, free-text sentiment, and proportions of negative feedback via **proportional z-tests**.

### Summary of Key Survey Metrics for Patient and Visitor Surveys

| Metric | Patient Surveys | Family/Visitor Surveys |
|---------|-----------------|------------------------|
| **Count** | 195 | 93 |
| **Kindness Practiced = “Yes”** | 91.3% | 92.4% |
| **All Information Received = “Yes”** | 81.5% | 87.0% |
| **Staff Responsiveness Rating** |  |  |
| 5 | 71.8% | 73.1% |
| 4 | 19.0% | 19.4% |
| 3 | 5.6% | 6.5% |
| 2 | 1.0% | 0.0% |
| 1 | 0.5% | 2.1% |
| **Follow Up Needed** | 9.2% | 8.6% |
| **Free Text Comment Response Rates** |  |  |
| Kindness Practiced | 74.6% | 79.8% |
| All Information Received | 55.8% | 69.1% |
| Staff Rating | 42.6% | 55.3% |
| Additional Notes | 33.5% | 30.9% |

### Sentiment Distribution Across Survey Prompts for Patient Free Text Responses

| Prompt | Positive Percentage | Neutral Percentage | Negative Percentage |
|---------|---------------------|--------------------|---------------------|
| **Staff Responsiveness Rating** | 48% | 22% | 30% |
| **Was All Info Received** | 43% | 37% | 20% |
| **Was Kindness Practiced** | 46% | 34% | 19% |


### Sentiment Distribution Across Survey Prompts for Visitor Free Text Responses

| Prompt | Positive Percentage | Neutral Percentage | Negative Percentage |
|---------|---------------------|--------------------|---------------------|
| **Staff Responsiveness Rating** | 66% | 24% | 10% |
| **Was All Info Received** | 44% | 42% | 14% |
| **Was Kindness Practiced** | 45% | 44% | 11% |


### Closed-Ended Response Comparison (Proportional z-Test for Negative Responses)

| Question | z-statistic | p-value | Significance |
|-----------|-------------|----------|---------------|
| Was Kindness Practiced | 0.316 | 0.752 | Not significant |
| Was All Info Received | 1.169 | 0.242 | Not significant |

### Free-Text Sentiment Comparison (Proportional z-Test for Negative Sentiment)

| Question | z-statistic | p-value | Significance |
|-----------|-------------|----------|---------------|
| Staff Responsiveness Rating | 2.706 | 0.007 | **Significant** |
| Was All Info Received | 0.998 | 0.318 | Not significant |
| Was Kindness Practiced | 1.518 | 0.129 | Not significant |

### Graphs
<img width="569" height="422" alt="Screenshot 2025-11-04 at 4 26 37 PM" src="https://github.com/user-attachments/assets/70a4ad3d-0357-465c-bba8-78eec3d87fbc" />
These visualizations show survey respondent counts and percentages, categorized by visitor or patient status, and response sentiment.

<img width="480" height="346" alt="Screenshot 2025-11-04 at 4 27 20 PM" src="https://github.com/user-attachments/assets/ee870654-f920-4bb3-9d7a-bd8fcd167de3" />
These visualizations above show survey respondent counts and percentages by UCLA the different Health facilities, categorized by response sentiment.

<img width="574" height="396" alt="Screenshot 2025-11-04 at 4 28 20 PM" src="https://github.com/user-attachments/assets/cc4846ef-8899-46a4-878a-526aac0249af" />
These visualizations show the counts and percentages of positive, neutral, and negative responses to each survey prompt.

<img width="561" height="362" alt="Screenshot 2025-11-04 at 4 28 58 PM" src="https://github.com/user-attachments/assets/2cd4a27e-ac90-425f-96d1-a684b53a7af3" />
These visualization shows the number of positive, neutral, and negative responses to each survey prompt for each UCLA Health facility.

<img width="617" height="288" alt="Screenshot 2025-11-04 at 4 29 24 PM" src="https://github.com/user-attachments/assets/4985daee-32d4-499d-aa8a-9ccded20a056" />
These visualization shows the number of positive, neutral, and negative responses to each survey prompt that received at least five responses, for each UCLA Health facility.

### Discussion

Patients and visitors expressed similar sentiments regarding kindness and general satisfaction. However, **visitors provided more detailed feedback** about communication and staff responsiveness—areas that directly affect family involvement in care. These findings suggest that enhancing information-sharing and responsiveness toward visitors could further improve overall patient experience outcomes.

---

## Named Entity Recognition (NER)

We applied **BERT Named Entity Recognition (NER)** to identify named persons and organizations within survey comments. BERT NER classifies entities into four categories: **Person (PER)**, **Organization (ORG)**, **Location (LOC)**, and **Miscellaneous (MISC)**.

### Observations
The base BERT NER model occasionally misclassified entities (e.g., “Kaiser” labeled as a person). To improve classification accuracy, we analyzed the model’s output weights and introduced threshold-based refinements.

| Class Label | Comment 130 (two named persons) | Comment 4 (named organization) |
|--------------|-------------------------------|--------------------------------|
| O | -0.93 | 0.01 |
| B-MISC | -0.88 | 0.37 |
| I-MISC | -2.42 | -3.15 |
| B-PER | **8.93** | **7.33** |
| I-PER | -1.96 | -1.90 |
| B-ORG | -0.26 | 0.74 |
| I-ORG | -2.89 | -3.20 |
| B-LOC | -0.18 | -0.20 |
| I-LOC | -2.36 | -2.61 |

### Threshold Tuning

| Threshold (T) & Solution | B-PER + I-PER Count | B-PER + I-PER Percent |
|---------------------------|--------------------|-----------------------|
| Solution 1 | 13 | 2.73% |
| Solution 2, T = 8 | 17 | 3.57% |
| Solution 2, T = 10 | 19 | **4.00%** |
| Solution 2, T = 12 | 21 | 4.42% |

Further breakdown of B-PER and I-PER counts:

| Threshold (T) & Solution | B-PER Count | B-PER % | I-PER Count | I-PER % |
|---------------------------|--------------|----------|--------------|----------|
| Solution 2, T = 8 | 13 | 2.73% | 4 | 0.84% |
| Solution 2, T = 10 | 15 | 3.15% | 4 | 0.84% |
| Solution 2, T = 12 | 17 | 3.57% | 4 | 0.84% |

The **T = 10% threshold** produced the most balanced differentiation of person vs. organization entities. This threshold-based adjustment reduced false positives such as “Kaiser” (ORG misclassified as PER) while maintaining sensitivity.

### Future Directions
Potential improvements include:
- Incorporating **domain-specific models** such as BioBERT or ClinicalBERT  
- Implementing **contextual word embedding augmentation (CWEA)** to expand labeled data  
- Leveraging **gazetteers** and **rule-based filters** for domain-specific correction  
- Fine-tuning transformer layers for higher recall and precision on healthcare-specific text

These steps would enhance the accuracy and adaptability of the NER pipeline for hospital survey data.

---




