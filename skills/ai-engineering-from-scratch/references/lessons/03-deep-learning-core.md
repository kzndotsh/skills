# Phase 03: Deep Learning Core

Upstream commit `1a8c4fd`. 13 lessons. Path pattern: `phases/03-deep-learning-core/<lesson>/docs/en.md`.
Audit status: 2 lessons sampled, both flawed (buggy doc code, bogus benchmark).

Columns: Type = Build or Learn; Lang = code file types; Quiz = has quiz.json; Out = reusable artifacts in outputs/; Trust = audit result (blank dash means not audited). Fetch a lesson per `repo-guide.md`.

| # | Folder | Title | Type | Time | Lang | Quiz | Out | Motto | Prerequisites | Trust |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `01-the-perceptron` | The Perceptron | Build | ~60 minutes | jl, py | y | 1 | The perceptron is the atom of neural networks. Split it open and you find weights, a bias, and a decision. | Phase 1 (Linear Algebra Intuition) | - |
| 02 | `02-multi-layer-networks` | Multi-Layer Networks and Forward Pass | Build | ~90 minutes | py | y | 1 | One neuron draws a line. Stack them, and you can draw anything. | Phase 01 (Math Foundations), Lesson 03.01 (The Perceptron) | - |
| 03 | `03-backpropagation` | Backpropagation from Scratch | Build | ~120 minutes | jl, py | y | 1 | Backpropagation is the algorithm that makes learning possible. Without it, neural networks are just expensive random number gener… | Lesson 03.02 (Multi-Layer Networks) | - |
| 04 | `04-activation-functions` | Activation Functions | Build | ~75 minutes | jl, py | y | 1 | Without nonlinearity, your 100-layer network is a fancy matrix multiply. Activations are the gates that let neural networks think… | Lesson 03.03 (Backpropagation) | - |
| 05 | `05-loss-functions` | Loss Functions | Build | ~75 minutes | jl, py | y | 2 | Your network makes a prediction. The ground truth says otherwise. How wrong is it? That number is the loss. Pick the wrong loss f… | Lesson 03.04 (Activation Functions) | - |
| 06 | `06-optimizers` | Optimizers | Build | ~75 minutes | py | y | 1 | Gradient descent tells you which direction to move. It says nothing about how far or how fast. SGD is a compass. Adam is GPS with… | Lesson 03.05 (Loss Functions) | - |
| 07 | `07-regularization` | Regularization | Build | ~75 minutes | py | y | 1 | Your model gets 99% on training data and 60% on test data. It memorized instead of learning. Regularization is the tax you impose… | Lesson 03.06 (Optimizers) | WRONG: Doc backward pass omits dropout mask; demo cannot overfit; 'conclusion' is hard-coded; GPT-3 tokens wrong |
| 08 | `08-weight-initialization` | Weight Initialization and Training Stability | Build | ~90 minutes | py | y | 1 | Initialize wrong and training never starts. Initialize right and 50 layers train as smoothly as 3. | Lesson 03.04 (Activation Functions), Lesson 03.07 (Regularization) | - |
| 09 | `09-learning-rate-schedules` | Learning Rate Schedules and Warmup | Build | ~90 minutes | py | y | 1 | The learning rate is the single most important hyperparameter. Not the architecture. Not the dataset size. Not the activation fun… | Lesson 03.06 (Optimizers), Lesson 03.08 (Weight Initialization) | - |
| 10 | `10-mini-framework` | Build Your Own Mini Framework | Build | ~120 minutes | py | y | 1 | You have built neurons, layers, networks, backprop, activations, loss functions, optimizers, regularization, initialization, and… | All of Phase 03 (Lessons 01-09) | - |
| 11 | `11-intro-to-pytorch` | Introduction to PyTorch | Build | ~75 minutes | py | y | 2 | You built the engine from pistons and crankshafts. Now learn the one everyone actually drives. | Lesson 03.10 (Build Your Own Mini Framework) | - |
| 12 | `12-intro-to-jax` | Introduction to JAX | Build | ~90 minutes | py | y | 2 | PyTorch mutates tensors. TensorFlow builds graphs. JAX compiles pure functions. That last one changes how you think about deep le… | Phase 03 Lessons 01-10, basic NumPy | WRONG: JIT benchmark lacks block_until_ready (bogus speedup); optax and PaLM claims wrong or unsourced |
| 13 | `13-debugging-neural-networks` | Debugging Neural Networks | Build | ~90 minutes | py | y | 2 | Your network compiled. It ran. It produced a number. The number is wrong and nothing crashed. Welcome to the hardest kind of debu… | Phase 03 Lessons 01-10 (especially backpropagation, loss functions, o… | - |
