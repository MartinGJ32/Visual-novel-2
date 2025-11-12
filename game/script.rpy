# The script of the game goes in this file.
define kira = Character("Kira")
define L = Character("L")
define light = Character("Light")
define matt = Character("Matt")
define mello = Character("Mello")
define mikami = Character("Mikami")
define misa = Character("Misa")
define near = Character("Near")
define rem = Character("Rem")
define ryuk = Character("Ryuk")
define sidoh = Character("Sidoh")
define takada = Character("Takada")
define watari = Character("Watari")
define padre = Character("Padre")
define yuri = Character("Yuri")
define jefe = Character("Jefe Yagami")
define mogi = Character("Mogi")
define matsuda = Character("Matsuda")
define aizawa = Character("Aizawa")
define profesor = Character('Profesor')
define mensaje = Character('Mensaje')
define transeunte_1 = Character('Trasenutne 1')
define transeunte_2 = Character('Trasenutne 2')
define noticiero = Character('Noticiero')
define estudiante_1 = Character('Estudiante 1')
define estudiante_2 = Character('Estudiante 2')
define locutor = Character('Locutor')

#fotos de personajes
image light_enojado = im.Scale("Light/light-enojado-1.png", 540, 540)
image light_estresado = im.Scale("Light/light-estresado-1.png", 540, 540)
image light_frente = im.Scale("Light/light-frente-1.png", 540, 540)
image light_perfil = im.Scale("Light/light-perfil-1.png", 540, 540)
image light_pensando = im.Scale("Light/light-pensando-1.png", 540, 540)
image light_sorpendido = im.Scale("Light/light-enojado-1.png", 540, 540)

image ryuk_frente = im.Scale("Ryuk/ryuk-frente.png", 540, 540)
image ryuk_perfil = im.Scale("Ryuk/ryuk-frente.png", 540, 540)

image yuri_i = im.Scale("yuri/yuri.png", 540, 540)

image padre_molesto = im.Scale("padre/padre-molesto.png", 540, 540)
image padre_normal = im.Scale("padre/padre-normal.png", 540, 540)
image padre_serio = im.Scale("padre/padre-serio.png", 540, 540)

image matsuda_asustado = im.Scale("matsuda/matsuda-asustado.png", 540, 540)
image matsuda_enojado = im.Scale("matsuda/matsuda-enojado.png", 540, 540)
image matsuda_estresado = im.Scale("matsuda/matsuda-estresado.png", 540, 540)
image matsuda_hablando = im.Scale("matsuda/matsuda-hablando.png", 540, 540)
image matsuda_miedo = im.Scale("matsuda/matsuda-miedo.png", 540, 540)
image matsuda_perfil = im.Scale("matsuda/matsuda-perfil.png", 540, 540)
image matsuda_riendose = im.Scale("matsuda/matsuda-asustado.png", 540, 540)

image jefe_discutiendo = im.Scale("jefe/jefe-discutiendo.png", 540, 540)
image jefe_enojado = im.Scale("jefe/jefe-enojado.png", 540, 540)
image jefe_frente = im.Scale("jefe/jefe-frente.png", 540, 540)
image jefe_renegando = im.Scale("jefe/jefe-renegando.png", 540, 540)
image jefe_serio = im.Scale("jefe/jefe-serio.png", 540, 540)
image jefe_sorprendido = im.Scale("jefe/jefe-sorprendido.png", 540, 540)

image l_asombrado = im.Scale("L/lawiet-asombrado.png", 540, 540)
image l_explicando = im.Scale("L/lawiet-explicando.png", 540, 540)
image l_molesto = im.Scale("L/lawiet-molesto.png", 540, 540)
image l_neutral = im.Scale("L/lawiet-neutral.png", 540, 540)
image l_pensando = im.Scale("L/lawiet-pensando.png", 540, 540)
image l_serio = im.Scale("L/lawiet-serio.png", 540, 540)
image l_sorprendido = im.Scale("L/lawiet-sorprendido.png", 540, 540)

#fotos de fondos
image salon = im.Scale("fondos/escuela.jpg", config.screen_width, config.screen_height)
image almacen = im.Scale("fondos/almacen.jpg", config.screen_width, config.screen_height)
image banco = im.Scale("fondos/banco.jpg", config.screen_width, config.screen_height)
image cafe = im.Scale("fondos/cafe.jpg", config.screen_width, config.screen_height)
image terrasa_colegio = im.Scale("fondos/colegio-colegio.jpg", config.screen_width, config.screen_height)
image fabricas = im.Scale("fondos/fabricas.jpg", config.screen_width, config.screen_height)
image headquarters = im.Scale("fondos/headquarters.jpg", config.screen_width, config.screen_height)
image kanto_1 = im.Scale("fondos/kanto-1.jpg", config.screen_width, config.screen_height)
image kanto_2 = im.Scale("fondos/kanto-2.jpg", config.screen_width, config.screen_height)
image kanto_3 = im.Scale("fondos/kanto-3.jpg", config.screen_width, config.screen_height)
image l_anuncio = im.Scale("fondos/l-anuncio.jpg", config.screen_width, config.screen_height)
image light_pieza = im.Scale("fondos/light-room.webp", config.screen_width, config.screen_height)
image l_hotel = im.Scale("fondos/pieza-l.jpg", config.screen_width, config.screen_height)
image pieza = im.Scale("fondos/pieza-protagonista.jpg", config.screen_width, config.screen_height)
image casa_yagami = im.Scale("fondos/Yagami_house.webp", config.screen_width, config.screen_height)
image comedor = im.Scale("fondos/comedor.jpg", config.screen_width, config.screen_height)
image mundo_shinigami = im.Scale("fondos/mundo-shinigami.webp", config.screen_width, config.screen_height)
image puerta_escuela = im.Scale("fondos/puerta-escuela.webp", config.screen_width, config.screen_height)
image escuela = im.Scale("fondos/escuela.jpg", config.screen_width, config.screen_height)
image subte = im.Scale("fondos/subte.jpg", config.screen_width, config.screen_height)


# Declaración de variables de inicio
default nombre = ""
default pronombre = ""
default tendencia = ""
default ciudad = ""
# Afinidades principales (0-30)
default alineacion_kira = 0
default alianza_l = 0
default codicia_dn = 0

# Relaciones personales (0-15)
default confianza_light = 5
default confianza_l = 0
default confianza_misa = 0

# Romance (booleano + nivel)
default romance_light = False
default romance_l = False
default nivel_romance = 0  # (0-10)

#Eventos menores de la historia
default almuerzo_azotea = False

# Estados críticos
default naomi_viva = False
default toco_death_note = False
default vio_shinigami = False
default l_muerto = False
default light_tiene_recuerdos = False

# Contadores
default decisiones_pro_kira = 0
default decisiones_pro_l = 0
default vidas_salvadas = 0



transform mover_personaje_izquierda:
    xalign 0.1
    yalign 0.5
    block:
        linear 0.5 yoffset 5
        linear 1.0 yoffset 0
        repeat
    time 10.0
    yoffset 0

transform mover_personaje_derecha:
    xalign 0.9
    yalign 0.5
    block:
        linear 0.5 yoffset 5
        linear 1.0 yoffset 0
        repeat
    time 10.0
    yoffset 0    

transform quieto_izquierda:
    xalign 0.1
    yalign 0.5
    yoffset 0

transform quieto_derecha:
    xalign 0.9
    yalign 0.5
    yoffset 0    



# The game starts here.

label start:

    scene black


    "Antes de comenzar, algunas preguntas..."

    $ nombre = renpy.input("¿Como te llamas?")
    $ nombre = nombre.strip()
    $ protagonista = Character(nombre)    

    $ ciudad = renpy.input("¿De donde eres?")
    $ ciudad = ciudad.strip()

    # Menú para género
    "¿Cual es tu gereno?"
    menu:
        'Masculino':
            $ pronombre = "El"
            pass
        'Femenino':
            $ pronombre = "Ella"
            pass
        'No binario':
            $ pronombre = "Ellx"
            pass

    "¿Cuál es tu mayor interés?"
    menu:
        'La justicia y el orden':
            $ tendencia = "L"
            pass
        'El cambio y la revolución':
            $ tendencia = "Kira"
            pass
        'El conocimiento y el poder':
            $ tendencia = "Death Note"
            pass   

    "Excelente. Tu historia está por comenzar, [nombre]. Recordá: cada decisión tiene consecuencias."

    jump escena_01_01           

label escena_01_01:
    scene mundo_shinigami

    'En el Reino Shinigami, los dioses de la muerte se aburren. Juegan, apuestan, observan cómo sus relojes de vida se acortan sin interés verdadero.'
    'Pero uno de ellos, Ryuk, parece más inquieto que los demás..."'
    show ryuk_perfil at quieto_izquierda
    ryuk 'Qué mundo tan podrido... incluso aquí arriba. Tal vez un poco de caos lo haría más entretenido'
    'Ryuk observa un cuaderno con letras goticas: "DEATH NOTE"'
    ryuk 'Veamos qué pasa si lo dejo caer... en el mundo humano'
    "Y así, sin saberlo, Ryuk acababa de cambiar el destino del mundo..."
    jump escena_01_02


label escena_01_02:
    scene kanto_1
    "Mientras tanto, en Kanto, tu vida estaba por cambiar también... aunque por razones completamente diferentes."
    "Hoy es tu primer día en la Secundaria Daikoku. Tu familia se mudó aquí hace apenas una semana. Tu padre consiguió un trabajo importante en la policía de Kanto, aunque nunca te cuenta mucho sobre lo que hace."
    scene puerta_escuela
    protagonista "Nueva ciudad, nueva escuela, nuevos compañeros... ¿Por qué siempre me pasa esto?"
    "¡Ey! ¿Estás perdido?"
    show yuri_i at mover_personaje_derecha
    "Ah, sos nuevo, ¿verdad? Soy Yuri. ¿Cuál es tu aula?"
    protagonista "Clase 3-A..."
    yuri "¡Perfecto! Yo también. Vení, te muestro. Tenemos suerte, está el mejor estudiante de todo Japón en nuestra clase."
    protagonista  "¿El mejor estudiante?"
    yuri "Sí, Light Yagami. Es un genio. Aunque... algunos lo encuentran un poco intimidante."
    hide yuri
    jump escena_01_03


