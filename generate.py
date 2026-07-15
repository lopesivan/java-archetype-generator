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
        "archetype_artifact_id": "java-console-app-archetype",
        "archetype_version": "2.0.1",
        "archetype_name": "Java Console App Archetype",
        "java_version": "17",
        "jakarta_servlet_version": "6.0.0",
        "maven_war_plugin_version": "3.4.0",
        "jetty_plugin_version": "11.0.20",
        "junit_version": "5.10.2",
        "lombok_version": "1.18.32",
        "maven_compiler_plugin_version": "3.13.0",
    }

    root = Path(ctx["archetype_artifact_id"])
    tpl = Path("templates")

    # 🔑 Variáveis de paths comuns
    main_resources = root / "src/main/resources/archetype-resources"
    main_java = main_resources / "src/main/java"
    main_webapp = main_resources / "src/main/webapp"
    test_resources = root / "src/test/resources/projects/basic"
    meta_inf = root / "src/main/resources/META-INF/maven"

    files = {
        "archetype-pom.xml.tmpl":
            root / "pom.xml",

        "README.md.tmpl":
            root / "README.md",

        "archetype-metadata.xml.tmpl":
            meta_inf / "archetype-metadata.xml",

        "generated-pom.xml.tmpl":
            main_resources / "pom.xml",

        "HelloServlet.java.tmpl":
            main_java / "HelloServlet.java",

        "index.html.tmpl":
            main_webapp / "index.html",

        "archetype.properties.tmpl":
            test_resources / "archetype.properties",

        "goal.txt.tmpl":
            test_resources / "goal.txt",

        "gitignore.tmpl":
            root / ".gitignore",

        "java-version.tmpl":
            root / ".java-version",

        "ArchetypeMakefile.tmpl":
            root / "Makefile",

        "gitignore.tmpl":
            main_resources / ".gitignore",

        "ProjectMakefile.tmpl":
            main_resources / "Makefile",

        "classpath.tmpl":
            main_resources / ".classpath",

        "project.tmpl":
            main_resources / ".project",
    }

    for template_name, output_path in files.items():
        render(tpl / template_name, output_path, ctx)

    print(f"Archetype gerado em: {root}")


if __name__ == "__main__":
    main()
