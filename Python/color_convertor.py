NO = ["no", "false", "n", "f", "0", "stop", "exit", "quit"]

def main():
    print("""
    ##################################
    ##       Colour Convertor       ##
    ##################################""")

    again = 1
    while again == 1: 
        main_convertor()
        asked = input("    Again? ")
        again = 0 if asked.lower() in NO else 1
    print("\n    Stopping...")

def main_convertor():
    colour = input("\n    Input (R, G, B), (C%, M%, Y%, K%) or #HEX to get started.\n        ")
    if colour in NO or len(colour) == 0:
        pass
    elif colour[0] == "#":
        h, e, x = colour[1:3], colour[3:5], colour[5:7]
        if len(h) == 0 or len(e) == 0 or len(x) == 0:
            print("    Nah, mate.")
            main_convertor()
        hex_convertor(h, e, x)
    else:
        try:
            r, g, b = map(int, colour.strip("()").split(", "))
            rgb_convertor(r, g, b)
        except ValueError:
            try:
                c, m, y, k = map(int, colour.strip("()").rstrip("%").split("%, "))
                cmyk_convertor(c, m, y, k)
            except ValueError:
                print("    Nah, mate.")
                main_convertor()

def hex_convertor(h, e, x):
    r, g, b = hex_to_rgb(h, e, x)
    rgb_convertor(r, g, b)

def rgb_convertor(r, g, b):
    c, m, y, k = rgb_to_cmyk(r, g, b)
    build_and_print(r, g, b, c, m, y, k)

def cmyk_convertor(c, m, y, k):
    r, g, b = cmyk_to_rgb(c, m, y, k)
    build_and_print(r, g, b, c, m, y, k)

def rgb_to_hex(r, g, b):
    return "#{0:x}{1:x}{2:x}".format(r, g, b)

def rgb_to_cmyk(r, g, b):
    k = 1 - (max(r, g, b) / 255)
    c = (1 - r / 255 - k) / (1 - k)
    m = (1 - g / 255 - k) / (1 - k)
    y = (1 - b / 255 - k) / (1 - k)
    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

def cmyk_to_rgb(c, m, y, k):
    r = int(255 * (1 - c / 100) * (1 - k / 100))
    g = int(255 * (1 - m / 100) * (1 - k / 100))
    b = int(255 * (1 - y / 100) * (1 - k / 100))
    return r, g, b

def hex_to_rgb(h, e, x):
    return int(h, 16), int(e, 16), int(x, 16)

def build_rgb(r, g, b):
    return "({0}, {1}, {2})".format(r, g, b)

def build_cmyk(c, m, y, k):
    return "({0}%, {1}%, {2}%, {3}%)".format(c, m, y, k)

def build_and_print(r, g, b, c, m, y, k):
    rgb = build_rgb(r, g, b)
    cmyk = build_cmyk(c, m, y, k)
    hexa = rgb_to_hex(r, g, b)
    print("\n    RGB:\t", rgb, "\n    CMYK:\t", cmyk, "\n    HEX:\t", hexa, "\n")

if __name__ == "__main__":
    main()