label escena_01_03:
    scene escuela
    "Tu primera clase es Inglés. El profesor te presenta frente a todos."
    profesor "Clase, tenemos un nuevo estudiante. Por favor, presentate."
    protagonista "Hola, soy [nombre]. Me mudé desde [ciudad]. Espero que podamos llevarnos bien." 
    profesor "Excelente. Podés sentarte en el asiento vacío junto a Yagami."
    show light_perfil at quieto_derecha
    "Light Yagami. El chico del que Yuri te habló. Tiene un aire de... superioridad. Pero también hay algo más. Algo en su mirada..."
    show light_perfil at mover_personaje_derecha
    light "Buenos dias"
    protagonista "Hola. Así que sos Light Yagami."
    light "(con leve sonrisa) Mi reputación me precede, al parecer. No le hagas caso. La gente exagera."
    profesor "Bien, continuemos. Yagami, traducí esta frase al japonés: 'In the end, all that matters is what we leave behind.'"
    light "'Al final, lo único que importa es lo que dejamos atrás.'"
    profesor  "Perfecto, como siempre."
    "Durante la clase, observás a Light. No toma apuntes. No presta atención. Y sin embargo, cuando el profesor le pregunta, siempre tiene la respuesta correcta."
    "Pero hay algo más que llamó tu atención..."
    'La pantalla de TV al fondo del aula muestra noticias silenciadas: "CRIMINAL PELIGROSO ENCONTRADO MUERTO - ATAQUE CARDÍACO"'
    "Light mira esas noticias con una intensidad particular. Como si supiera algo que los demás no saben."
    hide light_perfil
    jump escena_01_04

label escena_01_04:
    scene terrasa_colegio
    "Durante el almuerzo, decidiste explorar la escuela. La azotea está sorprendentemente vacía... excepto por una persona."
    protagonista  "Light... ¿Por qué alguien como él come solo?"

    menu:
        'Acercarte y hablar con él':
            jump escena_01_04_A
        'Observarlo desde lejos y luego irte':
            jump escena_01_04_B
        'Irte inmediatamente':
            jump escena_01_05

label escena_01_04_A:
    scene terrasa_colegio
    show light_perfil at mover_personaje_derecha
    protagonista "¿Puedo sentarme acá?"
    light '(cerrando el libro): "Claro. No hay muchos que vengan a la azotea.'
    protagonista "¿Por qué venís solo acá?"
    light "Digamos que prefiero la tranquilidad. La cafetería está llena de... ruido innecesario."
    protagonista  "¿Ruido innecesario? ¿Te referís a la gente?"
    light "(sonriendo levemente): No me malinterpretes. No es que no me guste la gente. Es solo que la mayoría de las conversaciones en la cafetería son... triviales. '¿Viste el último episodio?', '¿Quién te gusta?', '¿Qué vas a hacer el fin de semana?' Nada de sustancia."
    protagonista "Entonces, ¿qué tipo de conversación tiene sustancia para vos?"
    light  '(mirándote con interés renovado) Esa es una buena pregunta. Dime, [nombre], ¿viste las noticias esta mañana?'
    protagonista "¿Las noticias?"
    light  "Otro criminal murió anoche. Ataque cardíaco. Van como 50 en las últimas semanas. Todos criminales. Todos ataques cardíacos."
    protagonista "¿Y eso qué tiene de especial? La gente muere todo el tiempo."
    light '(inclinándose hacia adelante): Eso es lo que la mayoría piensa. Pero cuando es un patrón tan claro... ¿no te parece sospechoso? Es como si alguien estuviera... seleccionando criminales y eliminándolos.'
    menu:
        "Si alguien está matando criminales, no es tan malo. El mundo está podrido.":
            light "Exacto. El sistema judicial es lento, corrupto, imperfecto. Los criminales entran y salen de prisión. Víctimas que nunca obtienen justicia. Si alguien pudiera... corregir eso... ¿no estaría haciendo un bien al mundo?"
            protagonista "Es una idea peligrosa, Light."
            light "Las ideas peligrosas son las que cambian el mundo, [nombre]. La historia lo demuestra."
            'Suena la campana'
            light "Ha sido una conversación interesante. La mayoría de la gente me mira raro cuando hablo de estas cosas. Espero que podamos seguir charlando."
            protagonista "Sí... yo también."
            "Mientras bajás de la azotea, no podés dejar de pensar en las palabras de Light. Hay algo en él... algo que te inquieta y te fascina al mismo tiempo."
            jump escena_01_05
        "Matar es matar, sin importar quién sea la víctima. Es moralmente incorrecto.":
            'Light se queda pensando en lo que dijiste, suena la campana y Light se retira gentilmente'
            jump escena_01_05
        "Me pregunto cómo lo hace. Debe tener algún método especial.":
            'Light te mira con curiosidad, suena la campana y Light se retira gentilmente'
            jump escena_01_05



label escena_01_04_B:
    scene terrasa_colegio
    show light_frente
    'Parece que Light esta muy concentrado leyendo un libro de tapa de cuero negro. Este lleva el titulo de "DEATH NOTE" en su portada'
    'Suena la campana del recreo, te apuras a irte antes que Light te vea'
    jump escena_01_05



label escena_01_05:
    scene kanto_1
    "Caminás a casa pensando en tu primer día. Nueva escuela, nuevos compañeros... y Light Yagami, un chico brillante con ideas peligrosas."
    mensaje "Llegaré tarde esta noche. Caso importante. Hay comida en la heladera. - Papá"
    protagonista "Siempre llega tarde últimamente... ¿Qué estará investigando?"
    'Mientras caminás, notás una conmoción adelante'
    transeunte_1 "¡Llamá a la policía!"
    transeunte_2 "¡Otro ataque cardíaco! ¡Es el tercero hoy!"
    'Te acercas hacia la escena'
    protagonista "¿Qué pasó?"
    transeunte_1 "Un delincuente conocido... cayó muerto aquí mismo. Los paramédicos dicen que fue un ataque cardíaco."
    "Un escalofrío recorre tu espalda. Es como si alguien estuviera seleccionando criminales y eliminándolos."
    jump escena_01_06

label escena_01_06:
    scene black
    "Lo que no sabías en ese momento... lo que nadie sabía... era que ese mismo día, algo extraordinario había sucedido."
    scene puerta_escuela
    'Un libro negro va cayendo lentamente desde el cielo'
    show light_pensando at  mover_personaje_derecha
    light "'El humano cuyo nombre sea escrito en este cuaderno morirá...' Ridículo."
    hide light_pensando
    scene black
    "Pero esa noche, Light Yagami probó el cuaderno. Y funcionó."
    scene light_pieza
    show light_sorpendido at mover_personaje_derecha
    light "No puede ser... ¡realmente funciona!"
    "Y en ese momento, Light Yagami tomó una decisión que cambiaría el mundo para siempre."
    hide light_sorpendido
    show light_perfil at mover_personaje_derecha
    light "Voy a crear un nuevo mundo. Un mundo sin criminales. Un mundo perfecto."
    'Pero no estaba solo en esto...'
    show ryuk_frente at mover_personaje_izquierda
    ryuk "Te estabas divirtiendo sin mí, ¿eh?"
    hide ryuk_frente
    hide light_perfil
    scene black
    "Pero vos no sabías nada de esto. Aún no. Tu historia con Light Yagami apenas comenzaba..."
    jump escena_01_07

label escena_01_07:
    scene comedor
    "Esa noche, las noticias están llenas de reportes sobre las misteriosas muertes."
    noticiero  "...54 criminales muertos en las últimas dos semanas, todos por ataques cardíacos. La policía no tiene explicación. En internet, algunos lo llaman 'Kira'..."
    protagonista "Kira... ¿Quién sos?"
    'Tu padre llega a casa, se ve cansado'
    show padre_normal at mover_personaje_derecha
    padre "Aún despierto, hijo"
    protagonista "Papá, ¿es verdad? ¿Todos esos criminales muriendo?"
    'Tu padre suspira y toma asiento'
    hide padre_normal
    show padre_serio at mover_personaje_derecha
    padre "Sí. Es real. Y es... preocupante."
    protagonista "¿Preocupante? Pero si son criminales..."
    padre "Escuchame bien, [nombre]. No importa quiénes sean las víctimas. Si alguien está matando gente, es un asesino. Y mi trabajo es atraparlo."
    protagonista "¿Vos estás trabajando en ese caso?"
    padre  "No puedo hablar de eso. Pero... sí. Por eso voy a estar muy ocupado. Quiero que tengas cuidado, ¿ok?"
    protagonista "¿Cuidado de qué?"
    padre "De involucrarte en cosas peligrosas. Y... de la gente que conocés. No todos son lo que parecen."
    "Sus palabras te siguen mientras te vas a dormir. 'No todos son lo que parecen...' ¿A quién se refería?"
    jump escena_01_08

label escena_01_08:
    scene pieza
    "Acostado en tu cama, no podés dejar de pensar en todo lo que pasó hoy. Light y sus ideas sobre justicia. Los criminales muriendo. Tu padre preocupado. Y ese nombre: Kira."
    "Algo grande está pasando. Podés sentirlo. Y por alguna razón, sentís que estás destinado a ser parte de esto."

    '¿Qué pensás realmente sobre Kira?'
    menu:
        "Si Kira está limpiando el mundo de criminales... quizás no sea tan malo.":
            pass
        "Kira es un asesino. Debe ser detenido, sin importar sus motivos.":
            pass
        "Me pregunto qué poder tiene Kira... y si podría obtenerlo.":
            pass
    "Tu decisión quedará grabada en tu corazón. Y pronto, muy pronto, tendrás que actuar según esa convicción."
    scene black


