from bootstrapvz.base import Task
from bootstrapvz.common import phases


class Log(Task):
	description = 'Logging user specified message'
	phase = phases.preparation

	@classmethod
	def run(cls, info):
		import logging
		log = logging.getLogger(__name__)
		log.info(info.manifest.plugins['example']['message'])


class Gol(Task):
	description = 'Logging user specified message in reverse'
	phase = phases.cleaning

	@classmethod
	def run(cls, info):
		import logging
		log = logging.getLogger(__name__)
		log.info(info.manifest.plugins['example']['message'][::-1])
