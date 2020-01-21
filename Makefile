.PHONY: clean package release pypi-test-upload pypi-prod-upload

PKG_NAME="pycherwell"
PKG_NAME_EGG := $(subst -,_,$(PKG_NAME))
PKG_VERSION=$(shell cat setup.py | grep "VERSION =" | cut -d"\"" -f2)
PYBIN="python3"

all:
	@echo 'the only available options are: package' || false

clean:
	@find . -name \*.pyc -delete
	@rm -rf dist/ ${PKG_NAME_EGG}.egg-info *.egg build/

package: clean
	@pandoc --from=markdown --to=rst --output=${PKG_NAME}/README.rst README.md
	@cp LICENSE.txt ${PKG_NAME}/LICENSE.txt
	@$(PYBIN) setup.py sdist bdist_wheel
	@rm -rf ${PKG_NAME_EGG}.egg-info *.egg build/
	@find . -name \*.pyc -delete
	@#tar -tvf dist/${PKG_NAME}*.tar.gz

release:
	@tar -tvf dist/$(PKG_NAME)*.tar.gz
	@git tag -a "v$(PKG_VERSION)" -m "Release $(PKG_VERSION)"
	@git push
	@git push --tags

pypi-test-upload:
	@$(PYBIN) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi-prod-upload:
	@$(PYBIN) -m twine upload dist/*