label escena_02_01:
    scene terrasa_colegio
    'Una semana ha pasado desde tu primer día. Te has adaptado bien a la escuela. Hiciste algunos amigos. Y Light... bueno, Light sigue siendo un enigma.'
    estudiante_1 "¿Vieron las noticias? ¡Kira mató a 20 criminales ayer!"
    estudiante_2 "Dicen que puede matarlos con solo verlos. ¡Es como un dios!"
    show yuri_i at mover_personaje_derecha
    yuri "No sean idiotas. Kira es un asesino serial. Mi papá dice que la policía está desesperada por atraparlo."
    estudiante_1 "¿Asesino? ¡Está haciendo lo que la policía no puede! El mundo está mejor sin esos criminales."
    show yuri_i at mover_personaje_derecha
    yuri "¿Y quién decide quién merece morir? ¿Kira? ¡Nadie tiene ese derecho!"
    'La discusión se intensifica. Notás que Light está en una mesa cercana, escuchando todo con atención'
    protagonista '(pensando) Light parece muy interesado en esta conversación...'
    menu:
        'Unirte a la discusión defendiendo a Kira':
            protagonista 'Considero que kira es un heroe. piensenlo, hace lo que a todos si tuvieramos su poder lo hariamos. El mundo debe de ser mejorado'
            'Suena la campana'
            'Todos se dirigen hacia el aula'
            $ alineacion_kira += 1
            jump escena_02_02
        'Unirte a la discusión criticando a Kira':
            protagonista 'Considero que kira es un criminal. No se diferencia mucho de otros asesinos o genocidas que han habido en la historia de la humanidad'
            'Suena la campana'
            'Todos se dirigen hacia el aula'
            $ alianza_l += 1
            jump escena_02_02
        'Acercarte a Light y preguntarle qué piensa':
            hide yuri_i
            show light_perfil at quieto_derecha
            protagonista "Parece que Kira es el tema del momento."
            show light_perfil at mover_personaje_derecha
            light '(Te sonrie) Siempre lo es últimamente. Es fascinante cómo divide a la gente. Algunos lo ven como un héroe, otros como un villano.'
            protagonista "¿Y vos qué pensás?"
            show light_perfil at mover_personaje_derecha
            light "Yo creo... que Kira representa algo importante. Un deseo humano fundamental: el deseo de justicia. Verdadera justicia, no la versión burocrática y lenta que tenemos ahora."
            protagonista "Pero Kira mata gente."
            show light_perfil at mover_personaje_derecha
            light "Mata criminales. Personas que ya hicieron daño. Violadores, asesinos, corruptos. ¿No es eso diferente que matar inocentes?"
            protagonista "Supongo que sí... pero..."
            show light_perfil at mover_personaje_derecha
            light "Pensá en esto: si tuvieras el poder de eliminar el mal del mundo, ¿no lo usarías? Si pudieras salvar miles de vidas eliminando a cientos de criminales, ¿no sería tu deber hacerlo?"
            "Hay algo perturbador en la intensidad con la que Light habla de esto. Como si no fuera una hipótesis... como si fuera personal."
            protagonista "Es una pregunta difícil."
            show light_perfil at mover_personaje_derecha
            light "Las preguntas más importantes siempre lo son. Pero eventualmente, todos tenemos que elegir un lado, [nombre]. La neutralidad es solo otra forma de complicidad."
            'Suena la campana'
            show light_perfil at mover_personaje_derecha
            light "Pensá en lo que dije. Nos vemos en clase."
            $ confianza_light += 1
            jump escena_02_02
        'No haceer nada y observar la discusion':
            'Pierdes el interes en la conversacion y te dedicas a comer tu comida'
            'Suena la campana'
            'Todos se dirigen hacia el aula'
            jump escena_02_02



label escena_02_02:
    scene escuela
    "Durante la clase de Historia, el profesor enciende la TV para mostrar un documental. Pero en su lugar, aparece una transmisión especial."
    profesor "¿Qué es esto?"
    'En la pantalla aparece un hombre en traje, sentado en una habitación oscura'
    locutor 'Transmisión especial internacional. El siguiente mensaje es para Kira.'
    show light_estresado at quieto_derecha
    'Light se tensa visiblemente. Vos lo notás'
    hide light_estresado
    L "Tus acciones no son justicia. Son el trabajo de un asesino serial con delirios de grandeza. Y te prometo esto: te voy a encontrar. Te voy a atrapar. Y te voy a hacer pagar por cada vida que tomaste."
    "Podés sentir la tensión en el aire. Todos están conteniendo la respiración."
    L "De hecho, para probarte que puedo rastrearte, te digo esto: actualmente estoy transmitiendo solo en la región de Kanto. Si realmente podés matarme, Kira, hacelo ahora."
    'Estudiantes' '¡¡¿¿QUÉ??!!'
    profesor "Dios mío..."
    'Mirás a Light. Hay algo extraño en su expresión. ¿Sorpresa? ¿Ira? ¿Triunfo?'
    'La pantalla cambia a una gran letra "L" blanca sobre fondo negro'
    scene l_anuncio
    'Voz distorcionada' "Interesante, Kira. Pero ese no era yo. Era un prisionero condenado a muerte. Ahora sé tres cosas: Podés matar sin estar presente físicamente. Estás en la región de Kanto de Japón. Y sos infantil, porque no pudiste resistir la tentación de matarlo."
    'Voz distorcionada' "Soy el verdadero L. Y ahora que sé dónde estás... la cacería comienza. Nos vemos pronto, Kira."
    'La transmisión termina'
    scene escuela
    "El aula explota en conversaciones. Pero vos solo podés observar a Light, quien aprieta su puño con tanta fuerza que sus nudillos se ponen blancos."
    jump escena_02_03

label escena_02_03:
    scene puerta_escuela
    'Alcanzás a Light en la salida del colegio, ya todos se han ido'
    protagonista "Light, esperá."
    show light_perfil at mover_personaje_derecha
    light "(deteniéndose, su rostro es una máscara de calma) ¿Sí?"
    protagonista "Esa transmisión... te afectó."
    show light_perfil at mover_personaje_derecha
    light "¿Afectarme? Solo fue interesante ver a Kira caer en una trampa tan obvia."
    protagonista "No estabas molesto por la trampa. Estabas molesto porque funcionó."
    show light_frente at mover_personaje_derecha
    light  "(se volte y te mira fijamente) ¿Qué estás insinuando, [nombre]?"
    menu:
        "Nada. Solo que parecés muy involucrado en esto.":
            show light_perfil at mover_personaje_derecha
            light 'Puede ser, las acciones de Kira ponen a prueba la moral de todos, incluso la mia. En lo personal creo que Kira esta haciendo un trabajo necesario pero no puedo negar que va en contra de la ley'
            'Light se va, sientes que no te ha dicho su opinion completa'
            $ confianza_light += 1
        "Estás de su lado, ¿verdad? Del lado de Kira.":
            show light_perfil at mover_personaje_derecha
            light "(relajándose levemente) Digamos que entiendo su perspectiva. L habla de justicia, pero ¿qué clase de justicia? ¿La que permite que criminales salgan libres por tecnicismos? ¿La que demora años mientras las víctimas sufren?"
            protagonista "Pero usar a un prisionero como carnada..."
            show light_perfil at mover_personaje_derecha
            light "Fue inteligente. L es inteligente. Kira subestimó a su oponente. Pero esto está lejos de terminar."
            protagonista "Hablás como si conocieras personalmente a Kira."
            show light_perfil at mover_personaje_derecha
            light "(Sonriendo levemente) Digamos que entiendo cómo piensa. Alguien con ese poder, con esa visión... no se va a rendir solo porque un detective anónimo le puso una trampa. Si acaso, esto lo hará más cuidadoso. Más peligroso."
            protagonista "¿Más peligroso para quién? ¿Para los criminales o para todos?"
            show light_perfil at mover_personaje_derecha
            light "Esa es la pregunta del millón, ¿no? Pero te diré algo, [nombre]: cuando todo termine, cuando el polvo se asiente, el mundo será un lugar mejor. De eso podés estar seguro."
            $ confianza_light += 1
            $ alineacion_kira += 2
            'Light se va, dejándote con más preguntas que respuestas'
        "Kira deberia tener cuidado. L parece que sabe lo que hace.":
            show light_frente at mover_personaje_derecha
            'Light se queda pensando por unos segundo'
            light 'Si Kira deberia pensar mas las cosas...'
            'Light se va, sientes que esta charla ha sido incomoda'
            $ confianza_light -= 1
            $ alianza_l += 1

label escena_02_04:
    scene comedor
    show padre_molesto at quieto_derecha
    'Estás cenando con tu padre, quien se ve más estresado que nunca'
    protagonista "Papá, ¿viste la transmisión hoy?"
    show  padre_normal at mover_personaje_derecha
    padre "Sí. Todos en la oficina la vieron. Fue... impactante."
    protagonista "¿Quién es L?"
    show padre_serio at mover_personaje_derecha
    padre "(eligiendo sus palabras cuidadosamente) Es el mejor detective del mundo. Ha resuelto casos que parecían imposibles. Pero nadie sabe su verdadera identidad."
    protagonista "¿Ni siquiera la policía?"
    padre "Ni siquiera nosotros. Solo su asistente, Watari, puede contactarlo. Es... frustrante, para ser honesto. Pero si alguien puede atrapar a Kira, es L"
    protagonista "¿Vos querés que atrapen a Kira?"
    padre "Por supuesto. Kira es un asesino, sin importar cómo lo justifique la gente."
    protagonista "Pero... mató a ese hombre en la transmisión. Eso prueba que puede matar a cualquiera, ¿no? ¿No te preocupa estar investigándolo?"
    padre "(tocando tu mano) Me preocupa. Claro que me preocupa. Pero es mi trabajo. Alguien tiene que hacerlo."
    "Hay algo que tu padre no te está diciendo. Podés verlo en sus ojos. Está más involucrado en esto de lo que admite."
    padre "[nombre], quiero que me prometas algo."
    protagonista "¿Qué cosa?"
    padre "Si algo me pasara... si Kira viniera tras de mí... prométeme que no tratarás de vengarte. Prométeme que seguirás con tu vida."
    protagonista  "Papá, no digas esas cosas..."
    padre "Prométemelo."
    menu:
        "Te lo prometo, papá.":
            pass
        "No puedo prometerte eso.":
            pass
        "Nada te va a pasar.":
            pass
    jump escena_02_05

label escena_02_05:
    scene black
    "Mientras vos cenabas con tu padre, Light estaba en su habitación, planificando su próximo movimiento."
    scene light_pieza
    show ryuk_perfil at mover_personaje_derecha
    show light_estresado at mover_personaje_izquierda
    ryuk "Admitilo, Light. L te ganó esta ronda."
    light "Fue un golpe de suerte. Usó a un prisionero como carnada. Era impredecible."
    ryuk "¿Impredecible? Vos sos el que no pudo resistir matarlo. Te provocó y caíste."
    light "Ahora sé que L es real. Que está en Japón. Que me está buscando activamente. Eso no es una desventaja, Ryuk. Es información."
    ryuk "¿Y qué vas a hacer con esa información?"
    light "(sonriendo fríamente) Voy a encontrarlo. Voy a descubrir su verdadero nombre. Y lo voy a eliminar. Pero tengo que ser más cuidadoso. Más calculador. L es inteligente, pero yo también lo soy."
    'Ligth abre la Death Note'
    light "Voy a crear un mundo nuevo. Un mundo sin criminales. Un mundo donde yo sea dios. Y ni L ni nadie más me lo va a impedir."
    ryuk "Humano arrogante. Esto va a ser muy divertido de ver."
    hide ryuk_perfil
    hide light_estresado
    scene black
    jump escena_02_06

