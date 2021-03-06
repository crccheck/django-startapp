shorthash=$(shell git rev-parse --short HEAD)

# initial `gh-pages` branch created inside html directory which is gitignored
# by `master`

# WISHLIST setup docs/_build/html when it's destroyed

.PHONY: docs
docs:
	cd docs && $(MAKE) html
	cd docs/_build/html && \
	  git add . && \
	  git commit -m "build docs based on $(shorthash)" && \
	  git push origin gh-pages


push.project:
	git subtree push --prefix=project project master
