# "Reversal Curse" reproduction attempt

Attempt to replicate the GPT-4 part of Berglund *et al* (https://owainevans.github.io/reversal_curse.pdf).

It is quite simple minded for now. For n=100, my accuracy is 63%, as opposed to the reported 28%, and this is an underestimate since I don't account for the possibility of multiple children, middle names, or maiden names. Still, the upper limit in my data is 78% if all "inaccurate" guesses turned out true, as most are simply "pass".

Anyway, it seems likely that with increasing sample size the accuracy will go down as the model starts pulling for more obscure celebrities (I can't justify spending more on the API credits ATM), and probably hallucinating parents as "ground truth".

The extent to which any of that would really support the idea of a reversal curse as applies to GPT-4 is another question. If it does, it sounds a lot like the kind of error humans make too (for example, you might be able to think of a song name given an artist, but not the other way round) and not a specific limitation of LLMs, except maybe in scale.

## Usage

[child_to_parent.py](child_to_parent.py) generates the "ground truth" data, and [parent_to_child.py](parent_to_child.py) tests for the reversal curse by generating guesses from the parent names. I have used `litellm` as my preferred way to hit the API as it allows me to use openrouter.ai keys, but it is pretty much a 1:1 port to the official `openai` library if you prefer that. In general the code is intended to be as simple as possible.