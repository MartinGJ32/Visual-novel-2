# The script of the game goes in this file.
define kira = Character("Kira")
define l = Character("L")
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
image casa_yagami = im.Scale("fondos/Yagami_house.jpg", config.screen_width, config.screen_height)
image comedor = im.Scale("fondos/comedor.jpg", config.screen_width, config.screen_height)
image mundo_shinigami = im.Scale("fondos/mundo-shinigami.webp", config.screen_width, config.screen_height)
image puerta_escuela = im.Scale("fondos/puerta-escuela.webp", config.screen_width, config.screen_height)
image escuela = im.Scale("fondos/escuela.jpg", config.screen_width, config.screen_height)


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
            alineacion_kira += 1
            jump escena_02_02
        'Unirte a la discusión criticando a Kira':
            protagonista 'Considero que kira es un criminal. No se diferencia mucho de otros asesinos o genocidas que han habido en la historia de la humanidad'
            'Suena la campana'
            'Todos se dirigen hacia el aula'
            alianza_l += 1
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
            confianza_light += 1
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
            confianza_light += 1
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
            confianza_light += 1
            alineacion_kira += 2
            'Light se va, dejándote con más preguntas que respuestas'
        "Kira deberia tener cuidado. L parece que sabe lo que hace.":
            show light_frente at mover_personaje_derecha
            'Light se queda pensando por unos segundo'
            light 'Si Kira deberia pensar mas las cosas...'
            'Light se va, sientes que esta charla ha sido incomoda'
            confianza_light -= 1
            alianza_l += 1

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
    padre "[Nombre], quiero que me prometas algo."
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
            alineacion_kira += 3
            confianza_light += 2
            pass
        "Creo en L. Kira debe ser detenido.":
            confianza_light -= 1
            alianza_l += 1
            'A Light parece incomodarle tu respuesta. Se levanta del asiento y se despide respetuosamente. Parece que tu relacion con el se ha complicado'
            pass
        "Todavía no estoy seguro.":
            'Ligth no dice nada pero te observa paraciendo entender tu indecision. Pasan el resto del almuerzo juntos hablando sobre temas mas triviales'
            pass
        "Me pregunto como Kira habra obtenido sus poderes.":
            'Ligth muestra geninua sorpresa con tu respuesta, no le desagrada pero tampoco es la que esperaba. Pasan el resto del almuerzo juntos hablando sobre temas mas triviales'
            codicia_dn += 2
            pass
        jump escena_02_07

label escena_02_07:
    scene pieza
    "Esa noche, no podés dormir. Entrás a internet y buscás información sobre Kira. Lo que encontrás te sorprende."
    "Hay miles de páginas dedicadas a Kira. Algunos lo llaman dios. Otros, demonio. Pero todos están de acuerdo en una cosa: el crimen ha disminuido dramáticamente en las áreas donde Kira ha actuado."
    "Algunas estadisticas salen en la pantalla:
    - Crimen violento: -70% en Japón
    - Robos: -60% globalmente
    - Asesinatos: -75% en ciudades principales
    "
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
            alineacion_kira += 3
            pass
        "Apoyo a L. Nadie tiene derecho a ser juez, jurado y verdugo.":
            alianza_l += 3
            pass
        "No apoyo a ninguno. Solo quiero entender este poder.":
            codicia_dn += 3
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
    ligth "¿Distante? Solo he estado ocupado con estudios y cosas familiares."
    protagonista "¿Tiene que ver con Kira?"
    light "¿Por qué todo tiene que ver con Kira?"
    protagonista "Porque desde que L apareció, estás obsesionado con el tema. Y no sos el único. Las noticias dicen que Kira ha matado a más de 100 criminales solo esta semana."
    light "Lo que significa que el mundo es cada vez más seguro."
    protagonista "O que Kira está perdiendo el control."
    light "(mirándote fijamente) ¿Perdiendo el control? Kira es más calculador que nunca. Cada movimiento es preciso. Cada muerte tiene propósito."
    protagonista "Hablás como si lo conocieras personalmente."
    if confianza_light > 5:
        light "[Nombre], ¿puedo confiar en vos?"
        menu:
            "Sí, podés confiar en mí completamente.":
                ligth "(mirando alrededor, asegurándose de que estén solos) Hay cosas que no podés saber todavía. Pero quiero que sepas... que todo lo que está pasando, todo lo que va a pasar, es necesario. El mundo está cambiando. Y cuando todo termine, vas a entender por qué."
                protagonista "Light, me estás asustando."
                'Light te lleva suavemente hasta una parte donde nadie pueda verlos, casi que parece que te estuviera acorralando'
                light "No tengas miedo. Si estás de mi lado, si realmente creés en un mundo mejor, entonces no tenés nada que temer."
                protagonista "¿De tu lado? Light, ¿qué...?"
                'El celular de Light suena'
                light "Tengo que irme. Hablamos después."
                'Light se va rápidamente, dejándote con más preguntas'
                confianza_light += 1
                pass
            "Depende de qué me digas.":
                light "Depende de lo que quieras escuchar, Si quieres estar en el lado de kira hay cosas que aun debes de comprender."
                'Light se va rápidamente, dejándote con más preguntas'
                confianza_light += 1
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
            confianza_light += 1
            pass
        'Confrontarlo directamente: "¿Qué había en ese papel?"':
            confianza_light -= 2
            codicia_dn += 2
            pass
        'Ignorar el mensaje y seguir investigando solo':
            alianza_l += 1
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
    










            


