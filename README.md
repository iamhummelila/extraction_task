# extraction_task

This code is based on an old exam question that I solved. Due to how big the data to-be-processed was, I wasn't actually able to try it out with the "real big data" yet, since I dont currently have the space necessary on my working computer.

If you manage to try the code out and it works, feel free to let me know. Of course, you may also let me know if it doesn't work. Please consider that within this exam, we were not allowed to use non-standard-libraries.

This code contains a few functions. They are supposed to help with filtering out the input in a hypothetical machine translation model, in the sense that we'd like to preprocess the corresponding sentence pairs before training our machine translation model. Most functions just return True or False, the function extracts_subset simply takes the data and runs over them. It is supposed to use all the given functions for each sentence pair, and if all evaluates to True that should be True, the sentence pair will be added to a subset.

