#The script of the game goes in this file.
#Declare characters used by this game. The color argument colorizes the
#name of the character.

#variables: 
#choice 0
define room_count = 0
define tv_flag = False
define lab_flag = False
define nut_flag = False
    #choice 0 pac minigame order
define in_order = True
define in_order_number = 0
    #choice 0ish nuclear ending flag
define nuclear_flag = False

#choice 1 augustus
    #machine pac
define machine_path_good = False
define augustus_dead = False
    #encontrar augustus pac
define random_hide_place = 0
define hide_path_good = True
    #choice 2 light
define light_on = True

#functions:
init python:
    import random
    def compare_numbers(b, items, death_option):
        global in_order_number
        if in_order_number == b:
            in_order_number += 1
            renpy.jump(items)
        else:
            in_order = False
            renpy.jump(death_option)

    def machine_path_comparison(bool):
        global machine_path_good
        global augustus_dead
        machine_path_good = bool
        if machine_path_good == False:
            augustus_dead = True
        renpy.jump("choice1_kill_convergence")

    def generate_random_hide_place():
        global random_hide_place 
        random_hide_place = random.randint(0,2)
    
    def hide_path_comparison(bool):
        global hide_path_good
        global augustus_dead
        hide_path_good = bool
        if hide_path_good == False:
            augustus_dead = True
            renpy.jump("choice1_kill_convergence")
        else:
            augustus_dead = False
            renpy.jump("choice1_found_lives")
        
    def nuclear_first_ending_trigger():
        global nuclear_flag
        nuclear_flag = True
        renpy.jump("choice0_done")
    def choice0_rooms_count():
        global room_count
        room_count +=1

#characters:
define narrator = Character(
    None, 
    window_background = None,
    what_size=30,
    what_outlines=[( 2, "#000000", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout="subtitle")

define namomo_inner_dialogue = Character(
    "Namomo",
    window_background = None,
    color="#2b83ff",
    who_outlines=[(2,"#000000",0,0)],
    what_size=30,
    what_outlines=[( 2, "#000000", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout="subtitle")

define dembe = Character("Dembe", color="#ff0000")

define namomo = Character("Namomo", color="#2b83ff")

define wonka = Character("Willy Wonka", color="#800080")
define wonka_burn = Character("Willy Wonka", color="#800080")
define wonka_puppet = Character("Willy Wonka", color="#800080")
define charlie = Character("Charlie", color="#808080")
define veruca = Character("Veruca", color="#FFFF00")
define augustus = Character("Augustus", color="#D2691E")
define violet = Character("Violet", color="#FF69B4")
define mike = Character("Mike", color="#FFA500")
define unknown = Character("???", color="#ff0000")
define placeholder = Character("placeholder", color="#000000")


define loompa1 = Character("Oompa-Loompa 1", color="#ffffff")
define loompa2 = Character("Oompa-Loompa 2", color="#ffffff")
define loompa3 = Character("Oompa-Loompa 3", color="#ffffff")


#transform:
#mitades
transform center:
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 800

#mitades
transform midLeft:
    xanchor 0.5
    yanchor 0.5
    xpos 480
    ypos 800
transform midRight:
    xanchor 0.5
    yanchor 0.5
    xpos 1440
    ypos 800


#confront
transform confront1:
    xanchor 0.5
    yanchor 0.5
    xpos 200
    ypos 800
transform confront2:
    xanchor 0.5
    yanchor 0.5
    xpos 420
    ypos 800
transform confront3:
    xanchor 0.5
    yanchor 0.5
    xpos 1100
    ypos 800
transform confront4:
    xanchor 0.5
    yanchor 0.5
    xpos 1400
    ypos 800
transform confront5:
    xanchor 0.5
    yanchor 0.5
    xpos 1700
    ypos 800

#transform cuartos
transform cuartos1:
    xanchor 0.5
    yanchor 0.5
    xpos 384
    ypos 800
transform cuartos2:
    xanchor 0.5
    yanchor 0.5
    xpos 768
    ypos 800
transform cuartos3:
    xanchor 0.5
    yanchor 0.5
    xpos 1152
    ypos 800
transform cuartos4:
    xanchor 0.5
    yanchor 0.5
    xpos 1536
    ypos 800

#transform quintos
transform quintos1:
    xanchor 0.5
    yanchor 0.5
    xpos 320
    ypos 800
transform quintos2:
    xanchor 0.5
    yanchor 0.5
    xpos 640
    ypos 800
transform quintos3:
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 800
transform quintos4:
    xanchor 0.5
    yanchor 0.5
    xpos 1280
    ypos 800
transform quintos5:
    xanchor 0.5
    yanchor 0.5
    xpos 1600
    ypos 800
#transform decision
transform decisionL:
    xanchor 0.5
    yanchor 0.5
    xpos 200
    ypos 800
transform decisionR:
    xanchor 0.5
    yanchor 0.5
    xpos 1720
    ypos 800
transform nuclear_button_placing:
    xanchor 0.5
    yanchor 0.5
    xpos 0.08
    ypos 0.54
transform violet_flying:
    xanchor 0.5
    yanchor 0.5
    xpos -700
    ypos 0.5
    linear 1 xpos 2500

transform violet_flyingR:
    xanchor 0.5
    yanchor 0.5
    xpos 2500
    ypos 0.5
    rotate 180
    linear 1 xpos -700
transform violet_blob:
    xanchor 0.5
    yanchor 0.5
    xpos 0.48
    ypos 0.72
    rotate 0


#images:
#scenes:
image lab room = "scenes/lab room.png"
image tv room = "scenes/tv room.png"
image nut room = "scenes/nut room.png"

#charimages       
image namomo = "characters/namomo/namomo.png"
image dembe = "characters/dembe/dembe.png"
image dembe_pre = "characters/dembe pre/dembe_pre.png"
image wonka = "characters/wonka/wonka.png"
image wonka_puppet = "characters/wonka/wonka_puppet.png"
image mike = "characters/mike/mike.png"
image violet = "characters/violet/violet.png"
image augustus = "characters/augustus/augustus.png"
image veruca = "characters/veruca/veruca.png"
image charlie ="characters/charlie/charlie.png"
image loompa1 = "characters/loompas/umpa_1.png"
image loompa2 = "characters/loompas/umpa_2.png"
image loompa3 = "characters/loompas/umpa_3.png"
#objimages
image nuclear_button ="pac/button hover.png"

#objects:
#point_and_click:
screen displayTextScreen:  
    default displayText = ""
    default x = 0.5
    default y = 0.5
    vbox:
        xanchor 0.5
        yanchor 0.5
        xpos x
        ypos y
        frame:
            text displayText
screen lab_pac():
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.18
        ypos 0.73
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"), Function (compare_numbers, 0, "lab_pac_ins", "choice0_lab_death")]
        hovered Show("displayTextScreen", 
            displayText = "Prender hornalla", x = 0.18, y = 0.79) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.70
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"), Function (compare_numbers, 1, "lab_pac_ins", "choice0_lab_death")]
        hovered Show("displayTextScreen", 
            displayText = "Poner azúcar", x = 0.25, y = 0.64) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.34
        ypos 0.75
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 2, "lab_pac_ins", "choice0_lab_death")]
        hovered Show("displayTextScreen", 
            displayText = "Revolver", x = 0.34, y = 0.81) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.6
        ypos 0.73
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 3, "lab_pac_ins", "choice0_lab_death")]
        hovered Show("displayTextScreen", 
            displayText = "Cortar", x = 0.6, y = 0.79) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.78
        ypos 0.68
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 4, "lab_pac_ins", "choice0_lab_death")]
        hovered Show("displayTextScreen", 
            displayText = "Amasar", x = 0.78, y = 0.74) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.08
        ypos 0.54
        idle "pac/button idle.png"
        hover "pac/button hover.png"
        action [Function(nuclear_first_ending_trigger)]

