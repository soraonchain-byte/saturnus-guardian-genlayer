# 🪐 Saturnus Guardian

> **Architecting Cognitive Guardrails for the Agentic Economy.**

Saturnus Guardian is an **Intelligent Contract (IC)** deployed on **GenLayer Testnet Bradbury**. It is designed to eliminate the "Clarity Gap" in Web3—the dangerous disconnect between a user's intent and the technical reality of a transaction.

By leveraging **Subjective Consensus**, Saturnus interprets the *narrative intent* of a transaction before it reaches the execution layer, providing a cognitive safety net for both humans and autonomous agents.

---

## 🏗️ Architecture
Saturnus Guardian acts as a decentralized coordination infrastructure. Unlike traditional deterministic security, Saturnus evaluates transactions based on **Subjective Logic**.

### Core Components:
- **Semantic Intent Analyzer**: Parses transaction metadata using GenLayer’s intelligent layer to detect high-risk patterns (e.g., "drainers", "sweepers").
- **Narrative Security Posture**: A dynamic state-machine that adjusts the Guardian's strictness based on the current network threat level.
- **Subjective Validator (Roadmap)**: Future integration with the Trustless LLM Jury to evaluate complex, non-deterministic risks.

---

## 🚀 Deployment & Usage (Bradbury Testnet)

The contract is written in **Python** using GenLayer's latest Intelligent Contract standards.

### Features Implemented (v0.1.2):
- [x] **Dynamic Security Posture**: Admin-controlled security state (`update_security_posture`).
- [x] **Subjective Intent Analysis**: Real-time evaluation of transaction descriptions (`analyze_transaction_intent`).
- [x] **Native GenLayer Integration**: Fully compatible with the `py-genlayer` SDK and Bradbury consensus.

### How to Interact:
1. **Analyze Intent**: Call `analyze_transaction_intent` with a string description (e.g., *"I want to claim a free airdrop from an unknown link"*). 
2. **Security Feedback**: The contract will return a **Subjective Warning** if malicious patterns like "drain" or "claim airdrop" are detected.

---

## 🛠️ Technical Stack
- **Framework**: GenLayer SDK (`py-genlayer`)
- **Language**: Python
- **Environment**: GenLayer Studio / Bradbury Net
- **Ecosystem**: Part of **The Great Nine** (Portfolio of SoraOnchain)

---

## 📜 Vision: The Great Nine
Saturnus Guardian is one of the pillars of the **Agentic Economy**. As AI agents begin to manage capital autonomously, Saturnus provides the necessary guardrails to ensure that agentic actions remain aligned with their human creators' original intent.

---

## 📄 License
This project is a contribution to the **GenLayer Testnet Bradbury Hackathon**.
Developed with 🛡️ by **SoraOnchain**.