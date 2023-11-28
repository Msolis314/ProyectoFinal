import matplotlib.pyplot as plt

# Datos de ejemplo
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

# Crear el gráfico de pastel
fig, ax = plt.subplots()
pie_patches, _, autotexts = ax.pie(sizes, autopct='%1.1f%%')

# Personalizar los porcentajes automáticos
for autotext in autotexts:
    autotext.set_color('white')

# Crear la leyenda
legend_labels = [f'{label}: {size}%' for label, size in zip(labels, sizes)]
ax.legend(pie_patches, legend_labels, loc='upper right')

plt.show()

