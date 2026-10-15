# Phase 01: Math Foundations

Upstream commit `1a8c4fd`. 22 lessons. Path pattern: `phases/01-math-foundations/<lesson>/docs/en.md`.
Audit status: 2 lessons sampled: one sound, one with a statistical-advice error.

Columns: Type = Build or Learn; Lang = code file types; Quiz = has quiz.json; Out = reusable artifacts in outputs/; Trust = audit result (blank dash means not audited). Fetch a lesson per `repo-guide.md`.

| # | Folder | Title | Type | Time | Lang | Quiz | Out | Motto | Prerequisites | Trust |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `01-linear-algebra-intuition` | Linear Algebra Intuition | Learn | ~60 minutes | jl, py | y | 1 | Every AI model is just matrix math wearing a fancy hat. | Phase 0 | - |
| 02 | `02-vectors-matrices-operations` | Vectors, Matrices & Operations | Build | ~60 minutes | jl, py | y | 1 | Every neural network is just matrix multiplication with extra steps. | Phase 1, Lesson 01 (Linear Algebra Intuition) | - |
| 03 | `03-matrix-transformations` | Matrix Transformations | Build | ~75 minutes | jl, py | y | 1 | A matrix is a machine that reshapes space. Learn what it does to every point, and you understand the whole transformation. | Phase 1, Lessons 01-02 (Linear Algebra Intuition, Vectors & Matrices… | - |
| 04 | `04-calculus-for-ml` | Calculus for Machine Learning | Learn | ~60 minutes | jl, py | y | 1 | Derivatives tell you which way is downhill. That is all a neural network needs to learn. | Phase 1, Lessons 01-03 | - |
| 05 | `05-chain-rule-and-autodiff` | Chain Rule & Automatic Differentiation | Build | ~90 minutes | jl, py | y | 1 | The chain rule is the engine behind every neural network that learns. | Phase 1, Lesson 04 (Derivatives & Gradients) | - |
| 06 | `06-probability-and-distributions` | Probability and Distributions | Learn | ~75 minutes | jl, py | y | 1 | Probability is the language AI uses to express uncertainty. | Phase 1, Lessons 01-04 | - |
| 07 | `07-bayes-theorem` | Bayes' Theorem | Build | ~75 minutes | py | y | 1 | Probability is about what you expect. Bayes' theorem is about what you learn. | Phase 1, Lesson 06 (Probability Fundamentals) | - |
| 08 | `08-optimization` | Optimization | Build | ~75 minutes | jl, py | y | 1 | Training a neural network is nothing more than finding the bottom of a valley. | Phase 1, Lessons 04-05 (Derivatives, Gradients) | - |
| 09 | `09-information-theory` | Information Theory | Learn | ~60 minutes | py | y | 1 | Information theory measures surprise. Loss functions are built on it. | Phase 1, Lesson 06 (Probability) | ok: Formulas right; GPT-2 perplexity quoted as both ~30 and 50; MI-bias caveat missing |
| 10 | `10-dimensionality-reduction` | Dimensionality Reduction | Build | ~90 minutes | py | y | 1 | High-dimensional data has structure. You find it by looking from the right angle. | Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices… | - |
| 11 | `11-singular-value-decomposition` | Singular Value Decomposition | Build | ~120 minutes | jl, py | y | 1 | SVD is the Swiss Army knife of linear algebra. Every matrix has one. Every data scientist needs one. | Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors & Matrice… | - |
| 12 | `12-tensor-operations` | Tensor Operations | Build | ~90 minutes | py | y | 2 | Tensors are the common language between data and deep learning. Every image, every sentence, every gradient flows through them. | Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices… | - |
| 13 | `13-numerical-stability` | Numerical Stability | Build | ~120 minutes | py | y | 1 | Floating point is a leaky abstraction. It will bite you during training, and you will not see it coming. | Phase 1, Lessons 01-04 | - |
| 14 | `14-norms-and-distances` | Norms and Distances | Build | ~90 minutes | py | y | 1 | Your distance function defines what "similar" means. Choose wrong and everything downstream breaks. | Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors, Matrices… | - |
| 15 | `15-statistics-for-ml` | Statistics for Machine Learning | Build | ~120 minutes | py | y | 1 | Statistics is how you know if your model actually works or just got lucky. | Phase 1, Lessons 06 (Probability and Distributions), 07 (Bayes' Theor… | WRONG: Advises Wilcoxon on 5 CV folds (min p=0.0625, can never reach 0.05); no code in Build It |
| 16 | `16-sampling-methods` | Sampling Methods | Build | ~120 minutes | py | y | 1 | Sampling is how AI explores the space of possibilities. | Phase 1, Lessons 06-07 (Probability, Bayes' Theorem) | - |
| 17 | `17-linear-systems` | Linear Systems | Build | ~120 minutes | py | y | 1 | Solving $Ax = b$ is the oldest problem in mathematics that still runs your neural network. | Phase 1, Lessons 01 (Linear Algebra Intuition), 02 (Vectors & Matrice… | - |
| 18 | `18-convex-optimization` | Convex Optimization | Build | ~90 minutes | py | y | 1 | Convex problems have one valley. Neural networks have millions. Knowing the difference matters. | Phase 1, Lessons 04 (Calculus for ML), 08 (Optimization) | - |
| 19 | `19-complex-numbers` | Complex Numbers for AI | Learn | ~60 minutes | py | y | 1 | The square root of -1 is not imaginary. It is the key to rotations, frequencies, and half of signal processing. | Phase 1, Lessons 01-04 (linear algebra, calculus) | - |
| 20 | `20-fourier-transform` | The Fourier Transform | Build | ~90 minutes | py | y | 1 | Every signal is a sum of sine waves. The Fourier transform tells you which ones. | Phase 1, Lessons 01-04, 19 (complex numbers) | - |
| 21 | `21-graph-theory` | Graph Theory for Machine Learning | Build | ~90 minutes | py | y | 1 | Graphs are the data structure of relationships. If your data has connections, you need graph theory. | Phase 1, Lessons 01-03 (linear algebra, matrices) | - |
| 22 | `22-stochastic-processes` | Stochastic Processes | Learn | ~75 minutes | py | y | 1 | Randomness with structure. The math behind random walks, Markov chains, and diffusion models. | Phase 1, Lessons 06-07 (probability, Bayes) | - |
