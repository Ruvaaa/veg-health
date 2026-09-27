# VegHealth

A Deep Learning project for detecting and classifying vegetable health from images.

VegHealth explores computer vision techniques for identifying whether vegetables are healthy or affected by common diseases. The project is being developed incrementally, with individual vegetable categories trained and evaluated as separate components within one larger system.

## Project Overview

Plant diseases can significantly affect crop quality and agricultural productivity. Early identification can help farmers respond before diseases spread extensively.

**VegHealth** uses image classification and Deep Learning to investigate how computer vision can assist with vegetable disease detection.

The project currently focuses on building and evaluating models for individual vegetables before integrating them into a broader vegetable health classification system.

## Current Vegetables

| Vegetable          | Status         |
| ------------------ | -------------- |
| 🍅 Tomato          | In development |
| 🥔 Potato          | Planned        |
| 🌶️ Pepper         | Planned        |
| 🥬 More vegetables | Planned        |

The project structure is designed so additional vegetables can be added without creating separate repositories.

## Repository Structure

```text
VegHealth/
│
├── Tomato/
│   ├── data/
│   ├── model.ipynb
│   ├── train.py
│   └── ...
│
├── Potato/
│   └── ...
│
├── Pepper/
│   └── ...
│
├── .gitignore
├── requirements.txt
└── README.md
```

Each vegetable has its own directory containing the data-processing, experimentation, training, and evaluation work associated with that vegetable.

## Tomato Health Classification

The first component of VegHealth focuses on tomato health classification.

The model is trained to distinguish between different tomato health conditions using image data.

### Current workflow

```text
Image Dataset
      ↓
Data Exploration
      ↓
Preprocessing
      ↓
Train / Validation Split
      ↓
Deep Learning Model
      ↓
Training
      ↓
Evaluation
      ↓
Prediction
```

The tomato model is being developed and evaluated before moving on to additional vegetables.

## Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* TensorFlow / Keras
* Jupyter Notebook
* Git & GitHub

Additional libraries will be added as the project develops.

## Dataset

The project uses image datasets containing vegetable images organized according to their health condition.

Because image datasets and trained neural-network models can be very large, raw datasets and large model files are not committed directly to this repository.

The repository instead contains the code and notebooks required to work with the data.

## Model Files

Trained model files such as:

```text
.keras
.h5
```

are excluded from Git when they exceed practical repository limits.

This keeps the GitHub repository focused on the **code, experiments, methodology, and documentation** rather than large binary artifacts.

## Goals

The main goals of VegHealth are to:

1. Explore Deep Learning for agricultural computer vision.
2. Build image-classification models for different vegetables.
3. Compare model performance across vegetable health conditions.
4. Develop reusable preprocessing and training workflows.
5. Investigate how computer vision could support early plant-disease detection.
6. Eventually integrate the individual models into a broader VegHealth system.

## Development Roadmap

### Phase 1 — Foundation

* [x] Set up project repository
* [x] Create vegetable-specific project structure
* [x] Begin tomato classification
* [x] Explore tomato dataset
* [ ] Complete tomato model evaluation

### Phase 2 — Expansion

* [ ] Add potato classification
* [ ] Add pepper classification
* [ ] Add additional vegetables
* [ ] Standardize preprocessing
* [ ] Compare model performance

### Phase 3 — Integration

* [ ] Develop a unified inference pipeline
* [ ] Accept an uploaded vegetable image
* [ ] Identify the vegetable
* [ ] Predict its health condition
* [ ] Return prediction confidence
* [ ] Build a simple user interface

### Phase 4 — Improvement

* [ ] Experiment with transfer learning
* [ ] Improve generalization
* [ ] Evaluate class imbalance
* [ ] Perform error analysis
* [ ] Test the system on unseen images

## Project Philosophy

VegHealth is being developed as a learning and research project, with an emphasis on understanding the complete Deep Learning workflow rather than simply training a model and reporting its accuracy.

The project covers:

**Data → Exploration → Preprocessing → Modeling → Training → Evaluation → Deployment**

## Disclaimer

VegHealth is an experimental computer vision project.

Model predictions should not be treated as a definitive agricultural diagnosis. Real-world deployment would require testing on representative field data and validation by agricultural experts.

## Author

**Ruvarashe S Nemaramba**

BSc Honours Artificial Intelligence
Africa University

GitHub: **Ruvaaa**

---

*VegHealth is a work in progress.*
