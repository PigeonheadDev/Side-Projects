#VAGUE-PREFIX-LOCATION-DUNGEON-SUFFIX
import random

vague_list = ["Mystery", "Hidden", "Lovely", "Sacred", "Dragon", "Sky", "Apple", "Spiral", "Oblivion", "Crystal", "Dark", "Light", "Highwind", "Thunder", "Sexy", "Moon", "Domination", "Ass", "Inescapable", "Night", "Day", "Eclipse", "Melody", "Dilemma", "Pursuit", "Sunstroke", "Illusion", "Zero", "Lonely", "Skyhigh", "Trillionage", "Mushroom", "Stormswept", "Foreboding", "Agonizing", "Blistering", "Fiery", "Steam", "Burning", "Powder", "Howling", "Division", "Pegasus", "Strike", "Solar", "Lunar"]
prefix_list = ["Small", "Tiny", "Humongous", "Super", "Horrific", "Isle of", "Northern", "Eastern", "Western", "Southern", "Northeast", "Northwest", "Southeast", "Southwest", "Deep", "Miracle", "Great", "Massive", "Far-Off", "Buried", "Silver", "Golden", "Moonlit", "Forbidden", "Blue", "Sunken", "Unseen", "Frozen", "Black", "Divine", "Godkiller", "Nameless", "That Fuckin'", "Forlorn", "Lost", "Ancient", "Tall", "Bad Choice", "Poor Man's", "Reaper's", "Wartorn", "Seaside", "Shady", "Monster's", "Hazy", "Gently Weeping", "That", "Those", "Desecrated", "Revered", "Vile", "Waking", "Spacebound", "Earthbound", "Paralyzed", "Calamitous", "Perfect", "Devil's", "Clown's", "Nonsensical", "Another", "Sinful", "Lyon's", "Pallas", "The First", "The Second", "The Third", "The", "Central"]
location_list = ["Island", "Beach", "Waterfall", "Sea", "Land", "Glacier", "Savannah", "Shoal", "Overlook", "Swamp", "Marsh", "Desert", "Canyon", "Mountain", "Highland", "Garden", "Shore", "Tunnel", "Valley", "Mesa", "Volcano", "Forest", "Cave", "Cavern", "Riverbank", "Meadow", "Prairie", "Coast", "Wilderness", "Orchard", "Peak", "Shore", "Peninsula", "Rainforest"]
dungeon_list = ["Pit", "Abyss", "Wasteland", "Jail", "Spring", "Oasis", "Gorge", "Ruins", "Maze", "Gate", "Road", "Relic", "Crevice", "Hollows", "Dune", "Lookout", "Ravine", "Precipice", "Palace", "Tower", "Chasm", "Shrine", "Hill", "Fortress", "City", "Arena", "Way", "Path", "Ridge", "Underpass", "Field", "Pass", "Trail", "Colosseum", "Palm", "Cistern", "Shack", "Pizzeria"]
suffix_list = ["of Despair", "of Wonders", "of Spirits", "of Magic", "of Desolation", "of Masters", "of Gemstones", "By The Sea", "of Tyrants", "of Extinction", "of Wishes", "of Regrets", "of Pain", "of Deceit", "of No Return", "of Strength", "That Never Was", "of The Lost", "of Creation", "of Love", "of Disaster", "of Tomfoolery", "of Lust", "In The Reverse World", "of Good Times", "With Your Mom", "of Clowns", "Zero", "North", "South", "East", "West", "That May Be"]

vague_name = "ERROR"
prefix_name = "ERROR"
location_name = "ERROR"
dungeon_name = "ERROR"
suffix_name = "ERROR"

