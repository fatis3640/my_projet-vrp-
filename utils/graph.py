import matplotlib.pyplot as plt

def plot_routes(routes, coords, names):

    for i, route in enumerate(routes):

        x = []
        y = []

        for node in route:
            x.append(coords[node][0])
            y.append(coords[node][1])

        plt.plot(x, y, marker='o', label=f"Truck {i+1}")

    # أسماء المناطق
    for i, (x, y) in enumerate(coords):
        plt.text(x, y, names[i])

    plt.title("Optimisation des routes - Nouakchott")
    plt.legend()
    plt.grid()

    # 🔥 حفظ الصورة
    plt.savefig("vrp_result.png")

    plt.show()