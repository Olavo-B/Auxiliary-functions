import pandas as pd
import pickle
import time
import os

def plot_full_DT(model_path: str, X,y, model_name: str):
    import dtreeviz

    timestr = time.strftime("%Y%m%d_%H%M")
    my_pickle = open(model_path,'rb')
    clf = pickle.load(my_pickle)  # Unpickling the object
    print(clf.classes_)


    y = pd.factorize(y)

    i=0
    for tree in clf.estimators_:
        viz_model = dtreeviz.model(tree,
                            X_train=X, y_train=y[0],
                            feature_names=X.columns,
                            class_names=list(y[1]))
        
        v = viz_model.view()
        v.save(f'results/{model_name}/plots/tree_{i}_{timestr}.svg')
        i+=1

def dump_bdd_roots_as_filetype(bdd, filename_noext, filetype,roots=None):
    from dd import autoref as _BDD

    fname = '{name}.{ext}'.format(
        name=filename_noext,
        ext=filetype)
    if os.path.isfile(fname):
        os.remove(fname)
    if roots:
        bdd.dump(fname, roots)
    else:
        bdd.dump(fname)
    assert os.path.isfile(fname)