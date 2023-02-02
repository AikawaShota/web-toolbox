from .models import FillerTextModel


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
    dummy = FillerTextModel.objects.values_list('text', flat=True).get(value=text).replace("\r", "")
    if no_space:
        dummy = dummy.replace(" ", "").replace("　", "").replace("\n", "").replace("\t", "")
        result = text_length(dummy, count)
        return result
    else:
        result = text_length(dummy, count)
        return result
