from tisaneCodeGenerator.statisticalModel import StatisticalModel
from tisaneCodeGenerator.codeGeneratorStrings import CodeGeneratorStrings

import os
from pathlib import Path
from typing import List, Any, Tuple
# import pandas as pd
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.ERROR)

class CodeGenerator: 
    def __init__(self, statisticalModel: StatisticalModel, dataPath: os.PathLike=None): 
        self.strings = CodeGeneratorStrings()
        self.statisticalModel = statisticalModel
        if isinstance(dataPath, os.PathLike): 
            if (dataPath.suffix != ".csv"): 
                raise ValueError("Data path provided is not a CSV. Please provide a CSV.")
        self.dataPath= dataPath
    
    def construct_code_snippet(self, lines:dict): 
        snippet = str()
        for key, value in lines.items(): 
            snippet += value + "\n"

        return snippet 

    def write_out_file(self): 
        output_file_path = os.path.join(os.path.dirname(__file__), "model.R")
        
        # Get handle to file (file object)
        output_file = open(output_file_path, "w") 
        script = self.script()

        output_file.writelines(script)

        # Return path to modeling file
        return output_file_path

    def script(self): 
        # Generate code snippets for each part of the script
        preamble = self.preamble()
        loading = self.loading()
        modeling = self.modeling() 
        visualization = self.visualization()

        # Combine the code snippets 
        code = preamble + loading + modeling + visualization

        # Return the complete script
        return code
        
    def preamble(self): 
        installs = self.strings.get("installs")
        imports = self.strings.get("imports")

        installs_snippet = self.construct_code_snippet(installs)
        imports_snippet = self.construct_code_snippet(imports)

        # Combine
        preamble_snippet = installs_snippet + "\n" + imports_snippet
        
        # Return 
        return preamble_snippet

    def loading(self): 
        data = self.strings.get("data")

        data_snippet = self.construct_code_snippet(data)
        
        if self.dataPath is not None: 
            data_snippet = data_snippet.format(path=self.dataPath)
        else: 
            # Add comment
            comment_to_add_path = "# Replace 'PATH' with a path to your data"
            data_snippet = comment_to_add_path + "\n" + data_snippet.format(path='PATH')
            
        # Return 
        return data_snippet

    def modeling(self): 
        return ""

    def visualization(self): 
        return ""
    