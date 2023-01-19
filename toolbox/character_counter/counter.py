def character_counter(text):
    number_of_character = len(text.replace("\r", ""))
    no_space = len(text.replace(" ", "").replace("　", "").replace("\t", "").replace("\n", "").replace("\r", ""))
    manuscript_paper = len(text.replace("\r", "")) // 400 + 1
    if len(text.replace("\r", "")) % 400 == 0:
        manuscript_paper -= 1
    return [number_of_character, no_space, manuscript_paper]
