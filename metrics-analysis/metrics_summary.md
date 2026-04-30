# Metrics Summary Report

## Evaluation Objective

Evaluate OCR extraction performance across logistics document datasets using ground truth comparison workflows.

---

# Model Comparison

| Metric | Model V1 | Model V2 |
|---|---|---|
| Accuracy | 76% | 100% |
| Precision | 74% | 100% |
| Recall | 73% | 100% |
| F1 Score | 73.5% | 100% |

---

# Key Findings

## Model V1 Issues
- Formatting inconsistencies
- OCR character confusion (O vs 0)
- Spacing inconsistencies
- Header extraction errors
- Document normalization issues

---

## Model V2 Improvements
- Improved field extraction
- Better formatting normalization
- Reduced spacing inconsistencies
- Improved invoice number recognition
- Better shipper name extraction

---

# QA Analysis

Observed issues affecting Model V1 accuracy:

- Missing delimiter normalization
- OCR confusion between numeric and alphabetic characters
- Inconsistent whitespace handling
- Partial extraction of logistics entity names

---

# Final Evaluation

Model V2 demonstrated significantly improved extraction performance and reduced annotation inconsistencies compared to Model V1.

The evaluation workflow highlights the importance of:
- high-quality annotation
- dataset consistency
- OCR normalization
- QA validation workflows
- structured evaluation pipelines