screen tv_pac():
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.46
        ypos 0.62
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 0, "tv_pac_ins", "choice0_tv_death")]
        hovered Show("displayTextScreen", 
            displayText = "Acomodar televisor 1", x = 0.46, y = 0.68) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.82
        ypos 0.60
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 1, "tv_pac_ins", "choice0_tv_death")]
        hovered Show("displayTextScreen", 
            displayText = "Acomodar televisor 3", x = 0.82, y = 0.66) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.33
        ypos 0.61
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 2, "tv_pac_ins", "choice0_tv_death")]
        hovered Show("displayTextScreen", 
            displayText = "Equilibarar el televisor principal", x = 0.33, y = 0.67) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.24
        ypos 0.59
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 3, "tv_pac_ins", "choice0_tv_death")]
        hovered Show("displayTextScreen", 
            displayText = "Activar tablero", x = 0.24, y = 0.53) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.598
        ypos 0.605
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 4, "tv_pac_ins", "choice0_tv_death")]
        hovered Show("displayTextScreen", 
            displayText = "Acomodar televisor 2", x = 0.595, y = 0.545) 
        unhovered Hide("displayTextScreen")

screen nut_pac():
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.75
        ypos 0.26
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 0, "nut_pac_ins", "choice0_nut_death")]
        hovered Show("displayTextScreen", 
            displayText = "Ajustar el collar de la rata 1", x = 0.75, y = 0.32) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.51
        ypos 0.51
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 1, "nut_pac_ins", "choice0_nut_death")]
        hovered Show("displayTextScreen", 
            displayText = "Limpiar agujero", x = 0.51, y = 0.57) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.51
        ypos 0.23
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 2, "nut_pac_ins", "choice0_nut_death")]
        hovered Show("displayTextScreen", 
            displayText = "Lanzar bolsa de basura", x = 0.51, y = 0.29) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.1
        ypos 0.5
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 3, "nut_pac_ins", "choice0_nut_death")]
        hovered Show("displayTextScreen", 
            displayText = "Peinar rata 3", x = 0.1, y = 0.56) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.22
        ypos 0.34
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Hide("displayTextScreen"),Function (compare_numbers, 4, "nut_pac_ins", "choice0_nut_death")]
        hovered Show("displayTextScreen", 
            displayText = "Bañar rata 2", x = 0.22, y = 0.4) 
        unhovered Hide("displayTextScreen")

#machine pac
screen machine_closeup_pac():
    modal True
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.05
        ypos 0.23
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Function (machine_path_comparison, True)]
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.05
        ypos 0.52
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Function (machine_path_comparison, False)]

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.05
        ypos 0.791
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        action [Function (machine_path_comparison, False)]

screen find_augustus_pac():
    modal True
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.05
        ypos 0.5
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        if random_hide_place == 0:
            action [Hide("displayTextScreen"), Function (hide_path_comparison, True)]
        else:
            action [Hide("displayTextScreen"), Function (hide_path_comparison, False)]
        hovered Show("displayTextScreen", 
            displayText = "Buscar colina arriba", x = 0.155, y = 0.5) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.35
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        if random_hide_place==1:
            action [Hide("displayTextScreen"), Function (hide_path_comparison, True)]
        else:
            action [Hide("displayTextScreen"), Function (hide_path_comparison, False)]
        hovered Show("displayTextScreen", 
            displayText = "Buscar bosque adentro", x = 0.5, y = 0.41) 
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.9
        ypos 0.5
        idle "pac/test tube idle.png"
        hover "pac/test tube hover.png"
        if random_hide_place==2:
            action [Hide("displayTextScreen"), Function (hide_path_comparison, True)]
        else:
            action [Hide("displayTextScreen"), Function (hide_path_comparison, False)]
        hovered Show("displayTextScreen", 
            displayText = "Buscar por las orillas de la cascada", x = 0.73, y = 0.5) 
        unhovered Hide("displayTextScreen")

