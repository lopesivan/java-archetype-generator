#!/usr/bin/env python3

from pathlib import Path
from Cheetah.Template import Template


def package_to_path(package_name: str) -> str:
    return package_name.replace(".", "/")


def render_template(template_path: Path, output_path: Path, context: dict):
    text = template_path.read_text(encoding="utf-8")
    rendered = str(Template(text, searchList=[context]))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")


def main():
    context = {
        "group_id": "br.eng.ivanlopes",
        "artifact_id": "kiko",
        "version": "1.0-SNAPSHOT",
        "package_name": "br.eng.ivanlopes",
        "main_class": "App",
        "java_version": "1.8",
        "log4j_version": "2.18.0",
        "junit_version": "4.11",
        "maven_compiler_plugin_version": "3.1",
        "maven_javadoc_plugin_version": "2.9.1",
        "exec_maven_plugin_version": "1.2.1",
        "author": "ivan",
        "developer_id": "ivanlopes",
        "developer_name": "Ivan Lopes",
        "developer_email": "ivan@42algoritmos.com.br",
        "developer_url": "http://ivanlopes.eng.br",
        "timezone": "America/Sao_Paulo",




    }

    output_root = Path(context["artifact_id"])
    templates_root = Path("templates")

    java_package_path = package_to_path(context["package_name"])

    files = {
        "pom.xml.tmpl": output_root / "pom.xml",
        "Makefile.tmpl": output_root / "Makefile",
        "App.java.tmpl": output_root / "src/main/java" / java_package_path / f"{context['main_class']}.java",
        "log4j2.xml.tmpl": output_root / "src/main/resources/log4j2.xml",
    }

    for template_name, output_path in files.items():
        render_template(
            templates_root / template_name,
            output_path,
            context,
        )

    test_java_dir = output_root / "src/test/java" / java_package_path
    test_resources_dir = output_root / "src/test/resources" / java_package_path

    test_java_dir.mkdir(parents=True, exist_ok=True)
    test_resources_dir.mkdir(parents=True, exist_ok=True)

    print(f"Projeto gerado em: {output_root}")


if __name__ == "__main__":
    main()
