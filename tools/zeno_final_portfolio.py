import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def generate_branded_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    plt.subplots_adjust(bottom=0.2, hspace=0.4)

    x = np.linspace(-10, 10, 1000)
    psi = np.exp(-0.5 * (x + 3)**2) + 0.2 * np.exp(-0.5 * (x - 5)**2)
    time_h = np.arange(0, 24, 1)
    anomalies = np.random.poisson(lam=5, size=24)

    ax1.plot(x, psi, color='cyan', lw=2)
    ax1.fill_between(x, psi, color='cyan', alpha=0.1)
    ax1.set_title("Zeno Labs | Quantum Tunneling Analysis", fontsize=14)

    ax2.step(time_h, anomalies, where='post', color='lime', lw=2)
    ax2.set_title("Sentinel Engine | 24-Hour Variant Log", fontsize=14)

    # Diagonal Watermark
    fig.text(0.5, 0.5, 'INTERNAL USE ONLY - ZENO LABS', fontsize=40,
             color='white', alpha=0.05, ha='center', va='center', rotation=30)

    # Attribution for Zacheriah Alan Potter
    fig.text(0.1, 0.05, f"Zeno Labs Proprietary\nSystem Time: {timestamp}", color='gray', fontsize=9)
    fig.text(0.9, 0.05, f"Lead Architect:\nZacheriah Alan Potter", 
             color='white', fontsize=12, ha='right', fontweight='bold', family='monospace')

    plt.savefig('zeno_final_report.png', dpi=300)
    plt.close(fig)
    print("Success: Final branded report generated: zeno_final_report.png")

if __name__ == "__main__":
    generate_branded_report()