#The game starts here.
label start:

    scene broken ww room

    narrator "Estan en la oficina personal de Willy Wonka, está toda desordenada. Papeles tirados,  muebles rotos y fuego en el cesto de la basura. Un Oompa-Loompa esta en el fondo revolviendo el escritorio principal mientras otro mira consternado hacia el jugador y dice:"

    show dembe at midRight
    show namomo at midLeft
    with Dissolve(1)

    pause 

    namomo "Hola, mi nombre es {i}Namomo{/i} y el de allá atras es {i}Dembe{/i}."
    namomo "Se preguntaran como llegamos a esta situación. Bueno todo comenzó cuando el señor Wonka llego a Loompalandia a buscar un grupo de obreros para contribuir con su fabrica. Lue..."

    dembe "Cállate, no hace falta que vayas tan atras en la historia. Todo comenzo hoy por la mañana..."

    scene dark room
    with Dissolve(.5)
    play music classic noloop fadeout 1.0 volume 2.0
    pause 14
    stop music
    scene loompas room
    with Dissolve(.5)
    # clasic music
    show namomo at midLeft
    show dembe_pre at midRight
    wonka "Buen día {b}mierditas{/b}, la fabrica les dice hola. Hoy va a ser un dia bastante tranquilo con una jornada de {b}15 horas{/b}. Como todos los dias seleccionare a {b}dos{/b} de ustedes para que hagan la parte mas pesada..."
    wonka "Hoy le toca a... Dembe y... Namomo. Por favor presentense en mi oficina cuanto antes." 

    scene dark room
    with Dissolve(.5)
    pause 1
    scene ww room
    with Dissolve(.5)
    show namomo at confront1
    show dembe_pre at confront2
    show wonka  at confront5
    wonka "Bueno, les voy a leer rapidamente la lista de tareas para ustedes dos."

    scene lab room
    with Dissolve(.5)
    wonka "{cps=70}1. Prender hornalla. \n2. Poner azúcar.\n3. Revolver.\n4. Cortar.\n5. Amasar.{w=0.2}{nw}{/cps}" 
    scene tv room
    with Dissolve(.5)
    wonka "{cps=70}1. Acomodar televisor 1.\n2. Acomodar televisor 3.\n3. Equilibrar el televisor principal.\n4. Activar tablero.\n5. Acomodar televisor 2.{w=0.2}{nw}{/cps}"
    scene nut room
    with Dissolve(.5)
    wonka "{cps=70}1. Ajustar el collar de la rata 1.\n2. Limpiar agujero.\n3. Lanzar bolsa de basura.\n4. Peinar rata 3.\n5. Bañar rata 2.{w=0.2}{nw}{/cps}"

    scene ww room
    with Dissolve(.5)
    show dembe_pre at confront2
    show namomo at confront1
    show wonka at confront5
    wonka "Ahora vayan a trabajar que la lista no se hace sola. Que tenga un gran dia enanitos."

    hide wonka

    label choice0_done:
    if nuclear_flag == True:
        show namomo at midLeft
        narrator "Namomo siguiendo sus pensamiento intrusivos aprieta un botón rojo que dice claramente {b}Peligro no tocar{/b}."
        narrator "Al hacer esto el reactor que provee de energía a toda la planta comienza un proceso en cadena que comienza cortando la luz del laboratorio e iniciando el ruido de sirenas."
        show wonka at confront4
        play music napoleon noloop volume 2.0
        wonka "Namomo sos un estupido..."
        wonka "Ya no hay nada que hacer..."
        #napoleon meme
        scene bright room
        with Dissolve(.3)
        scene nuclear
        with Dissolve(.3)
        with Pause(5)
        scene final_explosivo
        with Dissolve(.5)
        with Pause(1)
        narrator ""
        jump game_end
        #Se hace un fundido blanco y aparece la imagen de un hongo nuclear.
    if(lab_flag and tv_flag and nut_flag and in_order):
        scene dark room
        with Dissolve (.5)
        narrator "En esta linea temporal sucede lo que todo el mundo ya sabe y conoce sobre esta historia."
        narrator "Si estas interesado en leer eso te dejamos un link para que puedas comprar el libro original escrito por Roald Dalh {a=https://www.yenny-elateneo.com/charlie-y-la-fabrica-de-chocolate/p/MLA21150892}aquí{/a}."
        scene final_canonico
        with Dissolve(.5)
        with Pause(1)
        narrator ""
        jump game_end
    if in_order == False:
        label choice0_lab_death:
            narrator "Dembe al hacer las cosas mal en el laboratorio crea un caramelo en mal estado."
            narrator "Wonka al probar este dulce se pone de un tono pálido  como un papel y se desploma sobre la mesa cual saco de papas. Namomo corre a socorrerlo pensando que estaba muerto."
            show wonka at center
            wonka "Que es esta asquerosidad alguien va sufrir las consecuencias..."
            narrator "Namomo lo ayuda a levantarse y trata de acompañarlo a la salida."
            scene wonka_lab_death
            with Dissolve (.5)
            play music bang_w noloop volume 4.0
            narrator "Al tratar de bajar por las escaleras estos se tropiezan. Lo cual hace que el chocolatero, ya débil  por el dulce, ruede por las escaleras y muera."
            jump choice0_game_continue
        label choice0_tv_death:
            narrator "Dembe está subiendo una televisión, este se desconcentra con una mosca y deja de hacer lo que estaba haciendo."
            play music bang_w noloop volume 4.0
            narrator "Esto hace que la televisión golpee a Wonka, haciéndolo volar por los aires, luego de una grácil pirueta cae de pie sobre el borde de una de las TVs."
            narrator "Este asombrado por haber caído de pie, se resbala y cae de cabeza hacia el piso. Pasan unos segundo y comienza a intentar levantarse."
            show namomo at center
            namomo "¿Qué pasó allá atrás?"
            scene wonka_tv_death
            with Dissolve(.5)
            play music bang_w_2 noloop volume 4.0
            narrator "Namomo al ver esto suelta lo que estaba sosteniendo y segundos después otra TV procede a rematar a nuestro querido chocolatero cual mosca."
            jump choice0_game_continue
        label choice0_nut_death:
            narrator "Dembe al asegurar las cadenas de las ratas se olvida de asegurar una de ellas. Esta se escapa y decide que no hay mejor lugar que ir a meterse en los pantalones de Wonka."
            play music bang_w noloop volume 4.0
            narrator "Esto lo desestabiliza, lo hace caer en al agujero y se sostiene con todas sus fuerzas para no terminar lleno de suciedad."
            wonka "¿El que me venga a rescatar tiene premio!"
            narrator "Namomo, ajeno a la situación que se está viviendo en la sala central del basurero, está moviendo un pequeño pero muy pesado bloque de malvavisco duro que salió mal."
            scene wonka_nut_death
            with Dissolve(.5)
            play music bang_w_2 noloop volume 4.0
            narrator "Al lanzarlo por los ductos hacia el agujero donde está Wonka, el chocolatero es asesinado al instante"
            jump choice0_game_continue

    scene ww room
    show namomo at decisionL
    show dembe_pre at decisionR

    menu:
        namomo "¿A que sala deberiamos de ir?" 

        "Ir a la sala de laboratorios":
            jump choice0_lab

        "Ir a la sala de televisores":
            jump choice0_tv

        "ir a la sala de basurero":
            jump choice0_nut

    label choice0_lab:
        if(lab_flag):
            scene ww room
            show namomo at midLeft
            show dembe_pre at midRight
            dembe "Ya pasamos por este cuarto tonto, no tenemos tiempo para perder"
            jump choice0_done
        else:
            $ in_order_number = 0
            label lab_pac_ins:
            scene lab room
            $ lab_flag = True
            if in_order_number == 5: #if todo bien
                show namomo at midLeft
                show dembe_pre at midRight
                python:
                    choice0_rooms_count()
                if room_count<3:
                    namomo "Ya hicimos todo lo que teniamos que hacer en este cuarto, vamos al siguiente"
                jump choice0_done
            call screen lab_pac #point and click
            if in_order == False:
                jump choice0_lab_death
    
    label choice0_tv:
        if(tv_flag):
            scene ww room
            show namomo at midLeft
            show dembe_pre at midRight
            dembe "Ya pasamos por este cuarto tonto, no tenemos tiempo para perder"
            jump choice0_done
        else:
            $ in_order_number = 0
            label tv_pac_ins:
            scene tv room
            $ tv_flag = True
            if in_order_number == 5: #if todo bien
                show namomo at midLeft
                show dembe at midRight
                python:
                    choice0_rooms_count()
                if room_count<3:
                    namomo "Ya hicimos todo lo que teniamos que hacer en este cuarto, vamos al siguiente"
                jump choice0_done
            call screen tv_pac #point and click
            if in_order == False:
                jump choice0_tv_death

    label choice0_nut:
        if(nut_flag):
            scene ww room
            show namomo at midLeft
            show dembe at midRight
            dembe "Ya pasamos por este cuarto tonto, no tenemos tiempo para perder"
            jump choice0_done
        else:
            $ in_order_number = 0
            label nut_pac_ins:
            scene nut room
            $ nut_flag = True
            if in_order_number == 5: #if todo bien
                show namomo at midLeft
                show dembe at midRight
                python:
                    choice0_rooms_count()
                if room_count<3:
                    namomo "Ya hicimos todo lo que teniamos que hacer en este cuarto, vamos al siguiente"
                jump choice0_done
            call screen nut_pac #point and click
            if in_order == False:
                jump choice0_nut_death

    #  After death sequences game continues here...

    label choice0_game_continue:
    scene dark room
    with Dissolve (.2)
    narrator "Luego del suceso, nuestros Oompa-Loompas buscan la oficina de Wonka en busca de respuestas y encuentran los expedientes de 4 niños: Augustus, Veruca, Mike y Violet junto con el plan de los boletos de oro."
    narrator "En ese momento Namomo y Dembe se miran aterrorizados y desorientados."

    scene broken ww room
    with Dissolve(.5)
    show namomo sad at midLeft
    show dembe at midRight

    dembe "Él piensa… bueno pensaba conseguir un reemplazo"
    namomo "¡Pero son unos niños!"
    dembe "No te dejes llevar por la edad, si el trozo de carne este los selecciono deben ser iguales o peor que el.."
    namomo "Pero Dembe…"
    dembe "Es que tiene todo el sentido del mundo. Tuvo que haber alguna razón para seleccionarlos y seguro no fue porque eran unos santos."
    namomo "¿Y que vamos a hacer? Va a resultar extraño si no permitimos que entren."
    dembe "Hmmm… se me ocurren un par de cosas para hacer... Deberíamos reunir al resto, hay que hacer una votación. "
    show namomo disappointed at midLeft
    namomo "Puede que sea una buena idea."
    
    #los loompas salen de la oficina arastrando a wonka por el piso
    scene speaker closeup
    
    dembe "¡Queridos compañeros! Soy Dembe les pido a todos que paren lo que están haciendo y vengan a las barracas. Hay algo muy importante que discutir."
    namomo "¡Apúrense por favor!"

    scene loompas room
    show namomo at confront1
    show dembe at confront2
    show loompa1 at confront3
    show loompa2 at confront4 
    show loompa3 at confront5

    loompa1 "Para mi hay que negarles la entrada."
    loompa2 "¡No! Hay que escapar lo más rápido posible."
    loompa3 "Pero si hacemos eso van a saber que fuimos nosotros."
    dembe "¡Callense! Dejen hablar a los mayores. Hay 2 opciones, la primera es hacerles el tour normal y que se vayan tranquilos pero vamos a tener que seleccionar a un nuevo dictador {i}ejem{/i} nadie quiere eso {i}ejem{/i} y la segunda, mi favorita por cierto, es asesinarlos antes de que nos puedan tocar un pelo."

    # Namomo mira a Dembe aterrorizado.
    show namomo sad at confront1
    namomo "¡Dembe! ¡Son niños!"

    dembe "¡Niños dicen! Los estuve investigando un poco y miren lo que encontré. "
    show namomo at confront1
    #Aparecen 4 diapositivas con info de los niños. hover screen o scene. popup proyecto screen
    dembe "{i}Augustus{/i}: Un niño obeso y con serios problemas mentales. Adicto al azúcar y, al igual que a toda su familia, a maltratar animales. Un carnicero cualquiera para variar. Y les aseguro que nosotros no somos personas para él."
    dembe "{i}Violet{/i}: Una niña arrogante y vanidosa. Lo único que le importa es su cuerpo y mascar chicle. Le gusta practicar kickboxing y nosotros somos una {b}gran{/b} bolsa de boxeo."
    dembe "{i}Veruca{/i}: Otra niña arrogante pero en este caso aparte es suuuuper rica. La niña mimada de papá. Su padre le enseña a usar a otros para conseguir sus objetivos. Ya sea por las buenas o por las malas. Ella nunca nos verá como iguales sino como sus esclavos."
    dembe "{i}Mike{/i}: Un adicto a los videojuegos violentos. Bastante descriptivo para ser honesto. Disfruta de disparar, rebanar y mutilar monstruos y personas por igual. A mis ojos él es el peor de todos."
    show namomo sad at confront1
    namomo " ¡Eso no prueba nada! Siguen siendo niños pueden cambiar, les queda toda una vida por delante. No podemos matarlos."
    namomo "¡No es justo para ellos!. No somos así. Los Oompa Loompas no matamos."
    dembe "Me parece que es hora de votar. Los que estén a favor de matarlos a todos que levanten la mano y los que no lo estén que se queden como están."
    show namomo cry at confront1
    narrator "La sala lentamente se llena de manos levantadas y Namomo estalla en llanto."
    namomo "Como pueden ser así, solo niños, no somos monstruos. Me niego a hacer esto."
    loompa1 "Tienes razón pero no podemos permitir que nos sigan explotando."
    loompa2 "Son niños pero elegidos por el mismísimo diablo."
    namomo "En eso tienen razón… quizás sea la única opción. Además la votación ya está hecha… no hay vuelta atrás."

    #animacion de salida de namomo 

    scene dark room
    namomo_inner_dialogue "No puedo dejar que hagan esto."

    scene loompas room
    show dembe at confront2
    show loompa1 at confront3
    show loompa2 at confront4
    show loompa3 at confront5

    dembe " Y bueno se fue... no tengo ganas de traerlo otra vez. Ahora propongo que dos de nosotros controlemos a Wonka como si fuese un títere. ¿Alguna otra idea revolucionaria? "
    loompa1 "..."
    dembe "¿No?"
    loompa3 "..."
    dembe "Bueno haremos eso."
    scene end chap 1
    with Dissolve (1)
    with Pause(1)
    scene factory gate
    with Dissolve (.5)
    show veruca at cuartos1
    show augustus at cuartos2
    show violet at cuartos3
    show mike at cuartos4

    narrator "Están los 4 chicos esperando en la puerta principal para entrar a la fábrica."
    narrator "Las rejas se abren de par en par dejando entrar así a los invitados."
    #animacion de entrada
    narrator "De pronto mientras se cierran las puertas aparece corriendo un quinto chico que nadie esperaba con su boleto dorado."
    charlie "¡No cierren la puerta que falto yo! Aaaaaah"
    #animacion de charlie
    #animacion show de bienvenida
    scene factory entrance
    show charlie at quintos1
    show veruca at quintos2
    show augustus at quintos3
    show violet at quintos4
    show mike at quintos5

    wonka "Hola mier... ''estrellitas'', el mundo les dice hola."
    hide charlie
    hide veruca
    hide augustus
    hide violet
    hide mike
    narrator "Los niños se ven recibidos por un espectaculo de bienvenida..."

    scene factory fire
    with Dissolve (0.5)
    narrator "Por mala suerte este rapidamente se incendia y arruina."
    show wonka burn at center
    wonka "Les doy la bienvenida a mi fábrica, por favor acérquense y entren a mi {i}maravilloso{/i} mundo. Y tengan cuidado con el fuego ya que {i}nadie{/i} querría salir lastimado. "
    scene factory small door
    narrator "Todos se adentran en la fabrica siguiendo un gran pasillo que terminan chocando con una pequeña puerta. La mayoria miran con desconfianza."
    show wonka puppet at center
    wonka "Es asi para mantener mis secretos encondidos dentro. Jejejeje. Denme un minuto."
    narrator "El chocolatero se pone cuerpo a tierra para abrir la puerta. Esta se abre junto a toda la pared y se ve un destello de luz."
    scene bright room
    with Dissolve(.7)
    #acto 2 image

    scene chocolate room main
    narrator "Entran en una sala que pareciera un paisaje del mundo exterior. Un campo lleno de cesped y lo que parecieran arboles, pero la diferencia es que todo estaba hecho de dulces."
    show augustus at center
    augustus "Wooo... ¿Es esto el cielo?"   #augustus asombrado
    show augustus at midLeft
    show wonka puppet at midRight
    wonka_puppet "¡E-Esperen! Pueden elegir, comer, hacer cualquier cosa en esta habitación, pero manténganse alejados del río de chocolate."  #wonka advierte sorprendido
    wonka_puppet "No queremos ningún 'niño' en nuestros chocolates, ¿verdad? No saben muy bien... ¡Jaja!."
    #El grupo simplemente miró al hombre con la risa incómoda antes de continuar cada uno con su propio espectáculo turístico en esta extraña cámara.
    wonka_puppet "Jajajajaja..."
    narrator "Pero Augustus tenía otros planes..."
    scene chocolate backroom
    with Dissolve(.5)
    narrator "Mientras tanto, Namomo y Dembe discutían sus planes, mientras los otros Oompa-Loompas comenzaban su trabajo para deshacerse de uno de los niños, en este caso, Augustus"
    show namomo at midLeft
    show dembe at midRight
    with Dissolve (.3)
    dembe "Hasta ahora todo va bien, ¿verdad, Namomo? Ese gordito está cayendo directo en nuestra trampa y sin esfuerzo. ¡Ja! Debo verificar si la máquina está lista en este momento..."
    show namomo sad at midLeft
    namomo " ¿Todavia estas seguro sobre la idea de matar niños? ¿No te carcome ni un poco la conciencia?" #angustiado
    dembe "No."
    show dembe happy at midRight
    dembe "Siendo honesto lo estoy disfrutando y mucho. ¿Y tu no tendrias que estar haciendo algo para ayudar?"
    show namomo at decisionL
    show dembe at decisionR
    
    menu:
            namomo_inner_dialogue "Tengo que evitar que esto suceda, pero ¿cómo?"

            "Verificar la máquina":
                jump choice1_machine

            "¿Dónde esta Augustus?":
                jump choice1_augustus
            
            "No hacer nada":
                $ augustus_dead = True
                jump choice1_do_nothing

    label choice1_machine:
        dembe "¡Oh, buena idea! No tardes mucho, ¡o te perderás el espectáculo, je~!"  #sonrisa desagradable
        #namomo sube una escalera hacia una colina
        narrator "El lugar estaba lleno de Oompa-Loompas corriendo, tratando de poner la máquina en funcionamiento para completar su tarea más importante hasta ahora: una que Namomo quería detener."
        #PAC machine
        scene pipes puzzle up
        show screen machine_closeup_pac
        narrator "{i}¡Debo abrir la valvula correcta o alguien saldra lastimado!{/i}"
        
        
    label choice1_do_nothing:
        scene chocolate backroom
        dembe "Jaja, nuestro plan es infalible."
        #Namomo y Dembe se ponen en posición para el espectaculo.
        label choice1_kill_convergence:
            hide screen machine_closeup_pac
            hide screen find_augustus_pac
        scene chocolate river
        show augustus at center
        narrator "Mientras tanto, el chico seguía alejándose del camino acordado, hacia el parche de césped más cercano que conducía al cuerpo de chocolate líquido. Su deseo estaba a punto de hacerse realidad."
        narrator "Cada pequeño paso que daba hacia el río, Augustus sentía que este lo llamaba más y más, y cada segundo parecía ralentizarse mientras se arrodillaba frente a él. Sus manos descendieron al {i}agua{/i}, sintiéndola viscosa entre sus dedos, y la llevó de vuelta a su boca."
        show augustus speak at center
        augustus "¡Por dios!"
        augustus "El sabor... La textura... El calor... Las sensaciones... Todo es increible, es un sueño echo realidad."
        narrator "El sentimiento era increible y poco a poco se fue sumergiendo mas y mas en el liquido"
        scene chocolate room main
        show charlie surprised at midLeft
        show wonka puppet at midRight
        charlie "¡Señor Wonka, Augustus cayo al río!" #charlie alarmado
        scene swimming aug1
        play music aSplash noloop volume 2.0
        narrator "Augustus se encontraba dando vueltas en litros de chocolate líquido. Para un chico que ni siquiera sabía nadar en agua, no había esperanza de sobrevivir en un río de cacao"
        augustus "¡A-Ayuda! ¡Ayúdenme!"
        scene swimming aug2
        narrator "Mientras Augustus seguía intentando con todas sus fuerzas librarse de las consecuencias de sus acciones, Charlie y Wonka se apresuraban al otro lado del Puente Eructante, podían oír que alguna especie de maquinaria..."
        scene chocolate scooper
        narrator "Una máquina tan masiva que todos simplemente la miraban maravillados por su tamaño, excepto los Oompa-Loompas, quienes ya sabian lo que se avecinaba."
        scene chocolate room main
        show wonka puppet at midLeft
        show veruca at midRight
        play music augustus_song fadein 1.0 noloop volume 2.0
        narrator "Poco a poco empezo un zumbido ritmico y musical, venia de los Oompa-Loompas que dejaron su trabajo regular y se unieron para cantarle algo a los visitantes."
        veruca "¿Qué están haciendo?" #expresion desagradable
        wonka "Parece que quieren que escuchemos una pequeña canción~"
        #Inserta "Augustus Gloop" de Danny Elfman
        scene chocolate scooper
        narrator "La enorme pieza de maravilla electrónica comenzó a absorber enormes cantidades de chocolate en el río, y con él, a Augustus mismo."
        narrator "Augustus se encontró siendo arrastrado hacia un remolino de cacao antes de ser propulsado por la tubería de plástico, hasta que... quedó atascado"
        narrator "El flujo de chocolate se detuvo, por su cuerpo que bloqueaba el paso del líquido."
        narrator "Mientras los Oompa-Loompas bailaban, cantaban y se reían de este niño. Augustus sentiría cómo el tubo de plástico a su alrededor comenzaba a apretarse cada vez más, hasta que de repente..."
        if machine_path_good:
            jump choice1_machine_lives
        augustus "Eh... ¿Alguien puede sacarme de a-"
        stop music
        play music augustus_chomp noloop volume 2.0
        narrator "La máquina comenzo a succionar más fuerte que nunca, de repente se aceleró y desgarró el cráneo del niño de su cuerpo, junto con sus hombros y brazos, arrojándose dentro de la máquina."
        scene chocolate room main
        show violet at center 
        violet "Oh."
        #chocolate  de la maquina teñido de rojo carmesi
        show namomo cry at quintos1
        namomo "Esta..."
        show charlie surprised at quintos5
        charlie "Muerto..."
        hide charlie
        hide namomo
        hide violet
        show wonka puppet at midRight
        show mike happy at midLeft
        mike "Sí, como en una mortalidad de Fatal Fight. ¡Muy bueno, Sr. W!" #mike sonrie
        #animacion el cuerpo de augustus sube a travez del tubo
        jump chapter_2half_start


    label choice1_augustus:
        scene chocolate backroom
        dembe "¿Eh? Oh, tienes razón. ¿Dónde fue ese chico...?"
        scene chocolate forest
        show screen find_augustus_pac
        python:
            generate_random_hide_place()
        narrator "{i}Debo encontrarlo antes que dembe, o sino...{/i}"

    label choice1_machine_lives:    #machine pac augustus lives
        scene chocolate scooper
        #''(¡RUIDOS REPENTINOS DE PARADA DE LA MÁQUINA!)''
        narrator "La sala se vio inundada por el silencio. Ni siquiera los Oompa-Loompas seguían cantando, todos miraban al niño atrapado en el tubo, su rostro cubierto de chocolate pasando de la desesperación a..."
        narrator "¿Incomodidad..?"
        augustus "Eh... ¿Alguien puede sacarme de aquí?"#incomodidad
        stop music   
        namomo "Oh, gracias a Dios..." #susurro -- Augustus escupido en cesped
        jump chapter_2half_start
    label choice1_found_lives:   #machine pac augustus lives
        hide screen find_augustus_pac
        unknown "¡Agarra la cuerda!"
        unknown "Vamos... Ya casi..."
        show namomo at midLeft
        show augustus at midRight
        narrator "El rescatador resultó ser el propio Namomo, su pequeño cuerpo anclado en la tierra intentando sacar a la enorme masa del río de chocolate, ¡antes de que el Scooper pudiera apoderarse de él!"
        narrator "Finalmente, luego de muchas luchas, el niño logró llegar a un lugar seguro, aunque todo cubierto de chocolate, tosiendo trozos de cacao líquido en el césped, antes de agradecer débilmente a Namomo, hasta que finalmente se rindió por agotamiento..."
        augustus "Gracias enano..."
        jump chapter_2half_start


    label chapter_2half_start:
        scene factory small door
        with Dissolve (.5)
        show wonka at midRight
        wonka_puppet "Bien... ¿Continuamos ahora?"#sonrisa siniestra
        if augustus_dead == True:
            show charlie surprised at midLeft
            charlie "Pe... pe... pero acaba de... de... de morir Augustus.  ¿Co... co... como pueden estar ta... ta... tan tranquilos todos?"
            narrator "Namomo se ve en la nesecidad de empujar a Charlie para que pueda seguirle el paso al grupo"
        else:
            hide wonka
            show augustus at midRight
            show charlie at midLeft
            charlie "¿Estás bien?"
            augustus "Obvio que estoy bien. No podría estar mejor. Acabo de cumplir mi mayor sueño."
        scene lab room
        with Dissolve (.5)
        narrator "Tras la salida del ascensor el grupo se halla en un enorme salón con gran maquinaria es el llamado {i}laboratorio de dulces{/i}"
        narrator "Al entrar Namomo se encuentra con la tecla de la luz"
        menu:
            namomo_inner_dialogue "Deberia apagar la luz?"
            "Apagar":
                jump choice2_apagada_inter
            "Dejar prendida":
                $ light_on = True
                jump choice2_luz_status_end
            
        label choice2_apagada_inter:
            scene laboratory light_off
        menu:
            narrator "Las luces principales del laboratorio se apagan y queda iluminado por varias luces muy tenues, unas de las propias máquinas y otras en el techo."
            "Dejar luz apagada":
                $ light_on = False
                jump choice2_luz_apagada
            "Volver a prender la luz":
                jump choice2_luz_status_end
    label choice2_luz_apagada:
        narrator "Al grupo no parece molestarle el apagado de luces, en cambio los azulejos reflectivos de la sala le dan un aura semi fantastica, casi salida de otro mundo."
        jump choice2_luz_status_end
    label choice2_luz_status_end:
    if light_on:
        scene laboratory light_on
    else:
        scene laboratory light_off
    if augustus_dead:
        show wonka puppet at center
        show namomo at quintos1
        show dembe at quintos5
        narrator "Aqui Wonka acompañado de sus dos enanos personales les presenta los futuros dulces que aun se encuentran en fase de pruebas, entre ellos una barra de chocolate roja y grumosa"
        show dembe happy at quintos5
        with Dissolve(.3)
        charlie "¿Pe... pero qué es ese chocolate? ¿Qué es ese color rojizo?"
        wonka_puppet "Ups..."
        wonka_puppet "Mmm... No estoy seguro que este sea un color que estén listos para ver de nuevo"
        dembe "Por más rica que sea, los niños no están acostumbrados a ver algo tan grotesco, al menos no por ahora."
        hide wonka
        hide dembe
        hide namomo
        with Dissolve(.1)
    else:
        show augustus speak at midRight
        show charlie at midLeft
        with Dissolve (.3)
        augustus "Mira Charlie una barra roja y grumosa. ¿Tendrá sabor a carne o mejor aún, a carne de oompa-loompa? Jajaja"
        show charlie surprised at midLeft
        charlie "¿Qué estás diciendo? Eso sería asqueroso."
        show augustus at midRight
        augustus "Pero eso sería divertido como si Wonka los usará para cocinar... literalmente."
        show augustus speak at midRight 
        show charlie happy at midLeft
        charlie "Eso puede ser divertido... ja... ja... jaja"
    hide augustus
    hide charlie
    narrator "Entre las máquinas una llama la atención, una especie de tanque enorme con un Oompa Loompa nadando dentro inspeccionando unas bolas del tamaño de una canica, Wonka apretó un botón y salió una."
    show wonka puppet at midRight
    wonka_puppet "Estas son los nuevos rompemuelas perpetuos, capaces de hacer feliz a un niño por un año entero, especialmente para las familias pobres."
    show veruca happy at midLeft
    narrator "Veruca es incapaz de contenerse le parece fascinante ser capaz de consumir lo que la gente pobre, nunca había experimentado nada de ese estrato de la sociedad."
    narrator "Le da una lamida y al sentir el poderoso sabor se lo mete en la boca y muerde..."
    play music veruca_crack noloop volume 2.0
    show veruca surprised at midLeft
    narrator "{b}¡Crack!{/b}"
    narrator "La dentadura perfecta de veruca se ve arruinada, las paletas de veruca explotan en trizas y se siente un grito de susto que deja fríos a todos."
    show veruca cry at midLeft
    with Dissolve (.1)
    play music veruca_scream noloop volume 2.0
    veruca "¡Mis dientes!¡Le voy a tener que pedir a papá que me lleve al dentista!"
    wonka_puppet "Lo siento mucho pero eso debera esperar, nos queda mucho por explorar."
    hide wonka
    hide veruca
    if light_on==False:
        label nuclear_ending2:
        show nuclear_button at nuclear_button_placing
        narrator "Namomo algo perdido en la sala no tiene mejor idea que buscar la tecla de la luz y al encontrarse con un botón levemente iluminado piensa que es ese."
        namomo "¡Que se haga la luz!"   #grito exaltado
        narrator "Al presionar el botón se empiezan a prenden unas luces de emergencia."
        play music nuclear_alarm loop volume 2.0
        narrator "El silencio se ve rápidamente interrumpido y se empiezan a escuchar estruendosas alarmas. A travez del intercomunicador automático se una advertencia..."
        narrator"¡Peligro de fisión nuclear inminente!"
        narrator "Dembe recuerda a Wonka hablar sobre el sistema de refrigeración del reactor."
        narrator "Recuerda que la consola se encontraba en este mismo laboratorio."
        narrator "Recuerda que el apagado era controlado por un botón rojo."
        scene bright room
        with Dissolve(.5)
        namomo "No hay nada que hacer..."
        stop sound fadeout 1.0
        scene nuclear cloud
        jump game_end
    narrator "Antes de llegar a la próxima máquina el grupo se encuentra con una consola de comandos, arriba de ella un cartel que lee, {i}Control energético de la fábrica{/i}"
    menu:
        narrator "A un lado de la consola hay un botón rojo levemente iluminado."
        "Tocar el botón":
            jump luz_encendida_boton_press1
        "Ignorarlo":
            jump luz_encendida_boton_ignore
    label luz_encendida_boton_press1:
        menu:
            narrator "Al acercarse a tocarlo Dembe recuerda las palabras de Wonka sobre lo peligroso de desactivar el sistema de refrigeración del núcleo de energía de la fábrica, sólo un estupido lo haría con el sistema aún en funcionamiento."
            "Tocar el botón":
                jump luz_encendida_boton_press2
            "Ignorarlo":
                jump luz_encendida_boton_ignore
    label luz_encendida_boton_press2:
        menu:
            narrator "Los pensamientos lo invaden pero la racionalidad lo detiene una vez más, mala suerte que no prestó mucha atención a las explicaciones de wonka, el solo era un esclavo más, no lo considero importante."
            "Tocar el botón":
                jump luz_encendida_boton_press3
            "Ignorarlo":
                jump luz_encendida_boton_ignore
    label luz_encendida_boton_press3:
        scene laboratory light_off 
        narrator "Al presionar el botón toda la fábrica se ve invadida por la oscuridad y se prenden unas luces de emergencia."
        play music nuclear_alarm loop volume 2.0
        narrator "El silencio acaba y se empiezan a escuchar estruendosas alarmas. Un intercomunicador automático repite..."
        narrator "¡Peligro de fisión nuclear inminente!"
        scene bright room
        with Dissolve(.5)
        narrator "Tocar el botón resultó fatal, tan cerca de lograr la libertad se vio cegado por la idiotez, en sus últimos momentos Dembe se abraza con Namomo..."
        stop sound fadeout 1.0
        scene nuclear
        with Dissolve (1)
        with Pause(1)
        
        jump game_end
    label luz_encendida_boton_ignore:
    narrator "Namomo sigue al grupo a la proxima maquina."
    show wonka puppet at midRight
    wonka_puppet "Esta máquina es capaz de crear un chicle con el valor nutricional de una comida compuesta de entrada plato principal y postre, es el chicle más asombroso de todo el universo"#risa siniestra
    wonka_puppet "Con esta máquina se pueden replicar todas las comidas existentes.."
    #violeta feliz
    narrator "Violet siendo mascadora profesional de chicle se ve obligada a probarlo, quién sino ella?"
    show violet at decisionL
    violet "Quiero sopa de verduras, carne al horno con papas y tarta de arándanos"
    hide wonka
    with Dissolve(.1)
    menu:
        narrator "Dembe ya preparado pone la maquina a funcionar y ordena a Namomo agregar un sabor {i}especial{/i} a la salsa de arándanos"
        "Efervescente":
            jump choice3_efervescente
        "Inflammable":
            jump choice3_inflammable
        "Ácido":
            jump choice3_acido

    label choice3_efervescente:
        show violet happy at center
        narrator "Violet toma el chicle con rapidez y pone el que estaba mascando en ese momento detrás de su oreja, sería la primera persona en probar este grandioso invento."
        narrator "Ella, mascadora profesional le enseñaría a wonka como se hace un chicle de verdad."
        narrator "Procede a comenzar a mascarlo, se siente extasiada por la mezcla de sabores primero la sopa de verduras siente su boca como se calienta con el calor del caldo y puede nombrar todas las verduras que contiene."
        narrator "Luego sigue la carne perfectamente a punto acompañada por papas al horno crujientes y sabrosas y para el final la mejor parte, su postre favorito. Tarta de arándanos, pero había algo raro en ella..."
        show violet speak at center
        with Dissolve(.1)
        narrator "Al comenzar a sentir el sabor de la tarta también empieza a sentir malestar, como si estuviera tomando una gaseosa con sabor a arándanos."
        show violet angry at center
        with Dissolve (.1)
        narrator "Siente ardor en su garganta a más no poder, su estómago se empieza a inflar y desde su boca se empieza a esparcir un color violeta tiñendo de a poco su piel y todo mientras su cuerpo se inflaba mas y mas hasta quintuplicar su tamaño."
        show violet fat at center
        with Dissolve(.5)
        narrator "Violeta acaba por convirtiéndose en una bola gigante, tras esto aparece una tropa de 5 oompa loompas que dicen venir a ayudar a la niña pero la empujan hasta desaparecer tras un pasillo."
        hide violet
        with Dissolve(.1)
        narrator "En el siguiente instante se escucha un estruendo..."
        show violet prop at violet_flying
        play music ballon_pop noloop volume 2.0
        narrator "{b}¡Zas!{/b}"
        narrator "¡Violet explotó como una bolsa de chicles al abrirse!"
        show violet prop at violet_flyingR
        narrator "Su cuerpo salió disparado como un globo desinflándose dejando salir una lluvia violeta semi viscosa a su paso."
        show violet blob at violet_blob
        narrator "Finalmente acabo por desinflarse por completo y caer en el medio de la sala como un un pedazo de goma medio aplastada sin huesos ni forma, solo un cascarón de la niña malcriada que fue."
        scene end chap 2
        with Dissolve (1)
        with Pause(3)
        scene tbc
        with Dissolve(.5)
        with Pause(1)
        narrator ""

        jump game_end
    label choice3_inflammable:
        show violet happy at center
        narrator "Procede a comenzar a mascarlo, se siente extasiada por la mezcla de sabores primero la sopa de verduras siente su boca como se calienta con el calor del caldo y puede nombrar todas las verduras que contiene."
        narrator "Luego sigue la carne perfectamente a punto acompañada por papas al horno crujientes y sabrosas y para el final la mejor parte, su postre favorito. Tarta de arándanos, pero había algo raro en ella..."
        
        show violet angry at center
        with Dissolve(.1)
        narrator "Cuando empieza a saborear la tarta junto a ella su saliva se vuelve cada vez mas y mas espesa como viscosa y de un sabor repugnante, había algo mal con el chicle..."
        narrator "Rápidamente lo escupe en dirección a Dembe quien operaba la máquina mientras le empieza a gritar"
        play music violet_scream noloop volume 2.0
        violet "¿¡Que es este chicle que es esto que me hiciste comer!?"
        violet "¡¡¡Me quema la garganta!!!"
        show dembe at midRight
        violet "¡¡¡Si de verdad crees que esto es comestible comelo vos!!!"
        hide violet
        show charlie surprised at midLeft
        narrator "Dembe en su afán de sobrevivir ve una oportunidad es su momento asesinar a Charlie y fuerza el chicle es su boca con todas sus fuerzas pero no puede evitar tragar parte del líquido viscoso"
        hide dembe
        narrator "Charlie confundido con la situación deja que ocurra pero al saborearlo entra en crisis y repite el proceso"
        show mike angry at midRight
        hide charlie
        show veruca angry at midLeft
        narrator "Como reacción lo fuerza en la boca de Mike quien odia los dulces y solo el sabor lo hace vomitar en dirección a Veruca..."
        hide mike
        show namomo sad at midRight
        narrator "Veruca grita en asco y repugnancia y se lo saca quisquillosamente de la boca y lo coloca con toda su fuerza en la boca de Namomo"
        narrator "Namomo acepta el pesar de su destino con tristeza..."
        hide veruca
        if augustus_dead == False:
            show augustus happy at midLeft
            narrator "La gula le gana a Augustus y le saca por su cuenta el chicle a Namomo de la boca y lo come y traga el mismo"
        hide augustus
        hide namomo
        narrator "A medida que esta reacción se encadena, la situación empeora cuando la saliva se empieza a mezclar con los ácidos estomacales."
        scene ashes ending
        with Dissolve(.5)
        narrator "La reacción comienza a gestarse de a poco fundiendo sus extrañas con un calor infernal cada uno convirtiéndose en un horno por sí mismo y al final una gran hoguera hasta que solo quedo ceniza."
        scene final_inflamable
        with Dissolve(.5)
        with Pause(1)
        narrator ""
        jump game_end
    label choice3_acido:
        show violet happy at center
        narrator "Procede a comenzar a mascarlo, se siente extasiada por la mezcla de sabores primero la sopa de verduras siente su boca como se calienta con el calor del caldo y puede nombrar todas las verduras que contiene."
        narrator "Luego sigue la carne perfectamente a punto acompañada por papas al horno crujientes y sabrosas y para el final la mejor parte, su postre favorito. Tarta de arándanos, pero había algo raro en ella..."
        show violet speak at center
        with Dissolve(.1)
        narrator "Cuando violeta llega a la tarta siente algo extraño,¿Acido?"
        narrator "Como puede su postre favorito saborear tan mal, sentir algo tan horrible solo la disgusta escupe el chicle y va rápidamente a gritarle al operador de la máquina."
        show violet angry at center
        with Dissolve (.1)
        violet "¿Porque son tan ácidos los arándanos?"
        violet "Sentí como si alguien echara limón en mi lengua es simplemente asqueroso"
        show namomo sad at midLeft
        with Dissolve(.3)
        namomo "Lo siento mucho esta maquina aun esta en prueba y aún no están perfeccionados los sabores"
        scene end chap 2
        with Dissolve (1)
        with Pause(3)
        scene tbc
        with Dissolve(.5)
        with Pause(1)
        narrator ""
        jump game_end



    # This ends the game.
    label game_end:
    return