'''
These data are provided for general information purposes only.
Only the data possessed by the competent authorities of the Member States is authentic.
Therefore, no rights or legal claims can be derived from the data displayed on this site.
Datasource (eea): https://www.eea.europa.eu/data-and-maps/data/natura-14


.csv struct:
COUNTRY_CODE,SITECODE,SPECIESNAME,SPECIESCODE,REF_SPGROUP,SPGROUP,SENSITIVE,NONPRESENCEINSITE,POPULATION_TYPE,LOWERBOUND,UPPERBOUND,COUNTING_UNIT,ABUNDANCE_CATEGORY,DATAQUALITY,POPULATION,CONSERVATION,ISOLATION,GLOBAL,INTRODUCTION_CANDIDATE

column definition:
COUNTRY_CODE: Two digit country code the site belongs to.
SITECODE: Unique code witch forms the key-item within the database.
SPECIESNAME: Scientific name of the protected species.
SPECIESCODE: Code the species.
REF_SPGROUP: Reptiles, Birds, Amphibians, Mammals, Invertebrates, Fish, Plants.
SPGROUP: Reptiles, Birds, Amphibians, Mammals, Invertebrates, Fish, Plants.
SENSITIVE: 0: no sensitive; 1: sensitive.
NONPRESENCEINSITE: In case that a species no longer exists in the site a value "1" is entered.
POPULATION_TYPE: p: permanent; r: reproducing; c: concentration; w: wintering.
LOWERBOUND: Lower limits for the species population size.
UPPERBOUND: Upper limits for the species population size.
COUNTING_UNIT: Units of population, i = individuals, p = pairs or other units.
ABUNDANCE_CATEGORY: C: common; R: rare; V: very rare; P: present
DATAQUALITY: G: 'Good' (e.g. based on surveys); M: 'Moderate' (e.g. based on partial data with some extrapolation); P: 'Poor' (e.g. rough estimation).
POPULATION: Size and density of the population of the species present on the site in relation to the populations present within national territory. A: 100% >= p > 15%; B: 15% >=p> 2%; C: 2% >=p> 0%; D: non-significant population.
CONSERVATION: A: conservation excellent; B: good conservation; C: Average or reduced conservation
ISOLATION: A: population (almost) isolated; B: population not-isolated, but on margins of area of distribution; C: population not-isolated within extended distribution range.
GLOBAL: Global assessment if the value of the site for conservation of the species concerned. A: excellent value; B: good value; C: significant value.
INTRODUCTION_CANDIDATE: Species referred to in Article 4 of Directive 2009/147/EC or species listed in Annex II to Directive 92/43/EEC considered as a candidate for introduction on the site.
'''
