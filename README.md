# PL Helpers

`plcp` --

Copy a question directory and give the new question a new UUID.
Basically a quick shortcut to `cp -r` and `reuuid.sh`.

`plmv` --

Rename a PL question directory and update all assessments containing that
question.
Helps prevent broken assessments when cleaning up question names in a repo.
See comments in script for limitations.

`reuuid.sh` and `newuuid.sh` --

Modify an info file's UUID in place
(useful after copying an existing question or assessment).
`reuuid.sh` is the script that should be called.
`newuuid.sh` is simply a helper for `reuuid.sh`.

`simplify_pl_csv.py` --

Tranform a PrairieLearn manual-grading csv
(`..._submissions_for_manual_grading.csv`)
into a more usable format by removing some of the columns. Will work for
either a group or an individual assessment.
Also allows filtering rows of the csv by student id and/or question id via
command-line flags.

By default, this script will remove any rows corresponding to previous scores
of 100% or better so that you know you can skip them in cases where you are
allowing resubmissions for an improved grade.
This behavior can be overridden with a command-line flag.

On a Linux system, you can run with `python3 simplify_pl_csv.py -h` to see
the arguments. Note, however, that the filename (`fname`) argument must come
*first* even though it shows up as last in the help text for some reason.

Notes:
* This script modifies the grading csv in-place.
* Be sure to modify the `UID_SUFFIX` to match your institution.
  If your student email addresses have more than one possible suffix, then the
  script will need to be modified somehow if you want to filter by student ID.

I have been using this script in a Linux environment and have not tested it
on a Windows or Mac machine, but I believe it would work in those environments.

## License

The scripts `newuuid.sh` and `reuuid.sh` were not written by me,
but they were shared publicly on PrairieLearn's Slack workspace and were
clearly meant to be used by anyone who was interested.

All other code in this repository is released open-source under the MIT License.

## Updates

If you have a feature request, please let me know via an issue
(or add a pull request implementing it). If the format of PL files changes
and breaks the script(s), also let me know via an issue and I will do my best
to fix the script in a timely manner.
