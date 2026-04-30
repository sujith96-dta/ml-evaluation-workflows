# Annotation QA Review

## Common Issues Observed

### 1. Bounding Box Alignment
Some extraction regions showed inconsistent boundary placement affecting OCR accuracy.

---

### 2. Table Segmentation Issues
Table cell boundaries occasionally overlapped adjacent regions causing extraction mismatches.

---

### 3. OCR Character Confusion
Observed OCR confusion between:
- O and 0
- I and 1
- spacing inconsistencies

---

### 4. Entity Extraction Inconsistency
Logistics company names showed inconsistent spacing and formatting across predictions.

Example:
- Blue Dart
- BlueDart

---

### 5. Header Field Variations
Date formatting inconsistencies affected extraction normalization.

Examples:
- 2026-04-10
- 2026/04/10

---

# QA Recommendations

- Improve annotation consistency
- Normalize formatting during preprocessing
- Add validation checks for extraction pipelines
- Improve OCR post-processing workflows
- Expand edge case dataset coverage
