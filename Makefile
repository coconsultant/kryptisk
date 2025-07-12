#include config.mk

# Detect container engine (podman preferred, fallback to docker)
CONTAINER_ENGINE := $(shell command -v podman 2> /dev/null || command -v docker 2> /dev/null || echo podman)

##########################################################################
# MENU
##########################################################################
.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

data/:
	mkdir -p data/

env:
	cp env.example env

.venv/: data/ env
	python -m venv .venv/
	source .venv/bin/activate && pip install --upgrade pip
	source .venv/bin/activate && pip install -r requirements.txt
	source .venv/bin/activate && pip install -r requirements-dev.txt
	source .venv/bin/activate && pre-commit install

.PHONY: migrate
migrate: ## Run Django migrations
	$(CONTAINER_ENGINE)-compose run --rm django ./manage.py migrate

.PHONY: merge
merge: ## Run Django migrations
	$(CONTAINER_ENGINE)-compose run --rm django ./manage.py makemigrations
	$(CONTAINER_ENGINE)-compose run --rm django ./manage.py migrate --merge

.PHONY: superuser
superuser: ## Create a superuser
	@echo 'from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists() or User.objects.create_superuser("admin", "admin@example.com", "admin")' | $(CONTAINER_ENGINE)-compose run --rm -T django ./manage.py shell

.PHONY: dev-bootstrap
dev-bootstrap: .venv/ ## Bootstrap the development environment
	$(CONTAINER_ENGINE)-compose pull
	$(CONTAINER_ENGINE)-compose build
	$(CONTAINER_ENGINE) ps -a | grep virtualgradstudent_postgres_1 && $(CONTAINER_ENGINE)-compose down -v || true
	$(CONTAINER_ENGINE)-compose up -d postgres
	$(MAKE) migrate
	$(MAKE) superuser
	$(CONTAINER_ENGINE)-compose down

.PHONY: dev-start
dev-start: ## Start the development environment
	$(CONTAINER_ENGINE)-compose up -d postgres
	sleep 10
	$(CONTAINER_ENGINE)-compose up -d
	sleep 5
	curl --request PUT http://localhost:9000/testbucket

.PHONY: dev-stop
dev-stop: ## Stop the development environment
	$(CONTAINER_ENGINE)-compose down

.PHONY: dev-restart-django
dev-restart-django: ## Restart the Django service
	$(CONTAINER_ENGINE)-compose down django
	$(CONTAINER_ENGINE) system prune -af
	$(CONTAINER_ENGINE)-compose build django
	$(CONTAINER_ENGINE)-compose up -d --force-recreate django

.PHONY: dev-clean
dev-clean: ## erase all the things.
	$(CONTAINER_ENGINE)-compose down
	$(CONTAINER_ENGINE) system prune -af
	/bin/rm -rf data/
	/bin/rm -rf src/staticfiles

.PHONY: snapshot-local-db
snapshot-local-db: ## Create a snapshot of the local database
	$(CONTAINER_ENGINE)-compose exec postgres pg_dump -U postgres -Fc django_reference > django_reference.dump

.PHONY: restore-local-db
restore-local-db: ## Restore the local database from a snapshot
	$(CONTAINER_ENGINE)-compose exec -T postgres pg_restore -U postgres -d django_reference < django_reference.dump
