# Glossary index

Source: `glossary/terms.md` at commit `1a8c4fd` (250 terms). This is an index only. Read definitions from `https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/1a8c4fd/glossary/terms.md` (search for `### <Term>`). Each entry has what it means, why it matters, a practical note, a common confusion, related terms, and sources. The glossary itself says current official documentation wins over its general definitions.

## Contents

- AI-native development (23 terms)
- Agents & tools (27 terms)
- Data & representations (13 terms)
- Evaluation & safety (17 terms)
- Infrastructure & serving (18 terms)
- Math & training (42 terms)
- Models & inference (29 terms)
- Multimodal systems (15 terms)
- Prompting & context (15 terms)
- Reliability & operations (17 terms)
- Retrieval & generation (14 terms)
- Security & governance (20 terms)

## Terms

| Term | Category | Lesson |
|---|---|---|
| Activation Checkpointing | Math & training | - |
| Activation Function | Math & training | `phases/03-deep-learning-core/04-activation-functions` |
| Adam (Optimizer) | Math & training | - |
| AdamW | Math & training | - |
| Admission Control | Reliability & operations | - |
| Agent | Agents & tools | `phases/14-agent-engineering/01-the-agent-loop` |
| Agent Harness | Agents & tools | `phases/14-agent-engineering/32-minimal-agent-workbench` |
| Agent Memory | Agents & tools | - |
| Agent State | Agents & tools | `phases/14-agent-engineering/34-repo-memory-and-state` |
| Agent Skill | Agents & tools | `phases/13-tools-and-protocols/22-skills-and-agent-sdks` |
| AI Risk Assessment | Security & governance | - |
| Alignment | Evaluation & safety | - |
| Approval Gate | Agents & tools | `phases/14-agent-engineering/38-verification-gates` |
| Approximate Nearest Neighbor (ANN) | Retrieval & generation | - |
| Attention | Models & inference | `phases/07-transformers-deep-dive/02-self-attention-from-scratch` |
| Audio Token | Multimodal systems | `phases/06-speech-and-audio/13-neural-audio-codecs` |
| Audit Log | Security & governance | - |
| Autograd | Math & training | `phases/01-math-foundations/05-chain-rule-and-autodiff` |
| Automatic Speech Recognition (ASR) | Multimodal systems | `phases/06-speech-and-audio/04-speech-recognition-asr` |
| Autoregressive | Models & inference | - |
| Autoscaling | Infrastructure & serving | `phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes` |
| Availability | Reliability & operations | - |
| Backpressure | AI-native development | - |
| Backpropagation | Math & training | `phases/03-deep-learning-core/03-backpropagation` |
| Batch Size | Math & training | - |
| Benchmark Contamination | Evaluation & safety | - |
| BM25 | Retrieval & generation | - |
| Byte Pair Encoding (BPE) | Data & representations | - |
| Calibration | Evaluation & safety | - |
| Canary Release | Reliability & operations | - |
| Chain of Thought (CoT) | Prompting & context | `phases/11-llm-engineering/02-few-shot-cot` |
| Checkpoint | Agents & tools | `phases/19-capstone-projects/47-checkpoint-save-resume` |
| Chunked Prefill | Infrastructure & serving | `phases/17-infrastructure-and-production/04-vllm-serving-internals` |
| Chunking | Retrieval & generation | - |
| Circuit Breaker | AI-native development | - |
| CNN (Convolutional Neural Network) | Models & inference | - |
| Coding Agent | AI-native development | `phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure` |
| Compensating Action | Agents & tools | - |
| Content Provenance | Security & governance | `phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa` |
| Context Compression | Prompting & context | - |
| Context Engineering | Prompting & context | `phases/11-llm-engineering/05-context-engineering` |
| Context Window | Prompting & context | `phases/11-llm-engineering/05-context-engineering` |
| Continuous Batching | Infrastructure & serving | - |
| Contrastive Learning | Math & training | - |
| Cosine Similarity | Data & representations | - |
| Cost per Successful Task | AI-native development | - |
| Cross-Attention | Multimodal systems | - |
| Cross-Entropy | Math & training | - |
| CUDA | Models & inference | - |
| Data Augmentation | Math & training | - |
| Data Classification | Security & governance | - |
| Data Deduplication | Data & representations | - |
| Data Exfiltration | Security & governance | `phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai` |
| Data Leakage | Data & representations | - |
| Data Lineage | Security & governance | - |
| Data Minimization | Security & governance | - |
| Data Provenance | Data & representations | - |
| Dataset Split | Data & representations | - |
| Datasheet for Datasets | Security & governance | `phases/18-ethics-safety-alignment/26-model-system-dataset-cards` |
| Deadline Propagation | Reliability & operations | - |
| Decode Phase | Infrastructure & serving | `phases/17-infrastructure-and-production/17-disaggregated-prefill-decode` |
| Decoder | Models & inference | - |
| Decoding Strategy | Models & inference | - |
| Defense in Depth | Security & governance | - |
| Delegation | Agents & tools | - |
| Dense Retrieval | Retrieval & generation | - |
| Diffusion Model | Models & inference | - |
| Disaggregated Serving | Infrastructure & serving | `phases/17-infrastructure-and-production/17-disaggregated-prefill-decode` |
| Distribution Shift | Evaluation & safety | - |
| DPO (Direct Preference Optimization) | Math & training | `phases/10-llms-from-scratch/08-dpo` |
| Dropout | Math & training | - |
| Durable Execution | Agents & tools | - |
| Dynamic Batching | Infrastructure & serving | `phases/17-infrastructure-and-production/04-vllm-serving-internals` |
| Early Fusion | Multimodal systems | `phases/12-multimodal-ai/11-chameleon-early-fusion-tokens` |
| Eigenvalue | Math & training | - |
| Embedding | Data & representations | `phases/11-llm-engineering/04-embeddings` |
| Encoder | Models & inference | - |
| Epoch | Math & training | - |
| Error Budget | Reliability & operations | - |
| Eval Set | Evaluation & safety | `phases/14-agent-engineering/30-eval-driven-agent-development` |
| Evaluation (Eval) | Evaluation & safety | `phases/11-llm-engineering/10-evaluation` |
| Exact Match (EM) | Evaluation & safety | - |
| Expert Parallelism | Infrastructure & serving | `phases/07-transformers-deep-dive/11-mixture-of-experts` |
| Feature | Data & representations | - |
| Few-Shot | Prompting & context | - |
| Fine-tuning | Math & training | `phases/11-llm-engineering/08-fine-tuning-lora` |
| Flaky Test | AI-native development | - |
| FlashAttention | Infrastructure & serving | `phases/07-transformers-deep-dive/12-kv-cache-flash-attention` |
| Function Calling | Agents & tools | `phases/11-llm-engineering/09-function-calling` |
| GAN (Generative Adversarial Network) | Models & inference | - |
| Goodput | Infrastructure & serving | `phases/17-infrastructure-and-production/08-inference-metrics-goodput` |
| GPT | Models & inference | - |
| Graceful Degradation | Reliability & operations | `phases/11-llm-engineering/13-production-app` |
| Gradient | Math & training | - |
| Gradient Accumulation | Math & training | - |
| Gradient Clipping | Math & training | - |
| Gradient Descent | Math & training | - |
| Grounding | Retrieval & generation | `phases/11-llm-engineering/06-rag` |
| Guardrails | Evaluation & safety | `phases/11-llm-engineering/12-guardrails` |
| Hallucination | Evaluation & safety | - |
| Handoff | AI-native development | `phases/14-agent-engineering/40-multi-session-handoff` |
| HNSW | Retrieval & generation | - |
| Human-in-the-Loop (HITL) | Agents & tools | - |
| Hybrid Retrieval | Retrieval & generation | `phases/11-llm-engineering/07-advanced-rag` |
| Hyperparameter | Math & training | - |
| Idempotency | AI-native development | - |
| Image Token | Multimodal systems | `phases/04-computer-vision/25-vision-language-models` |
| In-Context Learning | Prompting & context | - |
| Incident Response | Reliability & operations | `phases/17-infrastructure-and-production/23-sre-for-ai` |
| Indirect Prompt Injection | Security & governance | `phases/18-ethics-safety-alignment/15-indirect-prompt-injection` |
| Inductive Bias | Models & inference | - |
| Inference | Models & inference | - |
| Instruction Following | Prompting & context | - |
| Instruction Hierarchy | Prompting & context | - |
| Inter-Token Latency (ITL) | Infrastructure & serving | `phases/17-infrastructure-and-production/08-inference-metrics-goodput` |
| Jailbreak | Security & governance | `phases/19-capstone-projects/82-jailbreak-taxonomy` |
| JAX | Math & training | `phases/03-deep-learning-core/12-intro-to-jax` |
| Knowledge Distillation | Math & training | - |
| KV Cache | Models & inference | `phases/07-transformers-deep-dive/12-kv-cache-flash-attention` |
| Late Fusion | Multimodal systems | `phases/19-capstone-projects/61-cross-attention-fusion` |
| Latent Space | Data & representations | - |
| Learning Rate | Math & training | - |
| Learning Rate Schedule | Math & training | - |
| Least Privilege | Evaluation & safety | - |
| LLM (Large Language Model) | Models & inference | - |
| LLM-as-a-Judge | Evaluation & safety | `phases/14-agent-engineering/30-eval-driven-agent-development` |
| Load Shedding | Reliability & operations | - |
| Logits | Models & inference | - |
| LoRA (Low-Rank Adaptation) | Math & training | `phases/11-llm-engineering/08-fine-tuning-lora` |
| Loss Function | Math & training | - |
| Lost in the Middle | Prompting & context | - |
| Maximum Marginal Relevance (MMR) | Retrieval & generation | - |
| MCP (Model Context Protocol) | Agents & tools | `phases/11-llm-engineering/14-model-context-protocol` |
| Membership Inference | Security & governance | `phases/18-ethics-safety-alignment/22-differential-privacy-for-llms` |
| Mixed Precision | Math & training | - |
| Modality | Multimodal systems | `phases/12-multimodal-ai/16-mio-any-to-any-streaming` |
| Modality Alignment | Multimodal systems | `phases/19-capstone-projects/60-projection-layer-modality-align` |
| Model Card | Evaluation & safety | - |
| Model Router | AI-native development | - |
| Model Serving | Infrastructure & serving | `phases/17-infrastructure-and-production/28-self-hosted-serving-selection` |
| MoE (Mixture of Experts) | Models & inference | `phases/07-transformers-deep-dive/11-mixture-of-experts` |
| Multimodal Fusion | Multimodal systems | `phases/19-capstone-projects/61-cross-attention-fusion` |
| Multimodal Model | Multimodal systems | `phases/12-multimodal-ai/16-mio-any-to-any-streaming` |
| Multi Round-Trip Request (MRTR) | Agents & tools | `phases/13-tools-and-protocols/12-mcp-roots-and-elicitation` |
| NaN (Not a Number) | Math & training | - |
| Normalization | Math & training | - |
| Nucleus Sampling (Top-p) | Models & inference | - |
| Observability | AI-native development | `phases/14-agent-engineering/24-agent-observability-platforms` |
| Optimizer | Math & training | - |
| Orchestration | Agents & tools | - |
| Overfitting | Math & training | - |
| Paged KV Cache | Infrastructure & serving | `phases/17-infrastructure-and-production/04-vllm-serving-internals` |
| Parameter | Models & inference | - |
| Pass@k | Evaluation & safety | - |
| Patch | AI-native development | `phases/14-agent-engineering/41-workbench-for-real-repos` |
| Patch Embedding | Multimodal systems | `phases/12-multimodal-ai/01-vision-transformer-patch-tokens` |
| Perplexity | Models & inference | - |
| Pipeline Parallelism | Infrastructure & serving | `phases/10-llms-from-scratch/05-scaling-distributed` |
| Planning | Agents & tools | - |
| Postmortem | Reliability & operations | - |
| Precision & Recall | Evaluation & safety | - |
| Prefill | Infrastructure & serving | `phases/17-infrastructure-and-production/17-disaggregated-prefill-decode` |
| Prefix Caching | Infrastructure & serving | `phases/10-llms-from-scratch/12-inference-optimization` |
| Progressive Disclosure | AI-native development | `phases/14-agent-engineering/41-workbench-for-real-repos` |
| Prompt Cache | Prompting & context | `phases/11-llm-engineering/15-prompt-caching` |
| Prompt Engineering | Prompting & context | `phases/11-llm-engineering/01-prompt-engineering` |
| Prompt Injection | Evaluation & safety | `phases/14-agent-engineering/27-prompt-injection-defense` |
| Prompt Sensitivity | Prompting & context | - |
| Provenance Attestation | Security & governance | - |
| Purpose Limitation | Security & governance | - |
| QLoRA | Math & training | `phases/11-llm-engineering/08-fine-tuning-lora` |
| Quantization | Models & inference | - |
| RAG (Retrieval-Augmented Generation) | Retrieval & generation | `phases/11-llm-engineering/06-rag` |
| Rate Limit | AI-native development | - |
| ReAct | Agents & tools | - |
| Readiness Probe | Reliability & operations | `phases/11-llm-engineering/13-production-app` |
| Recall@K | Retrieval & generation | - |
| Reciprocal Rank Fusion (RRF) | Retrieval & generation | - |
| Red Teaming | Security & governance | - |
| Regression Test | AI-native development | `phases/14-agent-engineering/30-eval-driven-agent-development` |
| ReLU | Math & training | - |
| Repository Instructions | AI-native development | - |
| Repository Map | AI-native development | `phases/14-agent-engineering/34-repo-memory-and-state` |
| Reproducible Build | AI-native development | - |
| Reranker | Retrieval & generation | - |
| Retry Budget | Reliability & operations | - |
| Retry with Backoff | AI-native development | - |
| Reviewer Agent | AI-native development | `phases/14-agent-engineering/39-reviewer-agent` |
| RLHF (Reinforcement Learning from Human Feedback) | Math & training | `phases/10-llms-from-scratch/07-rlhf` |
| Rollback | Reliability & operations | - |
| ROUGE | Evaluation & safety | - |
| Sandbox | Agents & tools | `phases/14-agent-engineering/29-production-runtimes` |
| Saturation | Reliability & operations | - |
| Scope Contract | AI-native development | `phases/14-agent-engineering/36-scope-contracts` |
| Self-Attention | Models & inference | `phases/07-transformers-deep-dive/02-self-attention-from-scratch` |
| Semantic Cache | AI-native development | - |
| Semantic Search | Retrieval & generation | - |
| Separation of Duties | Security & governance | - |
| Service Level Indicator (SLI) | Reliability & operations | - |
| Service Level Objective (SLO) | Reliability & operations | `phases/17-infrastructure-and-production/08-inference-metrics-goodput` |
| SFT (Supervised Fine-Tuning) | Math & training | - |
| Shadow Traffic | Reliability & operations | `phases/17-infrastructure-and-production/20-shadow-canary-progressive` |
| Shared Embedding Space | Multimodal systems | `phases/12-multimodal-ai/02-clip-contrastive-pretraining` |
| Skill Bundle | Agents & tools | `phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability` |
| Skill Catalog | Agents & tools | `phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure` |
| Skill Discovery | Agents & tools | `phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure` |
| Skill Invocation | Agents & tools | `phases/13-tools-and-protocols/25-skill-invocation-and-routing` |
| Softmax | Math & training | - |
| Software Bill of Materials (SBOM) | Security & governance | - |
| Speculative Decoding | Models & inference | - |
| Stateless MCP | Agents & tools | `phases/13-tools-and-protocols/06-mcp-fundamentals` |
| Stochastic Gradient Descent (SGD) | Math & training | - |
| Stop Sequence | Models & inference | - |
| Streaming | Models & inference | `phases/11-llm-engineering/13-production-app` |
| Structured Output | Agents & tools | `phases/11-llm-engineering/03-structured-outputs` |
| Swarm | Agents & tools | - |
| System Prompt | Prompting & context | `phases/14-agent-engineering/33-instructions-as-executable-constraints` |
| Tail Latency | Reliability & operations | `phases/17-infrastructure-and-production/08-inference-metrics-goodput` |
| Temperature | Models & inference | - |
| Tensor | Data & representations | - |
| Tensor Parallelism | Infrastructure & serving | `phases/10-llms-from-scratch/05-scaling-distributed` |
| Termination Condition | Agents & tools | - |
| Test Oracle | AI-native development | - |
| Threat Model | Security & governance | - |
| Time per Output Token (TPOT) | Infrastructure & serving | `phases/17-infrastructure-and-production/08-inference-metrics-goodput` |
| Time to First Token (TTFT) | Models & inference | - |
| Token | Data & representations | `phases/10-llms-from-scratch/01-tokenizers` |
| Token Budget | Prompting & context | `phases/11-llm-engineering/05-context-engineering` |
| Tokenization | Data & representations | - |
| Tokens per Second (TPS) | Infrastructure & serving | - |
| Tool Contract | Agents & tools | `phases/14-agent-engineering/06-tool-use-and-function-calling` |
| Top-k Sampling | Models & inference | - |
| Trace | AI-native development | `phases/14-agent-engineering/23-otel-genai-conventions` |
| Transfer Learning | Math & training | - |
| Transformer | Models & inference | `phases/07-transformers-deep-dive/05-full-transformer` |
| Trust Boundary | Security & governance | `phases/19-capstone-projects/82-jailbreak-taxonomy` |
| Underfitting | Math & training | - |
| VAE (Variational Autoencoder) | Models & inference | - |
| Vector Database | Retrieval & generation | - |
| Verification Gate | Evaluation & safety | `phases/14-agent-engineering/38-verification-gates` |
| Vision-Language Model (VLM) | Multimodal systems | `phases/04-computer-vision/25-vision-language-models` |
| Vision Transformer (ViT) | Multimodal systems | `phases/04-computer-vision/14-vision-transformers` |
| Visual Grounding | Multimodal systems | `phases/19-capstone-projects/61-cross-attention-fusion` |
| Vocabulary | Data & representations | - |
| Warmup | Math & training | - |
| Weight | Math & training | - |
| Weight Decay | Math & training | - |
| Worktree | AI-native development | `phases/14-agent-engineering/41-workbench-for-real-repos` |
| Zero-Shot | Prompting & context | - |
| Zero Trust | Security & governance | `phases/17-infrastructure-and-production/25-security-secrets-audit` |
