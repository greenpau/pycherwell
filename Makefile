.PHONY: build run clean connect do

PKG_NAME="pycherwell"
PKG_NAME_EGG := $(subst -,_,$(PKG_NAME))
PKG_VERSION=$(shell cat setup.py | grep "VERSION =" | cut -d"\"" -f2)

all:
	@echo 'the only available options are: package' || false

clean:
	@find . -name \*.pyc -delete
	@rm -rf dist/

package: clean
	@pandoc --from=markdown --to=rst --output=${PKG_NAME}/README.rst README.md
	@cp LICENSE.txt ${PKG_NAME}/LICENSE.txt
	@python3 setup.py sdist
	@rm -rf ${PKG_NAME_EGG}.egg-info *.egg build/
	@find . -name \*.pyc -delete
	@#tar -tvf dist/${PKG_NAME}*.tar.gz

release:
	@tar -tvf dist/$(PKG_NAME)*.tar.gz
	@git tag -a "v$(PKG_VERSION)" -m "Release $(PKG_VERSION)"
	@git push
	@git push --tags
