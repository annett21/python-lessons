text = (
    "vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo"
    " jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt "
    "cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ "
    "bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf "
    "dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu "
    "zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt "
    "foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg "
    "hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip "
    "fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe "
    "ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf"
    " sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw "
    "jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf "
    "tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn "
    "jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf "
    'pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
)


def caesar_decoder(char, shift):
    if char == " ":
        return char
    return chr(ord(char) + shift)


new_text = "".join([caesar_decoder(char, -1) for char in text])

shift = 3
for word in new_text.split():
    current_shift = shift if len(word) > shift else shift % len(word)
    new_word = word[-current_shift:] + word[:-current_shift]
    print(new_word, end=" ")
    if new_word.endswith("."):
        print()
        shift += 1
