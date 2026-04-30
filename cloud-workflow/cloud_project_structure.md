# Simulated Cloud Project Structure

```text
cloud-storage/

logistics-ocr-evaluation/
│
├── annotations/
│   ├── cvat_exports/
│   ├── ground_truth/
│
├── predictions/
│   ├── model_v1/
│   ├── model_v2/
│
├── evaluation-configs/
│
├── metrics-reports/
│
├── mismatch-analysis/
│
└── qa-review/
```

---

# Workflow Notes

1. Annotated datasets exported from CVAT
2. Ground truth data uploaded to cloud project storage
3. Model predictions generated and stored
4. Evaluation configs executed through workflow orchestration
5. Metrics reports generated
6. QA analysis performed on extraction mismatches

---

# Evaluation Pipeline Components

- Dataset export handling
- Prediction comparison
- OCR evaluation workflows
- Annotation QA validation
- Metrics generation
- Report creation
