class Parser(object):
    def parse(self):
        raw = open("[English]_cleaned.txt", "r")
        ann = open("[English]_cleaned.ann", "r")
        data = raw.read()
        tags = []
        while ann:
            line = ann.readline()
            if line.startswith("R"):
                continue

            _, annotation, text = line.strip().split("\t")
            tag_name, span = annotation.split(" ", 1)
            start = int(span[0])
            end = int(span[-1])
            tags.append((tag_name, start, end))

