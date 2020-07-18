.PHONY: clean package release pypi-test-upload pypi-prod-upload logo docs test

PKG_NAME="pycherwell"
PKG_NAME_EGG := $(subst -,_,$(PKG_NAME))
PKG_VERSION=$(shell cat VERSION | head -1)
PYBIN="python3"
PIPBIN="pip3"
GIT_COMMIT:=$(shell git describe --dirty --always)
GIT_BRANCH:=$(shell git rev-parse --abbrev-ref HEAD -- | head -1)

all:
	@echo 'the only available options are: package' || false

clean:
	@find . -name \*.pyc -delete
	@rm -rf dist/ ${PKG_NAME_EGG}.egg-info *.egg build/

docs:
	@pandoc --from=markdown --to=rst --output=${PKG_NAME}/README.rst README.md

package: clean docs
	@cp LICENSE.txt ${PKG_NAME}/LICENSE.txt
	@#python3 -m pip install --user --upgrade setuptools wheel
	@$(PYBIN) setup.py sdist bdist_wheel
	@rm -rf ${PKG_NAME_EGG}.egg-info *.egg build/
	@find . -name \*.pyc -delete
	@#tar -tvf dist/${PKG_NAME}*.tar.gz

release: clean docs
	@#tar -tvf dist/$(PKG_NAME)*.tar.gz
	@echo "Making release"
	@if [ $(GIT_BRANCH) != "master" ]; then echo "cannot release to non-master branch $(GIT_BRANCH)" && false; fi
	@git diff-index --quiet HEAD -- || ( echo "git directory is dirty, commit changes first" && false )
	@versioned -patch
	@git add VERSION
	@git commit -m 'updated VERSION file'
	@versioned -sync setup.py
	@versioned -sync cherwell-client
	@versioned -sync pycherwell/__init__.py
	@versioned -sync pycherwell/app_configuration.py
	@versioned -sync pycherwell/app_client.py
	@echo "Patched version"
	@git add .
	@git commit -m "released v`cat VERSION | head -1`"
	@git tag -a v`cat VERSION | head -1` -m "v`cat VERSION | head -1`"
	@git push
	@git push --tags
	@echo "If necessary, run the following commands:"
	@echo "  git push --delete origin v$(PKG_VERSION)"
	@echo "  git tag --delete v$(PKG_VERSION)"

test:
	@#$(PIPBIN) install flake8 pytest --user
	@flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	@pytest

pypi-test-upload:
	@$(PYBIN) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi-prod-upload:
	@$(PYBIN) -m twine upload dist/*

logo:
	@convert -background black -fill white -font DejaVu-Sans-Bold -size 640x320! -gravity center -pointsize 96 label:'Cherwell\nAPI' PNG32:logo.png
