def get_tipo_dato(dato):

    if ',' in dato:

        dato = dato.replace('.', '')
        dato = dato.replace(',', '.')
        n_decimales = len(dato.split('.')[1])

        try:

            int(dato)
            return 'entero'
        except ValueError:
            try:

                float(dato)
                return f'decimal de {n_decimales} decimales'
            except ValueError:
                return 'text'
    return 'text'


def split_registros_con_fusion(texto, campos_por_registro, separador=';'):
    campos = texto.replace(' ', '.').split(';')
    if (separador != ';'):
        campos = texto.replace(' ', '.').split(separador)

    print(f'[DEBUG] Campos obtenidos: {campos}')
    longitud_primer_registro = len(campos[0])
    registros = []
    i = 0

    while i + campos_por_registro - 1 < len(campos):

        # Los primeros 24 campos
        registro = campos[i:i+campos_por_registro - 1]
        print(f'[DEBUG] REGISTRO CON {campos_por_registro-1} CAMPOS', registro)
        print(f'[DEBUG] Campo nº {campos_por_registro}: ',
              campos[i+campos_por_registro-2])
        n_campo = campos[i + campos_por_registro - 2]
        registro.append(n_campo)
        print(f'[DEBUG] REGISTRO CON {campos_por_registro} CAMPOS', registro)
        print(f'[DEBUG] Campo {campos_por_registro} corregido : ',
              n_campo[:-longitud_primer_registro].replace('.', ''))
        # El campo 25 viene fusionado con el campo 1 del siguiente registro
        campo_fusionado = campos[i + campos_por_registro - 1]
        primer_campo_siguiente = campo_fusionado[-longitud_primer_registro:]
        x = 1
        print('[DEBUG] Suposición del campo 1: ',
              campo_fusionado[-longitud_primer_registro:])
        for campo in registro:

            print(
                f'[INFO] Campo {x} : {campo} : {len(campo)} caracteres : tipo {get_tipo_dato(campo)}')
            x += 1
        total = sum(len(reg) for reg in registro)
        print(f'[INFO] Longitud total del registro: {total}')
        print(
            f'[INFO] Longitud de registros + separadores: {total + len(registro)} - 1 si no hay separador final {total + len(registro) - 1}')
        break

    return registros


texto = input("Introduce el texto a analizar:\n")
n_registros = 0
separador = input(
    "Introduce el separador de campos (por defecto ';'):\n") or ';'
while n_registros == 0:
    n_registros = int(
        input("Introduce el número de campos por registro: "))


registros = split_registros_con_fusion(texto, n_registros, separador)

for idx, r in enumerate(registros):
    print(f"Registro {idx+1} ({len(r)} campos): {r}")
