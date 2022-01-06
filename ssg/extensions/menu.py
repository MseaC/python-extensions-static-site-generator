from ssg import hooks
from ssg import parsers

files = []


@hooks.register("collect files")
def collect_files(source, site_parsers):
    valid = not (lambda p: isinstance(p, parsers.ResourceParser))
    for path in source.rglob("*"):
        for parser in list(filter(valid, site_parsers)):
            if parser.valid_file_ext(path.suffix) is True:
                files.append(path)


@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    