label escena_02_06:
    scene terrasa_colegio
    'Vas a la azotea a comer. Light ya está ahí'
    show light_frente at mover_personaje_derecha
    light "Te estaba esperando."
    protagonista "¿Me estabas esperando?"
    light "Sí. Quería disculparme si ayer fui... intenso. La transmisión de L me afectó más de lo que debería."
    protagonista "¿Por qué te afecta tanto?"
    light "Porque representa algo importante. Esta batalla entre Kira y L... no es solo sobre atrapar a un criminal. Es sobre dos filosofías opuestas de justicia. Y creo que todos tenemos que elegir un lado."
    protagonista "¿Y vos ya elegiste?"
    light "Sí. ¿Y vos?"
    menu:
        "Yo también creo en lo que Kira está haciendo.":
            light "(sonriendo genuinamente por primera vez) Me alegra escuchar eso. La mayoría tiene miedo de admitirlo públicamente, pero en el fondo, muchos piensan lo mismo. El mundo necesita un cambio radical. Kira lo está haciendo posible."
            protagonista "¿Pero no te preocupa que Kira tenga tanto poder?"
            light "El poder en sí no es malo. Todo depende de quién lo tenga y cómo lo use. Si Kira realmente está eliminando solo criminales, entonces está usando su poder correctamente."
            protagonista "¿Y si comete un error? ¿Si mata a un inocente?"
            light "Hasta ahora, no lo ha hecho. Cada persona que Kira ha eliminado era objetivamente culpable. Eso requiere investigación, inteligencia, disciplina. Kira no es un loco aleatorio. Es alguien con un plan, con una visión."
            "Hablás con Light durante todo el almuerzo. Se abre más contigo que con cualquier otra persona. Y mientras más habla, más te das cuenta de algo: Light no está simplemente defendiendo a Kira. Habla con la convicción de alguien que conoce a Kira íntimamente. Quizás demasiado íntimamente."
            $ alineacion_kira += 3
            $ confianza_light += 2
            pass
        "Creo en L. Kira debe ser detenido.":
            $ confianza_light -= 1
            $ alianza_l += 1
            'A Light parece incomodarle tu respuesta. Se levanta del asiento y se despide respetuosamente. Parece que tu relacion con el se ha complicado'
            pass
        "Todavía no estoy seguro.":
            'Ligth no dice nada pero te observa paraciendo entender tu indecision. Pasan el resto del almuerzo juntos hablando sobre temas mas triviales'
            pass
        "Me pregunto como Kira habra obtenido sus poderes.":
            'Ligth muestra geninua sorpresa con tu respuesta, no le desagrada pero tampoco es la que esperaba. Pasan el resto del almuerzo juntos hablando sobre temas mas triviales'
            $ codicia_dn += 2
            pass
    jump escena_02_07

label escena_02_07:
    scene pieza
    "Esa noche, no podés dormir. Entrás a internet y buscás información sobre Kira. Lo que encontrás te sorprende."
    "Hay miles de páginas dedicadas a Kira. Algunos lo llaman dios. Otros, demonio. Pero todos están de acuerdo en una cosa: el crimen ha disminuido dramáticamente en las áreas donde Kira ha actuado."
    "Algunas estadisticas salen en la pantalla:
    - Crimen violento: -70%% en Japón
    - Robos: -60%% globalmente
    - Asesinatos: -75%% en ciudades principales"
    "Los números no mienten. Kira está teniendo un efecto real. La gente tiene miedo de cometer crímenes. Y para muchos, eso es suficiente para justificar todo."
    'Un video blog aparece en pantalla'
    'Vlogger' "Kira nos está protegiendo. Por primera vez en mi vida, me siento segura caminando de noche. ¡Gracias, Kira!"
    'Comentarios llenan la pantalla: "Kira es justicia", "Que muera L", "El nuevo mundo está llegando"'
    protagonista "Light tiene razón. Kira está cambiando el mundo. Pero... ¿a qué costo?"
    "Cerrás la computadora y te acostás, pero el sueño no llega fácilmente. Tu mente está llena de preguntas. ¿Quién es Kira? ¿Qué es L? Y lo más importante... ¿de qué lado estás realmente?"
    scene black
    "Dos fuerzas se enfrentan. Kira, el ejecutor invisible que promete un mundo sin crimen. L, el detective fantasma que jura traer justicia verdadera. Y vos... estás en medio de ambos."
    menu:
        "Apoyo a Kira. El mundo necesita cambiar, sin importar el costo.":
            $ alineacion_kira += 3
            pass
        "Apoyo a L. Nadie tiene derecho a ser juez, jurado y verdugo.":
            $ alianza_l += 3
            pass
        "No apoyo a ninguno. Solo quiero entender este poder.":
            $ codicia_dn += 3
            pass
        "Necesito ver más antes de decidir.":
            pass
    "Tu elección resonará en todo lo que viene. El juego entre Kira y L apenas comienza. Y pronto, muy pronto, serás más que un observador. Serás un jugador."
    jump escena_03_01
    
label escena_03_01:
    scene escuela
    "Dos semanas han pasado desde la transmisión de L. El mundo ha cambiado. Kira sigue actuando, pero ahora con más cuidado. Y vos... vos has estado observando a Light más de cerca."
    show yuri_i at mover_personaje_derecha
    yuri "Oye, [nombre], ¿venís al karaoke con nosotros este sábado?"
    protagonista  "Mmm, no sé..."
    yuri "¡Vamos! Le preguntamos también a Light. Sería bueno que socialice más."
    'Mirás a Light, quien está guardando sus cosas'
    protagonista "¿Light va a ir?"
    yuri "Le voy a preguntar. Aunque últimamente está muy ocupado. ¿Con qué? Ni idea."
    hide yuri_i
    "Es verdad. Light ha estado cada vez más distante. Desaparece durante el almuerzo. Llega tarde a clases. Y cuando le preguntás qué está haciendo, siempre tiene excusas vagas."
    scene puerta_escuela
    'Alcanzás a Light antes de que se vaya'
    show light_frente at quieto_derecha
    protagonista "Light, ¿podemos hablar?"
    light "Claro. ¿Qué pasa?"
    protagonista "Has estado... diferente últimamente. Más distante."
    light "¿Distante? Solo he estado ocupado con estudios y cosas familiares."
    protagonista "¿Tiene que ver con Kira?"
    light "¿Por qué todo tiene que ver con Kira?"
    protagonista "Porque desde que L apareció, estás obsesionado con el tema. Y no sos el único. Las noticias dicen que Kira ha matado a más de 100 criminales solo esta semana."
    light "Lo que significa que el mundo es cada vez más seguro."
    protagonista "O que Kira está perdiendo el control."
    light "(mirándote fijamente) ¿Perdiendo el control? Kira es más calculador que nunca. Cada movimiento es preciso. Cada muerte tiene propósito."
    protagonista "Hablás como si lo conocieras personalmente."
    if confianza_light > 5:
        light "[nombre], ¿puedo confiar en vos?"
        menu:
            "Sí, podés confiar en mí completamente.":
                light "(mirando alrededor, asegurándose de que estén solos) Hay cosas que no podés saber todavía. Pero quiero que sepas... que todo lo que está pasando, todo lo que va a pasar, es necesario. El mundo está cambiando. Y cuando todo termine, vas a entender por qué."
                protagonista "Light, me estás asustando."
                'Light te lleva suavemente hasta una parte donde nadie pueda verlos, casi que parece que te estuviera acorralando'
                light "No tengas miedo. Si estás de mi lado, si realmente creés en un mundo mejor, entonces no tenés nada que temer."
                protagonista "¿De tu lado? Light, ¿qué...?"
                'El celular de Light suena'
                light "Tengo que irme. Hablamos después."
                'Light se va rápidamente, dejándote con más preguntas'
                $ confianza_light += 1
                pass
            "Depende de qué me digas.":
                light "Depende de lo que quieras escuchar, Si quieres estar en el lado de kira hay cosas que aun debes de comprender."
                'Light se va rápidamente, dejándote con más preguntas'
                $ confianza_light += 1
                pass
            "¿Por qué? ¿Qué me vas a decir?":
                'Hay algunas cosas de la cuales creo que deberias de....'
                'El celular de Light suena'
                light "Tengo que irme. Hablamos después."
                'Light se va rápidamente, dejándote con más preguntas'
                pass
    else:
        ligth "No creo que lo entiendas"
        'Light se va rápidamente, dejándote con más preguntas'
        pass
    jump escena_03_02

label escena_03_02:
    #AGREGAR FONDO DE PARADA DE COLECTIVO
    scene black
    "Es sábado. Decidiste ir al karaoke después de todo. Casualmente, tomás el mismo autobús que Light y algunos compañeros."
    'Suben al colectivo y stás sentado unas filas detrás de Light'
    #AGREGAR FONDO DE COLECTIVO
    "El viaje es normal hasta que un hombre sube en una parada. Algo en él te pone nervioso."
    protagonista "(Pensando) Ese tipo... parece peligroso."
    'Hombre' "¡NADIE SE MUEVA! ¡CONDUCTOR, SEGUÍ CONDUCIENDO!"
    "Tu corazón late rápidamente. Es un secuestro. Pero entonces notás algo extraño: Light está completamente calmado. Demasiado calmado."
    'Light susurra algo a un amigo y deja caer un papel'
    protagonista "(Pensando) ¿Qué está haciendo?"
    'Hombre en traje' "Soy agente del FBI. Suelte el arma ahora."
    'Secuetrador' "¡¿FBI?! ¡Atrás o disparo!"
    'En el caos, el secuestrador toma el papel que Light había pasado. Sus ojos se abren enormes, como si viera algo aterrador'
    'Secuestrador' "¡¿QUÉ ES ESO?! ¡¿QUÉ DEMONIOS ES ESO?!"
    'El secuestrador grita incoherentemente y obliga al conductor a detenerse. Corre hacia la puerta'
    'Una camioneta aparece de la nada y atropella al secuestrador, matándolo instantáneamente'
    'Mirás a Light. Por un momento, jurás que ves una pequeña sonrisa en sus labios antes de que se convierta en una expresión de shock'
    jump escena_03_03

