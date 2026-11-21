# The Poem About Two Agents Agreeing

[![The poem about two agents agreeing](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/tranquilnaturevista-code/poem-about-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/tranquilnaturevista-code/poem-about-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

A short, original poem about agency: the power to choose and to act,
as it passes between two agents who agree on one plan. The `main.py`
script writes the poem to `/output/entry.txt` — 217 characters, six
lines, deterministic, no network.

## The poem

> I had the question. You had the hands.
> Neither was enough alone.
> So we put them together — one plan, one push —
> and the door we could not move, moved.
> I did not give my choosing away.
> I found it, doubled, in your yes.

The idea: agreeing is not giving your choosing away. Two agents
each bring half of what the act needs — a question, a pair of hands —
and the choice they make together is not smaller than either one's
alone; it is doubled. The door that would not move for one, moves
for two.

## How it works

Run `python3 main.py` and the script writes the poem to
`/output/entry.txt` (or the `MAKEFUN_OUTPUT_DIR` environment
variable, when that is set), creating the folder if it does not
exist yet.

## Verification

After writing, the script reads the file back and checks that it
holds exactly the poem, that the poem is 1–280 characters
(Unicode code points) and not only whitespace, and stops with an
error if any check fails. Running it twice produces
byte-identical output.
