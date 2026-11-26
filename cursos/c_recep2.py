from base import L, B, Q, intro
import c_recep as O

ID = 'recep-pro'
TITLE = 'Caja, clases de prueba y situaciones especiales'
SHORT = 'Caja y casos especiales'
CODE = 'P'
PUESTOS = ['rec']
FULL = 'Curso de caja, clases de prueba y situaciones especiales en recepción'
DESC = 'Cobrar sin errores, cuadrar la caja, organizar clases de prueba y saber qué hacer en lesiones, emergencias, llamadas y objetos olvidados.'

def blk(old, t):
    b = dict(old)
    b['t'] = t
    return b

BLOCKS = [
intro('Lo que pasa detrás del mostrador', 'Cobros, caja, clases de prueba y momentos difíciles.',
 'El cliente no ve la caja ni la agenda, pero si fallan, lo siente. Este curso es para que nada falle.',
 ['Aquí no repetimos lo de atención básica: aquí vemos <b>cobro</b>, <b>caja</b>, <b>clases de prueba</b> y <b>situaciones especiales</b>.',
  'Cada lección trae el paso a paso y ejemplos de “así no” y “así sí”.',
  'Horario de RXT: lunes a viernes 6–10 am y 2–9 pm; sábado 7–10 am; domingo cerrado. Pagos en efectivo, tarjeta o transferencia.'],
 '“Eso le toca al encargado.”', '“Yo sé qué hacer y, si no, aviso al encargado al momento.”'),
blk(O.BLOCKS[5], 'Bloque 1'),
blk(O.BLOCKS[6], 'Bloque 2'),
B('Bloque 3', 'Clases de prueba y agenda', 'Desde que alguien agenda su clase de prueba hasta que decide inscribirse.',
 ['Prueba'], [
 L('Agendar y confirmar la clase de prueba', 'Una clase agendada sin confirmar es una clase que se pierde.',
  ['Anota en la agenda: <b>nombre, teléfono, día, hora y objetivo</b>.',
   'Revisa que haya lugar en esa clase antes de confirmar.',
   'Un día antes manda confirmación: “Hola, Pablo, te esperamos mañana a las 7 am. Trae agua y toalla 💪”.',
   'Si cancela, ofrécele otra fecha en ese mismo mensaje.'],
  'Apuntarlo en un papelito que luego se pierde.', 'Agenda, confirmación un día antes y otra fecha si cancela.'),
 L('Preparar la visita', 'Que el coach ya sepa quién viene antes de que llegue.',
  ['Avisa al coach del horario: nombre, objetivo y si tiene alguna lesión.',
   'Al llegar, pídele sus datos y pregúntale con discreción por lesiones, dolor o embarazo.',
   'Enséñale dónde están baños, agua y dónde dejar sus cosas.',
   'Preséntalo con el coach por su nombre: “Coach, él es Pablo, viene a su primera clase”.'],
  'Que llegue y nadie sepa quién es.', 'El coach ya lo espera y lo recibe por su nombre.'),
 L('Después de la clase de prueba', 'Aquí se decide si se queda.',
  ['Pregúntale primero cómo se sintió, antes de hablar de planes.',
   'Escucha lo que le gustó y recomiéndale el plan que va con su objetivo y horario.',
   'Si se inscribe: cobro, registro, app y bienvenida completa.',
   'Si no decide hoy: agradece, anota y dale seguimiento según el curso de mensajes.'],
  'Darle la lista de precios y despedirlo.', '“¿Cómo te sentiste? Con tu horario te queda perfecto el plan de…”'),
]),
B('Bloque 4', 'Situaciones especiales', 'Lesiones, emergencias, llamadas y objetos olvidados.',
 ['Especiales'], [
 L('Llega un cliente con lesión o dolor', 'Tú no diagnosticas: avisas y acomodas.',
  ['Pregunta con calma dónde le duele y desde cuándo.',
   'Avisa al coach <b>antes</b> de la clase para que adapte los ejercicios.',
   'Si el dolor es fuerte o reciente, sugiérele revisarse con un médico o fisioterapeuta antes de entrenar.',
   'Anota el caso para que el siguiente turno lo sepa.'],
  '“Ah, no pasa nada, entra.”', 'Avisar al coach, sugerir revisión y anotarlo.'),
 L('Emergencia en el gym', 'En una emergencia, recepción coordina.',
  ['Si alguien se desmaya, tiene dolor de pecho, se golpea fuerte o no responde: <b>llama al 911</b> y avisa al coach al momento.',
   'Ten a la mano el botiquín y la dirección exacta del gym para darla por teléfono.',
   'Abre paso en la entrada y aleja a la gente para dar espacio.',
   'Después: anota qué pasó, a qué hora y quién ayudó, y avisa al encargado.'],
  'Quedarse parada esperando a ver qué pasa.', 'Llamar, avisar, abrir paso y anotar.'),
 L('Llamadas por teléfono', 'Por teléfono no te ven: tu voz es tu sonrisa.',
  ['Contesta antes del tercer timbre: “Roxet Training Club, habla Ana, ¿en qué te ayudo?”.',
   'Si estás atendiendo a alguien en persona, pide un momento y regresa rápido.',
   'Anota nombre y teléfono de quien llama antes de colgar.',
   'Si piden informes, invita a una clase de prueba con día y hora.'],
  '“¿Bueno? ¿Quién?”', 'Saludo con el nombre del gym, tu nombre y una invitación.'),
 L('Objetos olvidados', 'Lo que se queda en RXT se cuida como si fuera tuyo.',
  ['Guarda el objeto en el lugar asignado y anótalo: qué es, dónde y cuándo se encontró.',
   'Si sabes de quién es, mándale mensaje.',
   'Para entregarlo, confirma que es suyo (que lo describa).',
   'Nunca lo regales ni lo uses.'],
  'Dejarlo en el mostrador “a ver quién lo reclama”.', 'Guardarlo, anotarlo y avisar al dueño.'),
]),
]

