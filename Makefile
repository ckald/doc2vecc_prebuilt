.PHONY: doc2vecc, wheel, clean

-include makefile.inc


doc2vecc: doc2vecc/doc2vecc
	git submodule update --init --recursive
	cd doc2vecc; \
		rm -f doc2vecc; \
		gcc doc2vecc.c -o doc2vecc -lm -pthread -O3 -march=native -funroll-loops

wheel: doc2vecc
	python setup.py sdist bdist_wheel

clean:
	rm -f doc2vecc/doc2vecc
	rm -rf ./build
	rm -rf ./dist
