def accuracy_from_targets(counts: dict, targets: list[str]) -> float:
    """
    Compute accuracy (%) for multiple correct outputs.
    """
    total_shots = sum(counts.values())
    if total_shots == 0:
        return 0.0

    correct = sum(counts.get(t, 0) for t in targets)
    return 100.0 * correct / total_shots