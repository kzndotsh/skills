# Phase 09: Reinforcement Learning

Upstream commit `1a8c4fd`. 12 lessons. Path pattern: `phases/09-reinforcement-learning/<lesson>/docs/en.md`.
Audit status: Not audited.

Columns: Type = Build or Learn; Lang = code file types; Quiz = has quiz.json; Out = reusable artifacts in outputs/; Trust = audit result (blank dash means not audited). Fetch a lesson per `repo-guide.md`.

| # | Folder | Title | Type | Time | Lang | Quiz | Out | Motto | Prerequisites | Trust |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `01-mdps-states-actions-rewards` | MDPs, States, Actions & Rewards | Learn | ~45 minutes | py | - | 1 | A Markov Decision Process is five things: states, actions, transitions, rewards, a discount. Everything in RL — Q-learning, PPO,… | Phase 1 · 06 (Probability & Distributions), Phase 2 · 01 (ML Taxonomy) | - |
| 02 | `02-dynamic-programming` | Dynamic Programming — Policy Iteration & Value Iteration | Build | ~75 minutes | py | - | 1 | Dynamic programming is RL with cheating. You already know the transition and reward functions; you just iterate the Bellman equat… | Phase 9 · 01 (MDPs) | - |
| 03 | `03-monte-carlo-methods` | Monte Carlo Methods — Learning from Complete Episodes | Build | ~75 minutes | py | - | 1 | Dynamic programming needs a model. Monte Carlo needs nothing but episodes. Run the policy, watch the returns, average them. The s… | Phase 9 · 01 (MDPs), Phase 9 · 02 (Dynamic Programming) | - |
| 04 | `04-q-learning-sarsa` | Temporal Difference — Q-Learning & SARSA | Build | ~75 minutes | py | - | 1 | Monte Carlo waits until the episode ends. TD updates after every step by bootstrapping the next value estimate. Q-learning is off… | Phase 9 · 01 (MDPs), Phase 9 · 02 (Dynamic Programming), Phase 9 · 03… | - |
| 05 | `05-dqn` | Deep Q-Networks (DQN) | Build | ~75 minutes | py | - | 1 | 2013: Mnih trained one Q-learning network on raw pixels, beat every classical RL agent on seven Atari games. 2015: extended to 49… | Phase 3 · 03 (Backpropagation), Phase 9 · 04 (Q-learning, SARSA) | - |
| 06 | `06-policy-gradients-reinforce` | Policy Gradient — REINFORCE from Scratch | Build | ~75 minutes | py | - | 1 | Stop estimating value. Parameterize the policy directly, compute the gradient of expected return, step uphill. Williams (1992) wr… | Phase 3 · 03 (Backpropagation), Phase 9 · 03 (Monte Carlo), Phase 9 ·… | - |
| 07 | `07-actor-critic-a2c-a3c` | Actor-Critic — A2C and A3C | Build | ~75 minutes | py | - | 1 | REINFORCE is noisy. Add a critic that learns $\hat{V}(s)$, subtract it from the return, and you get an advantage that has the sam… | Phase 9 · 04 (TD Learning), Phase 9 · 06 (REINFORCE) | - |
| 08 | `08-ppo` | Proximal Policy Optimization (PPO) | Build | ~75 minutes | py | - | 1 | A2C throws away each rollout after one update. PPO wraps the policy gradient in a clipped importance ratio so you can do 10+ epoc… | Phase 9 · 06 (REINFORCE), Phase 9 · 07 (Actor-Critic) | - |
| 09 | `09-reward-modeling-rlhf` | Reward Modeling & RLHF | Build | ~45 minutes | py | - | 1 | Humans cannot write a reward function for "good assistant response," but they can compare two responses and pick the better one.… | Phase 5 · 05 (Sentiment), Phase 9 · 08 (PPO) | - |
| 10 | `10-multi-agent-rl` | Multi-Agent RL | Build | ~45 minutes | py | - | 1 | Single-agent RL assumes the environment is stationary. Put two learning agents in the same world and that assumption breaks: each… | Phase 9 · 04 (Q-learning), Phase 9 · 06 (REINFORCE), Phase 9 · 07 (Ac… | - |
| 11 | `11-sim-to-real-transfer` | Sim-to-Real Transfer | Learn | ~45 minutes | py | - | 1 | A policy trained in a simulator that fails on hardware is a policy that memorized the simulator. Domain randomization, domain ada… | Phase 9 · 08 (PPO), Phase 2 · 10 (Bias/Variance) | - |
| 12 | `12-rl-for-games` | RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era | Build | ~120 minutes | py | - | 1 | 1992: TD-Gammon beat human champions at backgammon with pure TD. 2016: AlphaGo beat Lee Sedol. 2017: AlphaZero dominated chess, s… | Phase 9 · 05 (DQN), Phase 9 · 08 (PPO), Phase 9 · 09 (RLHF), Phase 9… | - |
