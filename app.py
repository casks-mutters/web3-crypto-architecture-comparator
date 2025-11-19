#!/usr/bin/env python3
import argparse
import json
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional
import hashlib
import time


@dataclass
class ProofSystem:
    key: str
    name: str
    family: str
    description: str
    proving_complexity: float    # abstract score 1–10
    verification_cost: float     # abstract score 1–10
    privacy_strength: float      # abstract score 1–10
    soundness_guarantee: float   # abstract score 1–10


SYSTEMS: Dict[str, ProofSystem] = {
    "aztec": ProofSystem(
        key="aztec",
        name="Aztec Noir-style ZK System",
        family="ZK-SNARK privacy model",
        description="A zk system enabling encrypted transactions and private state.",
        proving_complexity=7.8,
        verification_cost=2.1,
        privacy_strength=9.3,
        soundness_guarantee=8.4,
    ),
    "zama": ProofSystem(
        key="zama",
        name="Zama FHE Cryptosystem",
        family="Fully Homomorphic Encryption",
        description="FHE compute model with encrypted inputs, outputs, and logic.",
        proving_complexity=9.2,
        verification_cost=7.8,
        privacy_strength=8.7,
        soundness_guarantee=9.1,
    ),
    "soundness": ProofSystem(
        key="soundness",
        name="Formal Soundness Verification Model",
        family="Proof-oriented protocol engineering",
        description="A system built around rigorous soundness proofs and verifiable execution.",
        proving_complexity=6.1,
        verification_cost=3.2,
        privacy_strength=6.4,
        soundness_guarantee=10.0,
    ),
}


def compute_hash(metadata: Dict[str, Any]) -> str:
    enc = json.dumps(metadata, sort_keys=True).encode()
    return hashlib.sha256(enc).hexdigest()


def compute_quality_index(system: ProofSystem, tx_rate: int) -> float:
    # score explained:
    # privacy + soundness are benefits
    # proving_complexity + verification_cost are penalties
    # tx_rate lightly influences efficiency curve
    benefit = 0.42 * system.privacy_strength + 0.43 * system.soundness_guarantee
    penalty = 0.10 * system.proving_complexity + 0.05 * system.verification_cost
    throughput_factor = min(1.0, max(0.35, 1 - (tx_rate / 20000)))
    return round((benefit - penalty) * throughput_factor, 4)


def build_summary(system: ProofSystem, tx_rate: int) -> Dict[str, Any]:
    base = asdict(system)
    base["txRate"] = tx_rate
    base["qualityIndex"] = compute_quality_index(system, tx_rate)
    base["timestamp"] = int(time.time())
    base["hash"] = compute_hash(base)
    return base


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Cryptographic architecture comparator for Web3 systems."
    )
    p.add_argument(
        "tx_rate",
        type=int,
        help="Transactions per second to evaluate the system under.",
    )
    p.add_argument(
        "--system",
        choices=list(SYSTEMS.keys()),
        default="aztec",
        help="Which proof system to model.",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of human text.",
    )
    return p.parse_args()


def print_human(summary: Dict[str, Any]):
    print("🔐 Cryptographic Architecture Model")
    print(f"System: {summary['name']} ({summary['key']})")
    print(f"Family: {summary['family']}")
    print(f"Description: {summary['description']}")
    print("")
    print(f"Transactions/sec: {summary['txRate']}")
    print(f"Privacy strength: {summary['privacy_strength']}")
    print(f"Soundness guarantee: {summary['soundness_guarantee']}")
    print(f"Proving complexity: {summary['proving_complexity']}")
    print(f"Verification cost:  {summary['verification_cost']}")
    print("")
    print(f"🏁 Quality Index: {summary['qualityIndex']}")
    print(f"🧬 Metadata hash: {summary['hash']}")


def main():
    args = parse_args()
    system = SYSTEMS[args.system]
    data = build_summary(system, args.tx_rate)

    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print_human(data)


if __name__ == "__main__":
    main()
