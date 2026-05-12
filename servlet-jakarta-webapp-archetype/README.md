# servlet-jakarta-webapp-archetype

Maven archetype for a modern Jakarta Servlet web application.


```bash
mvn install
```


```bash
mvn archetype:generate \
  -DarchetypeGroupId=project._42algoritmos \
  -DarchetypeArtifactId=servlet-jakarta-webapp-archetype \
  -DarchetypeVersion=2.0.0 \
  -DarchetypeCatalog=local
```

```bash
mvn archetype:generate \
  -DarchetypeGroupId=project._42algoritmos \
  -DarchetypeArtifactId=servlet-jakarta-webapp-archetype \
  -DarchetypeVersion=2.0.0 \
  -DarchetypeCatalog=local \
  -DgroupId=br.eng.ivanlopes \
  -DartifactId=my-webapp \
  -Dversion=1.0-SNAPSHOT \
  -Dpackage=br.eng.ivanlopes \
  -DinteractiveMode=false
```
```bash
cd my-webapp
mvn jetty:run
```

Then open:

http://localhost:8080/hello


```bash
chmod +x generate.py
./generate.py
```

Depois:

```bash
cd servlet-jakarta-webapp-archetype
mvn install
```


```bash
mvn archetype:generate \
  -DarchetypeGroupId=project._42algoritmos \
  -DarchetypeArtifactId=servlet-jakarta-webapp-archetype \
  -DarchetypeVersion=2.0.0 \
  -DarchetypeCatalog=local \
  -DgroupId=br.eng.ivanlopes \
  -DartifactId=my-webapp \
  -Dversion=1.0-SNAPSHOT \
  -Dpackage=br.eng.ivanlopes \
  -DinteractiveMode=false
```

Rodar:

```bash
cd my-webapp
mvn jetty:run
```
