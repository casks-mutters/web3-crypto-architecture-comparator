# web3-crypto-architecture-comparator

A compact research tool for comparing Web3 cryptographic architectures.  
This project models abstract properties of systems inspired by:

- **Aztec** (ZK-SNARK private computation)  
- **Zama** (FHE encrypted compute)  
- **Soundness-first labs** (formal verification and proof-oriented protocol engineering)

The repository contains **exactly two files**:
- `app.py`
- `README.md`


## Purpose

This tool evaluates privacy-oriented and correctness-oriented architectures by computing:

- Privacy strength  
- Soundness / assurance properties  
- Proving complexity  
- Verification overhead  
- A composite **Quality Index**  
- A reproducible **metadata hash** identifying each evaluation snapshot

It is designed for early-stage protocol design, research, and architectural comparison.


## Installation

Requirements:
- Python 3.8+

Steps:

1. Clone the repository.
2. Ensure `app.py` and `README.md` are in the project root.
3. Run with python:



## Output Description

Each execution prints:

- System name  
- Cryptographic family  
- Short description  
- Privacy strength  
- Soundness guarantee  
- Proving & verification costs  
- A computed **Quality Index**  
- Timestamp  
- Deterministic SHA-256 metadata hash  


## Notes

- All system parameters are conceptual abstractions, not real-world benchmarks.  
- The tool does not connect to a blockchain or RPC endpoint.  
- The profiles can be extended to model custom architectures or real protocol metrics.

