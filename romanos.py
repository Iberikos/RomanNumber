simbolos = {
    'unidades':['','I','II','III','IV','V','VI','VII','VIII','IX'],
    'decenas': ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],    
    'centenas': ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
    'millares': ['','M','MM','MMM']
    }

digitos_romanos = {
    'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000

    }

def a_numero(cadena):
    acumulador = 0
    valor_ant = 0
    cuenta_repeticiones = 0
    cuenta_resta = 0
    
    for caracter in cadena:
        valor = digitos_romanos.get(caracter)
        if not valor:
            raise ValueError("El mío")
        
        if valor_ant > 0 and valor > valor_ant:
            if cuenta_resta > 0:
                raise ValueError("No se pueden hacer restas consecutivas")
            if cuenta_repeticiones > 0:
                raise ValueError("No se puede hacer restas dentro de repeticiones")
        
            if valor_ant in (5, 50, 500):
                raise ValueError("No se pueden restar V, L, D")
            
            if valor_ant > 0 and valor > 10 * valor_ant:
                raise ValueError("No se admiten restas entre digitos 10 veces mayor")
            
            acumulador = acumulador - valor_ant
            acumulador = acumulador + valor - valor_ant3
            cuenta_resta += 1
        else:
            acumulador += valor
            cuenta_resta = 0
            
        if valor == valor_ant:
            if valor in (5, 50, 500):
                raise ValueError('No se puede repetir V, L o D')   
            cuenta_repeticiones += 1
            if cuenta_repeticiones ==3:
                raise ValueError("Demasiadas repeticiones de {}".format(caracter))
        
        else:
            cuenta_repeticiones = 0
        
        valor_ant = valor
    
    return acumulador    

def validar(n):
    if not isinstance(n, int):
        raise ValueError("{} debe ser un entero".format(n))

    if n < 0 or n > 3999:
        raise ValueError("{} debe de estar entre 0 y 3999".format(n))
    
def a_romano(n):
    validar(n)
    c="{:04d}".format(n)
    
    unidades = int(c[-1])
    decenas = int(c[-2])
    centenas = int(c[-3])
    millares = int (c[-4])
    
    return simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]





