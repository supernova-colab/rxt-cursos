def L(title, lead, steps, no, si):
    return [title, lead, steps, [no, si]]

def B(t, n, d, quiz, lessons):
    return {"t": t, "n": n, "d": d, "quiz": quiz, "lessons": lessons}

def Q(topic, q, opts, ok, why):
    assert len(opts) == 4 and 0 <= ok < 4
    return [topic, q, opts, ok, why]

def intro(n, d, lead, steps, no, si):
    howto = L('Cómo funciona este curso', 'Bloques cortos, un mini examen por bloque y un examen final.',
              ['Lee cada lección con calma y marca cada punto cuando lo leas.',
               'Al final de cada bloque contesta el mini examen. Con 90% se abre el siguiente.',
               'Si no llegas a 90%, repasa y vuelve a intentar las veces que necesites.',
               'Al terminar todos los bloques se abre el examen final y, si apruebas, tu certificado.'],
              'Contestar sin leer para terminar rápido.', 'Leer, practicar con los ejemplos y preguntar si algo no queda claro.')
    return B('Introducción', n, d, [], [L(n, lead, steps, no, si), howto])
