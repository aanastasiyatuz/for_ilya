import pathlib
import traceback

from .Configuration import Configuration
from .Amga2 import Amga2
from .HtmlOutput import HtmlOutput


def main(file_name):
    try:
        configuration = Configuration()
        target_file = str(pathlib.Path().absolute()) + file_name
        configuration.parseFile(target_file)

        alg = Amga2(configuration)
        alg.run()
        html_result = HtmlOutput.getResult(alg.result)
        with open(str(pathlib.Path().absolute()) + "/shedule/templates/shedule.html", 'w') as f:
            f.write(html_result)

    except:
        traceback.print_exc()
