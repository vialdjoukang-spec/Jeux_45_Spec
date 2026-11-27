# Syndromes radiologiques validés
Un fichier par organe (`<stem>.json`, même nom que dans `niveaux/`) : `{"<pathologie telle qu'écrite dans la source>": "Syndrome de masse (tumoral)"}`.
Une chaîne vide `""` supprime la ligne. Ce tableau l'emporte sur les mots-clés de `SYNDROMES_RADIO` (constructeur).
Vocabulaire fermé : de masse (tumoral), kystique, alvéolaire, interstitiel, bronchique, d'atélectasie, d'épanchement, aérique extra-digestif (gaz anormal), obstructif, vasculaire, ischémique, hémorragique, traumatique, infectieux, inflammatoire, compressif, dégénératif ou atrophique, malformatif ; précisions admises (ex. « Syndrome de masse médiastinale antérieure », « Syndrome pleural liquidien »). Jamais un nom de maladie.
