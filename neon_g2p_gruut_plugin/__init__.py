from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin
from gruut import sentences


class GruutPlugin(Grapheme2PhonemePlugin):

    def get_ipa(self, word, lang):
        for sent in sentences(word, lang=lang):
            for word in sent:
                if word.phonemes:
                    return [p.replace('ˈ', "") for p in word.phonemes]
