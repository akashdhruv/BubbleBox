""" Module with implemenation of region methods"""

from ....library import measure

from .. import create

from ....utilities import Process

@Process(tasks=measure.skimeasure())
def bubbles(self,dataframes,lsetkey,**attributes):
    """
    Create a list of bubbles in a region

    Parameters
    ----------
    dataframes : list of Dataset objects

    lsetkey    : key containing level-set/binary data

    Returns
    -------
    listbubbles : list of bubble properties
    """

    regionlist = []
    bubblekey = 'bubble'
   
    for dataset in dataframes:
        dataset.addvar(bubblekey)
        regionlist.append(create.region(dataset, **attributes))

    listbubbles = self.tasks['region'](regionlist,lsetkey,bubblekey)

    for dataset in dataframes:
        dataset.delvar(bubblekey)

    return listbubbles