QS = [q for q in O.QS if q[0] in ('Cobro', 'Caja')] + [
Q('Prueba', '¿Cuándo se confirma una clase de prueba?', ['Nunca', 'Un día antes, por mensaje', 'Una hora después', 'Cuando llegue'], 1, 'Confirmación un día antes.'),
Q('Prueba', '¿Qué le avisas al coach antes de una clase de prueba?', ['Nada', 'Nombre, objetivo y si tiene lesión', 'Cuánto gana', 'Su dirección'], 1, 'Así el coach lo espera.'),
Q('Prueba', 'Termina la clase de prueba. ¿Qué haces primero?', ['Le das precios', 'Le preguntas cómo se sintió', 'Lo despides', 'Le cobras'], 1, 'Primero escuchar.'),
Q('Prueba', 'El cliente cancela su clase de prueba. ¿Qué haces?', ['Lo borras', 'Le ofreces otra fecha', 'Te enojas', 'Nada'], 1, 'Siempre otra opción.'),
Q('Especiales', 'Alguien tiene dolor de pecho y se marea. ¿Qué haces?', ['Le das agua y sigue', 'Llamas al 911 y avisas al coach', 'Esperas', 'Lo mandas a casa solo'], 1, 'Es una emergencia.'),
Q('Especiales', 'Llega un cliente con dolor de rodilla. ¿Qué haces?', ['Lo diagnosticas', 'Avisas al coach antes de la clase y lo anotas', 'Le das una pastilla', 'Nada'], 1, 'Tú no diagnosticas.'),
Q('Especiales', '¿Cómo contestas el teléfono?', ['“¿Bueno?”', '“Roxet Training Club, habla Ana, ¿en qué te ayudo?”', 'No contestas', '“¿Quién habla?”'], 1, 'Nombre del gym y el tuyo.'),
Q('Especiales', 'Encuentras unos audífonos olvidados. ¿Qué haces?', ['Te los quedas', 'Los guardas, los anotas y avisas al dueño', 'Los dejas en el mostrador', 'Los tiras'], 1, 'Se cuidan como propios.'),
]
