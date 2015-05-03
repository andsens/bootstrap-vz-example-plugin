import tasks

__version__ = '0.9.5'


def validate_manifest(data, validator, error):
	import os.path
	schema_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'manifest-schema.yml'))
	validator(data, schema_path)


def resolve_tasks(taskset, manifest):
	taskset.add(tasks.Log)


def resolve_rollback_tasks(taskset, manifest, completed, counter_task):
	counter_task(taskset, tasks.Log, tasks.Gol)
