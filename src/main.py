import os
from functions import (
    load_orders,
    load_invoicing_data,
    get_crate_distribution_per_company,
    create_contact_full_name
)

def main():
    # Rutas a los archivos de datos
    orders_file_path = os.path.join('data', 'orders.csv')
    invoicing_file_path = os.path.join('data', 'invoicing_data.json')

    # Cargar los datos
    orders_df = load_orders(orders_file_path)
    invoicing_df = load_invoicing_data(invoicing_file_path)

    # Calcular la distribución de tipos de cajas por compañía
    crate_distribution = get_crate_distribution_per_company(orders_df)
    print("Distribución de Tipos de Cajas por Compañía:")
    print(crate_distribution)

    # Crear un DataFrame con nombres completos de contactos
    df_1 = create_contact_full_name(orders_df)
    print("DataFrame con Nombres Completos de Contactos:")
    print(df_1)

if __name__ == '__main__':
    main()