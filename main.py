def eliminar_recursividad_izquierda(gramatica):
    nueva_gramatica = {}
    for simbolo, producciones in gramatica.items():
        alfa = [p for p in producciones if p[0] == simbolo]
        beta = [p for p in producciones if p[0] != simbolo]
        nueva_gramatica[simbolo] = []
        if alfa:
            nuevo_simbolo = simbolo + "'"
            for p in beta:
                nueva_gramatica[simbolo].append(p + (nuevo_simbolo,))
            nueva_gramatica[nuevo_simbolo] = [p[1:] + (nuevo_simbolo,) for p in alfa]
            nueva_gramatica[nuevo_simbolo].append(('ε',))
        else:
            nueva_gramatica[simbolo].extend(producciones)
    return nueva_gramatica

def factorizar_terminos_comunes(gramatica):
    nueva_gramatica = {}
    
    
    for simbolo, producciones in gramatica.items():
        repetidos = {}
        prefijos_unicos = set()
        prefijos_comunes = {}
        nueva_gramatica[simbolo] = []
        for produccion in producciones:
            for i in range(len(produccion)):
                prefijo = produccion[:i + 1]
                sufijo = produccion[i + 1:]
                
                if prefijo not in prefijos_comunes:
                    prefijos_comunes[prefijo] = []
                prefijos_comunes[prefijo].append(sufijo)
        
        for prefijo1, sufijos1 in prefijos_comunes.items():
            for prefijo2, sufijo2 in prefijos_comunes.items():
                if prefijo1 != prefijo2 and prefijo1[:len(prefijo2)] == prefijo2:
                    repetidos[prefijo2]= sufijo2
                else:
                    prefijos_unicos.add(prefijo1)
        
        elejido = max(repetidos.keys(), key=lambda x: len(x))
        
    
        if len(repetidos[elejido]) < 2 :
            nueva_gramatica[simbolo] = gramatica[simbolo]
            continue
        
        
        del repetidos[elejido]
        
        prefijos_filtrados = {}
        for prefijo, sufijos in prefijos_comunes.items():
            if prefijo not in repetidos.keys() and (prefijo not in prefijos_unicos or prefijo == elejido):
                prefijos_filtrados[prefijo] = sufijos

        elejido_str = ''.join(elejido)
        for prefijo, sufijos in prefijos_filtrados.items():
            if prefijo == elejido and elejido:
                nuevo_simbolo = simbolo + '*' 
                nueva_gramatica[simbolo].append(prefijo + (nuevo_simbolo,))
                nueva_gramatica[nuevo_simbolo] = sufijos
            else:
                nueva_gramatica[simbolo].append(prefijo)

        for prefijo_unido in prefijos_unicos:
            prefijo_unido_str = ''.join(prefijo_unido)
            if not prefijo_unido_str.startswith(elejido_str) and prefijo_unido not in repetidos.keys():
                nueva_gramatica[simbolo].append(prefijo_unido)
    return nueva_gramatica

# Gramática dada
gramatica = {
    'S': [('uno', 'S', 'dos'), ('uno', 'S', 'tres'), ('ε',)],
    'A': [('uno', 'A', 'cuatro'), ('ε',)]
}

# Aplicar eliminación de recursividad por la izquierda y factorización de términos comunes
nueva_gramatica_factorizacion = factorizar_terminos_comunes(gramatica)
nueva_gramatica_rec_izquierda = eliminar_recursividad_izquierda(gramatica)

def imprimir_gramatica(gramatica):
    for simbolo, producciones in gramatica.items():
        print(f"{simbolo} -> ", end="")
        for i, produccion in enumerate(producciones):
            if i > 0:
                print(" | ", end="")
            print(" ".join(map(str, produccion)), end="")
        print()

# Ejemplo de uso:
print("Gramática original:")
imprimir_gramatica(gramatica)
print("\nGramática después de eliminar recursividad por la izquierda:")
imprimir_gramatica(nueva_gramatica_rec_izquierda)
print("\nGramática después de factorización de términos comunes:")
imprimir_gramatica(nueva_gramatica_factorizacion)
