from gruut import sentences
from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin


class GruutPlugin(Grapheme2PhonemePlugin):

    def get_ipa(self, word, lang, ignore_oov=False):
        for sent in sentences(word, lang=lang):
            for word in sent:
                if word.phonemes:
                    return [p for p in word.phonemes]

    @staticmethod
    def get_languages():
        # TODO - check at runtime which extras have been installed
        return ["ar", "cs", "de", "es", "en", "fa", "fr", "it", "lb", "nl", "pt", "ru", "sv", "sw"]

    @property
    def available_languages(self):
        """Return languages supported by this G2P implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return set(self.get_languages())


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all keys represent an example valid config for the plugin
GruutG2PConfig = {
    l: [
        {"lang": l,
         "display_name": f"Gruut ({l})",
         "priority": 60,
         "native_alphabet": "IPA",
         "durations": False,
         "offline": True}
    ] for l in GruutPlugin.get_languages()
}