label escena_03_03:
    #AGREGAR FONDO DE CALLE
    'La policía está interrogando a los pasajeros. Te acercás a Light'
    protagonista "(en voz baja) Light, ¿qué pasó ahí adentro?"
    light  "Fue horrible. Ese hombre estaba claramente drogado o algo. Gracias a Dios que el agente del FBI estaba ahí."
    protagonista "El papel que dejaste caer..."
    light  "¿Qué con eso?"
    protagonista  "El secuestrador lo vio. Y actuó como si hubiera visto algo aterrador."
    light "Era solo una nota diciendo que había alguien armado detrás. Lo asustó, supongo."
    protagonista "Light..."
    'Un hombre se acerca: el agente del FBI'
    'Agente del FBI' "Disculpe, joven. ¿Puedo hacerle algunas preguntas?"
    light "Por supuesto, oficial."
    "Observás la interacción. El agente hace preguntas rutinarias. Light responde con calma perfecta. No hay nada aparentemente sospechoso. Y sin embargo... algo no cuadra."
    "Cuando el agente se va, notás su tarjeta de identificación: Raye Penber, FBI."
    jump escena_03_04

label escena_03_04:
    scene pieza
    "Esa noche, no podés dejar de pensar en lo que pasó. Algo sobre toda la situación te molesta. Decidís investigar."
    'Abrís tu computadora y buscás información sobre el secuestrador'
    "Kiichiro Osoreda - Buscado por robo a mano armada y asesinato. Muerto en accidente de tráfico tras intento de secuestro de autobús."
    protagonista  "Un criminal buscado... muere justo después de ver ese papel. ¿Coincidencia?"
    'Buscás más información. Encontrás un patrón'
    '"Últimas víctimas de Kira:
    - Todos criminales conocidos
    - Algunos murieron en circunstancias inusuales, no solo ataques cardíacos
    - Accidentes, suicidios, otros métodos"
    '
    protagonista "Kira puede controlar cómo mueren... Y Light estaba ahí. Light le dio ese papel al secuestrador, indirectamente."
    "Una idea aterradora se forma en tu mente. Una idea que no querés creer, pero que cada vez tiene más sentido."
    protagonista "No... no puede ser. Light no puede ser Kira. Es mi amigo. Es..."
    'Tu celular vibra. Mensaje de Light'
    light "¿Estás bien después de lo de hoy? Sé que fue traumático. Si necesitás hablar, avisame."
    menu:
        'Responder normalmente, actuar como si no sospecharas nada':
            $ confianza_light += 1
            pass
        'Confrontarlo directamente: "¿Qué había en ese papel?"':
            $ confianza_light -= 2
            $ codicia_dn += 2
            pass
        'Ignorar el mensaje y seguir investigando solo':
            $ alianza_l += 1
            pass
        "Estoy bien. Pero tengo que preguntarte algo importante mañana.":
            pass
    jump escena_03_05

label escena_03_05:
    scene comedor
    show padre_serio at mover_personaje_derecha
    padre "Perdón por llegar tarde otra vez, hijo/a."
    protagonista "Papá, ¿podés contarme en qué estás trabajando? De verdad."
    padre "Ya te dije que no puedo..."
    protagonista "Tiene que ver con Kira, ¿verdad? Y con el FBI."
    padre '¿Cómo sabés sobre el FBI?'
    protagonista  "Había un agente en el autobús que casi secuestran. Raye Penber."
    padre "¿Estabas en ese autobús? ¡¿Por qué no me lo dijiste?!"
    protagonista "Papá, ¿qué está pasando realmente?"
    padre "Está bien. Creo que merecés saber algo. Pero lo que te diga no puede salir de esta casa. ¿Entendés?"
    protagonista "Entiendo."
    padre  "Estoy trabajando con un grupo especial de investigación de Kira. L nos está ayudando, aunque solo nos contacta a través de su asistente. Y sí, pedimos ayuda al FBI para seguir a sospechosos potenciales."
    protagonista "¿Sospechosos? ¿Como quién?"
    padre "No puedo darte nombres. Pero L tiene una lista de personas que encajan con el perfil de Kira. Jóvenes, inteligentes, con acceso a información policial..."
    protagonista  "¿Light Yagami está en esa lista?"
    padre "¿Cómo...? ¿Lo conocés?"
    protagonista "Es mi compañero de clase. Es... mi amigo."
    padre "Entonces necesitás alejarte de él. Ahora."
    protagonista"¿Por qué? ¿Creés que él es Kira?"
    padre "No lo sé. Pero L lo considera uno de los principales sospechosos. El hijo del jefe Yagami... es una situación complicada."
    "Tu mente está corriendo. Light, Kira, el FBI siguiéndolo... todo empieza a conectarse de maneras aterradoras."
    protagonista "Papá, ¿y si pudiera ayudar?"
    padre "¿Ayudar? No, absolutamente no. Esto es demasiado peligroso."
    protagonista  "Pero estoy cerca de Light. Puedo observarlo sin que sospeche. Sería útil para L, ¿no?"
    padre "No voy a usar a mi hijo/a como cebo para Kira."
    protagonista  "No sería cebo. Sería... un observador. Y si Light NO es Kira, entonces no hay peligro y probaria que mi amigo no es un asesino."
    padre "Dejame... hablar con L. Pero no prometo nada. Y mientras tanto, tenés que prometerme que no vas a hacer nada imprudente."
    protagonista 'Te lo prometo'

label escena_03_06:
    scene subte
    "El fin de semana siguiente, estás en el centro comercial. Y por casualidad, o quizás no, te encontrás con Light."
    show light_perfil at mover_personaje_derecha
    light "[nombre]! Qué sorpresa."
    protagonista "Light. ¿Qué hacés acá?"
    light "Solo estaba paseando. ¿Y vos?"
    show light_estresado at quieto_derecha
    "Hay algo diferente en él. Está más tenso. Sus ojos constantemente miran alrededor, como si buscara a alguien."
    protagonista "¿Estás bien? Te ves nervioso."
    light "¿Nervioso? Para nada. Solo... pensando en cosas."
    protagonista "¿Cosas de Kira?"
    light "(Rie levemente) Siempre volvemos a Kira, ¿no? Es como si fuera lo único de lo que podemos hablar."
    protagonista "Es lo único importante que está pasando."
    light "Cierto. Y hablando de eso... ¿escuchaste las últimas noticias"
    protagonista "¿Qué noticias?"
    light "Doce agentes del FBI murieron ayer. Todos ataques cardíacos. Todos estaban investigando a Kira."
    "Sentís un frío recorrer tu espalda."
    protagonista "¿Doce agentes? ¿Cómo es posible?"
    light "Kira los mató. Obviamente. Lo que significa que Kira sabe que el FBI lo está investigando. Y sabe quiénes son los agentes."
    protagonista "¿Cómo podría saber eso?"
    light "Esa es la pregunta del millón, ¿no? Kira es... increíblemente inteligente. Y ahora eliminó a los agentes que lo estaban rastreando. L va a tener que reconsiderar su estrategia."
    protagonista "Light... uno de esos agentes era Raye Penber. El del autobús."
    light "(sin mostrar emoción) ¿En serio? Qué coincidencia trágica."
    protagonista "¿Coincidencia?"
    light '¿Qué más podría ser? [nombre], ¿estás insinuando algo?'
    menu:
        "No, nada. Solo es... raro.":
            light "Todo ha sido raro ultimamente, no? de todas formas tengo que ir a hacer unas compras. Nos vemos mas tarde [nombre]"
            pass
        "Light, si sabés algo sobre Kira, podés confiar en mí.":
            light "Caminemos. Hay un lugar más privado donde podemos hablar."
            'Te lleva a una esquina menos concurrida del centro comercia'
            light "(en voz muy baja) ¿Qué tan comprometido estás con la idea de un mundo mejor?"
            protagonista "¿Qué querés decir?"
            light "Un mundo sin crimen. Sin corrupción. Donde la gente pueda vivir sin miedo. ¿Harías lo que fuera necesario para crear ese mundo?"
            protagonista  "Depende de qué sea 'lo necesario'."
            light "Sacrificios. Siempre hay sacrificios en cualquier revolución. Los agentes del FBI... eran un obstáculo. Estaban protegiendo el viejo sistema corrupto."
            protagonista "Light, ¿estás diciendo que...?"
            light "No estoy diciendo nada. Solo estoy... especulando. Sobre lo que Kira podría estar pensando. Sobre por qué hace lo que hace."
            protagonista "Pero hablás como si lo conocieras."
            light "Quizás lo conozco. O quizás solo entiendo su lógica mejor que la mayoría. ¿Eso me hace cómplice? ¿O simplemente... perceptivo?"
            "Está jugando contigo. Dandote pistas sin admitir nada. Probándote para ver si podés ser confiable."
            protagonista "Si Kira me pidiera ayuda... ¿debería dársela?"
            light "Esa es una pregunta que solo vos podés responder. Pero te diré esto: las personas que están del lado de Kira no tienen nada que temer. Son las que se oponen a él las que deberían preocuparse."
            protagonista "¿Eso es una amenaza?"
            light "Es un consejo. De un amigo."
            'La tension aumenta pero tu conversacion con Light se ve interrumpida, ya que el recibe una llamada.'
            light 'Tengo que irme [nombre], pero piensa en lo que hablamos'
            $ confianza_light += 2
            pass
        "Necesito irme.":
            'Light, te mira entre confusion y sospecha pero afirma con su cabeza. Te escapas rapidamente de la escena. Todo lo que dijo Light te ha asustado'
            $ alianza_l += 1
            $ confianza_light -= 2
            pass
    jump escena_03_07

