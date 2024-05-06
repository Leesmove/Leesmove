import matplotlib.pyplot as plt

# Datos de ejemplo: ventas mensuales
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ventas = [100, 120, 110, 90, 95, 130, 140, 150, 160, 170, 180, 200]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(meses, ventas, color='skyblue')

# Añadir título y etiquetas
plt.title('Ventas Mensuales de Producto X en 2024')
plt.xlabel('Mes')
plt.ylabel('Ventas')

# Mostrar el gráfico
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visualización
plt.tight_layout()  # Ajustar el diseño para que no se recorten las etiquetas
plt.show()
