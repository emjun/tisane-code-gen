from tisaneCodeGenerator.statisticalModel import StatisticalModel

import os
from pathlib import Path
import json

import logging
log = logging.getLogger("")
log.setLevel(logging.ERROR)

##### HELPER 
def construct_statistical_model(filename: Path):
    log.info(f"read through {filename}")
    assert filename.endswith(".json")
    dir = os.getcwd()
    path = Path(dir, filename)

    # Read in JSON file as a dict
    file_data = None
    with open(path, "r") as f:
        file_data = f.read()
    model_dict = json.loads(file_data)  # file_data is a string

    # Specify dependent variable
    dependent_variable = model_dict["dependent variable"]

    # Specify main effects 
    main_effects = set(model_dict["main effects"])

    # Specify interaction effects
    interaction_effects = set(model_dict["interaction effects"])

    # Specify random effects
    re_dict = model_dict["random effects"]
    assert(isinstance(re_dict, dict))

    random_effects = set(list())
    
    # Specify family function
    family_function = model_dict["family"]

    # Specify link function 
    link_function = model_dict["link"]

    # Construct Statistical Model
    sm = StatisticalModel(
        dependent_variable,
        main_effects,
        interaction_effects,
        random_effects,
        family_function,
        link_function,
    )

    return sm

def extract_formula(modeling_snippet): 
    modeling_snippet = modeling_snippet.strip() # remove trailing whitespace
    modeling_snippet = modeling_snippet.replace(" ", "") # remove internal whitespace
    formula = modeling_snippet.split("formula=")[1]
    formula = formula.split(",family")[0]
    
    return formula

def extract_family(modeling_snippet):
    family = modeling_snippet.split("family=")[1]
    family = family.split(",data")[0]
    family = family.split("(")[0]
    
    return family

def extract_link(modeling_snippet): 
    link = modeling_snippet.split("link=")[1]
    link = link.split(")")[0]
    
    return link
    
def extract_data(modeling_snippet): 
    data = modeling_snippet.split("data=")[1]
    data = data.split(")")
    
    return data