label escena_03_07:
    scene comedor
    'Llegás a casa. Tu padre ya está ahí, esperándote'
    show padre_serio at mover_personaje_derecha
    padre "Necesitamos hablar. Ahora."
    protagonista "¿Qué pasó?"
    padre "Hablé con L. Sobre vos. Sobre tu oferta de ayudar."
    protagonista "¿Y?"
    padre "Él quiere conocerte. Personalmente."
    protagonista "¿L quiere conocerme?"
    padre "Sí. Dice que necesita 'perspectivas jóvenes' en el equipo. Y dado que ya conocés a uno de los principales sospechosos sin que él lo sepa... podés ser útil."
    protagonista "¿Entonces aceptó?"
    padre "Con condiciones. Primero, no podés decirle a NADIE sobre esto. Ni a tus amigos, ni a Light, NADIE. Segundo, hacés exactamente lo que L dice. Nada más, nada menos. Y tercero... si la situación se vuelve peligrosa, te retirás inmediatamente. ¿Entendido?"
    protagonista "Entendido."
    padre "Bien. Mañana, después de la escuela, vas a ir a una dirección que te voy a dar. Ahí conocerás a L y al resto del equipo de investigación."
    protagonista "Espera, ¿mañana? ¿Tan pronto?"
    padre "L no pierde tiempo. Especialmente ahora que Kira acaba de matar a doce agentes del FBI. Esto se está intensificando rápidamente."
    "Tu corazón late rápidamente. Mañana conocerás a L, el mejor detective del mundo. Y oficialmente te unirás a la investigación de Kira. La investigación de tu amigo."
    hide padre_serio
    scene black
    '¿Cuál es tu verdadera motivación para unirte a la investigación?'
    menu:
        "Quiero ayudar a atrapar a Kira. Si es Light, debe pagar.":
            $ alianza_l += 4
            pass
        "Quiero proteger a Light. Es alguien muy importante para mi.":
            $ alineacion_kira += 4
            pass
        "Quiero entender cómo funciona el poder de Kira.":
            $ codicia_dn += 4
            pass
    "Tu decisión está tomada. Mañana, todo cambia. Te convertirás en parte de algo más grande que vos. La pregunta es: ¿de qué lado vas a estar cuando todo termine?"
    jump escena_04_01

label escena_04_01:
    scene l_hotel
    "Después de la escuela, tu padre te lleva a una dirección en el centro de la ciudad. Es un hotel elegante pero discreto."
    padre "Recordá las reglas. No toques nada sin permiso. No hagas preguntas innecesarias. Y sobre todo... no subestimes a L."
    'La habitación está llena de pantallas, computadoras, cables por todos lados. Hay cinco hombres presentes. Y en el centro, sentado de forma extraña en una silla, hay un joven de pelo negro despeinado, ojos enormes, comiendo dulces'
    show l_neutral at quieto_derecha
    "Ese es L. No es lo que esperabas. Parece tener tu edad, quizás un poco mayor. Está descalzo, sentado con las rodillas contra el pecho. Y sin embargo... hay algo en sus ojos. Una inteligencia que te hace sentir como si pudiera ver a través de vos."
    L 'ese es tu hijo/a, supongo."'
    padre "Sí, L. Este es [nombre]."
    L "Hmm. Más joven de lo que pensé. [nombre], ¿tenés idea de por qué te pedí venir?"
    protagonista "Mi padre dijo que necesitabas... perspectivas jóvenes."
    L "Una forma amable de decirlo. La verdad es: necesito a alguien que pueda acercarse a Light Yagami sin levantar sospechas. Los adultos no pueden hacerlo. Ya sabe que lo estamos vigilando, por eso mató a los agentes del FBI."
    protagonista "¿Entonces estás seguro de que Light es Kira?"
    L "Un 85%% de probabilidad. Quizás 90%%. Pero necesito pruebas. Y ahí es donde entrás vos."
    protagonista "¿Qué querés que haga?"
    L "(chupando un dulce) Por ahora, nada. Solo seguí siendo su amigo. Observá. Escuchá. Si dice o hace algo sospechoso, reportámelo. No lo confrontes, no lo acuses, solo... observá."
    "Otro investigador" "L, ¿estás seguro de esto? Es solo un estudiante. Si Light realmente es Kira..."
    L "Si Light es Kira, ya sospecha de todos los adultos alrededor de él. Pero un compañero de clase, un amigo... esa es su zona ciega. Los sociópatas subestiman las relaciones personales porque no las entienden realmente."
    protagonista "¿Sociópata? Light no es..."
    L  "Light Yagami: estudiante perfecto, atleta superior, campeón de tenis, hijo modelo. Pero desde que Kira apareció, su comportamiento ha cambiado. Sutilmente. Desapariciones inexplicables, interés obsesivo en criminología, y... estuvo en el autobús donde murió el agente Penber."
    "L muestra una foto del autobús. Light está claramente visible."
    L "Penber estaba siguiendo a Light. Y días después, murió. Junto con otros once agentes que estaban investigando la familia Yagami y otras familias relacionadas con la policía."
    protagonista "Eso no prueba que Light sea Kira."
    L "No. Por eso necesito pruebas. Pruebas que vos vas a ayudarme a conseguir."
    menu:
        "Haré lo que sea necesario para atrapar a Kira.":
            L 'Me gusta tu determinacion. Seras un activo muy valioso en esta investigacion'
            L 'Pasemos con una actividad sencilla'
            $ alianza_l += 4
            pass
        "Solo quiero la verdad. Si Light es inocente, lo probaré.":
            L "Una actitud razonable. Bien. Entonces comenzaremos con algo simple."
            L "Estos son todos los movimientos conocidos de Light en las últimas dos semanas. Quiero que los compares con los horarios de las muertes de Kira. Si hay discrepancias, si Light tiene coartadas sólidas, entonces reduciré mi porcentaje de sospecha."
            protagonista "¿Y si coinciden?"
            $ alianza_l += 1
            L "Entonces pasamos a la siguiente fase."
            pass
        "¿Y si descubro que NO es Kira? ¿Buscarás a otro sospechoso?":
            L 'Seria lo correcto a hacer en una invetigacion. Aunque reafirmo lo que dije hace un momento. Hay un 85%% de probabilidad de que Light sea kira'
            L 'Pero pasemos con una actividad sencilla'
            pass
    "Pasás las siguientes horas revisando datos con L y el equipo. Es agotador pero fascinante. Ves cómo piensa L, cómo conecta piezas que parecen no tener relación."
    L  "Mirá este patrón. Cada vez que Light estaba en casa entre las 7 PM y 10 PM, múltiples criminales morían. Pero cuando estaba en alguna actividad escolar documentada, las muertes paraban o disminuían drásticamente."
    protagonista "Eso podría ser coincidencia."
    L "Una vez es coincidencia. Dos veces es un patrón. Treinta y siete veces es evidencia."
    show matsuda_hablando at mover_personaje_izquierda
    matsuda "Pero, L, ¿cómo podría matar sin estar presente? ¿Magia?"
    L "No magia. Algo que no entendemos aún. El primer mensaje de Kira mencionó 'dioses de la muerte'. Quizás hay algo sobrenatural involucrado."
    protagonista "¿Sobrenatural? ¿Lo decís en serio?"
    L "Elimino lo imposible. Lo que queda, por improbable que sea, debe ser la verdad. Y lo imposible es que alguien esté matando a distancia sin ningún método conocido. Lo improbable es que haya algún poder que no entendemos."
    "Pasas horas más analizando. Al final, los datos son innegables: Light estaba libre durante el 93%% de las muertes de Kira. Las únicas excepciones son cuando estaba en la escuela... pero incluso entonces, las muertes ocurrían en horarios específicos que podrían planearse con anticipación."
    L "Bien. Ahora que entendés el patrón, aquí está tu primera misión."
    L "Este es un micrófono y rastreador miniatura. Quiero que lo coloques en la mochila de Light."
    protagonista "¿Espiarlo? No puedo... es mi amigo."
    L "Si es tu amigo e inocente, entonces no tendrá nada que esconder. Y si no lo es... entonces no es realmente tu amigo, ¿verdad?"
    padre "[nombre], no tenés que hacer esto si no querés."
    L "Cierto. No tenés que hacerlo. Pero entonces no puedo continuar con tu participación en la investigación. Necesito saber si puedo confiar en que pondrás la justicia por encima de la lealtad personal."
    protagonista "Está bien. Lo haré."
    L "Bien. Mañana en la escuela, durante el almuerzo. Light siempre deja su mochila en el aula cuando va a la azotea. Tendrás aproximadamente 15 minutos. Será suficiente."
    protagonista "¿Y si alguien me ve?"
    L "Decí que estás buscando tu propia mochila. O que Light te pidió que sacaras algo de la suya. Improvisá. Sos inteligente."
    matsuda "L, ¿no es peligroso para el chico/a?"
    L "Todo es peligroso cuando investigás a un asesino serial. Pero esta es la opción menos peligrosa."
    "Te dan el dispositivo. Es increíblemente pequeño, del tamaño de un botón. Fácil de esconder. Fácil de colocar. Pero la decisión de hacerlo... eso es lo difícil."
    jump escena_04_02

label escena_04_02:
    scene pieza
    "Esa noche, no podés dormir. El dispositivo está en tu escritorio, brillando levemente bajo la luz de la luna."
    protagonista "Mañana voy a traicionar a mi amigo. O... voy a ayudar a capturar a un asesino serial. ¿Cómo puedo distinguir entre ambos?"
    'Tu telefono vibra. Mensaje de Light'
    'Mensaje de Light' "Oye, ¿almorzamos mañana en la azotea? Quiero hablar sobre algo importante."
    "El timing no podría ser peor. O mejor, dependiendo de cómo lo veas. Si decides aceptar complicara tu mision pero si rechazas la oferta de Light levantaras sospechas"
    menu:
        'Aceptar almorzar con Light ':
            'Le mandas un mensaje afirmativo a light y te vas a dormir'
            $ confianza_light += 1
            $ almuerzo_azotea = True
        'Hacer una excusa':
            'Le mandas un mensaje poniendo una excusa a light y te vas a dormir'
            $ confianza_light -= 1
            $ almuerzo_azotea = False
    jump escena_04_03

label escena_04_03:
    scene escuela
    "Es la hora del almuerzo. Light se levanta de su asiento."
    show light_perfil at mover_personaje_derecha
    light "Voy a la azotea. ¿Venís?"
    if almuerzo_azotea == True:
        protagonista "Mmm, en un momento. Olvidé algo en mi casillero."
        light "Ok, te espero arriba."
        pass
    else:
        protagonista 'Lo siento Light, ya le habia dicho a Yuri de comer con ella y los chicos'
        light 'Esta bien. No te preocupes, nos vemos despues'
        pass
    "Light se retira"
    "Este es el momento. La mochila de Light está a dos metros de vos. Nadie está mirando. Podés hacerlo ahora."
    protagonista "Dios, ¿qué estoy haciendo?"
    'Te levantás. Caminás hacia la mochila de Light'
    "Tus manos están temblando. Abrís el cierre de la mochila lentamente. Adentro hay libros, cuadernos, lapiceras... nada inusual."
    protagonista "Solo tengo que colocarlo en un bolsillo lateral. Nadie lo notará."
    "Justo cuando estás por colocar el dispositivo, escuchás una voz"
    yuri "¡[nombre]! ¿Qué estás haciendo?"
    "Tu corazón se detiene. Te girás. Yuri está en la puerta del aula."
    protagonista "Yo... Light me pidió que sacara su libro de matemáticas. Me lo quiere prestar."
    yuri "Ah, ok. ¿Vas a almorzar?"
    if almuerzo_azotea == True:
        protagonista "Lo siento, ya habia acordado en comer con Light"
        pass
    else:
        protagonista "Sí, en un momento."
        pass
    yuri "Bueno, nos vemos luego."
    "Yuri se va. Respirás aliviado"
    "Rápidamente colocás el dispositivo en un bolsillo pequeño dentro de la mochila. Invisible. Indetectable. Traición invisible."
    "Lo hiciste. Ahora Light será monitoreado 24/7. Cada palabra, cada conversación, grabada y analizada por L."
    protagonista  "Dios que estoy haciendo, Light perdóname."
    if almuerzo_azotea == True:
        jump escena_04_04
    else:
        jump escena_04_05
    
