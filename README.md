# Introduction

## Problem Statement
Patient experience surveys are essential for evaluating hospital quality but are currently limited by manual review and inefficiency. This project aims to develop a scalable, automated way to extract insights from hospital and departmental patient experience surveys using sentiment analysis.

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


