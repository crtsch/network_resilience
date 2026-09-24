[*🇬🇧 English below*](#road-network-resilience-evaluation)

# Évaluation de la robustesse d'un réseau routier

> *Ce repo contient les bases théoriques et le code utilisés pour ma soutenance de TIPE (Travail d'Initiative Personnelle Encadrée)*

**Thème de l'année :** "Cycles, boucles"

**Note finale :** 17,1/20


## Organisation du repo

- 📁 `code` : le code que j'ai utilisé pour mon TIPE, écrit en Python. Il est documenté et partagé en différents dossiers et fichiers :

    - 📁 `imports` : les graphes à importer pour le calcul de robustesse
        - 📋 `genes.json` : graphe représentant une version simplifiée du réseau routier de Gênes
    - 📁 `exports` : les différents exports relatifs au calcul de robustesse (génération de graphes aléatoires, visualisations...)
    - 🐍 `graphe.py` : fonctions relatives à la manipulation de graphes
    - 🐍 `matrice.py` : fonctions relatives à la manipulation de matrices
    - 🐍 `metriques.py` : fonctions de calcul des métriques
    - 🐍 `main.py` *(exemple)* :  génération de 10 graphes aléatoires, calcul de leur courbe de Lorenz et indice de Gini

- 📄 `MCOT_epreuve.pdf` : la Mise en Cohérence des Objectifs du TIPE, document à compléter en amont de l'épreuve et qui donne une vision d'ensemble du sujet (positionnements thématiques, références bibliographiques...). **Version envoyée au SCEI**

- ~~📄 `MCOT_adaptee.pdf` : version de la MCOT plus cohérente avec mon travail final (cf. [Remarque sur la MCOT](#remarque-sur-la-mcot))~~

- 📄 `Annexe.pdf` : le document que j'ai imprimé et remis au jury contenant des explications et démonstrations mathématiques, ainsi que tout mon code (qui est exactement celui dans `code/`)

- 📄 `Beamer.pdf` : la présentation utilisée comme support le jour de l'épreuve

- ~~📄 `Rapport.pdf` : la trame complète de ma présentation (rédigée après coup) qui rend compte de ce que j'ai présenté au jury~~

**|** *Les documents barrés seront ajoutés ultérieurement*


## Résumé du travail

Dans un monde où la voiture est utilisée comme moyen de transport principal, il me semble important de chercher à agir afin de permettre des déplacements fluides à chacun, et ce malgré les incidents qu'une forte sollicitation du réseau implique.

Pour cela, j'ai cherché à évaluer la robustesse d'un réseau routier donné, c'est-à-dire sa capacité à limiter les conséquences d'une perturbation sur les usagers, en minimisant les rallongements de temps de trajets lors de la fermeture d'un ou de plusieurs axe(s).

Mon travail cherche à montrer l'importance de la présence de cycles dans un réseau routier pour en garantir la robustesse. Pour cela, j'ai tout d'abord construit une métrique visant à quantifier l'importance d'un cycle dans un graphe, puis je l'ai utilisée pour en déduire la robustesse globale d'un réseau.


## Remarque sur la MCOT

La bibliographie de ma MCOT est très variée, car mon projet initial consistait à comparer plusieurs métriques de robustesse puis de les utiliser pour construire une « méta-métrique ». Faute de temps (15 min de passage), j'ai finalement retenu une seule métrique, que j'ai adaptée et complétée par la courbe de Lorenz et l'indice de Gini. Comme la MCOT devait être envoyée au SCEI en février (5 mois avant l'épreuve), elle ne traduit pas exactement mon travail final.

Vous trouverez donc dans ce repo deux MCOT : `MCOT_epreuve.pdf`, remise au SCEI, et `MCOT_adaptee.pdf`*, rédigée après l'épreuve et plus fidèle à mon travail final. Cette dernière correspond à la version que j'aurais remise si mes objectifs de février avaient été les mêmes qu'en juin. La bibliographie est adaptée (articles que j'ai effectivement utilisés), c'est celle que vous trouverez dans [Bibliographie](#bibliographie).

*\* disponible plus tard*


## Bibliographie

**[1]** Vincenzo Petito, Maurizio Leotta et Marina Ribaudo : *Improving the performance of road network analysis: the Morandi Bridge case study*. https://doi.org/10.5220/0007745702590266 (2019)

**[2]** Pierre-Louis Giscard et Yohan Hosten : *Peut-on quantifier l'importance du périphérique parisien ?* https://inria.hal.science/hal-05372993/ (2025)

**[3]** Pauline Gauthier, Angelo Funo et Nour-Eddin El Faouzi : *Network resilience: how to identify critical links subject to day-to-day disruption*. https://doi.org/10.1177/0361198118792115 (2018)

**[4]** Max O. Lorenz : *Methods of measuring the concentration of wealth*. American Statistical Association (1905)

**[5]** Corrado Gini : *Mesurement of inequality of income*. Economic Journal 31 (1921)

**[6]** Keith Paton : *An algorithm for finding a fundamental set of cycles of a graph*. https://doi.org/10.1145/363219.363232 (1969)

**[7]** François De Marçay : *Décomposition $A = LU$ de matrice $A$ quelconque*. https://www.imo.universite-paris-saclay.fr/~joel.merker/Enseignement/Algebre-Lineaire-Geometrie/lu.pdf


&nbsp;


# Road Network Resilience Evaluation

> *This repo contains the theoretical basis and code used for my TIPE defense (Travail d'Initiative Personnelle Encadrée)*

**Theme of the year:** "Cycles, loops"

**Final grade:** 17.1/20


## Repo organization

- 📁 `code`: the code I used for my TIPE, written in Python. It is documented and shared in different folders and files:

    - 📁 `imports`: graphs to import for resilience calculation
        - 📋 `genes.json`: graph representing a simplified version of Gene's road network
    - 📁 `exports`: various exports related to resilience calculation (random graph generation, visualizations...)
    - 🐍 `graphe.py`: functions related to graph manipulation
    - 🐍 `matrice.py`: functions related to matrix manipulation
    - 🐍 `metriques.py`: metric calculation functions
    - 🐍 `main.py` *(example)*: generation of 10 random graphs, calculation of their Lorenz curve and Gini index

- 📄 `MCOT_epreuve.pdf`: the "Mise en Cohérence des Objectifs du TIPE" document, to be completed before the defense and which gives an overview of the subject (thematic positioning, bibliographic references...). **Version sent to SCEI**

- ~~📄 `MCOT_adaptee.pdf`: version of the MCOT more consistent with my final work (see [Remark on the MCOT](#remark-on-the-mcot))~~

- 📄 `Annexe.pdf`: the document I printed and submitted to the jury containing explanations and mathematical demonstrations, as well as all my code (which is exactly the same as in `code/`)

- 📄 `Beamer.pdf`: the presentation used as support on the day of the defense

- ~~📄 `Rapport.pdf`: the complete outline of my presentation (written afterwards) which reports on what I presented to the jury~~

**|** *Crossed-out documents will be added later*


## Summary of the work

In a world where the car is used as the main means of transport, it seems important to me to seek to act in order to allow smooth travel for everyone, despite the incidents that heavy use of the network implies.

To do this, I sought to evaluate the resilience of a given road network, that is, its ability to limit the consequences of a disruption on users, by minimizing travel time extensions when one or more axes are closed.

My work seeks to show the importance of the presence of cycles in a road network to ensure its resilience. To do this, I first built a metric aimed at quantifying the importance of a cycle in a graph, and then I used it to deduce the overall resilience of a network.


## Remark on the MCOT

The bibliography of my MCOT is very varied, because my initial project was to compare several resilience metrics and then use them to build a "meta-metric". Due to time constraints (15 minutes of presentation), I ultimately retained only one metric, which I adapted and supplemented with the Lorenz curve and Gini index. Since the MCOT had to be sent to SCEI in February (5 months before the defense), it does not exactly reflect my final work.

Thus, you will find in this repo two MCOTs: `MCOT_epreuve.pdf`, submitted to SCEI, and `MCOT_adaptee.pdf`*, written after the defense and more faithful to my final work. The latter corresponds to the version I would have submitted if my objectives in February had been the same as in June. The bibliography is adapted (articles that I actually used), it is the one you will find in [Bibliography](#bibliography).

*\* available later*


## Bibliography

**[1]** Vincenzo Petito, Maurizio Leotta and Marina Ribaudo: *Improving the performance of road network analysis: the Morandi Bridge case study*. https://doi.org/10.5220/0007745702590266 (2019)

**[2]** Pierre-Louis Giscard and Yohan Hosten: *Peut-on quantifier l'importance du périphérique parisien ?* https://inria.hal.science/hal-05372993/ (2025)

**[3]** Pauline Gauthier, Angelo Funo and Nour-Eddin El Faouzi: *Network resilience: how to identify critical links subject to day-to-day disruption*. https://doi.org/10.1177/0361198118792115 (2018)

**[4]** Max O. Lorenz: *Methods of measuring the concentration of wealth*. American Statistical Association (1905)

**[5]** Corrado Gini: *Mesurement of inequality of income*. Economic Journal 31 (1921)

**[6]** Keith Paton: *An algorithm for finding a fundamental set of cycles of a graph*. https://doi.org/10.1145/363219.363232 (1969)

**[7]** François De Marçay: *Décomposition $A = LU$ de matrice $A$ quelconque*. https://www.imo.universite-paris-saclay.fr/~joel.merker/Enseignement/Algebre-Lineaire-Geometrie/lu.pdf