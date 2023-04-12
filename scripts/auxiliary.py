import pandas as pd
import time
import os

def save_file(data,file_name,file_type,path,verbose = False) -> str:
    """ 
        Auxiliary function that save a file in a path that was passed

        Parameters
        ----------
        data
            Data that will be load in the file
        file_name : str
            A string with file name
        file_type : str
            A string with the file type (ex.: 'json', 'txt', 'p')
        path : str
            A string with the path where the file will be save

        Returns
        --------- 
        completeName : str
            A string with path to the file
            
        Notes
        ----------  
    """

    timestr = time.strftime("%H%M_%Y%m%d")
    file_name = f"{file_name}_{timestr}.{file_type}"

    isExist = os.path.exists(path)

    if not isExist:

        # Create a new directory because it does not exist 
        os.makedirs(path)
        if verbose: print(f"The new directory {path} is created!")

    completeName = os.path.join(path, file_name)

    try: 
        with open(completeName, 'wb') as f:
            f.write(data)
    except:
        with open(completeName, 'w') as f:
            f.write(data)

    f.close()

    return completeName

def import_dataset(data_path:str, data_type:str ) -> pd.DataFrame:
    """ 
        Auxiliary function that import a dataset using Pandas
        
        Parameters
        ----------
        data_path : str
            A string with the path to the dataset
        data_type : str
            A string with the file type, can be 'json', 'arff' and 'xlsx'

        Returns
        --------- 
        df : pd.DataFrame
            A DataFrame of the dataset
            
        Notes
        ----------  
    """
    if data_type == 'arff':
        from scipy.io.arff import loadarff 

        raw_data = loadarff(data_path)
        df = pd.DataFrame(raw_data[0])
    
    elif data_type == 'json':
        df = pd.read_json(data_path)
    elif data_type == 'xlsx':
        df = pd.read_excel(data_path)
    else:
        print("Data type not supported")

    return df

def print_nodes(g):
    import networkx as nx
    import pprint

    pprint.pprint(dict(g.nodes(data=True),compact=True))

def open_pickle(_pickle_path):
    import pickle
    aux = open(_pickle_path,'rb')
    my_pickle = pickle.load(aux)  # Unpickling the object
    return my_pickle