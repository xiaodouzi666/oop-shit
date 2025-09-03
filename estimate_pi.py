import argparse
import numpy as np


def estimate_pi(num_points: int, seed: int | None = None):
    if seed is not None:
        np.random.seed(seed)  # 固定 RNG，保证复现
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)
    inside = (x * x + y * y) <= 1
    pi_est = 4 * inside.sum() / num_points

    print(f"Number of points: {num_points}")
    print(f"Points inside circle: {inside.sum()}")
    print(f"Estimated value of Pi: {pi_est}")
    print(f"Seed used: {seed}")


def main():
    parser = argparse.ArgumentParser(
        description="Estimate Pi using Monte Carlo simulation."
    )
    parser.add_argument(
        "--num-points",
        type=int,
        default=100_000,
        help="Number of random points to generate.",
    )
    parser.add_argument(
        "--seed", type=int, default=None, help="Random seed for reproducibility."
    )
    args = parser.parse_args()
    estimate_pi(args.num_points, args.seed)


if __name__ == "__main__":
    main()
