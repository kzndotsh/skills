# Phase 02: Ml Fundamentals

Upstream commit `1a8c4fd`. 21 lessons. Path pattern: `phases/02-ml-fundamentals/<lesson>/docs/en.md`.
Audit status: Not audited.

Columns: Type = Build or Learn; Lang = code file types; Quiz = has quiz.json; Out = reusable artifacts in outputs/; Trust = audit result (blank dash means not audited). Fetch a lesson per `repo-guide.md`.

| # | Folder | Title | Type | Time | Lang | Quiz | Out | Motto | Prerequisites | Trust |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `01-what-is-machine-learning` | What Is Machine Learning | Learn | ~45 minutes | py | y | 1 | Machine learning is teaching computers to find patterns in data instead of writing rules by hand. | Phase 1 (Math Foundations) | - |
| 02 | `02-linear-regression` | Linear Regression | Build | ~90 minutes | jl, py | y | 1 | Linear regression draws the best straight line through your data. It is the "hello world" of machine learning. | Phase 1 (Linear Algebra, Calculus, Optimization), Phase 2 Lesson 1 | - |
| 03 | `03-logistic-regression` | Logistic Regression | Build | ~90 minutes | jl, py | y | 1 | Logistic regression bends a straight line into an S-curve to answer yes-or-no questions with probabilities. | Phase 2 Lesson 1-2 (What Is ML, Linear Regression) | - |
| 04 | `04-decision-trees` | Decision Trees and Random Forests | Build | ~90 minutes | py | y | 1 | A decision tree is just a flowchart. But a forest of them is one of the most powerful tools in ML. | Phase 1 (Lessons 09 Information Theory, 06 Probability) | - |
| 05 | `05-support-vector-machines` | Support Vector Machines | Build | ~90 minutes | jl, py | y | 1 | Find the widest street between two classes. That is the entire idea. | Phase 1 (Lessons 08 Optimization, 14 Norms and Distances, 18 Convex O… | - |
| 06 | `06-knn-and-distances` | K-Nearest Neighbors and Distances | Build | ~90 minutes | py | y | 1 | Store everything. Predict by looking at your neighbors. The simplest algorithm that actually works. | Phase 1 (Lesson 14 Norms and Distances) | - |
| 07 | `07-unsupervised-learning` | Unsupervised Learning | Build | ~90 minutes | py | y | 1 | No labels, no teacher. The algorithm finds structure on its own. | Phase 1 (Norms & Distances, Probability & Distributions), Phase 2 Les… | - |
| 08 | `08-feature-engineering` | Feature Engineering & Selection | Build | ~90 minutes | py | y | 1 | A good feature is worth a thousand data points. | Phase 1 (Statistics for ML, Linear Algebra), Phase 2 Lessons 1-7 | - |
| 09 | `09-model-evaluation` | Model Evaluation | Build | ~90 minutes | jl, py | y | 1 | A model is only as good as the way you measure it. | Phase 1 (Probability & Distributions, Statistics for ML), Phase 2 Les… | - |
| 10 | `10-bias-variance` | Bias-Variance Tradeoff | Learn | ~75 minutes | py | y | 1 | Every model error comes from one of three sources: bias, variance, or noise. You can only control the first two. | Phase 2, Lessons 01-09 (ML basics, regression, classification, evalua… | - |
| 11 | `11-ensemble-methods` | Ensemble Methods | Build | ~120 minutes | py | y | 2 | A group of weak learners, combined correctly, becomes a strong learner. This is not a metaphor. It is a theorem. | Phase 2, Lesson 10 (Bias-Variance Tradeoff) | - |
| 12 | `12-hyperparameter-tuning` | Hyperparameter Tuning | Build | ~90 minutes | py | y | 1 | Hyperparameters are the knobs you turn before training starts. Turning them well is the difference between a mediocre model and a… | Phase 2, Lesson 11 (Ensemble Methods) | - |
| 13 | `13-ml-pipelines` | ML Pipelines | Build | ~120 minutes | py | y | 1 | A model is not a product. A pipeline is. The pipeline is everything from raw data to deployed prediction, and every step must be… | Phase 2, Lesson 12 (Hyperparameter Tuning) | - |
| 14 | `14-naive-bayes` | Naive Bayes | Build | ~75 minutes | py | y | 1 | The "naive" assumption is wrong, and it works anyway. That's the beauty of it. | Phase 2, Lessons 01-07 (classification, Bayes' theorem) | - |
| 15 | `15-time-series` | Time Series Fundamentals | Build | ~90 minutes | py | y | 1 | Past performance does predict future results -- if you check for stationarity first. | Phase 2, Lessons 01-09 | - |
| 16 | `16-anomaly-detection` | Anomaly Detection | Build | ~75 minutes | py | y | 1 | Normal is easy to define. Abnormal is whatever doesn't fit. | Phase 2, Lessons 01-09 | - |
| 17 | `17-imbalanced-data` | Handling Imbalanced Data | Build | ~90 minutes | py | y | 1 | When 99% of your data is "normal," accuracy is a lie. | Phase 2, Lessons 01-09 (especially evaluation metrics) | - |
| 18 | `18-feature-selection` | Feature Selection | Build | ~75 minutes | py | y | 1 | More features is not better. The right features is better. | Phase 2, Lessons 01-09, 08 (feature engineering) | - |
| 19 | `19-ml-system-design` | ML System Design — From Problem to Deployed Model | Build | ~110 minutes | py | y | 1 | A model is one part of a system. The design decides what the model predicts, who acts on it, what it costs, and what happens when… | Phase 2, Lessons 09 (Model Evaluation) and 13 (ML Pipelines) | - |
| 20 | `20-model-monitoring-and-drift` | Monitoring Models in Production — Data Drift and Concept Dr… | Build | ~110 minutes | py | y | 1 | A deployed model fails without an error message. It keeps returning scores while the world moves away from its training data, and… | Phase 2, Lessons 09 (Model Evaluation), 16 (Anomaly Detection), and 1… | - |
| 21 | `21-feature-stores-and-training-serving-skew` | Feature Stores and Training-Serving Skew | Build | ~100 minutes | py | y | 1 | A feature has one definition and two readers. Training reads its history as of each label time, and serving reads its latest valu… | Phase 2, Lessons 08 (Feature Engineering), 13 (ML Pipelines), 15 (Tim… | - |
