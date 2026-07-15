
TARGET=servlet-jakarta-webapp-archetype

build:
	./generate.py

clean:
	rm -rf $(TARGET)

install:
	make -C $(TARGET)

uninstall:
	make -C $(TARGET) uninstall

deploy: build install
