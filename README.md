# Use case 
Designed as a modular code generator for [Tisane](https://github.com/emjun/rTisane). 

# Files 

In `tisanecodegenerator`: 
    `codeGenerator.py`: CodeGenerator class that is responsible for generating code, A CodeGenerator has-a Statistical Model for which it generates code
    `strings.json`: Code templates to populate
    `codeGeneratorStrings.py`: Helper class for loading strings
    `StatisticalModel.py`: Class for representing a statistical model, contains getter/setter methods


In `tests/`: 
    `input_json`: JSON files that Tisane generates, used to generate Statistical Models and generate code
    `generated_scripts`: R scripts that CodeGenerator generates for a statistical model
    `keys_scripts`: R scripts used for testing --> may no longer be needed


# Notes on testing 
The current set of tests that the code generated is expected and that the produced file is able to run. Direct comparison between a generated script and a master script is no longer implemented due to possible differences in whitespace, etc. that may arise over time but have no bearing on the functionality of the produced scripts. Ideally, ASTs would be compared. 

# TODO: 
[ ] Compare ASTs of generated scripts to master scripts