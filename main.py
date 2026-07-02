from naca4digit import NACA4Digit

def main():
    foil = NACA4Digit(
        chord=1.0,
        mcamber=0.04,
        p=0.4,
        mthick=0.12,
        n_points=500
    )

    foil.plot()

if __name__ == "__main__":
    main()
