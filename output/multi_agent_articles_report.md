# Multi-Agent Systems: Literature Search Report

## Overview

This report collects recent arXiv papers on multi-agent systems. The search covered three themes:

1. **Cooperative multi-agent reinforcement learning (MARL)**
2. **LLM-based multi-agent systems**
3. **Applied and other multi-agent systems** (perception, traffic, robotics, drones, security)

**Search queries used**
- `abs:"multi-agent" AND abs:cooperation`
- `abs:"multi-agent reinforcement learning"`
- `abs:"multi-agent" AND abs:"large language model"`

**Total papers reviewed:** 24 (18 included below)

**Notes on fields**
- *Year* is taken from the first arXiv submission date (`published` field).
- *Topic relevance* is a short statement of how each paper relates to multi-agent systems.

---

## Theme 1: Cooperative Multi-Agent Reinforcement Learning

### 1. From Solo to Symphony: Orchestrating Multi-Agent Collaboration with Single-Agent Demos
- **Authors:** Xun Wang, Zhuoran Li, Yanshan Lin, Hai Zhong, Longbo Huang
- **Year:** 2025
- **Link:** https://arxiv.org/abs/2511.02762v1
- **Topic relevance:** Proposes SoCo, which pretrains a shared solo policy from single-agent demonstrations and transfers it to cooperative MARL. It addresses the high cost of multi-agent training data.

### 2. Learning Attentional Communication for Multi-Agent Cooperation
- **Authors:** Jiechuan Jiang, Zongqing Lu
- **Year:** 2018
- **Link:** https://arxiv.org/abs/1805.07733v3
- **Topic relevance:** An attention-based model that learns when agents should communicate and what information to integrate. It targets communication in large-scale cooperation, where broadcasting everything can hurt learning.

### 3. Consensus Learning for Cooperative Multi-Agent Reinforcement Learning
- **Authors:** Zhiwei Xu, Bin Zhang, Dapeng Li, Zeren Zhang, Guangchong Zhou, Hao Chen, Guoliang Fan
- **Year:** 2022
- **Link:** https://arxiv.org/abs/2206.02583v3
- **Topic relevance:** Lets agents infer a shared discrete "consensus" from local observations, which gives them a common signal during decentralized execution. This addresses the centralized-training / decentralized-execution gap.

### 4. CM3: Cooperative Multi-goal Multi-stage Multi-agent Reinforcement Learning
- **Authors:** Jiachen Yang, Alireza Nakhaei, David Isele, Kikuo Fujimura, Hongyuan Zha
- **Year:** 2018
- **Link:** https://arxiv.org/abs/1809.05188v3
- **Topic relevance:** Handles settings where each agent has its own goal as well as a shared cooperative objective. It uses a two-stage curriculum and a localized credit-assignment function.

### 5. Cooperative Multi-Agent Policy Gradients with Sub-optimal Demonstration
- **Authors:** Peixi Peng, Junliang Xing
- **Year:** 2018
- **Link:** https://arxiv.org/abs/1812.01825v2
- **Topic relevance:** Learns decentralized policies for sparse-reward cooperative tasks (RTS combat) by combining imperfect demonstrations with Nash-equilibrium guidance.

### 6. Shapley Value Based Multi-Agent Reinforcement Learning: Theory, Method and Its Application to Energy Network
- **Authors:** Jianhong Wang
- **Year:** 2024
- **Link:** https://arxiv.org/abs/2402.15324v1
- **Topic relevance:** Uses cooperative game theory (Markov Shapley value) as a principled credit-assignment method for MARL. It includes algorithms SHAQ, SQDDPG, and SMFPPO and an energy-network application.

### 7. Modeling Human Reputation-Seeking Behavior in a Spatio-Temporally Complex Public Good Provision Game
- **Authors:** Edward Hughes, Tina O. Zhu, Martin J. Chadwick, Raphael Koster, Antonio García Castañeda, Charles Beattie, Thore Graepel, Matthew M. Botvinick, Joel Z. Leibo
- **Year:** 2025
- **Link:** https://arxiv.org/abs/2506.06032v1
- **Topic relevance:** Uses MARL agents to model human group cooperation in the Clean Up public-goods game, and compares results with human lab experiments on reputation and anonymity.

### 8. Partially Observable Mean Field Multi-Agent Reinforcement Learning Based on Graph-Attention
- **Authors:** Min Yang, Guanjun Liu, Ziyuan Zhou
- **Year:** 2023
- **Link:** https://arxiv.org/abs/2304.12653v4
- **Topic relevance:** Scales MARL to large populations under partial observability. It combines a graph-attention module with mean-field approximation (GAMFQ).

---

## Theme 2: LLM-Based Multi-Agent Systems

### 9. Literature Review of Multi-Agent Debate for Problem-Solving
- **Authors:** Arne Tillmann
- **Year:** 2025
- **Link:** https://arxiv.org/abs/2506.00066v1
- **Topic relevance:** Survey of multi-agent LLM (MA-LLM) research covering agent profiles, communication structures, and decision-making. It also discusses scalability and computational cost.

### 10. On the Discussion of Large Language Models: Symmetry of Agents and Interplay with Prompts
- **Authors:** Qineng Wang, Zihao Wang, Ying Su, Yangqiu Song
- **Year:** 2023
- **Link:** https://arxiv.org/abs/2311.07076v1
- **Topic relevance:** Gives a theoretical justification for multi-agent discussion through agent symmetry. It also proposes a scalable "conquer and merge" discussion mechanism.

