character_map = {
    ord(';') : None
}

for line in open("a.txt"):
    a = line.strip().translate(character_map).split(" ")
    a[1] = a[1].translate({ord('_'):None})
    if(not a[0].startswith("List")):
        print("this._{0} = jsonRes['{0}'];".format(a[1]))
    else:
        b = a[0].translate({ord('>'):None, ord('<'):None})[4:]
        if(b == ""):
            print("this._{0} = jsonRes['{0}'];".format(a[1]))
        else:
            print("this._{0} = new List<{1}>();".format(a[1], b))
            print("for(var i in jsonRes['{0}']) {1}".format(a[1], "{"))
            print("  this._{0}.add(new {1}(i));".format(a[1], b))
            print("}")