label escena_04_04:
    scene terrasa_colegio
    'Subís a la azotea. Light está ahí, esperando'
    light  "Ahí estás. Pensé que te habías olvidado."
    protagonista "No, solo tardé un poco. Dijiste que querías hablar de algo importante."
    'Light se acerca al borde de la azotea, observando la ciudad'
    light "Sí. He estado pensando mucho últimamente. Sobre vos, sobre mí, sobre... lo que está pasando en el mundo."
    protagonista "¿A qué te referís?"
    light "Kira ha estado activo por casi dos meses ahora. Y el mundo está cambiando. El crimen está bajando. La gente tiene miedo de hacer cosas malas. ¿No es eso... bueno?"
    protagonista "Es bueno que el crimen baje. Pero no se si así."
    light "¿Por qué no? ¿Qué importa el método si el resultado es un mundo mejor?"
    protagonista "El método importa porque define quiénes somos. Si usamos el asesinato para lograr paz, entonces la paz está construida sobre sangre."
    light "Todo está construido sobre sangre, [nombre]. Cada civilización, cada imperio, cada era de paz. La diferencia es que Kira está siendo honesto sobre ello."
    protagonista "Light, ¿por qué defendés tanto a Kira?"
    light "Porque creo que es lo correcto. Y creo que vos también lo creés, en el fondo. Por eso seguís hablando conmigo sobre esto. Por eso no me has denunciado."
    protagonista "¿Denunciarte? ¿Por qué te denunciaría?"
    light "Buena pregunta. ¿Por qué no lo has hecho?"
    "Hay un peso en sus palabras. Como si supiera algo. Como si estuviera probándote."
    menu:
        "Porque sos mi amigo y confío en vos.":
            light "Gracias. Necesitaba escuchar eso. Últimamente siento que no puedo confiar en nadie. El FBI me estaba siguiendo, ¿sabías? Antes de que murieran."
            protagonista "¿Te estaban siguiendo?"
            light "Sí. Penber, el agente del autobús. Estaba siguiéndome porque mi padre está en la policía y encajo en el perfil de Kira. Joven, inteligente, acceso a información. Es casi cómico."
            protagonista "¿Y no te asusta? Si te seguían..."
            light "Ya no importa. Están muertos. Kira los eliminó. Lo cual me hace preguntarme...¿Kira me estaba protegiendo? ¿O protegiendo su secreto? Si yo fuera Kira, matar a los agentes que me siguen sería la jugada obvia. Pero también sería increíblemente sospechoso. Es una paradoja interesante...."
            "Está jugando contigo otra vez. Hablando en hipotéticos que no son tan hipotéticos."
            $ confianza_light +=2
            jump escena_04_05
            
        "¿Qué estás insinuando, Light?":
            light "No insinuo nada, [nombre]. Solo que si repasamos los hechos que han ocurrido ultimamente cosas raras han pasado alrededor mio y eso podria hacerme parecer culpable de algo. Las casualidades son impresionantes no?"
            "Está jugando contigo otra vez. Hablando de casualidades."
            jump escena_04_05
        "Porque no tengo nada que denunciar... ¿o sí?":
            light 'No creo que tengas nada que puedas denuciar igualmente...¿o sí?'
            "Está jugando contigo otra vez. Devolviendote la pregunta."
            protagonista 'No, realmente no....'
            light 'Entonces mejor dejemos el tema de lado'
            $ confianza_light -=2
            jump escena_04_05


label escena_04_05:
    scene l_hotel
    'Después de la escuela, vas directo al hotel'
    if almuerzo_azotea == True:
        L "Interesante. Muy interesante."
        protagonista "¿Qué pensás?"
        L "Light está confesando sin confesar. Es inteligente. Habla en tercera persona sobre Kira, crea distancia psicológica, pero al mismo tiempo te está diciendo exactamente lo que hizo."
        matsuda "¿Pero eso es suficiente para arrestarlo?"
        L "No. No es admisible en corte. Y además, podría argumentar que solo estaba especulando. Necesitamos evidencia física."
        pass
    else:
        L '(con un aire pensativo) Para lo popular que es el joven Yagami parece que no ha hablado con nadie ademas que su madre y hermana, pense que estaria'
        protagonista 'Es que son epocas de examen....'
        jefe 'Es verdad, Light siempre pone toda su concentracion en los examenes'
        matsuda 'Entonces no deberias de estar estudiando vos tambien, [nombre]....'
        L '(Interrumpiendo ya molesto) Bueno esta operacion de poner el microfono fue inutil, necesitamos una puebra contundente'
        pass
    protagonista "¿Cómo qué?"
    L "El arma. Lo que sea que Kira use para matar. Debe existir algo físico. Un objeto, un dispositivo, algo. Y Light lo tiene en algún lugar."
    jefe "¿Querés registrar su casa? Puedo conseguir una orden."
    L "No. Si lo hacemos de forma oficial, Kira sabrá que estamos cerca. Destruirá la evidencia. Necesitamos otro método."
    L "[nombre], ¿has estado en la casa de Light?"
    protagonista "No, nunca."
    L "¿Podrías ir? ¿Cómo amigo?"
    menu:
        "Sí, puedo intentar visitarlo.":
            L "Excelente. No necesitás buscar nada específico. Solo observá. Su habitación, sus hábitos, cualquier cosa inusual. Y si ves algo que parezca importante, haceme saber."
            padre "L, esto está volviéndose muy peligroso. Si Light realmente es Kira y descubre que mi hijo/a lo está espiando..."
            L "Por eso debemos ser cuidadosos. [nombre], si sentís algún peligro, salís inmediatamente. ¿Entendido?"
            protagonista "Entendido."
            $ alianza_l += 2
            jump escena_04_06

        "Como planteas algo asi L? eso sería ir demasiado lejos.":
            L '[nombre], pense que al entrar al equipo habias comprendido que bajo estas circustancias especiales los metodos deben ser igual de especiales. Si no eres capaz de entender eso estas invitado a retirarte'
            padre 'L, es solo un chico/a, creo que estas poniendo mucha presion sobre el/ella'
            jefe 'Exacto, no puedes pedirle a un joven que traicione sus valores'
            'Piensas dos veces las cosa, si te quitan de la invetigacion, talvez nunca puedas descubrir la verdad'
            protagonista 'No...esta bien, no me siento bien con lo que vamos a hacer pero lo voy a hacer por la verdad'
            $ alianza_l -= 2
            jump escena_04_06

        "¿Qué estaría buscando exactamente?":
            L 'Bueno [nombre] ese es exactamente tu trabajo, descubrir que podria ser una evidencia o que deberiamos investigar. Es muy probable, no, es seguro de que si Light es Kira nunca te mostraria su arma o forma de matar de inmediato'
            protagonista 'Entonces como deberia de proceder?'
            L 'Hazlo hablar, Kira es alguien que sufre de un complejo de dios inimaginable y estoy seguro que ama hablar de si mismo'
            protagonista 'Entendido.'
            $ codicia_dn += 2
            jump escena_04_06

label escena_04_06:
    scene pieza
    "Esa noche, planificás cómo pedirle a Light que te invite a su casa. Tiene que parecer natural, no forzado."
    'Escribís y borrás varios mensajes antes de decidirte por uno'
    "MENSAJE A LIGHT" "Oye, ¿tenés apuntes de la clase de química? Me perdí la última y estoy confundido con el tema."
    "Enviás el mensaje. Esperás. Cinco minutos después, responde."
    'MENSAJE A LIGHT' "Sí, tengo apuntes completos. ¿Querés que te los pase mañana o podés venir a mi casa después de la escuela? Podemos estudiar juntos."
    "Perfecto. Cayó en la trampa. O... ¿vos caíste en la de él?"
    'MENSAJE A LIGHT' "Suena bien. ¿Qué hora?"
    'MENSAJE DE LIGHT' "A las 5 PM. Te mando la dirección."
    "Lo lograste. Mañana entrarás en la casa de un posible asesino serial. Y si L tiene razón, también descubrirás el secreto más peligroso del mundo."
    jump escena_04_07

label escena_04_07:
    scene light_pieza
    "Lo que no sabías es que Light ya sospechaba de vos."
    ryuk "Ese es tu amigo, ¿verdad? El nuevo estudiante."
    light "Sí. Y probablemente un espía de L."
    ryuk "¿Y lo vas a invitar a tu casa? ¿Sos boludo Light?"
    light "Al contrario. Es la jugada perfecta. Si realmente está trabajando para L, entonces L espera que encuentre algo. Pero no encontrará nada porque no hay nada que encontrar. Mi habitación está limpia."
    ryuk "¿Y el Death Note?"
    light "Escondido en un lugar donde nadie puede encontrarlo. Incluso si registran mi habitación, no lo hallarán. Y además, tengo sistemas de seguridad."
    'Light muestra un pequeño mecanismo en su escritorio'
    light "Si alguien abre mi cajón sin desarmar este mecanismo primero, todo se incendiará. El Death Note, mis notas, todo. Prefiero destruir la evidencia que dejar que L la encuentre."
    ryuk "Humano paranoico."
    light "Humano cauteloso. Hay una diferencia."
    'Light se sienta en su cama'
    light  "[nombre] es inteligente. Pero no tanto como yo. Mañana veremos exactamente cuánto sabe L. Y si [nombre] es un problema o un aliado... en todo caso, Kira puede eliminar problemas."
    ryuk "Esto va a ser divertido."
    jump escena_04_08

