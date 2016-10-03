from enum import Enum

class Language(Enum):
	English = 'en'
	German = 'de'
	French = 'fr'

class Category(Enum):
	Business = 'business'
	Entertainment = 'entertainment'
	Gaming = 'gaming'
	General = 'general'
	Music = 'music'
	ScienceNature = 'science-and-nature'
	Sport = 'sport'
	Technology = 'technology'

class Country(Enum):
	Australia = 'au'
	Germany = 'de'
	GreatBritain = 'gb'
	India = 'in'
	UnitedStates = 'us'