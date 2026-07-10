#!/usr/bin/env python3

from pathlib import Path
from Cheetah.Template import Template


def render(template_file: Path, output_file: Path, ctx: dict):
    text = template_file.read_text(encoding="utf-8")
    result = str(Template(text, searchList=[ctx]))

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(result, encoding="utf-8")


def main():
    ctx = {
        "archetype_group_id": "project._42algoritmos",
        "archetype_artifact_id": "servlet-jakarta-webapp-archetype",
        "archetype_version": "2.0.0",
        "archetype_name": "Servlet Jakarta WebApp Archetype",

        "java_version": "17",
        "jakarta_servlet_version": "6.0.0",
        "junit_version": "5.10.2",
        "lombok_version": "1.18.32",
        "maven_compiler_plugin_version": "3.13.0",
        "maven_war_plugin_version": "3.4.0",
        "jetty_plugin_version": "11.0.20",
    }

    root = Path(ctx["archetype_artifact_id"])
    tpl = Path("templates")

    files = {
        "archetype-pom.xml.tmpl":
            root / "pom.xml",

        "README.md.tmpl":
            root / "README.md",

        "archetype-metadata.xml.tmpl":
            root / "src/main/resources/META-INF/maven/archetype-metadata.xml",

        "generated-pom.xml.tmpl":
            root / "src/main/resources/archetype-resources/pom.xml",

        "HelloServlet.java.tmpl":
            root / "src/main/resources/archetype-resources/src/main/java/HelloServlet.java",

        "index.html.tmpl":
        root / "src/main/resources/archetype-resources/src/main/webapp/index.html",

        "archetype.properties.tmpl":
            root / "src/test/resources/projects/basic/archetype.properties",

        "goal.txt.tmpl":
            root / "src/test/resources/projects/basic/goal.txt",

        "gitignore.tmpl":
            root / ".gitignore",

        "java-version.tmpl":
            root / ".java-version",

        "ArchetypeMakefile.tmpl":
        root / "Makefile",

        "ProjectMakefile.tmpl":
        root / "src/main/resources/archetype-resources/Makefile",
    }

    for template_name, output_path in files.items():
        render(tpl / template_name, output_path, ctx)

    print(f"Archetype gerado em: {root}")


if __name__ == "__main__":
    main()
