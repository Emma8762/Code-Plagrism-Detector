
import numpy as np

def tx_line_params(R, L, G, C, f, d, ZL):
    omega = 2 * np.pi * f

    # Propagation constant
    gamma = np.sqrt((R + 1j*omega*L) * (G + 1j*omega*C))
    alpha = np.real(gamma)
    beta = np.imag(gamma)

    # Characteristic impedance
    Z0 = np.sqrt((R + 1j*omega*L) / (G + 1j*omega*C))

    # Propagation velocity and wavelength
    vp = omega / beta
    wavelength = 2 * np.pi / beta

    # Reflection coefficient
    Gamma = (ZL - Z0) / (ZL + Z0)

    # Standing Wave Ratio
    SWR = (1 + abs(Gamma)) / (1 - abs(Gamma)) if abs(Gamma) < 1 else np.inf

    # Input impedance at distance d
    Zin = Z0 * (ZL + 1j*Z0*np.tan(beta*d)) / (Z0 + 1j*ZL*np.tan(beta*d))

    return {
        "alpha (Np/m)": alpha,
        "beta (rad/m)": beta,
        "Z0 (ohm)": Z0,
        "vp (m/s)": vp,
        "wavelength (m)": wavelength,
        "Reflection Coefficient Γ": Gamma,
        "SWR": SWR,
        "Input Impedance Zin (ohm)": Zin
    }

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("---- Transmission Line Calculator ----")

    # User inputs
    R = float(input("Enter Resistance per unit length R (ohm/m): "))
    L = float(input("Enter Inductance per unit length L (H/m): "))
    G = float(input("Enter Conductance per unit length G (S/m): "))
    C = float(input("Enter Capacitance per unit length C (F/m): "))
    f = float(input("Enter Frequency f (Hz): "))
    d = float(input("Enter Line length d (m): "))

    # Load impedance input
    real_ZL = float(input("Enter Real part of Load Impedance ZL (ohm): "))
    imag_ZL = float(input("Enter Imaginary part of Load Impedance ZL (ohm): "))
    ZL = complex(real_ZL, imag_ZL)

    # Calculate
    results = tx_line_params(R, L, G, C, f, d, ZL)

    # Display results
    print("\n---- Results ----")
    for key, value in results.items():
        print(f"{key}: {value}")




"""# Example test
params = tx_line_params(R=0.1, L=250e-9, G=0, C=100e-12, f=1e9, d=0.1, ZL=50+30j)
for k, v in params.items():
    print(f"{k}: {v}") """