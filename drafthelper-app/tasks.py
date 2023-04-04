from invoke import task

@task
def start(c):
	c.run('python3 src/interface.py', pty=True)

@task
def test(c):
	c.run('poetry run pytest src', pty=True)

@task
def coverage(c):
	c.run('coverage run --branch -m pytest src', pty=True)

@task(coverage)
def coverage_report(c):
	c.run('coverage html')
