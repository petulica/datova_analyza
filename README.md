# Datová analýza / Data analysis  
pandas, csv

## short English description

Scripts for quantitative analysis upon data collected from NUSL, Czech R&D Information System and OpenAIRE for master's thesis purpose. The output of this repository is stored in dataset available from Zenodo.

**thesis**  
Petra Černohlávková. (2019). Relationships of research outputs and projects: NUSL, Czech R&D Information System and OpenAIRE. Prague. Master thesis. Charles University. Supervisior Dvořák, Jan.

**dataset**  
Petra Černohlávková. (2019). Relationships of research outputs and projects in NUSL, Czech R&D Information System and OpenAIRE: Supporting Data for Master Thesis [Data set]. Zenodo. http://doi.org/10.5281/zenodo.3338675

The details of this repository, which are given in the rest of this file, are described in the Czech language.

## popis v češtině  

Repozitář (část "kontrola") zkontroluje stav dat získaných ze třech zdrojů (NUŠL, RIV, OpenAIRE; viz dataset soubory *zdroj*.csv) na chybějící údaje a duplicity. Záhlaví souborů obsahuje identifikátory záznamů, rok vydání dokumentu, jazyk(y) dokumentu, typ(y) dokumentu, identifikátor projektu/ů a počet identifiktárů projektů uvedených u záznamu.

Poté zjištěné nedostatky zakomponuje do souborů označené "analyza". V části "analyza" seskupuje údaje podle roku a počtu projektů, podle jazyku výsledku a počtu projektů, podle typu dokumentů a počtu projektů. Výstupy jsou uloženy ve formátu csv s následující strukturou:

projects_year_*zdroj*.csv  
projects_langs_*zdroj*.csv  
projects_doctypes_*zdroj*.csv  

více viz dataset

Pro každý zdroj v tomto repozitáři existují dva soubory - kontrola a analyza. Každý se nepatrně liší v závislosti na datech získaných ze zdrojů.

Repozitář je možné využít pro obdobnou kvantitativní analýzu vazeb mezi výsledky a projekty v různých zdrojích. Nejprve je potřeba si v kontrole ověřit stav dat a poté přizpůsobit soubor "analyza" potřebám konkrétního zdroje.
