from .models import FillerTextModel

text_dic = {
    'alice': 1,
    'constitution_of_japan': 2,
    'dagon': 3,
    'frankenstein': 4,
    'lorem_ipsum': 5,
    'lorem_ipsum_upper': 6,
    'pangram': 7,
    'rashomon': 8,
    'sample': 9,
}


def text_length(text, count):
    if len(text) >= count:
        return text[:count]
    else:
        for i in range(count):
            if len(text) > count:
                text = text[:len(text)-(len(text)-count)]
                break
            text = text + text
        return text


def filler_text(text, count, no_space):
    dummy = FillerTextModel.objects.values_list('text', flat=True).get(pk=text_dic[text]).replace("\r", "")
    if no_space:
        dummy = dummy.replace(" ", "").replace("　", "").replace("\n", "").replace("\t", "")
        result = text_length(dummy, count)
        return result
    else:
        result = text_length(dummy, count)
        return result
