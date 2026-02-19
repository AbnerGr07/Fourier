import numpy as np          #ñibrerias necesarias para hacer esto // si no tienes nada, instalar python, vs o cualquier hacer entorno virtual e intalar estas librerias
import matplotlib.pyplot as plt
#commentar mas para que sea legible el codigo
# def coefficientes_f1 y para cada n q hay se va incrementando 1 en def fourier series
def coefficients_f1(n):       
    """
    f(t) = t^2 + 2πt +π^2 en [-π, π]
    """
    a0 = 4 * np.pi**2 / 3
    an = 4 * (-1)**n / n**2
    bn = 4 * np.pi * (-1)**n / n
    return a0, an, bn

def coefficients_f2(n):
    """
    f(t) = 0 para t en [-π, 0]
    f(t) = e^-t pata t en [0, π]
    """
    e_pi = np.exp(-np.pi)  #numpy np.exp para e elevado a algo y -np.pi es pi negativo
    a0 = (1 - e_pi) / np.pi     #en fourier se usa a0/2 y si multiplicamos esto quitamos los 2 por eso se pone asi
    an = (1 - (-1)**n * e_pi) / (np.pi * (1 + n**2))
    bn = n * (1 - (-1)**n * e_pi) / (np.pi * (1 + n**2))
    return a0, an, bn

def coefficients_f3(n):
    """
    f(t) = 1 para t ∈ [-π, 0]
    f(t) = e^-t  para t ∈ [0,  π]
    """
    e_pi = np.exp(-np.pi)
    a0 = 1 + (1 - e_pi) / np.pi
    an = (1 - (-1)**n * e_pi) / (np.pi * (1 + n**2))
    bn = (1 / np.pi) * ((1 - (-1)**n) / n + n * (1 - (-1)**n * e_pi) / (1 + n**2))
    return a0, an, bn

def coefficients_f4(n):
    """
    f(t) = t/np.pi + 1 para t ∈ [-π, 0]
    f(t) = e^-t  para t ∈ [0,  π]
    a0 = 1 + (1 + e^{-π})/π
    """
    e_pi = np.exp(-np.pi)
    a0 = 1 + (1 + e_pi) / np.pi #igual que la 2 se le quitan los 2 dividiendo
    an = (1 - (-1)**n) / (np.pi**2 * n**2) + (1 - (-1)**n * e_pi) / (np.pi * (1 + n**2))
    bn = -1 / (np.pi * n) + n * (1 - (-1)**n * e_pi) / (np.pi * (1 + n**2))
    return a0, an, bn

def coefficients_f5(n):
    """
    Función triangular impar (de la gráfica):
      f(t) = (t+π)/2   en [-π, -π/2]  → sube de 0 a π/4
      f(t) = -t/2      en [-π/2,  0]  → baja de π/4 a 0
      f(-t) = -f(t)    (impar)
    Solo bₙ (an = 0 por ser función impar):
      bn = -2/(π·n²) · sin(nπ/2)
    """
    a0 = 0
    an = 0
    bn = (-2 / (np.pi * n**2)) * np.sin(n * np.pi / 2)
    return a0, an, bn

# suma de todo en fourier series

def fourier_series(t, N, coeff_func):   #t es el vector tiempo, N numero de vueltas, ciclos y coeff cual funcion
    approximation = coeff_func(1)[0] / 2   # a0/2 (a0 no depende de n)
    for n in range(1, N + 1):
        a0, an, bn = coeff_func(n)  #se obtiene los coeficientes para el valor de n
        approximation = approximation + an * np.cos(n * t) + bn * np.sin(n * t)  #aproximacion
    return approximation

# Se configura de donde hasta donde va a ir la onda y cuantos periodos se ven y 4000 = n que tan pixeleado pero pueeds hacer un calculo 8pi/n =
t = np.linspace(-4 * np.pi, 4 * np.pi, 4000)

PI_TICKS  = np.arange(-4, 5) * np.pi   #posicion munerica donde van marcas
PI_LABELS = [r'$-4\pi$', r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$',   # textos donde se muestra
             r'$\pi$',   r'$2\pi$',  r'$3\pi$',  r'$4\pi$']
functions = [          #diccionarios con 3 claves  /// ¡¡¡Si solo quieres ver la grafica especifica comenta todas las que no quieres desde el corchete de avertura {¨ hasta el de cierre  }, en https://python-fiddle.com/examples/matplotlib  porque esta raro y aveces acepta 1 o te da todas como se supone que debe funcionar
    {
        "name":  r"$f_1(t)=t^2+2\pi t + \pi^2$",
        "coeff": coefficients_f1,
        "color": "#E74C3C",
    },
    {
        "name":  r"$f_2(t)$: $0$ and $e^{-t}$",  #$ se usan diferente para espacios y acomodar asi
        "coeff": coefficients_f2,
        "color": "#2ECC71", 
    },
    {
        "name":  r"$f_3(t)$: $1$ and $e^{-t}$",   
        "coeff": coefficients_f3,
        "color": "#F39C12", 
    },
    {
        "name":  r"$f_4(t)=t+e^t$",                  
        "coeff": coefficients_f4,
        "color": "#3498DB",
    },
    {
        "name":  r"$f_5(t)$: -π , π  (sawtooth wave)",
        "coeff": coefficients_f5,
        "color": "#9B59B6", 
    },
]
# cuantas vueltas o n o ciclos quieres
while True:
    try:
        N = int(input("Número de componentes de Fourier (entero positivo): "))
        if N > 0:
            break
        else:
            print("Ingresa un entero positivo.")
    except ValueError:
        print("Entrada inválida. Ingresa un entero.")

# Las 5 en diferentes ventanas
for i, func in enumerate(functions):
    f_approx = fourier_series(t, N, func["coeff"])
    fig, ax = plt.subplots(figsize=(14, 5), num=i + 1)   # num= evita sobreescribir
    ax.plot(t, f_approx, color=func["color"], linewidth=2,
            label=f'Fourier Series  N={N}\n{func["name"]}')
    ax.set_xlabel("t")
    ax.set_ylabel("f(t)")
    ax.set_title(f'Fourier Series – {func["name"]}')
    ax.set_xticks(PI_TICKS)
    ax.set_xticklabels(PI_LABELS)
    ax.grid(True, alpha=0.4)
    ax.legend(fontsize=11)
    fig.tight_layout()
plt.show()   # muestra TODAS las ventanas juntas al final

# SI QUIERO QUE TODAS ESTEN EN UNA GRAFICA DESCOMENTO ESTO DE ABAJO Y TIENES QUE COMENTAR DESDE EL FOR HASTA PTL.SHOW DE ARRIBA ¡quidar indentacion
##fig, ax = plt.subplots(figsize=(16, 6))
##for func in functions:
##    f_approx = fourier_series(t, N, func["coeff"])
##    ax.plot(t, f_approx, color=func["color"], linewidth=2, label=func["name"])
##ax.set_xlabel("t")
##ax.set_ylabel("f(t)")
##ax.set_title(f"Series de Fourier – Todas las funciones  (N={N})")
##ax.set_xticks(PI_TICKS)
##ax.set_xticklabels(PI_LABELS)
##ax.grid(True, alpha=0.4)
##ax.legend(fontsize=11)
##plt.tight_layout()
##plt.show()