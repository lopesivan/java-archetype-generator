

build:
	./generate.py

clean:
	rm -rf java-console-app-archetype

install:
	make -C java-console-app-archetype

uninstall:
	make -C java-console-app-archetype uninstall

deploy: build install