def find_name():
  config = random.randrange(1,21)
  match config:
    case _ if config < 3:
      namePL()
    case _ if config < 5:
      namePD()
    case _ if config < 6:
      namePLS()
    case _ if config < 7:
      namePDS()
    case _ if config < 9:
      nameVL()
    case _ if config < 11:
      nameVD()
    case _ if config < 12:
      nameVLS()
    case _ if config < 13: 
      nameVDS()
    case _ if config < 15:
      nameLD()
    case _ if config < 16:
      nameLDS()
    case _ if config < 18:
      nameLS()
    case _ if config < 20:
      nameDS()
    case _ if config == 20:
      nameALL()

def namePL():
  prefix_name = prefix_list[random.randrange(1,len(prefix_list))]
  location_name = location_list[random.randrange(1,len(location_list))]
  print(prefix_name, location_name)
def namePD():
  prefix_name = prefix_list[random.randrange(1,len(prefix_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  print(prefix_name, dungeon_name)
def namePLS():
  prefix_name = prefix_list[random.randrange(1,len(prefix_list))]
  location_name = location_list[random.randrange(1,len(location_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(prefix_name, location_name, suffix_name)
def namePDS():
  prefix_name = prefix_list[random.randrange(1,len(prefix_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(prefix_name, dungeon_name, suffix_name)
def nameVL():
  vague_name = vague_list[random.randrange(1,len(vague_list))]
  location_name = location_list[random.randrange(1,len(location_list))]
  print(vague_name, location_name)
def nameVD():
  vague_name = vague_list[random.randrange(1,len(vague_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  print(vague_name, dungeon_name)
def nameVLS():
  vague_name = vague_list[random.randrange(1,len(vague_list))]
  location_name = location_list[random.randrange(1,len(location_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(vague_name, location_name, suffix_name)
def nameVDS():
  vague_name = vague_list[random.randrange(1,len(vague_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(vague_name, dungeon_name, suffix_name)
def nameLD():
  location_name = location_list[random.randrange(1,len(location_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  print(location_name, dungeon_name)
def nameLDS():
  location_name = location_list[random.randrange(1,len(location_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(location_name, dungeon_name, suffix_name)
def nameLS():
  location_name = location_list[random.randrange(1,len(location_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(location_name, suffix_name)
def nameDS():
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(dungeon_name, suffix_name)
def nameALL():
  vague_name = vague_list[random.randrange(1,len(vague_list))]
  prefix_name = prefix_list[random.randrange(1,len(prefix_list))]
  location_name = location_list[random.randrange(1,len(location_list))]
  dungeon_name = dungeon_list[random.randrange(1,len(dungeon_list))]
  suffix_name = suffix_list[random.randrange(1,len(suffix_list))]
  print(vague_name, prefix_name, location_name, dungeon_name, suffix_name)

def control1():
  print("The following program generates dungeon names in the general style of the Mystery Dungeon franchise.")
  print("This generator is not meant to be 100% perfect, but simply to get ideas flowing and to amuse yourself with.")
  print("")
  print("DISCLAIMER - This generator has a small amount of mature language as well as inside jokes between me and my friends.")
  print("This program was created by @PigeonheadDev. Contact me on Twitter for any questions, comments, feedback, or concerns.")
  print("This program is open source and can be modified and shared by users without restriction, as long as proper credit to the original author is given.")
  #UPDATE LINE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  print("The version you are using is: v1.0, updated on 2/9/23")
  print("")
  print("~~~MAIN MENU~~~")
  print("")
  print("Please use one of the following commands (make sure to use all caps):")
  print("HELP to repeat the inputs.")
  print("EXPLAIN to learn more about how this program works.")
  print("LIST to view the various libraries that the program uses to generate names.")
  print("END to terminate the program.")
  print("Enter anything else (including nothing) to generate a random dungeon name.")
  print("")
  command = input("ENTER YOUR COMMAND >")
  print("")
  match command:
    case "HELP":
      help_func()
    case "EXPLAIN":
      explain_func()
    case "LIST":
      list_func1()
    case "END":
      quit()
    case other:
      print("Your random dungeon name is:")
      find_name()
      print("")
      control2()

def control2():
  command = input("ENTER YOUR COMMAND >")
  print("")
  match command:
    case "HELP":
      help_func()
    case "EXPLAIN":
      explain_func()
    case "LIST":
      list_func1()
    case "END":
      quit()
    case other:
      print("Your random dungeon name is:")
      find_name()
      print("")
      control2()

def help_func():
  print("~~~MAIN MENU~~~")
  print("")
  print("Please use one of the following commands (make sure to use all caps):")
  print("HELP to repeat the inputs.")
  print("EXPLAIN to learn more about how this program works.")
  print("LIST to view the various libraries that the program uses to generate names.")
  print("END to terminate the program.")
  print("Enter anything else (including nothing) to generate a random dungeon name.")
  print("")
  control2()

def explain_func():
  print("This program uses preset percentages to combine certain keyword categories in a preset order.")
  print("")
  print("The categories are: Vague, Prefix, Location, Dungeon, Suffix.")
  print("Vague words are general words that can be seen in a dungeon name.")
  print("Prefix words are general adjectives or other descriptors.")
  print("Location words are general non-threatening locations that usually occur in nature.")
  print("Dungeon words are threatening locations that are typically artificial and manmade.")
  print("Suffix words are general descriptions that add slightly more flavor to a name, typically in the form of 'of X'.")
  print("")
  print("Here are the formats the keyword categories can be displayed as, as well as their precentages:")
  print("Prefix + Location, 10%")
  print("Prefix + Dungeon, 10%")
  print("Prefix + Location + Suffix, 5%")
  print("Prefix + Dungeon + Suffix, 5%")
  print("Vague + Location, 10%")
  print("Vague + Dungeon, 10%")
  print("Vague + Location + Suffix, 5%")
  print("Vague + Dungeon + Suffix. 5%")
  print("Location + Dungeon, 10%")
  print("Location + Dungeon + Suffix, 5%")
  print("Location + Suffix, 10%")
  print("Dungeon + Suffix, 10%")
  print("Vague + Prefix + Location + Dungeon + Suffix, 5%")
  print("")
  print("~~~RETURNED TO MAIN MENU~~~")
  print("")
  control2()

def list_func1():
  print("Use one of the following commands to view the terms in that libray:") 
  print("VAGUE, PREFIX, LOCATION, DUNGEON, SUFFIX.")
  print("Type BACK to return to the previous menu.")
  print("Remember to type in all caps.")
  print("(Also note that the list will be formatted exactly as it is in the code, it simply makes my job easier. Perhap that'll get removed in a future version if someone cares enough.)")
  print("")
  print_list = input("ENTER YOUR COMMAND. >")
  print("")
  match print_list:
    case "VAGUE":
      print(vague_list)
      list_func2()
    case "PREFIX":
      print(prefix_list)
      list_func2()
    case "LOCATION":
      print(location_list)
      list_func2()
    case "DUNGEON":
      print(dungeon_list)
      list_func2()
    case "SUFFIX":
      print(suffix_list)
      list_func2()
    case "BACK":
      print("")
      print("~~~RETURNED TO MAIN MENU~~~")
      print("")
      control2()
    case other:
      print("I'm sorry, that is not a valid command.")
      list_func2()

def list_func2():
  print("")
  print_list = input("ENTER YOUR COMMAND. >")
  print("")
  match print_list:
    case "VAGUE":
      print(vague_list)
      list_func2()
    case "PREFIX":
      print(prefix_list)
      list_func2()
    case "LOCATION":
      print(location_list)
      list_func2()
    case "DUNGEON":
      print(dungeon_list)
      list_func2()
    case "SUFFIX":
      print(suffix_list)
      list_func2()
    case "BACK":
      print("~~~RETURNED TO MAIN MENU~~~")
      print("")
      control2()
    case other:
      print("I'm sorry, that is not a valid command.")
      list_func2()

control1()