### 11. Investigating Multi-Agent Deliberation in Law
- **Authors:** Cor Steging, Ludi van Leeuwen, Tadeusz Zbiegień
- **Year:** 2026
- **Link:** https://arxiv.org/abs/2606.30906v1
- **Topic relevance:** Introduces two multi-agent frameworks inspired by courtroom procedure and legal argumentation. It finds they solve different cases from single-LLM baselines, which suggests value for multi-perspective reasoning.

### 12. AutoGenesisAgent: Self-Generating Multi-Agent Systems for Complex Tasks
- **Authors:** Jeremy Harper
- **Year:** 2024
- **Link:** https://arxiv.org/abs/2404.17017v1
- **Topic relevance:** A multi-agent system that designs and deploys other multi-agent systems, covering specification, design, generation, and deployment. It is a proof-of-concept for automating multi-agent system design.

### 13. Large Language Model-Enabled Multi-Agent Manufacturing Systems
- **Authors:** Jonghan Lim, Birgit Vogel-Heuser, Ilya Kovalenko
- **Year:** 2024
- **Link:** https://arxiv.org/abs/2406.01893v2
- **Topic relevance:** Uses LLMs so manufacturing agents can communicate in natural language and interpret human instructions. A case study covers G-code allocation among agents.

### 14. AEMA: Verifiable Evaluation Framework for Trustworthy and Controlled Agentic LLM Systems
- **Authors:** YenTing Lee, Keerthi Koneru, Zahra Moslemi, Sheethal Kumar, Ramesh Radhakrishnan
- **Year:** 2026
- **Link:** https://arxiv.org/abs/2601.11903v1
- **Topic relevance:** A process-aware, auditable framework for evaluating LLM multi-agent systems under human oversight. It is compared against a single LLM-as-a-Judge.

### 15. Extending the OWASP Multi-Agentic System Threat Modeling Guide
- **Authors:** Klaudia Krawiecka, Christian Schroeder de Witt
- **Year:** 2025
- **Link:** https://arxiv.org/abs/2508.09815v1
- **Topic relevance:** Security. Identifies threats specific to LLM multi-agent architectures, such as cross-agent hallucination propagation, unsafe delegation, and multi-agent backdoors.

### 16. LLM-MARS: Large Language Model for Behavior Tree Generation and NLP-enhanced Dialogue in Multi-Agent Robot Systems
- **Authors:** Artem Lykov, Maria Dronova, Nikolay Naglov, Mikhail Litvinov, Sergei Satsevich, Artem Bazhenov, Vladimir Berman, Aleksei Shcherbak, Dzmitry Tsetserukou
- **Year:** 2023
- **Link:** https://arxiv.org/abs/2312.09348v1
- **Topic relevance:** Applies an LLM to multi-robot systems. It generates behavior trees from operator commands and answers questions about robot actions. Tested on two robots in the Eurobot 2023 setting.

---

## Theme 3: Applied and Other Multi-Agent Systems

### 17. Unsupervised Multi-agent and Single-agent Perception from Cooperative Views
- **Authors:** Haochen Yang, Baolu Li, Lei Li, Delin Ren, Jiacheng Guo, Minghai Qin, Tianyun Zhang, Hongkai Yu
- **Year:** 2026
- **Link:** https://arxiv.org/abs/2604.05354v1
- **Topic relevance:** Cooperative LiDAR perception among connected vehicles or robots. It shares sensor data between agents and uses cooperative views as unsupervised guidance for 3D detection (UMS framework).

### 18. Distributionally Robust Multi-Agent Reinforcement Learning for Intelligent Traffic Control
- **Authors:** Shuwei Pei, Joran Borger, Arda Kosay, Muhammed O. Sayin, Saeed Ahmed
- **Year:** 2025
- **Link:** https://arxiv.org/abs/2512.18558v1
- **Topic relevance:** Multi-intersection traffic signal control with PPO agents under centralized training and decentralized execution. It adds robustness to demand uncertainty, with up to 51% shorter queues in worst-case scenarios.

---

## Additional Papers Reviewed (not in detailed list)

| Title | Year | Link | Reason excluded |
|---|---|---|---|
| A Comprehensive Survey on Multi-Agent Cooperative Decision-Making | 2025 | https://arxiv.org/abs/2503.13415v2 | Strong survey; could be added as a general reference |
| Universal Policies to Learn Them All | 2019 | https://arxiv.org/abs/1908.09184v1 | Narrower scope (multi-scenario generalization) |
| CH-MARL: A Multimodal Benchmark for Cooperative, Heterogeneous MARL | 2022 | https://arxiv.org/abs/2208.13626v1 | Benchmark paper; relevant but secondary |
| Modeling Sensorimotor Coordination as MARL with Differentiable Communication | 2019 | https://arxiv.org/abs/1909.05815v1 | Neuroscience-oriented |
| An ensemble Multi-Agent System for non-linear classification | 2022 | https://arxiv.org/abs/2209.06824v1 | Adaptive MAS for ML; niche |
| Software Simulation and Visualization of Quantum Multi-Drone RL | 2022 | https://arxiv.org/abs/2211.15375v3 | Quantum MARL for drones; niche |

---

## Summary

- **Cooperative MARL** remains the most active area in the set. Recent work focuses on communication (2018 onward), transferring knowledge from single-agent data (2025), and credit assignment through game theory (2024).
- **LLM-based multi-agent systems** (2023–2026) cover debate and deliberation, automated system design, domain applications (law, manufacturing), evaluation, and security.
- **Applied multi-agent systems** include cooperative perception for autonomous vehicles and robust traffic control.
- Recurring open challenges include scalability, non-stationarity, cost of multi-agent communication, and evaluation and security of agent systems.

*Limitations:* This is a search sample of 24 papers from three queries, not an exhaustive review. Dates are as reported by the search tool, and some entries carry 2026 submission dates.
