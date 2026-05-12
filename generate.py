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
        "archetype_artifact_id": "console-java-archetype",
        "archetype_version": "1.0.0",
        "archetype_name": "Java Console Application Archetype",

        "java_version": "17",
        "junit_version": "5.10.2",
        "log4j_version": "2.23.1",

        "maven_compiler_plugin_version": "3.13.0",
        "exec_maven_plugin_version": "3.3.0",
        "maven_jar_plugin_version": "3.4.2",
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

        "App.java.tmpl":
            root / "src/main/resources/archetype-resources/src/main/java/App.java",

        "log4j2.xml.tmpl":
            root / "src/main/resources/archetype-resources/src/main/resources/log4j2.xml",

        "ProjectMakefile.tmpl":
            root / "src/main/resources/archetype-resources/Makefile",

        "ArchetypeMakefile.tmpl":
            root / "Makefile",

        "archetype.properties.tmpl":
            root / "src/test/resources/projects/basic/archetype.properties",

        "goal.txt.tmpl":
            root / "src/test/resources/projects/basic/goal.txt",

        "gitignore.tmpl":
            root / ".gitignore",

        "java-version.tmpl":
            root / ".java-version",
    }

    for template_name, output_path in files.items():
        render(tpl / template_name, output_path, ctx)

    print(f"Archetype gerado em: {root}")


if __name__ == "__main__":
    main()

