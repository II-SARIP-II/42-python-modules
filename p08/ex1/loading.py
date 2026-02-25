import sys


def check_loaded_modules() -> None:
    try:
        import pandas as pd
        import numpy as np
        import matplotlib
        from matplotlib import pyplot as plt

        targets = {
            "pandas": pd,
            "numpy": np,
            "matplotlib": matplotlib
        }

        for name, mod in targets.items():
            if any(name in m for m in sys.modules):
                print(f"[OK] {name} ({mod.__version__}) - Data manipulation "
                      "ready")
            else:
                print(f"ALERT: {name} is NOT loaded.")

        print("Analyzing Matrix data...")
        data = {
            "Timeline": np.arange(100),
            "Signal": np.random.randn(100).cumsum()
        }
        df = pd.DataFrame(data)

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.plot(df["Timeline"], df["Signal"], color='green',
                 label='Neural Link')
        plt.title("Matrix Neural Signal Analysis")
        plt.xlabel("Time (ms)")
        plt.ylabel("Stability")

        filename = "matrix_analysis.png"
        plt.savefig(filename)
        print(f"Analysis complete!\nResults saved to: {filename}")
        plt.close()

    except ImportError as ie:
        print(f"Extraction Failed: Missing bio-digital components. {ie}")
    except Exception as e:
        print(f"Detection failed: {e}")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    check_loaded_modules()
