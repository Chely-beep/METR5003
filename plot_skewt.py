# Create the Skew-T background
fig, ax = plot_skewt.create_skewt(skew=-20)

# Pressure levels from the model (convert Pa -> hPa)
p_mid_hPa = grid["p_mid"] / 100.0

# Plot final equilibrium profiles
for mode, color in zip(
    ["radiative", "dry", "moist"],
    ["blue", "red", "orange"]
):
    T_final_K = np.array(history_save[mode]["T"][-1])
    T_final_C = T_final_K - 273.15

    T_sk = plot_skewt.skewT(T_final_C, p_mid_hPa, skew=-20)

    ax.plot(
        T_sk,
        p_mid_hPa,
        linewidth=2.5,
        label=f"{mode} equilibrium"
    )

ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
plt.tight_layout()
plt.show()