ESCP = "#"
CHAP = "chapter"
TEXT = "text"
DUAL = "dual"

def compile_chapter(source):
    return "\\section{" + source.strip() + "}"

def compile_text(source):
    return source.strip()

def compile_dual(source):
    tex_lines = []
    for source_line in source.strip().split("\n"):
        source_line = source_line.strip()
        if source_line == "":
            continue
        tex_duals = []
        for expr in source_line.split("|"):
            split = expr.split(">")
            if len(split) == 1:
                tex_duals.append("\\textrm{" + expr.strip() + "}")
            else:
                esp = split[0].strip()
                otr = split[1].strip()
                tex_duals.append("\\underbracket{\\vphantom{q}\\textrm{" + esp + "}}_{\\textrm{" + otr + "}}")
        tex_lines.append("$$" + "\n\\hphantom{|}".join(tex_duals) + "$$")
    return "\n".join(tex_lines)

def consume(text, part):
    return text.split(part, 1)[1]

def compile_blocks(blocks):
    tex_lines = []
    for block in blocks:
        if block.startswith(CHAP):
            tex_lines.append(compile_chapter(consume(block, CHAP)))
        elif block.startswith(TEXT):
            tex_lines.append(compile_text(consume(block, TEXT)))
        elif block.startswith(DUAL):
            tex_lines.append(compile_dual(consume(block, DUAL)))
    return "\n\n".join(tex_lines)

if __name__ == "__main__":
    with open("content.meta", "r") as content_meta:
        content_tex = compile_blocks(content_meta.read().split(ESCP))
        with open("content.tex", "w") as tex:
            tex.write(content_tex + "\n")
