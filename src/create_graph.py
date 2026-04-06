import matplotlib.pyplot as plt

# Results obtained by running main.py on each test.in file
results = [
    (40, 0.000152),
    (40, 0.000236),
    (80, 0.000694),
    (80, 0.000567),
    (120, 0.001237),
    (120, 0.001243),
    (160, 0.002286),
    (160, 0.002633),
    (200, 0.003582),
    (200, 0.003492),
]


def plot_results(results):
    ns = [r[0] for r in results]
    runtimes = [r[1] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(ns, runtimes, marker='o')

    plt.title('Runtime vs String Length')
    plt.xlabel('String Length (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)

    output_file = 'data/tests/runtime_graph.png'
    plt.savefig(output_file)
    print(f"Graph saved to {output_file}")


if __name__ == "__main__":
    plot_results(results)