label escena_04_08:
    scene pieza
    "Mañana visitarás a Light. Entrarás en su mundo. Y dependiendo de lo que descubras, tu vida podría cambiar para siempre."
    protagonista "¿Qué espero encontrar? ¿Evidencia de que es Kira? ¿O prueba de su inocencia?"
    "Pero hay algo más importante que considerar: ¿Qué harás si descubrís la verdad?"
    menu:
        "Lo denunciaré a L inmediatamente.":
            $ alianza_l += 5
            pass
        'Le daré la oportunidad de explicarse primero.':
            $ alineacion_kira += 3
            pass
        'Intentaré tomar su aram para mí.':
            $ codicia_dn  += 5
            pass
        'No sé. Depende de lo que sienta en el momento.':
            pass
    "Tu decisión está tomada, aunque quizás no lo sepas aún. Mañana, la verdad te estará esperando. La pregunta es: ¿estás listo para ella?"    
    jump escena_05_01

label escena_05_01:
    scene casa_yagami
    "Es viernes por la tarde. Saliste de la escuela directo hacia la casa de Light. En tu bolsillo llevás un pequeño dispositivo de L: una cámara miniatura disfrazada de bolígrafo."
    protagonista "Puedo hacer esto. Solo entro, estudio con él, observo, y salgo. Simple."
    "La familia Yagami vive en un vecindario respetable. La casa se ve normal, familiar. No es el tipo de lugar donde esperarías encontrar a un asesino serial."
    'Tocás el timbre'
    light "¡[nombre]! Justo a tiempo."
    light "Mis padres están trabajando y mi hermana tiene club después de la escuela, así que tenemos la casa para nosotros por un par de horas."
    protagonista "¿Tu padre sigue trabajando en el caso Kira?"
    light  "Obsesivamente. Apenas lo vemos últimamente. Pero así es él: cuando tiene un caso, no descansa hasta resolverlo....Que malos modales los mios! pasa pasa"
    "Subís las escaleras. El dispositivo de grabación que plantaste en su mochila está activo, y L está escuchando todo en tiempo real."
    scene light_pieza
    light "Esta es mi habitación."
    "La habitación de Light es exactamente lo que esperarías: inmaculadamente ordenada. Libros perfectamente alineados, escritorio sin una mota de polvo, cama hecha con precisión militar."
    protagonista "Tu habitación está muy... limpia."
    light "Mi mamá dice lo mismo. Supongo que soy un poco obsesivo con el orden."
    "Mientras Light busca sus apuntes, aprovechás para observar discretamente. Los libros son todos académicos o clásicos de literatura. No hay nada sospechoso a simple vista."
    protagonista "(Pensando) ¿Dónde escondería el Death Note? Si yo fuera Kira..."
    light "Aquí están los apuntes de química. ¿Querés que repasemos juntos o preferís llevártelos?"
    menu:
        "Repasemos juntos.":
            protagonista "Repasemos juntos. Siempre entiendo mejor cuando alguien me explica."
            light "Claro."
            'Se sientan en el escritorio. Light comienza a explicar, pero vos estás más concentrado en observar la habitación'
            "Desde tu posición, podés ver el cajón del escritorio. Tiene un pequeño mecanismo extraño en el borde. No es un cierre normal."
            protagonista  "(Pensando) ¿Qué es eso?"
            'De repente, notás algo en la ventana: un pequeño trozo de papel adherido en un ángulo específico'
            "Es casi invisible a menos que sepas qué buscar. Un mecanismo de seguridad. Si alguien abriera la ventana desde afuera, el papel caería. Light sabría que alguien entró."
            light "¿[nombre]? ¿Me estás escuchando?"
            protagonista "Perdón, me distraje. ¿Qué decías?"
            light "Decía que esta ecuación es particularmente complicada. ¿Estás bien? Parecés nervioso."
            protagonista "No, solo... es que tu habitación es muy diferente a la mía. Tan ordenada."
            light "El orden externo refleja orden interno. O al menos eso intento."
            "Continúan estudiando por 20 minutos. Entonces, Light se levanta"
            light "Voy a traer algo de beber. ¿Té está bien?"
            protagonista "Perfecto."
            "Este es el momento. Light salió. Tenés quizás dos minutos antes de que regrese."
            protagonista "L dijo que buscara algo inusual. Ese cajón con el mecanismo extraño..."
            "Rápidamente sacás el bolígrafo-cámara que L te dio. Con manos temblorosas, tomás fotos de todo: el escritorio, el mecanismo del cajón, el papel en la ventana, los libros."
            protagonista "Vamos, vamos, más rápido..."
            'Escuchás pasos en las escaleras]'
            "¡Light está volviendo! Guardás el bolígrafo justo cuando la puerta se abre."
            light "Aquí está. Espero que te guste el té verde."
            protagonista "Gracias."
            light "¿Seguro que estás bien? Parecés muy tenso."
            protagonista "Es solo que... este tema de química es más complicado de lo que pensaba."
            light "Hmm. Bueno, tomémonos un descanso entonces. Hablemos de otra cosa."
            light "[nombre], puedo preguntarte algo personal?"
            protagonista "Claro."
            light "¿Qué pensás honestamente de Kira? Sin filtros, sin preocuparte por lo que es 'políticamente correcto'."
            "Sabes que L esta escuchando"
            protagonista "Es... complicado."
            light "La mayoría de las cosas importantes lo son. Pero debe haber una parte de vos que piensa algo específico. ¿Héroe o villano?"
            menu:
                "Héroe. El mundo es mejor gracias a Kira.":
                    light "Exactamente. Finalmente alguien que lo entiende. El crimen ha bajado globalmente en un 70%%. ¿Sabés cuántas vidas inocentes eso representa?"
                    protagonista "Miles. Quizás millones."
                    light "Millones. Y todo lo que Kira ha hecho es eliminar a criminales que de todas formas no merecían vivir. Violadores, asesinos, traficantes. El mundo literalmente es un lugar mejor sin ellos."
                    protagonista "Pero L dice que Kira es un asesino."
                    light "(inclinandose) L está protegiendo el sistema viejo y corrupto. Obviamente va a decir eso. Pero pensá: ¿cuántos casos ha resuelto L? ¿Cientos? ¿Miles? Y en ese mismo tiempo, cuántos crímenes más se cometieron. Kira está solucionando el problema desde la raíz."
                    protagonista "Es un argumento convincente."
                    light  "No es solo un argumento. Es la realidad. Y creo que vos lo ves, ¿verdad? Creo que entendés que a veces, para crear un mundo mejor, hay que estar dispuesto a ensuciarse las manos."
                    "Hay algo en la forma en que Light habla. No es teórico. No está especulando. Habla con la convicción de alguien que SABE. Alguien que está personalmente involucrado."
                    $ confianza_light += 2
                    $ confianza_l -=2
                    pass
                "Villano. Nadie tiene derecho a matar.":
                    'Se siente un aire tenso en el aire. No es la respuesta que Light esperaba o tal vez si. Pero no esta contento con esta'
                    light "Pense que serias alguien mas abierta de mente, considerando los datos"
                    protagonista 'Los datos? Light, no importa que resultados esten dado las acciones de Kira. Es un asesino'
                    "Light reflexiona sobre lo que va a decir. Parece que se dio cuenta de algo"
                    $ confianza_light -= 2
                    $ confianza_l +=2
                    pass
                "No lo sé. Por eso estoy aquí, tratando de entender.":
                    light 'Como todos los demas, como todo los demas....'
                    pass
            'La puerta se abre de golpe'
            'Sayu' "¡Onii-chan! ¿Tenés mi... oh, lo siento, no sabía que tenías visita."
            light "Sayu, esta es [nombre], un compañero de clase. [nombre], mi hermana menor, Sayu."
            'Sayu' "¡Hola! ¿Sos el/la nuevo/a del que Light habló?"
            protagonista "Supongo que sí."
            'Sayu' "Es raro ver a Light con amigos en casa. Usualmente solo estudia. Es súper aburrido."
            light "Sayu, ¿necesitabas algo?"
            'Sayu'  "Sí, mi calculadora. Creo que la dejé aquí ayer cuando me ayudaste con la tarea."
            'Sayu entra y busca en el escritorio. Vos y Light se tensionan simultáneamente'
            light "No está en el escritorio, Sayu. Revisá tu mochila de nuevo."
            'Sayu' "Pero estoy segura que..."
            'Sayu está a punto de abrir el cajón con el mecanismo'
            light "¡Sayu! Ya revisé ahí esta mañana. No está."
            'Sayu' "Ok, ok. Voy a revisar abajo. Perdón por molestar."
            'Sayu sale, claramente confundida por la reacción de Light'
            "Light se sienta de nuevo, respirando profundo. Por primera vez, lo viste perder el control, aunque sea levemente."
            protagonista "¿Estás bien?"
            light "Sí. Es solo que Sayu a veces es... invasiva. No respeta la privacidad."
            protagonista "¿Qué hay en ese cajón que no querés que vea?"
            light "Nada de su interés. Solo... cosas privadas. Todos tenemos secretos, ¿no?"
            "La tensión en el aire es palpable. Light te está midiendo, evaluando cuánto sospechás."
            if (confianza_light >= 10):
                light "[nombre], puedo confiar en vos, ¿verdad?"
                protagonista "¿Confiar en mí para qué?"
                light "Para... entender cosas que la mayoría no entiende. Para ver el panorama completo. Para no juzgar antes de conocer todos los hechos."
                protagonista "Light, ¿qué me estás tratando de decir?"
                light "Que el mundo está cambiando. Y las personas tendrán que elegir de qué lado estar. El lado del cambio, o el lado del estancamiento."
                protagonista "Eso suena como una amenaza."
                "Light se acerca, casi tirandose sobre vos. Puedes ver como mueve suavemente su mano y la apoya en tu pecho, justo donde tienes guardado el boligrafo. Siempre supo que lo estaban espiando! Hay una gran tension entre ustedes dos pero Light esta mucho mas calmado que antes"
                light "No es una amenaza. Es una realidad. Y quiero asegurarme de que, cuando llegue el momento de elegir, vos…"
                pass
            else:
                light 'Bueno, sigamos estudiando...'
                pass
            pass 
        "Los llevaré, no quiero molestarte.":
            light 'Seguro que no necesitas ayuda para estudiar'
            protagonista 'Si, creo que soy capaz por mi mismo, cualquier cosa te aviso'
            'Light te guia hasta la puerta de vuelta, talvez no descubriste mucho pero lograste hacer un mapeo general de la pieza de Light....'
            pass
    'CONTINUARA'



        
 








            


