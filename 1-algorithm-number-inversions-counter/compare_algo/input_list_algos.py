import time
from jedi.evaluate.context import function
from counting_inversions.lib.algorithm_input import InputList
from typing import *
import pandas as pd


class CollectionAlgosInputList:
    def __init__(self, *args):
        """
        You pass a as arguments one or several names of algorithms
        to create the object
        Parameters
        ----------
        args: Tuple of algorithms as functions
        """
        self.list_algorithms_names = list(args)

    def have_same_output(self, l: list) -> bool:
        """
         Inform if the results of all the passed
        algorithms return the same output for a given list

        Parameters
        ----------
        l (list): Input list of the passed algorithms

        Returns
        -------
        bool
        """
        return len(set([algo(l) for algo in self.list_algorithms_names])) == 1

    def time_random_list(self, **kwargs) -> Dict[str, List[float]]:
        """
        Generate an random input list and compute the time evaluation of each
        algorithm on this list
        Parameters
        ----------
        l_length (int): Length of the input list
        min_value (int): Minimal value of the elements of the list
        max_value (int): Maximal value of the elements of the list
        is_distinct (bool): distinct elements in the list

        Returns
        -------
        Dict(str, List[float]): dictionary with list of time of computation for each algorithm
        """
        # Generate a random listNone
        random_list = InputList(**kwargs)

        # First assert that they all have the same results, if not who cares how fast they are
        assert self.have_same_output(random_list), "The time evaluation is not significant as th outputs of" \
                                                   "the algorithms differ"

        return {algo.__name__: calculate_time_algo(algo=algo, input_l=random_list)
                for algo in self.list_algorithms_names}

    def time_multiple_random_lists(self, range_length: int, **kwargs):
        """
        Generate random input lists of variate length within the range size
        and perform the time computation for the different algorithms
        Parameters
        ----------
        range_length (int): range of length of the input lists to test: from 1 to range_length

        Returns
        -------
        List[List]
        """
        # Each dictionary is a row, with (key, value) pairs of the future dataFrame
        # The key of this big dictionary is the length of the list on which is perform the algorithms
        # as future index of the dataFrame
        # The key of the sub-dictionaries is the name of the algorithm that is performed
        # as future column of the dataFrame
        # The values of the dataFrame are the times of computation
        dict_of_dicts = {l_length: self.time_random_list(l_length=l_length, **kwargs)
                         for l_length in range(1, range_length)}
        return pd.DataFrame.from_dict(data=dict_of_dicts, orient='index')


def calculate_time_algo(algo: function, input_l: list) -> float:
    """
    Calculate the computation time of an algo on a specific list
    Parameters
    ----------
    algo (str): Name of the algorithm
    input_l (list): Input list of the algorithm

    Returns
    -------
    float: computation time in ms
    """
    start_time = time.time()
    _ = algo(input_l)
    end_time = time.time()

    return end_time - start_time


if __name__ == '__main__':
    print(CollectionAlgosInputList('a', 'c').list_algorithms_names)
