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

define tralalero = Character('Tralalero-tralala')
define center_pos = Position(xalign=0.2, yalign=0.5)
define tuntunsahur = Character('Tun Tun Sahur')

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
# Variables principales
default alineacion_kira = 0      # Pro-Kira
default alianza_l = 0            # Pro-L
default codicia_dn = 0           # Interés en el Death Note

# Variables de relación
default confianza_light = 5      # Inicia neutral
default confianza_l = 0          # Inicia en 0
default confianza_misa = 0       # Con Misa Amane
default sospecha_general = 0     # Si sube mucho, game over

# Variables de estado
default tiene_death_note = False
default tiene_ojos_shinigami = False
default conoce_identidad_l = False
default light_sospecha = False

# Variables de historia
default naomi_viva = True       # Puede cambiar
default misa_capturada = False
default light_capturado = False


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
