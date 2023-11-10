import random
import time


class Character:
    name = None
    description = str()
    agi = 0
    strength = 0
    health = int()
    weapon = (0, 0, None)
    key = False

    def take_hit(self, hit, dmg=int()):
        if hit >= 10 + self.agi:
            self.health = self.health - dmg

    position = int
    target = None  # character

    def take_weapon(self):
        tmp = self.weapon
        self.weapon = None
        return tmp

    def take_key(self):
        if self.key & self.health < 1:
            self.key = False
            return True


class Guard(Character):
    weapon = (0, 8, "Pistola de Plasma")
    agi = 3
    chase = False


class Rat(Character):
    strength = 2
    weapon = (4, 4, "Vidrio con trapo")
    question = 11 * random.randint(1, 10)
    answer = None


class Player(Character):
    dymorph = None # X False Y True
    agi = 4
    strength = 1
    rod = False


class Room:
    connections = (None, None, None, None)
    name = ""
    description = ""
    key = None
    bar = None
    move_description = ""

    trigger = None  # Function

    def __init__(self, n, d, md):
        self.name = n
        self.description = d
        self.move_description = md

class Scene:
    pc = Player()
    guards = [Guard()]
    splint = Rat
    map = [Room]
    def map_build(self):
        self.map.append(
            Room("Celda", "una celda futurista con barrotes de aluminio, sin vistas, pero buena seguridad y alquiler barato",
                 "al Sur de la celda la puerta está rota"))
        self.map.append(Room("Pasillo C1", "pasillo que hace esquina delante de una celda cerrada, más limpia que la tuya.",
                        "se puede ir hacia el Sur y Este a traves de sendas puertas"))
        self.map.append(Room("Pasillo C2", "cruce de pasillos delante de tu acogedora celda",
                        "tu celda al Norte, y un pasillo en cada otra dirección"))
        self.map.append(Room("Pasillo C3",
                        "cruce de pasillos delante de una celda que emite un olor hediondo, una masa de carne informe se mece en una esquina",
                        "los pasillos continuan al Sur, Este y Oeste"))
        self.map.append(Room("Acceso Seguridad",
                        "el pasillo más próximo al Centro de seguridad. Si quiero una muerte rápida y dolorosa debería acercarme a saludar",
                        "se puede continuar al Centro de Seguridad hacia el Este o volver hacia los pasillos al Oeste"))
        self.map.append(Room("Centro de Seguridad",
                        "están limpiando los restos calcinados de mi amigo de encima de una mesa, los guardias se voltean al verme, junto con dos enormes torretas láser que cuelgan del techo. Buenos días, caballeros.",
                        ""))
        self.map.append(Room("Pasillo E2", "", ""))
        self.map.append(Room("Habitación derrumbada", "", ""))
        self.map.append(Room("Habitación E4", "", ""))
        self.map.append(Room("Pasillo E4", "", ""))
        self.map.append(Room("Pasillo Garita", "", ""))
        self.map.append(Room("Habitación E1", "", ""))
        self.map.append(Room("Suministros", "", ""))
        self.map.append(Room("Agujero Splinter", "", ""))
        self.map.append(Room("Tunel 1", "", ""))
        self.map.append(Room("Tunel 2", "", ""))
        self.map.append(Room("Cápsula de Escape Innacesible", "", ""))
        self.map[0].connections = (None, 2, None, None),
        self.map[1].connections = (None, 6, 2, None)
        self.map[2].connections = (0, 8, 3, 1)
        self.map[3].connections = (None, 9, 4, 2)
        self.map[4].connections = (None, None, 5, 3)
        self.map[5].connections = (None, None, None, 4)
        self.map[6].connections = (1, 10, -7, None)
        self.map[7].connections = (None, 11, 8, 6)
        self.map[8].connections = (2, 12, -9, 7)
        self.map[9].connections = (3, None, None, 8)
        self.map[10].connections = (6, 14, -11, None)
        self.map[11].connections = (7, None, 12, -10)
        self.map[12].connections = (8, 15, 13, 11)
        self.map[13].connections = (None, 16, None, 12)
        self.map[14].connections = (10, None, 15, None)
        self.map[15].connections = (12, None, None, 14)
        self.map[16].connections = (13, None, None, None)

    def intro(self):
        print("Bienvenido a Python Mini Crawler.")
        self.print_type(("\n\nAbres los ojos y es otro ciclo más en la esquina del espacio donde quiera que estés metid{}. ".format("o" if self.pc.dymorph else "a")),
                        "En una celda cuyo beige inerte envuelve tu mirada en todas direcciones. Todas, salvo en la dirección que\n",
                        "tu implante indica como ANTInormal, donde hay una capa polimérica que nos mantiene encerrados. Tanto a tí como a Greg.\n",
                        "\n\t[<Humano> Greg]:\tSabes, estuve pensando en todo el tema del racismo este intelectual y la amnistía de la experimentacion,y al fin y al cabo,\n\t",
                        "creo que esto es, si no, una oportunidad para que podamos optar a trabajos para los que la raza humana originalmente no está capacitada,\n\t",
                        "tenemos los implantes y tal, pero ya sabes, siempre se van quedando obsoletos, y quien rechazaría un cerebro bioelectrónico con refrigeracion mejorada?\n\t",
                        "Nadie, si lo piensas un poco.\n")
        choice=self.print_choice("\n\t[<Yo> {}]\n".format(self.pc.name),
                     "\t\t\t[1]Cállate Greg, no, hasta que no tenga cafeína.\n\t\t\t[2]Tienes razón, además todas esas cosas son algo caras. Son "+
                     "todo ventajas\n\t\t\t[3]Tu crees que nos van a tratar decentemente? Ni siguiera tienen esterilizadores "+
                     "multiespectro en las celdas. Sólo uno de partículas alfa casi gastado.\n")
        self.print_type("Greg se queda pensativo en la esquina junto a la membrana.\n\n"+
                   "Tras unos instantes lo que parece un xeno con unas garas negras y afiladas desciende amenazante desde el techo,\n"+
                   "mostrando una boca recursiva de dientes hambrientos, mientras el chip de la base de tu craneo hace su trabajo dando significado\n"+
                   "a los sonidos chasqueantes que emite esta criatura.\n"+
                   "\n\t[<Xeno> 983812]\tGomiiiiisss, tu dar gomiinoollaassss..\n\n"+
                   "Instantes despues y tras un breve destello, el cuerpo sin vida del xeno se desploma en el pasillo mientras se encoje sobre si mismo.\n"+
                   "\n\t[<Guardia> Nbei]\tOtra vez las putas plagas, estoy hasta los cojones de ellas. \n\tSe están comiendo las barras de proteínas de los especímenes."+
                   "Vamos a tener que encargar un kit de bacterias come-xenos otra vez.\n\n"+
                   "A Greg se le ilumina su greñoso rostro y ojeras causadas de la locura transitoria sobre la que se estaba hundiendo lentamente "+
                   "y se abalanza sobre la membrana,\ncuerpo desnudo presionándola y flexionandola suavemente.\n"+
                   "Ante esta terrorífica visión de un humano desnudo, con sus flagelos extendidos y con sus 6 extremidades "+
                   "contra la membrana de contención,\nel pobre Nbei reacciona disparando su lanzador de plasma hacia el humano"+
                   " Greg, perforando la membrana y seccionando el brazo derecho.\n"+
                   "\n\t[<Guardia> Nbei]\tMierda, mierda, mierda, la primera vez que conseguimos unos humanos y ya rompo uno. Tengo "+
                   "que ver si estos les vuelven a crecer o no.\n\tTu, sé buen human{} y quédate en tu camita, ahora vengo.\n\n".format("o" if self.pc.dymorph else "a")+
                   "Dicho eso, el guardia, bastante más pequeño que Greg, se lo coloca encima sangrante y desmayado y se marcha por la compuerta hacia PROgrado.")


    def print_type(self,*texts):
        for text in texts:
            for char in text:
                print(char, end="")
                if char == " ":
                    time.sleep(0.2)
                if char == "\n":
                    time.sleep(0.75)
                if char == ",":
                    time.sleep(0.4)
                if char == ".":
                    time.sleep(.6)
                if char == ":":
                    time.sleep(1.0)
    def print_choice(self,title,*texts):
        print(title, end="")
        self.print_type(texts)
        inp = input("\t\t\t[?]:")
        print("\r"+" "*texts.__len__()) # Borra las opciones para poner el resultado

    def initialization(self):
        self.pc = Player()
        self.splint = Rat()
        self.guards.append(Guard())
        self.guards.append(Guard())
        self.splint.position = 12
        self.guards[0].position = 10
        self.guards[1].position = 3
        self.pc.position = 0
        print("Escoja Cromosoma [X|Y]")
        while self.pc.dymorph is None:
            option = input("[?]:")
            option = option.lower()
            self.pc.dymorph = True if option=="y" else False if option=="x" else None
        print("Escoja Identificador Alfafónico [Nombre]")
        while self.pc.name is None:
            option = input("[?]:").capitalize()
            self.pc.name = option if option != "" else None

#     def turn(self):
#         detection()
#         npc_target()
#         narrate_room()
#         narrate_room_items()
#         narrate_characters()
#         load_actions()
#         take_npc_action()
#         narrate_action()
#         take_player_actions()
#         move_player()
#         move_npc()
#         if player.health>0 : return 1
#         else : return 0
# if __name__ == '__main__':
def main():
    # Generación
    s = Scene()
    s.map_build()
    s.initialization()
    # print("la respuesta a la pregunta de splinter es:{}".format(c_splinter.question))
    s.intro()
    # Turno
    # while out>0 :
    #     out=turn(pc)
    # gameover()
    return 0


main()
