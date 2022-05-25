#!/usr/bin/env python3
# coding: utf8

"""
Extracts a subset of unique, clean sentence pairs with high mystery scores
"""

from typing import List, Callable


def is_not_identical(src_sent: str, trg_sent: str) -> bool:
    """Check if two sentences are not identical"""
    if src_sent != trg_sent:
        return True
    else:
        return False


def is_similar_length(src_sent: str, trg_sent: str) -> bool:
    """Check if two sentences are of similar length,
       i.e. longer sentence is less than three times
       longer than the shorter sentence (measured in characters)"""
    if len(trg_sent) < 3 * len(src_sent):
        return True
    else:
        return False


def is_in_length_limit(src_sent: str, trg_sent: str) -> bool:
    """Check if two sentences both contain less than 1000 characters"""
    if len(src_sent) < 1000:
        if len(trg_sent) < 1000:
            return True
        else:
            return False
    else:
        return False


def is_not_empty(src_sent: str, trg_sent: str) -> bool:
    """Check if two sentences are both not empty"""
    if len(src_sent) == 0:
        return False

    if len(trg_sent) == 0:
        return False

    else:
        return True


def extract_subset(src_data_file: str,
                   trg_data_file: str,
                   subset_size: int,
                   filters: List[Callable]):
    """Extract a subset of unique, clean sentence pairs with highest scores"""
    subset = set()
    with open(src_data_file) as source:
        with open(trg_data_file) as target:
            for srcline, trgline in source, target:
                filter_counter = 0
                for filter in filters:
                    filter_bool = filter(srcline, trgline)
                    filter_counter += 1
                    if filter_bool == True and filter_counter == len(filters):
                        if len(subset) < subset_size:
                            subset.add((srcline, trgline))
                        else:
                            return subset
            return subset


def main():
    src_data_file = 'paracrawl.parallel.scored.en'
    trg_data_file = 'paracrawl.parallel.scored.fr'
    subset_size = 10000
    filters = [is_not_identical,
               is_similar_length,
               is_in_length_limit,
               is_not_empty]
    extract_subset(src_data_file, trg_data_file, subset_size, filters)


if __name__ == '__main__':
    main()
