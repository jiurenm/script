character_map = {
    ord(';') : None
}

for line in open("a.txt"):
    a = line.strip().translate(character_map).split(" ")
    for i in a:
        a[1] = a[1].translate({ord('_'):None})
    print("{0[0]} get {0[1]} => this._{0[1]};".format(a))
    print("set {0[1]}({0[0]} {0[1]}) => this._{0[1]} = {0[1]};".format(a))
    print("\t")